---
category: performance
topic: db-query-patterns
status: draft
---

## Проблема / Контекст

Database queries are the most common source of server-side latency in a Next.js App Router app. Unlike REST APIs with a fixed response shape, Server Components and Server Actions fetch data in TypeScript — making it easy to write inefficient queries that work in development (small dataset) but become 10-100x slower in production. The three biggest problems are: N+1 queries, over-fetching columns, and missing indexes.

---

## Решение

### N+1 Query Problem

**The pattern:** A loop that runs one query per item in a collection. With 50 products you get 51 DB round trips instead of 2.

```typescript
// BAD — N+1: 1 query for orders + 1 per order for user
const orders = await db.select().from(ordersTable); // 1 query

for (const order of orders) {
  const user = await db.query.users.findFirst({
    where: eq(users.id, order.userId), // N queries — one per order
  });
  console.log(order.id, user?.name);
}
// Total: 1 + N queries. With 100 orders: 101 round trips to Postgres.

// GOOD — use Drizzle relations to JOIN in a single query
const ordersWithUsers = await db.query.orders.findMany({
  with: {
    user: {
      columns: { id: true, name: true, email: true }, // select only what you need
    },
    items: {
      with: {
        product: {
          columns: { id: true, name: true, priceInCents: true },
        },
      },
    },
  },
  limit: 50,
});
// Total: 1 query (or 2 with Drizzle's IN-based relation loading)
```

**Drizzle schema setup for relations:**

```typescript
// src/db/schema.ts
import { pgTable, text, integer, timestamp, uuid } from "drizzle-orm/pg-core";
import { relations } from "drizzle-orm";

export const users = pgTable("users", {
  id: uuid("id").primaryKey().defaultRandom(),
  name: text("name").notNull(),
  email: text("email").notNull().unique(),
});

export const orders = pgTable("orders", {
  id: uuid("id").primaryKey().defaultRandom(),
  userId: uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
  totalCents: integer("total_cents").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const orderItems = pgTable("order_items", {
  id: uuid("id").primaryKey().defaultRandom(),
  orderId: uuid("order_id").notNull().references(() => orders.id, { onDelete: "cascade" }),
  productId: uuid("product_id").notNull().references(() => products.id),
  quantity: integer("quantity").notNull(),
  priceInCents: integer("price_in_cents").notNull(),
});

// Define relations — required for db.query.*.findMany({ with: {} })
export const ordersRelations = relations(orders, ({ one, many }) => ({
  user: one(users, { fields: [orders.userId], references: [users.id] }),
  items: many(orderItems),
}));

export const orderItemsRelations = relations(orderItems, ({ one }) => ({
  order: one(orders, { fields: [orderItems.orderId], references: [orders.id] }),
  product: one(products, { fields: [orderItems.productId], references: [products.id] }),
}));
```

---

### Select only needed columns

```typescript
// BAD — select * fetches all columns including large blobs/text
const users = await db.select().from(usersTable);
// Returns: id, name, email, passwordHash, bio (10KB), avatar (URL), metadata (JSON), ...

// GOOD — columns object limits what's fetched from Postgres
const users = await db.select({
  id: usersTable.id,
  name: usersTable.name,
  email: usersTable.email,
  // passwordHash intentionally omitted — never fetch it unless comparing
}).from(usersTable);

// With query builder:
const user = await db.query.users.findFirst({
  where: eq(users.id, userId),
  columns: {
    id: true,
    name: true,
    email: true,
    // passwordHash: false is the default for omitted fields
  },
  with: {
    orders: {
      columns: { id: true, totalCents: true, createdAt: true },
      limit: 5,
      orderBy: [desc(orders.createdAt)],
    },
  },
});
```

---

### Pagination: cursor-based vs offset

```typescript
// OFFSET PAGINATION — simple but slow on large tables
// Works fine for: admin panels, small datasets (< 10k rows)

export async function getProductsOffset(page: number, pageSize: number = 20) {
  const [items, [{ count }]] = await Promise.all([
    db.select().from(products)
      .limit(pageSize)
      .offset((page - 1) * pageSize)
      .orderBy(products.createdAt),

    db.select({ count: sql<number>`count(*)::int` }).from(products),
  ]);

  return {
    items,
    totalPages: Math.ceil(count / pageSize),
    hasNextPage: page * pageSize < count,
  };
}
// Problem: OFFSET 10000 requires Postgres to scan 10,000 rows before returning 20.
// Performance degrades linearly with offset size.

// CURSOR PAGINATION — fast on any dataset size
// Use for: infinite scroll, large tables, real-time feeds

export async function getProductsCursor(
  cursor?: string, // ISO date string of the last item's createdAt
  pageSize: number = 20
) {
  const items = await db.select({
    id: products.id,
    name: products.name,
    createdAt: products.createdAt,
  })
  .from(products)
  .where(
    cursor
      ? lt(products.createdAt, new Date(cursor)) // fetch items BEFORE the cursor
      : undefined
  )
  .limit(pageSize + 1) // fetch one extra to determine if there's a next page
  .orderBy(desc(products.createdAt));

  const hasNextPage = items.length > pageSize;
  const data = hasNextPage ? items.slice(0, -1) : items;
  const nextCursor = hasNextPage ? data.at(-1)?.createdAt.toISOString() : undefined;

  return { items: data, nextCursor, hasNextPage };
}

// Composite cursor for stable pagination (handles ties in createdAt)
export async function getProductsCursorComposite(
  cursor?: { createdAt: string; id: string },
  pageSize: number = 20
) {
  const items = await db.select().from(products)
    .where(
      cursor
        ? or(
            lt(products.createdAt, new Date(cursor.createdAt)),
            and(
              eq(products.createdAt, new Date(cursor.createdAt)),
              lt(products.id, cursor.id)
            )
          )
        : undefined
    )
    .limit(pageSize + 1)
    .orderBy(desc(products.createdAt), desc(products.id));

  const hasNextPage = items.length > pageSize;
  const data = hasNextPage ? items.slice(0, -1) : items;
  const last = data.at(-1);
  const nextCursor = last
    ? { createdAt: last.createdAt.toISOString(), id: last.id }
    : undefined;

  return { items: data, nextCursor };
}
```

---

### Indexes: what to index

```typescript
// src/db/schema.ts — add indexes to the schema, Drizzle generates the migration

import { pgTable, index, uniqueIndex } from "drizzle-orm/pg-core";

export const products = pgTable("products", {
  id: uuid("id").primaryKey().defaultRandom(),
  slug: text("slug").notNull(),
  name: text("name").notNull(),
  categoryId: uuid("category_id").references(() => categories.id),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  publishedAt: timestamp("published_at"),
  searchVector: tsvector("search_vector"), // for full-text search
}, (table) => ({
  // Unique index — also creates a constraint
  slugIdx: uniqueIndex("products_slug_idx").on(table.slug),

  // Foreign key index — always index FK columns for JOIN performance
  categoryIdx: index("products_category_id_idx").on(table.categoryId),

  // Index for sorting — queries that ORDER BY createdAt benefit enormously
  createdAtIdx: index("products_created_at_idx").on(table.createdAt),

  // Partial index — only index published products (smaller, faster)
  publishedIdx: index("products_published_idx")
    .on(table.publishedAt)
    .where(sql`published_at IS NOT NULL`),

  // Composite index for common query pattern: WHERE category_id = ? ORDER BY created_at
  categoryCreatedAtIdx: index("products_category_created_at_idx")
    .on(table.categoryId, table.createdAt),

  // GIN index for full-text search
  searchVectorIdx: index("products_search_vector_idx")
    .using("gin", table.searchVector),
}));

// Rules for indexing:
// 1. Always index FK columns (Postgres does NOT do this automatically)
// 2. Index columns used in WHERE clauses on large tables (>10k rows)
// 3. Index columns used in ORDER BY on paginated queries
// 4. Composite indexes: left-to-right matters — put equality columns first
// 5. Don't over-index — indexes slow down INSERT/UPDATE/DELETE
```

---

### Connection pooling with PgBouncer

```typescript
// Serverless environments (Vercel) create a new DB connection per invocation.
// Without pooling: 100 concurrent requests = 100 Postgres connections.
// Postgres max connections default is 100 — you'll hit "too many connections".

// SOLUTION: Use a connection pooler between your app and Postgres.
// On Railway/Supabase/Neon: PgBouncer is available as a sidecar.

// Two connection strings in .env:
DATABASE_URL=postgresql://user:pass@db.railway.app:5432/mydb  # direct (for migrations)
DATABASE_POOL_URL=postgresql://user:pass@pgbouncer.railway.app:6432/mydb  # pooled (for queries)

// src/db/index.ts
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "./schema";

// Use pooled URL for runtime queries
const connection = postgres(process.env.DATABASE_POOL_URL!, {
  max: 10,          // max connections from this process to PgBouncer
  idle_timeout: 20, // close idle connections after 20s
  connect_timeout: 10,
  // PgBouncer transaction mode: prepared statements must be disabled
  prepare: false,
});

export const db = drizzle(connection, { schema });

// src/db/migrate.ts — uses direct connection for migrations (bypasses pooler)
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import { migrate } from "drizzle-orm/postgres-js/migrator";

const migrationClient = postgres(process.env.DATABASE_URL!, { max: 1 });
const migrationDb = drizzle(migrationClient);
await migrate(migrationDb, { migrationsFolder: "./drizzle" });
await migrationClient.end();
```

---

### Query analysis with EXPLAIN ANALYZE

```typescript
// src/lib/db-debug.ts — only use in development
import { sql } from "drizzle-orm";

export async function explainQuery(query: string, params: unknown[] = []) {
  if (process.env.NODE_ENV !== "development") {
    throw new Error("explainQuery is only for development");
  }

  const result = await db.execute(
    sql.raw(`EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) ${query}`)
  );
  console.log(JSON.stringify(result[0], null, 2));
}

// Usage during development:
// explainQuery(
//   `SELECT * FROM products WHERE category_id = $1 ORDER BY created_at DESC LIMIT 20`,
//   ['some-uuid']
// );
// Look for:
// - "Seq Scan" on large tables → needs an index
// - "Rows Removed by Filter: 9800" → bad selectivity → different index needed
// - Actual time > 100ms → optimize
```

### Query logging in development

```typescript
// src/db/index.ts
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "./schema";

const isDev = process.env.NODE_ENV === "development";

const connection = postgres(process.env.DATABASE_URL!, {
  max: isDev ? 5 : 10,
  // Log all queries in development
  onnotice: isDev ? console.log : undefined,
});

export const db = drizzle(connection, {
  schema,
  logger: isDev
    ? {
        logQuery(query, params) {
          console.log("\n[DB Query]", query);
          if (params.length) console.log("[DB Params]", params);
        },
      }
    : false,
});
```

---

## Антипаттерн

```typescript
// BAD: N+1 in a Server Component
export default async function OrdersPage() {
  const orders = await db.select().from(ordersTable);

  return (
    <ul>
      {orders.map(async (order) => {
        const user = await db.query.users.findFirst({ // N queries!
          where: eq(users.id, order.userId),
        });
        return <li key={order.id}>{user?.name}: {order.totalCents}</li>;
      })}
    </ul>
  );
}
// Note: React does not support async functions in .map() for Server Components.
// This won't work AND it's N+1. Use findMany with { with: { user: true } }.

// BAD: Fetching without pagination on a page that will have > 100 rows
const allProducts = await db.select().from(products); // grows unbounded

// BAD: Running migrations at request time
export async function GET() {
  await migrate(db, { migrationsFolder: "./drizzle" }); // runs on EVERY request
  // ...
}
// Migrations should run once at deploy time, never per-request.

// BAD: Opening a new postgres() connection per Server Action invocation
// In a Serverless environment this exhausts connection limits
export async function someAction() {
  const conn = postgres(process.env.DATABASE_URL!); // new connection every call
  const db = drizzle(conn, { schema });
  // ...
  await conn.end(); // might not run if action throws
}
// GOOD: Export a singleton db from src/db/index.ts and import it everywhere.
```

---

## Связанные документы

- `knowledge/custom/07-performance/cwv-nextjs.md` — LCP depends on fast data fetching
- `knowledge/custom/02-patterns/data-fetching.md` — Server Component data fetching patterns
- `knowledge/custom/05-testing/test-strategy.md` — integration tests with test database

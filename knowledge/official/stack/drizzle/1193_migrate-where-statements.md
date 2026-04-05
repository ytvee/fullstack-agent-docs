##### Migrate `where` statements

You can check our [Select Filters docs](/docs/rqb-v2#select-filters) to see examples and a complete API reference.

With the new syntax, you can use `AND`, `OR`, `NOT`, and `RAW`, plus all the filtering operators that 
were previously available in Relations v1.

**Examples**
<CodeTabs items={["simple eq", "using AND", "using OR", "using NOT", "complex example using RAW"]}>
<CodeTab>
```ts
const response = db.query.users.findMany({
  where: {
    age: 15,
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name"
from "users" 
where ("users"."age" = $1)
```
</CodeTab>
<CodeTab>
```ts
const response = db.query.users.findMany({
  where: {
    age: 15,
    name: 'John'
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name"
from "users" 
where ("users"."age" = $1 and "users"."name" = $2)
```
</CodeTab>
<CodeTab>
```ts
const response = await db.query.users.findMany({
  where: {
    OR: [
      {
        id: {
          gt: 10,
        },
      },
	  {
		name: {
          like: "John%",
        },
	  }
    ],
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name" 
from "users" 
where ("users"."id" > $1 or "users"."name" like $2)
```
</CodeTab>
<CodeTab>
```ts
const response = db.query.users.findMany({
  where: {
    NOT: {
      id: {
        gt: 10,
      },
    },
    name: {
      like: "John%",
    },
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name" 
from "users" 
where (not "users"."id" > $1 and "users"."name" like $2)
```
</CodeTab>
<CodeTab>
```ts
// schema.ts
import { integer, jsonb, pgTable, text, timestamp } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: integer("id").primaryKey(),
  name: text("name"),
  email: text("email").notNull(),
  age: integer("age"),
  createdAt: timestamp("created_at").defaultNow(),
  lastLogin: timestamp("last_login"),
  subscriptionEnd: timestamp("subscription_end"),
  lastActivity: timestamp("last_activity"),
  preferences: jsonb("preferences"),      // JSON column for user settings/preferences
  interests: text("interests").array(),     // Array column for user interests
});
```
```ts
const response = db.query.users.findMany({
  where: {
    AND: [
      {
        OR: [
          { RAW: (table) => sql`LOWER(${table.name}) LIKE 'john%'` },
          { name: { ilike: "jane%" } },
        ],
      },
      {
        OR: [
          { RAW: (table) => sql`${table.preferences}->>'theme' = 'dark'` },
          { RAW: (table) => sql`${table.preferences}->>'theme' IS NULL` },
        ],
      },
      { RAW: (table) => sql`${table.age} BETWEEN 25 AND 35` },
    ],
  },
});
```
```sql
```
</CodeTab>
</CodeTabs>


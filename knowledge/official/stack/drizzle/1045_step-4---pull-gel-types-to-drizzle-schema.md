#### Step 4 - Pull Gel types to Drizzle schema

Pull your database schema:
<Npx>
drizzle-kit pull
</Npx>

Here is an example of the generated schema.ts file:

<Callout type="warning">
You'll get more than just the `Identity` table from `ext::auth`. Drizzle will pull in all the 
`auth` tables you can use. The example below showcases just one of them.
</Callout>

```ts
import { gelTable, uniqueIndex, uuid, text, gelSchema, timestamptz, foreignKey } from "drizzle-orm/gel-core"
import { sql } from "drizzle-orm"

export const extauth = gelSchema('ext::auth');

export const identityInExtauth = extauth.table('Identity', {
	id: uuid().default(sql`uuid_generate_v4()`).primaryKey().notNull(),
	createdAt: timestamptz('created_at').default(sql`(clock_timestamp())`).notNull(),
	issuer: text().notNull(),
	modifiedAt: timestamptz('modified_at').notNull(),
	subject: text().notNull(),
}, (table) => [
	uniqueIndex('6bc2dd19-bce4-5810-bb1b-7007afe97a11;schemaconstr').using(
		'btree',
		table.id.asc().nullsLast().op('uuid_ops'),
	),
]);

export const user = gelTable('User', {
	id: uuid().default(sql`uuid_generate_v4()`).primaryKey().notNull(),
	email: text().notNull(),
	identityId: uuid('identity_id').notNull(),
	username: text().notNull(),
}, (table) => [
	uniqueIndex('d504514c-26a7-11f0-b836-81aa188c0abe;schemaconstr').using(
		'btree',
		table.id.asc().nullsLast().op('uuid_ops'),
	),
	foreignKey({
		columns: [table.identityId],
		foreignColumns: [identityInExtauth.id],
		name: 'User_fk_identity',
	}),
]);
```

🎉 Now you can use the `auth` tables in your queries!

Source: https://orm.drizzle.team/docs/include-or-exclude-columns


import Section from "@mdx/Section.astro";
import IsSupportedChipGroup from "@mdx/IsSupportedChipGroup.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Callout from "@mdx/Callout.astro";

<IsSupportedChipGroup chips={{PostgreSQL: true, MySQL: true, SQLite: true}}/>

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql), [MySQL](/docs/get-started-mysql) and [SQLite](/docs/get-started-sqlite)
- [Select statement](/docs/select)
- [Get typed table columns](/docs/goodies#get-typed-table-columns)
- [Joins](/docs/joins)
- [Relational queries](/docs/rqb)
- [Partial select with relational queries](/docs/rqb#partial-fields-select)
</Prerequisites>

Drizzle has flexible API for including or excluding columns in queries. To include all columns you can use `.select()` method like this:

<CodeTabs items={["index.ts", "schema.ts"]}>
	<CodeTab>
    ```ts copy {5}
    import { posts } from './schema';

    const db = drizzle(...);

    await db.select().from(posts);
    ```

    ```ts
    // result type
    type Result = {
      id: number;
      title: string;
      content: string;
      views: number;
    }[];
    ```
  </CodeTab>

  ```ts copy
  import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

  export const posts = pgTable('posts', {
    id: serial('id').primaryKey(),
    title: text('title').notNull(),
    content: text('content').notNull(),
    views: integer('views').notNull().default(0),
  });
	```
</CodeTabs>

To include specific columns you can use `.select()` method like this:

<Section>
  ```ts copy {1}
  await db.select({ title: posts.title }).from(posts);
  ```

  ```ts
  // result type
  type Result = {
    title: string;
  }[];
  ```
</Section>

To include all columns with extra columns you can use `getColumns()` utility function like this:

<Callout type='warning'>
`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](/docs/upgrade-v1))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`
</Callout>


<Section>
  ```ts copy {5,6}
  import { getColumns, sql } from 'drizzle-orm';

  await db
    .select({
      ...getColumns(posts),
      titleLength: sql<number>`length(${posts.title})`,
    })
    .from(posts);
  ```

  ```ts
  // result type
  type Result = {
    id: number;
    title: string;
    content: string;
    views: number;
    titleLength: number;
  }[];
  ```
</Section>

To exclude columns you can use `getColumns()` utility function like this:

<Callout type='warning'>
`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](/docs/upgrade-v1))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`
</Callout>

<Section>
  ```ts copy {3,5}
  import { getColumns } from 'drizzle-orm';

  const { content, ...rest } = getColumns(posts); // exclude "content" column

  await db.select({ ...rest }).from(posts); // select all other columns
  ```

  ```ts
  // result type
  type Result = {
    id: number;
    title: string;
    views: number;
  }[];
  ```
</Section>

This is how you can include or exclude columns with joins:

<CodeTabs items={["index.ts", "schema.ts"]}>
  <CodeTab>
    ```ts copy {5,9,10,11}
    import { eq, getColumns } from 'drizzle-orm';
    import { comments, posts, users } from './db/schema';

    // exclude "userId" and "postId" columns from "comments"
    const { userId, postId, ...rest } = getColumns(comments);

    await db
      .select({
        postId: posts.id, // include "id" column from "posts"
        comment: { ...rest }, // include all other columns
        user: users, // equivalent to getColumns(users)
      })
      .from(posts)
      .leftJoin(comments, eq(posts.id, comments.postId))
      .leftJoin(users, eq(users.id, posts.userId));
    ```

    ```ts
    // result type
    type Result = {
      postId: number;
      comment: {
        id: number;
        content: string;
        createdAt: Date;
      } | null;
      user: {
        id: number;
        name: string;
        email: string;
      } | null;
    }[];
    ```
  </CodeTab>

  ```ts copy
  import { integer, pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';

  export const users = pgTable('users', {
    id: serial('id').primaryKey(),
    name: text('name').notNull(),
    email: text('email').notNull(),
  });

  export const posts = pgTable('posts', {
    id: serial('id').primaryKey(),
    title: text('title').notNull(),
    content: text('content').notNull(),
    views: integer('views').notNull().default(0),
    userId: integer('user_id').notNull().references(() => users.id),
  });

  export const comments = pgTable('comments', {
    id: serial('id').primaryKey(),
    postId: integer('post_id').notNull().references(() => posts.id),
    userId: integer('user_id').notNull().references(() => users.id),
    content: text('content').notNull(),
    createdAt: timestamp('created_at').notNull().defaultNow(),
  });
  ```
</CodeTabs>

Drizzle has useful relational queries API, that lets you easily include or exclude columns in queries. This is how you can include all columns:

<CodeTabs items={["index.ts", "schema.ts"]}>
  <CodeTab>
    ```ts copy {5,7,8,9,12,13,14,17,18,19,20,21,22}
    import * as schema from './schema';

    const db = drizzle(..., { schema });

    await db.query.posts.findMany();
    ```

    ```ts
    // result type
    type Result = {
      id: number;
      title: string;
      content: string;
      views: number;
    }[]
    ```
  </CodeTab>

  ```ts copy
  import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

  export const posts = pgTable('posts', {
    id: serial('id').primaryKey(),
    title: text('title').notNull(),
    content: text('content').notNull(),
    views: integer('views').notNull().default(0),
  });
	```
</CodeTabs>

This is how you can include specific columns using relational queries:

<Section>
  ```ts copy {2,3,4}
  await db.query.posts.findMany({
    columns: {
      title: true,
    },
  });
  ```

  ```ts
  // result type
  type Result = {
    title: string;
  }[]
  ```
</Section>

This is how you can include all columns with extra columns using relational queries:

<Section>
  ```ts copy {4,5,6}
  import { sql } from 'drizzle-orm';

  await db.query.posts.findMany({
    extras: {
      titleLength: sql<number>`length(${posts.title})`.as('title_length'),
    },
  });
  ```

  ```ts
  // result type
  type Result = {
    id: number;
    title: string;
    content: string;
    views: number;
    titleLength: number;
  }[];
  ```
</Section>

This is how you can exclude columns using relational queries:

<Section>
  ```ts copy {2,3,4}
  await db.query.posts.findMany({
    columns: {
      content: false,
    },
  });
  ```

  ```ts
  // result type
  type Result = {
    id: number;
    title: string;
    views: number;
  }[]
  ```
</Section>

This is how you can include or exclude columns with relations using relational queries:

<CodeTabs items={["index.ts", "schema.ts"]}>
  <CodeTab>
  ```ts copy {7,12,13,16}
  import * as schema from './schema';

  const db = drizzle(..., { schema });

  await db.query.posts.findMany({
    columns: {
      id: true, // include "id" column
    },
    with: {
      comments: {
        columns: {
          userId: false, // exclude "userId" column
          postId: false, // exclude "postId" column
        },
      },
      user: true, // include all columns from "users" table
    },
  });
  ```

  ```ts
  // result type
  type Result = {
    id: number;
    user: {
      id: number;
      name: string;
      email: string;
    };
    comments: {
      id: number;
      content: string;
      createdAt: Date;
    }[];
  }[]
  ```
  </CodeTab>

  ```ts copy
  import { relations } from 'drizzle-orm';
  import { integer, pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';

  export const users = pgTable('users', {
    id: serial('id').primaryKey(),
    name: text('name').notNull(),
    email: text('email').notNull(),
  });

  export const posts = pgTable('posts', {
    id: serial('id').primaryKey(),
    title: text('title').notNull(),
    content: text('content').notNull(),
    views: integer('views').notNull().default(0),
    userId: integer('user_id').notNull().references(() => users.id),
  });

  export const comments = pgTable('comments', {
    id: serial('id').primaryKey(),
    postId: integer('post_id').notNull().references(() => posts.id),
    userId: integer('user_id').notNull().references(() => users.id),
    content: text('content').notNull(),
    createdAt: timestamp('created_at').notNull().defaultNow(),
  });

  export const usersRelations = relations(users, ({ many }) => ({
    posts: many(posts),
    comments: many(comments),
  }));

  export const postsRelations = relations(posts, ({ many, one }) => ({
    comments: many(comments),
    user: one(users, { fields: [posts.userId], references: [users.id] }),
  }));

  export const commentsRelations = relations(comments, ({ one }) => ({
    post: one(posts, { fields: [comments.postId], references: [posts.id] }),
    user: one(users, { fields: [comments.userId], references: [users.id] }),
  }));
  ```
</CodeTabs>

This is how you can create custom solution for conditional select:

<CodeTabs items={["index.ts", "schema.ts"]}>
  <CodeTab>
    ```ts copy {7}
    import { posts } from './schema';

    const searchPosts = async (withTitle = false) => {
      await db
        .select({
          id: posts.id,
          ...(withTitle && { title: posts.title }),
        })
        .from(posts);
    };

    await searchPosts();
    await searchPosts(true);
    ```

    ```ts
    // result type
    type Result = {
      id: number;
      title?: string | undefined;
    }[];
    ```
  </CodeTab>

  ```ts copy
  import { integer, pgTable, serial, text } from 'drizzle-orm/pg-core';

  export const posts = pgTable('posts', {
    id: serial('id').primaryKey(),
    title: text('title').notNull(),
    content: text('content').notNull(),
    views: integer('views').notNull().default(0),
  });
	```
</CodeTabs>


Source: https://orm.drizzle.team/docs/incrementing-a-value

import Section from "@mdx/Section.astro";
import IsSupportedChipGroup from "@mdx/IsSupportedChipGroup.astro";
import Prerequisites from "@mdx/Prerequisites.astro";

<IsSupportedChipGroup chips={{PostgreSQL: true, MySQL: true, SQLite: true}}/>

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql), [MySQL](/docs/get-started-mysql) and [SQLite](/docs/get-started-sqlite)
- [Update statement](/docs/update)
- [Filters](/docs/operators) and [sql operator](/docs/sql)
</Prerequisites>

To increment a column value you can use `update().set()` method like below:

<Section>
```ts copy {8}
import { eq, sql } from 'drizzle-orm';

const db = drizzle(...)
  
await db
  .update(table)
  .set({
    counter: sql`${table.counter} + 1`,
  })
  .where(eq(table.id, 1));
```

```sql
update "table" set "counter" = "counter" + 1 where "id" = 1;
```
</Section>

Drizzle has simple and flexible API, which lets you easily create custom solutions. This is how you do custom increment function:

```ts copy {4,10,11}
import { AnyColumn } from 'drizzle-orm';

const increment = (column: AnyColumn, value = 1) => {
  return sql`${column} + ${value}`;
};

await db
  .update(table)
  .set({
    counter1: increment(table.counter1),
    counter2: increment(table.counter2, 10),
  })
  .where(eq(table.id, 1));
```


Source: https://orm.drizzle.team/docs/limit-offset-pagination


import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Section from "@mdx/Section.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import IsSupportedChipGroup from "@mdx/IsSupportedChipGroup.astro";

<IsSupportedChipGroup chips={{PostgreSQL: true, MySQL: true, SQLite: true}}/>

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql), [MySQL](/docs/get-started-mysql) and [SQLite](/docs/get-started-sqlite)
- [Select statement](/docs/select) with [order by clause](/docs/select#order-by) and [limit & offset clauses](/docs/select#limit--offset)
- [Relational queries](/docs/rqb) with [order by clause](/docs/rqb#order-by) and [limit & offset clauses](/docs/rqb#limit--offset)
- [Dynamic query building](/docs/dynamic-query-building)
</Prerequisites>

This guide demonstrates how to implement `limit/offset` pagination in Drizzle:

<CodeTabs items={["index.ts", "schema.ts"]}>
  <CodeTab>
    ```ts copy {9,10,11}
    import { asc } from 'drizzle-orm';
    import { users } from './schema';

    const db = drizzle(...);

    await db
      .select()
      .from(users)
      .orderBy(asc(users.id)) // order by is mandatory
      .limit(4) // the number of rows to return
      .offset(4); // the number of rows to skip
    ```

    ```sql
    select * from users order by id asc limit 4 offset 4;
    ```

    ```ts
    // 5-8 rows returned
    [
      {
        id: 5,
        firstName: 'Beth',
        lastName: 'Davis',
        createdAt: 2024-03-11T20:51:46.787Z
      },
      {
        id: 6,
        firstName: 'Charlie',
        lastName: 'Miller',
        createdAt: 2024-03-11T21:15:46.787Z
      },
      {
        id: 7,
        firstName: 'Clara',
        lastName: 'Wilson',
        createdAt: 2024-03-11T21:33:46.787Z
      },
      {
        id: 8,
        firstName: 'David',
        lastName: 'Moore',
        createdAt: 2024-03-11T21:45:46.787Z
      }
    ]
    ```
  </CodeTab>
  <CodeTab>
    ```ts copy
    import { pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';

    export const users = pgTable('users', {
      id: serial('id').primaryKey(),
      firstName: text('first_name').notNull(),
      lastName: text('last_name').notNull(),
      createdAt: timestamp('created_at').notNull().defaultNow(),
    });
    ```

    ```plaintext
    +----+------------+-----------+----------------------------+
    | id | first_name | last_name |         created_at         |
    +----+------------+-----------+----------------------------+
    |  1 | Alice      | Johnson   | 2024-03-08 12:23:55.251797 |
    +----+------------+-----------+----------------------------+
    |  2 | Alex       | Smith     | 2024-03-08 12:25:55.182    |
    +----+------------+-----------+----------------------------+
    |  3 | Aaron      | Williams  | 2024-03-08 12:28:55.182    |
    +----+------------+-----------+----------------------------+
    |  4 | Brian      | Brown     | 2024-03-08 12:34:55.182    |
    +----+------------+-----------+----------------------------+
    |  5 | Beth       | Davis     | 2024-03-08 12:40:55.182    |
    +----+------------+-----------+----------------------------+
    |  6 | Charlie    | Miller    | 2024-03-08 13:04:55.182    |
    +----+------------+-----------+----------------------------+
    |  7 | Clara      | Wilson    | 2024-03-08 13:22:55.182    |
    +----+------------+-----------+----------------------------+
    |  8 | David      | Moore     | 2024-03-08 13:34:55.182    |
    +----+------------+-----------+----------------------------+
    ```
  </CodeTab>
</CodeTabs>

Limit is the number of rows to return `(page size)` and offset is the number of rows to skip `((page number - 1) * page size)`. 
For consistent pagination, ensure ordering by a unique column. Otherwise, the results can be inconsistent.

If you need to order by a non-unique column, you should also append a unique column to the ordering.

This is how you can implement `limit/offset` pagination with 2 columns:

<Section>
```ts copy {5}
const getUsers = async (page = 1, pageSize = 3) => {
  await db
    .select()
    .from(users)
    .orderBy(asc(users.firstName), asc(users.id)) // order by first_name (non-unique), id (pk)
    .limit(pageSize) 
    .offset((page - 1) * pageSize);
}

await getUsers();
```
</Section>

Drizzle has useful relational queries API, that lets you easily implement `limit/offset` pagination:

<Section>
```ts copy {7,8,9}
import * as schema from './db/schema';

const db = drizzle({ schema });

const getUsers = async (page = 1, pageSize = 3) => {
  await db.query.users.findMany({
    orderBy: (users, { asc }) => asc(users.id),
    limit: pageSize,
    offset: (page - 1) * pageSize,
  });
};

await getUsers();
```
</Section>

Drizzle has simple and flexible API, which lets you easily create custom solutions. This is how you can create custom function for pagination using `.$dynamic()` function:

<Section>
```ts copy {11,12,13,16}
import { SQL, asc } from 'drizzle-orm';
import { PgColumn, PgSelect } from 'drizzle-orm/pg-core';

function withPagination<T extends PgSelect>(
  qb: T,
  orderByColumn: PgColumn | SQL | SQL.Aliased,
  page = 1,
  pageSize = 3,
) {
  return qb
    .orderBy(orderByColumn)
    .limit(pageSize)
    .offset((page - 1) * pageSize);
}

const query = db.select().from(users); // query that you want to execute with pagination

await withPagination(query.$dynamic(), asc(users.id));
```

</Section>

You can improve performance of `limit/offset` pagination by using `deferred join` technique. This method performs the pagination on a subset of the data instead of the entire table.

To implement it you can do like this:

```ts copy {10}
const getUsers = async (page = 1, pageSize = 10) => {
   const sq = db
    .select({ id: users.id })
    .from(users)
    .orderBy(users.id)
    .limit(pageSize)
    .offset((page - 1) * pageSize)
    .as('subquery');

   await db.select().from(users).innerJoin(sq, eq(users.id, sq.id)).orderBy(users.id);
};
```

**Benefits** of `limit/offset` pagination: it's simple to implement and pages are easily reachable, which means that you can navigate to any page without having to save the state of the previous pages.

**Drawbacks** of `limit/offset` pagination: degradation in query performance with increasing offset because database has to scan all rows before the offset to skip them, and inconsistency due to data shifts, which can lead to the same row being returned on different pages or rows being skipped.

This is how it works:

<Section>
```ts copy
const getUsers = async (page = 1, pageSize = 3) => {
  await db
    .select()
    .from(users)
    .orderBy(asc(users.id))
    .limit(pageSize)
    .offset((page - 1) * pageSize);
};

// user is browsing the first page
await getUsers();
```

```ts
// results for the first page
[
  {
    id: 1,
    firstName: 'Alice',
    lastName: 'Johnson',
    createdAt: 2024-03-10T17:17:06.148Z
  },
  {
    id: 2,
    firstName: 'Alex',
    lastName: 'Smith',
    createdAt: 2024-03-10T17:19:06.147Z
  },
  {
    id: 3,
    firstName: 'Aaron',
    lastName: 'Williams',
    createdAt: 2024-03-10T17:22:06.147Z
  }
]
```

```ts
// while user is browsing the first page, a row with id 2 is deleted
await db.delete(users).where(eq(users.id, 2));

// user navigates to the second page
await getUsers(2);
```

```ts
// second page, row with id 3 was skipped
[
  {
    id: 5,
    firstName: 'Beth',
    lastName: 'Davis',
    createdAt: 2024-03-10T17:34:06.147Z
  },
  {
    id: 6,
    firstName: 'Charlie',
    lastName: 'Miller',
    createdAt: 2024-03-10T17:58:06.147Z
  },
  {
    id: 7,
    firstName: 'Clara',
    lastName: 'Wilson',
    createdAt: 2024-03-10T18:16:06.147Z
  }
]
```
</Section>

So, if your database experiences frequently insert and delete operations in real time or you need high performance to paginate large tables, you should consider using [cursor-based](/docs/guides/cursor-based-pagination) pagination instead.

To learn more about `deferred join` technique you should follow these guides: [Planetscale Pagination Guide](https://planetscale.com/blog/mysql-pagination) and [Efficient Pagination Guide by Aaron Francis](https://aaronfrancis.com/2022/efficient-pagination-using-deferred-joins).


Source: https://orm.drizzle.team/docs/mysql-local-setup


import Section from "@mdx/Section.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Steps from '@mdx/Steps.astro';

<Prerequisites>
- Install latest [Docker Desktop](https://www.docker.com/products/docker-desktop/). Follow the instructions for your operating system.
</Prerequisites>

<Steps>


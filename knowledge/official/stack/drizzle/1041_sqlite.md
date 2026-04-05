### SQLite

SQLite doesn't have an array data type, but you can use `text` data type for the same purpose. To set an empty array as a default value in SQLite, you can use `json_array()` function or `sql` operator with `'[]'` syntax:

<Section>
```ts copy {9,13}
import { sql } from 'drizzle-orm';
import { integer, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const users = sqliteTable('users', {
  id: integer('id').primaryKey(),
  tags1: text('tags1', { mode: 'json' })
    .notNull()
    .$type<string[]>()
    .default(sql`(json_array())`),
  tags2: text('tags2', { mode: 'json' })
    .notNull()
    .$type<string[]>()
    .default(sql`'[]'`),
});
```

```sql
CREATE TABLE `users` (
	`id` integer PRIMARY KEY NOT NULL,
	`tags1` text DEFAULT (json_array()) NOT NULL,
	`tags2` text DEFAULT '[]' NOT NULL
);
```
</Section>

The `mode` option defines how values are handled in the application. With `json` mode, values are treated as JSON object literal. 

You can specify `.$type<..>()` for json object inference, it will not check runtime values. It provides compile time protection for default values, insert and select schemas.


Source: https://orm.drizzle.team/docs/full-text-search-with-generated-columns


import Section from "@mdx/Section.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql)
- [Select statement](/docs/select)
- [Indexes](/docs/indexes-constraints#indexes)
- [sql operator](/docs/sql) 
- [Full-text search](/learn/guides/postgresql-full-text-search)
- [Generated columns](/docs/generated-columns)
</Prerequisites>

This guide demonstrates how to implement full-text search in PostgreSQL with Drizzle and generated columns. A generated column is a special column that is always computed from other columns. It is useful because you don't have to compute the value of the column every time you query the table:

<CodeTabs items={["schema.ts", "migration.sql"]}>
  <CodeTab>
  ```ts copy {18,19,20,23}
import { SQL, sql } from 'drizzle-orm';
import { index, pgTable, serial, text, customType } from 'drizzle-orm/pg-core';

export const tsvector = customType<{
  data: string;
}>({
  dataType() {
    return `tsvector`;
  },
});

export const posts = pgTable(
  'posts',
  {
    id: serial('id').primaryKey(),
    title: text('title').notNull(),
    body: text('body').notNull(),
    bodySearch: tsvector('body_search')
      .notNull()
      .generatedAlwaysAs((): SQL => sql`to_tsvector('english', ${posts.body})`),
  },
  (t) => [
    index('idx_body_search').using('gin', t.bodySearch),
  ]
);
  ```
  </CodeTab>
  ```sql
CREATE TABLE "posts" (
	"id" serial PRIMARY KEY NOT NULL,
	"title" text NOT NULL,
	"body" text NOT NULL,
	"body_search" "tsvector" GENERATED ALWAYS AS (to_tsvector('english', "posts"."body")) STORED NOT NULL
);
--> statement-breakpoint
CREATE INDEX "idx_body_search" ON "posts" USING gin ("body_search");
  ```
</CodeTabs>

When you insert a row into a table, the value of a generated column is computed from an expression that you provide when you create the column:

<Section>
```ts 
import { posts } from './schema';

const db = drizzle(...);

const body = "Golden leaves cover the quiet streets as a crisp breeze fills the air, bringing the scent of rain and the promise of change"

await db.insert(posts).values({
    body,
    title: "The Beauty of Autumn",
  }
).returning();
```

```json
[
  {
    id: 1,
    title: 'The Beauty of Autumn',
    body: 'Golden leaves cover the quiet streets as a crisp breeze fills the air, bringing the scent of rain and the promise of change',
    bodySearch: "'air':13 'breez':10 'bring':14 'chang':23 'cover':3 'crisp':9 'fill':11 'golden':1 'leav':2 'promis':21 'quiet':5 'rain':18 'scent':16 'street':6"
  }
]
```
</Section>

This is how you can implement full-text search with generated columns in PostgreSQL with Drizzle ORM.  The `@@` operator is used for direct matches:

<Section>
```ts copy {6}
const searchParam = "bring";

await db
  .select()
  .from(posts)
  .where(sql`${posts.bodySearch} @@ to_tsquery('english', ${searchParam})`);
```

```sql
select * from posts where body_search @@ to_tsquery('english', 'bring');
```
</Section>

This is more advanced schema with a generated column. The `search` column is generated from the `title` and `body` columns and `setweight()` function is used to assign different weights to the columns for full-text search.
This is typically used to mark entries coming from different parts of a document, such as title versus body.

<CodeTabs items={["schema.ts", "migration.sql"]}>
  <CodeTab>
  ```ts copy {18,19,20,21,22,23,24,28}
import { SQL, sql } from 'drizzle-orm';
import { index, pgTable, serial, text, customType } from 'drizzle-orm/pg-core';

export const tsvector = customType<{
  data: string;
}>({
  dataType() {
    return `tsvector`;
  },
});

export const posts = pgTable(
 'posts',
 {
   id: serial('id').primaryKey(),
   title: text('title').notNull(),
   body: text('body').notNull(),
   search: tsvector('search')
     .notNull()
     .generatedAlwaysAs(
        (): SQL =>
         sql`setweight(to_tsvector('english', ${posts.title}), 'A')
          ||
          setweight(to_tsvector('english', ${posts.body}), 'B')`,
     ),
  },
  (t) => [
    index('idx_search').using('gin', t.search),
  ],
);
  ```
  </CodeTab>
  ```sql
CREATE TABLE "posts" (
	"id" serial PRIMARY KEY NOT NULL,
	"title" text NOT NULL,
	"body" text NOT NULL,
	"search" "tsvector" GENERATED ALWAYS AS (setweight(to_tsvector('english', "posts"."title"), 'A')
          ||
          setweight(to_tsvector('english', "posts"."body"), 'B')) STORED NOT NULL
);
--> statement-breakpoint
CREATE INDEX "idx_search" ON "posts" USING gin ("search");
  ```
</CodeTabs>

This is how you can query the table with full-text search:

<Section>
```ts copy {6}
const search = 'travel';

await db
  .select()
  .from(posts)
  .where(sql`${posts.search} @@ to_tsquery('english', ${search})`);
```

```sql
select * from posts where search @@ to_tsquery('english', 'travel');
```
</Section>


Source: https://orm.drizzle.team/docs/gel-ext-auth

import Prerequisites from "@mdx/Prerequisites.astro";
import Callout from "@mdx/Callout.astro";
import Npx from "@mdx/Npx.astro";

<Prerequisites>
- Get started with [Gel](/docs/get-started-gel)
- Using [drizzle-kit pull](/docs/drizzle-kit-pull)
</Prerequisites>


### PostgreSQL

To set an empty array as a default value in PostgreSQL, you can use `sql` operator with `'{}'` or `ARRAY[]` syntax:

<Section>
```ts copy {10,14}
import { sql } from 'drizzle-orm';
import { pgTable, serial, text } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  tags1: text('tags1')
    .array()
    .notNull()
    .default(sql`'{}'::text[]`),
  tags2: text('tags2')
    .array()
    .notNull()
    .default(sql`ARRAY[]::text[]`),
});
```

```sql
CREATE TABLE IF NOT EXISTS "users" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" text NOT NULL,
	"tags1" text[] DEFAULT '{}'::text[] NOT NULL,
	"tags2" text[] DEFAULT ARRAY[]::text[] NOT NULL
);
```
</Section>



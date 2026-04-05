### MySQL

MySQL doesn't have an array data type, but you can use `json` data type for the same purpose. To set an empty array as a default value in MySQL, you can use `JSON_ARRAY()` function or `sql` operator with `('[]')` syntax:

<Section>
```ts copy {7,11,15}
import { sql } from 'drizzle-orm';
import { json, mysqlTable, serial, varchar } from 'drizzle-orm/mysql-core';

export const users = mysqlTable('users', {
  id: serial('id').primaryKey(),
  name: varchar('name', { length: 255 }).notNull(),
  tags1: json('tags1').$type<string[]>().notNull().default([]),
  tags2: json('tags2')
    .$type<string[]>()
    .notNull()
    .default(sql`('[]')`), // the same as default([])
  tags3: json('tags3')
    .$type<string[]>()
    .notNull()
    .default(sql`(JSON_ARRAY())`),
});
```

```sql
CREATE TABLE `users` (
	`id` serial AUTO_INCREMENT NOT NULL,
	`name` varchar(255) NOT NULL,
	`tags1` json NOT NULL DEFAULT ('[]'),
	`tags2` json NOT NULL DEFAULT ('[]'),
	`tags3` json NOT NULL DEFAULT (JSON_ARRAY()),
	CONSTRAINT `users_id` PRIMARY KEY(`id`)
);
```
</Section>

The `mode` option defines how values are handled in the application. With `json` mode, values are treated as JSON object literal. 

You can specify `.$type<..>()` for json object inference, it will not check runtime values. It provides compile time protection for default values, insert and select schemas.


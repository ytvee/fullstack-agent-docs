# SQL Select
Drizzle provides you the most SQL-like way to fetch data from your database, while remaining type-safe and composable.
It natively supports mostly every query feature and capability of every dialect,
and whatever it doesn't support yet, can be added by the user with the powerful [`sql`](/docs/sql) operator.

For the following examples, let's assume you have a `users` table defined like this:
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
<Tab>
```typescript
import { pgTable, serial, text } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age'),
});
```
</Tab>
<Tab>
```typescript
import { mysqlTable, serial, text, int } from 'drizzle-orm/mysql-core';

export const users = mysqlTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: int('age'),
});
```
</Tab>
<Tab>
```typescript
import { sqliteTable, integer, text } from 'drizzle-orm/sqlite-core';

export const users = sqliteTable('users', {
  id: integer('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age'),
});
```
</Tab>
<Tab>
```typescript
import { singlestoreTable, serial, text, int } from 'drizzle-orm/singlestore-core';

export const users = singlestoreTable('users', {
  id: int('id').primaryKey(),
  name: text('name').notNull(),
  age: int('age'),
});
```
</Tab>
<Tab>
```typescript
import { mssqlTable, int, text } from 'drizzle-orm/mssql-core';

export const users = pgTable('users', {
  id: int().primaryKey(),
  name: text().notNull(),
  age: int(),
});
```
</Tab>
<Tab>
```typescript
import { cockroachTable, int4, text } from 'drizzle-orm/cockroach-core';

export const users = pgTable('users', {
  id: int4().primaryKey(),
  name: text().notNull(),
  age: int4(),
});
```
</Tab>
</Tabs>


#### **Tables and columns declaration** 

A table in Drizzle should be defined with at least 1 column, the same as it should be done in database. There is one important thing to know,
there is no such thing as a common table object in drizzle. You need to choose a dialect you are using, PostgreSQL, MySQL or SQLite

![](@/assets/images/table-structure.svg)

<CodeTabs items={["PostgreSQL Table", "MySQL Table", "SQLite Table"]}>
```ts copy
import { pgTable, integer } from "drizzle-orm/pg-core"

export const users = pgTable('users', {
  id: integer()
});
```
```ts copy
import { mysqlTable, int } from "drizzle-orm/mysql-core"

export const users = mysqlTable('users', {
  id: int()
});
```
```ts copy
import { sqliteTable, integer } from "drizzle-orm/sqlite-core"

export const users = sqliteTable('users', {
  id: integer()
});
```
</CodeTabs>

By default, Drizzle will use the TypeScript key names for columns in database queries. 
Therefore, the schema and query from the example will generate the SQL query shown below

<Callout>
This example uses a db object, whose initialization is not covered in this part of the documentation. To learn how to connect to the database, please refer to the [Connections Docs](/docs/get-started-postgresql)
</Callout>

\
**TypeScript key = database key**
<Section>
```ts
// schema.ts
import { integer, pgTable, varchar } from "drizzle-orm/pg-core";

export const users = pgTable('users', {
  id: integer(),
  first_name: varchar()
})
```
```ts
// query.ts
await db.select().from(users);
```
```sql
SELECT "id", "first_name" from users;
```
</Section>

If you want to use different names in your TypeScript code and in the database, you can use column aliases

<Section>
```ts
// schema.ts
import { integer, pgTable, varchar } from "drizzle-orm/pg-core";

export const users = pgTable('users', {
  id: integer(),
  firstName: varchar('first_name')
})
```
```ts
// query.ts
await db.select().from(users);
```
```sql
SELECT "id", "first_name" from users;
```
</Section>


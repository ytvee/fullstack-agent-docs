#### **Schemas**

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
\
In PostgreSQL, there is an entity called a `schema` (which we believe should be called `folders`). This creates a structure in PostgreSQL:

![](@/assets/images/postgresql-db-structure.png)

You can manage your PostgreSQL schemas with `pgSchema` and place any other models inside it.

Define the schema you want to manage using Drizzle
```ts
import { pgSchema } from "drizzle-orm/pg-core"

export const customSchema = pgSchema('custom');
```

Then place the table inside the schema object
```ts {5-7}
import { integer, pgSchema } from "drizzle-orm/pg-core";

export const customSchema = pgSchema('custom');

export const users = customSchema.table('users', {
  id: integer()
})
```
</Tab>
<Tab>
\
In MySQL, there is an entity called `Schema`, but in MySQL terms, this is equivalent to a `Database`. 

You can define them with `drizzle-orm` and use them in queries, but they won't be detected by `drizzle-kit` or included in the migration flow

![](@/assets/images/mysql-db-structure.png)

Define the schema you want to manage using Drizzle
```ts
import { mysqlSchema } from "drizzle-orm/mysql-core"

export const customSchema = mysqlSchema('custom');
```

Then place the table inside the schema object
```ts {5-7}
import { int, mysqlSchema } from "drizzle-orm/mysql-core";

export const customSchema = mysqlSchema('custom');

export const users = customSchema.table('users', {
  id: int()
})
```
</Tab>
<Tab>
\
In SQLite, there is no concept of a schema, so you can only define tables within a single SQLite file context

![](@/assets/images/sqlite-db-structure.png)
</Tab>
</Tabs>


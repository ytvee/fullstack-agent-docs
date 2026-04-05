### Camel and Snake casing

Database model names often use `snake_case` conventions, while in TypeScript, it is common to use `camelCase` for naming models. 
This can lead to a lot of alias definitions in the schema. To address this, Drizzle provides a way to automatically 
map `camelCase` from TypeScript to `snake_case` in the database by including one optional parameter during Drizzle database initialization

For such mapping, you can use the `casing` option in the Drizzle DB declaration. This parameter will 
help you specify the database model naming convention and will attempt to map all JavaScript keys accordingly

<Section>
```ts
// schema.ts
import { drizzle } from "drizzle-orm/node-postgres";
import { integer, pgTable, varchar } from "drizzle-orm/pg-core";

export const users = pgTable('users', {
  id: integer(),
  firstName: varchar()
})
```
```ts
// db.ts
const db = drizzle({ connection: process.env.DATABASE_URL, casing: 'snake_case' })
```
```ts
// query.ts
await db.select().from(users);
```
```sql
SELECT "id", "first_name" from users;
```
</Section>


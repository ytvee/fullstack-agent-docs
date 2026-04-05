#### Create a table

Create a `schema.ts` file in the `src/db` directory and declare a table schema:

```typescript copy filename="src/db/schema.ts"
import { integer, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const usersTable = sqliteTable('users_table', {
  id: integer('id').primaryKey(),
  name: text('name').notNull(),
  age: text('age').notNull(),
  email: text('email').notNull().unique(),
})
```


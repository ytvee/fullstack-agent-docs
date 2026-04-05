#### Create a table

Create a `schema.ts` file in your `src` directory and declare a table schema:

```typescript copy filename="src/schema.ts"
import { pgTable, serial, text, integer } from "drizzle-orm/pg-core";

export const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull()
})
```

This file will be used to generate migrations for your database.


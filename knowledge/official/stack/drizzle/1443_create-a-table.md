#### Create a table

Create a `schema.ts` file in the `src/db` directory and declare a table schema:

```typescript copy filename="src/db/schema.ts"
import { pgTable, serial, text } from "drizzle-orm/pg-core";

export const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: text('age').notNull(),
  email: text('email').notNull().unique(),
})
```


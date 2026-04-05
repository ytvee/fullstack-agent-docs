#### Create a table

Create a `schema.ts` file in the `netlify/edge-functions/common` directory and declare a table schema:

```typescript copy filename="netlify/edge-functions/common/schema.ts"
import { pgTable, serial, text, integer } from "drizzle-orm/pg-core";

export const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull(),
  email: text('email').notNull().unique(),
})
```


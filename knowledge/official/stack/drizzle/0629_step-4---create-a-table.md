#### Step 4 - Create a table

Create a `schema.ts` file in the `db` directory and declare your table:

```typescript copy filename="src/db/schema.ts"
import { int, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const usersTable = sqliteTable("users_table", {
  id: int().primaryKey({ autoIncrement: true }),
  name: text().notNull(),
  age: int().notNull(),
  email: text().notNull().unique(),
});
```


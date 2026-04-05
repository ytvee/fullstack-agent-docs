#### Declare todo schema

```tsx copy filename="src/db/schema.ts"
import { integer, text, boolean, pgTable } from "drizzle-orm/pg-core";

export const todo = pgTable("todo", {
  id: integer("id").primaryKey(),
  text: text("text").notNull(),
  done: boolean("done").default(false).notNull(),
});
```

Here we define the **`todo`** table with fields **`id`**, **`text`**, and **`done`**, using data types from Drizzle ORM.


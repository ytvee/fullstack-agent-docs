#### Define your schema

Create a `schema.ts` file to define your tables:

```typescript copy filename="schema.ts"
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text().notNull(),
  email: p.text().unique().notNull(),
  createdAt: p.timestamp().defaultNow().notNull(),
});
```


### Factory functions

For more advanced use cases, you can use the `createSchemaFactory` function.

**Use case: Using an extended Typebox instance**

```ts copy
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createSchemaFactory } from 'drizzle-orm/typebox';
import { t } from 'elysia'; // Extended Typebox instance

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const { createInsertSchema } = createSchemaFactory({ typeboxInstance: t });

const userInsertSchema = createInsertSchema(users, {
  // We can now use the extended instance
  name: (schema) => t.Number({ ...schema }, { error: '`name` must be a string' })
});
```


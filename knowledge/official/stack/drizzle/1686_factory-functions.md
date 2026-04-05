### Factory functions

For more advanced use cases, you can use the `createSchemaFactory` function.

**Use case: Using an extended Zod instance**

```ts copy
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createSchemaFactory } from 'drizzle-orm/zod';
import { z } from '@hono/zod-openapi'; // Extended Zod instance

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const { createInsertSchema } = createSchemaFactory({ zodInstance: z });

const userInsertSchema = createInsertSchema(users, {
  // We can now use the extended instance
  name: (schema) => schema.openapi({ example: 'John' })
});
```

**Use case: Type coercion**

```ts copy
import { pgTable, timestamp } from 'drizzle-orm/pg-core';
import { createSchemaFactory } from 'drizzle-orm/zod';
import { z } from 'zod/v4';

const users = pgTable('users', {
  ...,
  createdAt: timestamp().notNull()
});

const { createInsertSchema } = createSchemaFactory({
  // This configuration will only coerce dates. Set `coerce` to `true` to coerce all data types or specify others
  coerce: {
    date: true
  }
});

const userInsertSchema = createInsertSchema(users);
// The above is the same as this:
const userInsertSchema = z.object({
  ...,
  createdAt: z.coerce.date()
});
```


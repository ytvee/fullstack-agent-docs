### Refinements

Each create schema function accepts an additional optional parameter that you can used to extend, modify or completely overwite a field's schema. Defining a callback function will extend or modify while providing a Zod schema will overwrite it.

```ts copy
import { pgTable, text, integer, json } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/zod';
import { z } from 'zod/v4';

const users = pgTable('users', {
  id: integer().primaryKey(),
  name: text().notNull(),
  bio: text(),
  preferences: json()
});

const userSelectSchema = createSelectSchema(users, {
  name: (schema) => schema.max(20), // Extends schema
  bio: (schema) => schema.max(1000), // Extends schema before becoming nullable/optional
  preferences: z.object({ theme: z.string() }) // Overwrites the field, including its nullability
});

const parsed: {
  id: number;
  name: string,
  bio?: string | undefined;
  preferences: {
    theme: string;
  };
} = userSelectSchema.parse(...);
```


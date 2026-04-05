### Refinements

Each create schema function accepts an additional optional parameter that you can used to extend, modify or completely overwite a field's schema. Defining a callback function will extend or modify while providing a Valibot schema will overwrite it.

```ts copy
import { pgTable, text, integer, json } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/valibot';
import { parse, pipe, maxLength, object, string } from 'valibot';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  bio: text(),
  preferences: json()
});

const userSelectSchema = createSelectSchema(users, {
  name: (schema) => pipe(schema, maxLength(20)), // Extends schema
  bio: (schema) => pipe(schema, maxLength(1000)), // Extends schema before becoming nullable/optional
  preferences: object({ theme: string() }) // Overwrites the field, including its nullability
});

const parsed: {
  id: number;
  name: string,
  bio?: string | undefined;
  preferences: {
    theme: string;
  };
} = parse(userSelectSchema, ...);
```


### Refinements

Each create schema function accepts an additional optional parameter that you can used to extend, modify or completely overwite a field's schema. Defining a callback function will extend or modify while providing a Typebox schema will overwrite it.

```ts copy
import { pgTable, text, integer, json } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/typebox-legacy';
import { Type } from '@sinclair/typebox';
import { Value } from '@sinclair/typebox/value';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  bio: text(),
  preferences: json()
});

const userSelectSchema = createSelectSchema(users, {
  name: (schema) => Type.String({ ...schema, maxLength: 20 }), // Extends schema
  bio: (schema) => Type.String({ ...schema, maxLength: 1000 }), // Extends schema before becoming nullable/optional
  preferences: Type.Object({ theme: Type.String() }) // Overwrites the field, including its nullability
});

const parsed: {
  id: number;
  name: string,
  bio?: string | undefined;
  preferences: {
    theme: string;
  };
} = Value.Parse(userSelectSchema, ...);
```


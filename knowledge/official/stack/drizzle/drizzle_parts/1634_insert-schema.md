### Insert schema

Defines the shape of data to be inserted into the database - can be used to validate API requests.

```ts copy
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createInsertSchema } from 'drizzle-orm/typebox-legacy';
import { Value } from '@sinclair/typebox/value';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userInsertSchema = createInsertSchema(users);

const user = { name: 'John' };
const parsed: { name: string, age: number } = Value.Parse(userInsertSchema, user); // Error: `age` is not defined

const user = { name: 'Jane', age: 30 };
const parsed: { name: string, age: number } = Value.Parse(userInsertSchema, user); // Will parse successfully
await db.insert(users).values(parsed);
```


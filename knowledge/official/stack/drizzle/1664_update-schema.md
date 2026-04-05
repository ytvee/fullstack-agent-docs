### Update schema

Defines the shape of data to be updated in the database - can be used to validate API requests.

```ts copy
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createUpdateSchema } from 'drizzle-orm/valibot';
import { parse } from 'valibot';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userUpdateSchema = createUpdateSchema(users);

const user = { id: 5, name: 'John' };
const parsed: { name?: string | undefined, age?: number | undefined } = parse(userUpdateSchema, user); // Error: `id` is a generated column, it can't be updated

const user = { age: 35 };
const parsed: { name?: string | undefined, age?: number | undefined } = parse(userUpdateSchema, user); // Will parse successfully
await db.update(users).set(parsed).where(eq(users.name, 'Jane'));
```


### Select schema

Defines the shape of data queried from the database - can be used to validate API responses.

```ts copy
import { pgTable, text, integer } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/arktype';

const users = pgTable('users', {
  id: integer().generatedAlwaysAsIdentity().primaryKey(),
  name: text().notNull(),
  age: integer().notNull()
});

const userSelectSchema = createSelectSchema(users);

const rows = await db.select({ id: users.id, name: users.name }).from(users).limit(1);
const parsed: { id: number; name: string; age: number } = userSelectSchema(rows[0]); // Error: `age` is not returned in the above query

const rows = await db.select().from(users).limit(1);
const parsed: { id: number; name: string; age: number } = userSelectSchema(rows[0]); // Will parse successfully
```

Views and enums are also supported.

```ts copy
import { pgEnum } from 'drizzle-orm/pg-core';
import { createSelectSchema } from 'drizzle-orm/arktype';

const roles = pgEnum('roles', ['admin', 'basic']);
const rolesSchema = createSelectSchema(roles);
const parsed: 'admin' | 'basic' = rolesSchema(...);

const usersView = pgView('users_view').as((qb) => qb.select().from(users).where(gt(users.age, 18)));
const usersViewSchema = createSelectSchema(usersView);
const parsed: { id: number; name: string; age: number } = usersViewSchema(...);
```


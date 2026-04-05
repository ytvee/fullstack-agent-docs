### Many-to-many
Drizzle ORM provides you an API to define `many-to-many` relations between tables through so called `junction` or `join` tables,
they have to be explicitly defined and store associations between related tables.  

Example of `many-to-many` relation between users and groups we are using `through` to bypass junction table selection and directly select many `groups` for each `user`.
```typescript copy {27-39}
import { defineRelations } from 'drizzle-orm';
import { integer, pgTable, primaryKey, text } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
  id: integer().primaryKey(),
  name: text(),
});

export const groups = pgTable('groups', {
  id: integer().primaryKey(),
  name: text(),
});

export const usersToGroups = pgTable(
  'users_to_groups',
  {
    userId: integer('user_id')
      .notNull()
      .references(() => users.id),
    groupId: integer('group_id')
      .notNull()
      .references(() => groups.id),
  },
  (t) => [primaryKey({ columns: [t.userId, t.groupId] })],
);

export const relations = defineRelations({ users, groups, usersToGroups },
  (r) => ({
    users: {
      groups: r.many.groups({
        from: r.users.id.through(r.usersToGroups.userId),
        to: r.groups.id.through(r.usersToGroups.groupId),
      }),
    },
    groups: {
      participants: r.many.users(),
    },
  })
);
```

**Query example:**
```ts
const res = await db.query.users.findMany({
  with: { 
    groups: true 
  },
});

// response type
type Response = {
  id: number;
  name: string | null;
  groups: {
    id: number;
    name: string | null;
  }[];
}[];
```

<Callout type='error' title='Relational Queries v1'>
Previously, you would need to query through a `junction` table and then map it out for every response

❌ You don't need to do it now!
```ts
const response = await db._query.users.findMany({
	with: {
		usersToGroups: {
			columns: {},
			with: {
				groups: true,
			},
		},
	},
});

// response type
type Response = {
  id: number;
  name: string | null;
  usersToGroups: {
    groups: {
       id: number;
       name: string | null;
    }
  }[];
}[];
```
</Callout>


#### Many-to-many Relationships

Many-to-many relationships, implemented using junction tables, require a slightly 
more nuanced indexing strategy to ensure optimal query performance. 
Consider the "users and groups" example with the `usersToGroups` junction table.

<Callout>
For many-to-many relationships, it is generally recommended to create the following 
indexes on the junction table:
1.  **Index on each foreign key column individually:** This optimizes queries that 
filter or join based on a single side of the relationship 
(e.g., finding all groups for a user OR all users in a group).
2.  **Composite index on both foreign key columns together:** This is crucial for 
efficiently resolving the many-to-many relationship itself. It speeds up queries that need to find the connections between both entities.
</Callout>

<Callout collapsed='Why it is important'>
When querying many-to-many relations, especially when using `through` in Drizzle ORM, the database needs to efficiently navigate the junction table.

- Indexes on individual foreign key columns (`userId`, `groupId` in `usersToGroups`) help when you are querying from one side to find the other (e.g., "find groups for a user").
- The composite index on `(userId, groupId)` in `usersToGroups` is particularly important for quickly finding all relationships defined in the junction table. This is used when Drizzle ORM resolves the `many-to-many` relation to fetch related entities.
</Callout>

**Example:**

In the "users and groups" example, the `usersToGroups` junction table connects `users` and `groups`.

```typescript
import { defineRelations } from 'drizzle-orm';
import * as p from 'drizzle-orm/pg-core';

export const users = p.pgTable('users', {
  id: p.integer().primaryKey(),
  name: p.text(),
});

export const groups = p.pgTable('groups', {
  id: p.integer().primaryKey(),
  name: p.text(),
});

export const usersToGroups = p.pgTable(
  'users_to_groups',
  {
    userId: p.integer('user_id')
      .notNull()
      .references(() => users.id),
    groupId: p.integer('group_id')
      .notNull()
      .references(() => groups.id),
  },
  (t) => [p.primaryKey({ columns: [t.userId, t.groupId] })],
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

To optimize queries for users and groups, create indexes on `usersToGroups` table as follows:

```typescript {26-28}
import { defineRelations } from 'drizzle-orm';
import * as p from 'drizzle-orm/pg-core';

export const users = p.pgTable('users', {
  id: p.integer().primaryKey(),
  name: p.text(),
});

export const groups = p.pgTable('groups', {
  id: p.integer().primaryKey(),
  name: p.text(),
});

export const usersToGroups = p.pgTable(
  'users_to_groups',
  {
    userId: p.integer('user_id')
      .notNull()
      .references(() => users.id),
    groupId: p.integer('group_id')
      .notNull()
      .references(() => groups.id),
  },
  (t) => [
    p.primaryKey({ columns: [t.userId, t.groupId] }),
    p.index('users_to_groups_user_id_idx').on(table.userId),
    p.index('users_to_groups_group_id_idx').on(table.groupId),
    p.index('users_to_groups_composite_idx').on(table.userId, table.groupId),
  ],
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
```sql
CREATE INDEX idx_users_to_groups_user_id ON users_to_groups (user_id);
CREATE INDEX idx_users_to_groups_group_id ON users_to_groups (group_id);
CREATE INDEX idx_users_to_groups_composite ON users_to_groups (userId, groupId);
```

By applying these indexing strategies, you can significantly improve the performance of your Drizzle ORM applications when working with relational data, especially as your data volume grows and your queries become more complex. Remember to choose the indexes that best suit your specific query patterns and application needs.


##### What is new?

**`through` for many-to-many relations**

Previously, you would need to query through a junction table and then map it out for every response

You don't need to do it now!

<Callout collapsed='Schema'>
```ts
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.integer().primaryKey(),
  name: p.text(),
  verified: p.boolean().notNull(),
});

export const groups = p.pgTable("groups", {
  id: p.integer().primaryKey(),
  name: p.text(),
});

export const usersToGroups = p.pgTable(
  "users_to_groups",
  {
    userId: p
      .integer("user_id")
      .notNull()
      .references(() => users.id),
    groupId: p
      .integer("group_id")
      .notNull()
      .references(() => groups.id),
  },
  (t) => [p.primaryKey({ columns: [t.userId, t.groupId] })]
);
```
</Callout>

<Callout title="❌ v1">
```ts
export const usersRelations = relations(users, ({ many }) => ({
  usersToGroups: many(usersToGroups),
}));

export const groupsRelations = relations(groups, ({ many }) => ({
  usersToGroups: many(usersToGroups),
}));

export const usersToGroupsRelations = relations(usersToGroups, ({ one }) => ({
  group: one(groups, {
    fields: [usersToGroups.groupId],
    references: [groups.id],
  }),
  user: one(users, {
    fields: [usersToGroups.userId],
    references: [users.id],
  }),
}));
```
```ts
// Query example
const response = await db.query.users.findMany({
  with: {
    usersToGroups: {
      columns: {},
      with: {
        group: true,
      },
    },
  },
});
```
</Callout>

<Callout title='✅ v2'>
```ts
import * as schema from './schema';
import { defineRelations } from 'drizzle-orm';

export const relations = defineRelations(schema, (r) => ({
  users: {
    groups: r.many.groups({
      from: r.users.id.through(r.usersToGroups.userId),
      to: r.groups.id.through(r.usersToGroups.groupId),
    }),
  },
  groups: {
    participants: r.many.users(),
  },
}));
```
```ts
// Query example
const response = await db.query.users.findMany({
  with: {
    groups: true,
  },
});
```
</Callout>

**Predefined filters**

<Callout title="❌ v1">
Was not supported in v1
</Callout>

<Callout title='✅ v2'>
```ts {10-12}
import * as schema from './schema';
import { defineRelations } from 'drizzle-orm';

export const relations = defineRelations(schema,
  (r) => ({
    groups: {
      verifiedUsers: r.many.users({
        from: r.groups.id.through(r.usersToGroups.groupId),
        to: r.users.id.through(r.usersToGroups.userId),
        where: {
          verified: true,
        },
      }),
    },
  })
);
```
```ts {4}
// Query example: get groups with all verified users
const response = await db.query.groups.findMany({
  with: {
    verifiedUsers: true,
  },
});
```
</Callout>


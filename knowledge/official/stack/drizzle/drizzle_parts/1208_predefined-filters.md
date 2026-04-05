### Predefined filters

Predefined `where` statements in Drizzle's relation definitions are a type of polymorphic relations implementation, but it's not fully it. Essentially, they allow you to
connect tables not only by selecting specific columns but also through custom `where` statements. Let's look at some examples:

We can define a relation between `groups` and `users` so that when querying group's users, we only retrieve those whose `verified` column is set to `true`
<CodeTabs items={["Relations", "Schema"]}>
<Section>
```ts
import { defineRelations } from "drizzle-orm";
import * as p from "drizzle-orm/pg-core";
import * as schema from './schema';

export const relations = defineRelations(schema,(r) => ({
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

...

await db.query.groups.findMany({
    with: {
      verifiedUsers: true,
    },
});
```
</Section>
<Section>
```ts
import { defineRelations } from "drizzle-orm";
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.integer().primaryKey(),
  name: p.text().notNull(),
  verified: p.boolean().notNull(),
});

export const groups = p.pgTable("groups", {
  id: p.integer().primaryKey(),
  title: p.text().notNull(),
});

export const usersToGroups = p.pgTable(
  "users_to_groups",
  {
    userId: p
      .integer("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    groupId: p
      .integer("group_id")
      .notNull()
      .references(() => groups.id, { onDelete: "cascade" }),
  },
  (t) => [p.primaryKey({ columns: [t.groupId, t.userId] })]
);
```
</Section>
</CodeTabs>

<Callout type='warning'>
You can only specify filters on the target (to) table. So in this example, the where clause will only include columns from the `users` table since we are establishing a relation **TO** users

```ts {7}
export const relations = defineRelations(schema,(r) => ({
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
</Callout>


##### Migrate `many-to-many` queries

Relational Queries v1 had a very complex way of managing many-to-many queries.
You had to use junction tables to query through them explicitly, and then map those tables out, like this:

```ts
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

After upgrading to Relational Queries v2, your many-to-many relation will look like this:

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

And when you migrate your query, it will become this:

```ts
// Query example
const response = await db.query.users.findMany({
  with: {
    groups: true,
  },
});
```


### Relations Filters

With Drizzle Relations, you can filter not only by the table you're querying but also by any table you include in the query.

**Example:** Get all `users` whose ID>10 and who have at least one post with content starting with "M"
```ts
const usersWithPosts = await db.query.usersTable.findMany({
  where: {
    id: {
      gt: 10
    },
    posts: {
      content: {
        like: 'M%'
      }
    }
  },
});
```

**Example:** Get all `users` with posts, only if user has at least 1 post
```ts
const response = db.query.users.findMany({
  with: {
    posts: true,
  },
  where: {
    posts: true,
  },
});
```


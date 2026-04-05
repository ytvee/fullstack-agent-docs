##### Filtering by relations

<Callout title="❌ v1">
Was not supported in v1
</Callout>

<Callout title='✅ v2'>
Example: Get all users whose ID>10 and who have at least one post with content starting with “M”

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
</Callout>


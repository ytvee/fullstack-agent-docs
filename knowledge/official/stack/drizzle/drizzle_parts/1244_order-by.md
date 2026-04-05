### Order By
Drizzle provides API for ordering in the relational query builder.  

You can use same ordering **[core API](/docs/select#order-by)** or use
`order by` operator from the callback with no imports.  

<Callout title='important'>
When you use multiple `orderBy` statements in the same table, they will be included in the query in the same order in which you added them
</Callout>

<Section>
```typescript copy
await db.query.posts.findMany({
  orderBy: {
    id: "asc",
  },
});
```
</Section>

**Order by `asc` + `desc`:**
```typescript copy
  await db.query.posts.findMany({
    orderBy: { id: "asc" },
    with: {
      comments: {
        orderBy: { id: "desc" },
      },
    },
  });
```

You can also use custom `sql` in order by statement:

```typescript copy
await db.query.posts.findMany({
  orderBy: (t) => sql`${t.id} asc`,
  with: {
    comments: {
      orderBy: (t, { desc }) => desc(t.id),
    },
  },
});
```


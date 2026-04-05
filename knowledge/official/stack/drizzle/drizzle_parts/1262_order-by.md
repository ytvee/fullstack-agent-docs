### Order By
Drizzle provides API for ordering in the relational query builder.  

You can use same ordering **[core API](/docs/select#order-by)** or use
`order by` operator from the callback with no imports.  

<Section>
```typescript copy
import { desc, asc } from 'drizzle-orm';

await db._query.posts.findMany({
	orderBy: [asc(posts.id)],
});
```
```typescript copy
await db._query.posts.findMany({
	orderBy: (posts, { asc }) => [asc(posts.id)],
});
```
</Section>

**Order by `asc` + `desc`:**
```typescript copy
await db._query.posts.findMany({
	orderBy: (posts, { asc }) => [asc(posts.id)],
	with: {
		comments: {
			orderBy: (comments, { desc }) => [desc(comments.id)],
		},
	},
});
```


### Select filters
Just like in our SQL-like query builder, 
relational queries API lets you define filters and conditions with the list of our **[`operators`](/docs/operators)**.  

You can either import them from `drizzle-orm` or use from the callback syntax:
<Section>
```typescript copy
import { eq } from 'drizzle-orm';

const users = await db._query.users.findMany({
	where: eq(users.id, 1)
})
```
```ts copy
const users = await db._query.users.findMany({
	where: (users, { eq }) => eq(users.id, 1),
})
```
</Section>

Find post with `id=1` and comments that were created before particular date:
```typescript copy
await db._query.posts.findMany({
	where: (posts, { eq }) => (eq(posts.id, 1)),
	with: {
		comments: {
			where: (comments, { lt }) => lt(comments.createdAt, new Date()),
		},
	},
});
```


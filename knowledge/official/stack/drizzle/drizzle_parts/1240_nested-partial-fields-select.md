### Nested partial fields select
Just like with **[`partial select`](#partial-select)**, you can include or exclude columns of nested relations:
```typescript copy
const posts = await db.query.posts.findMany({
	columns: {
		id: true,
		content: true,
	},
	with: {
		comments: {
			columns: {
				authorId: false
			}
		}
	}
});
```


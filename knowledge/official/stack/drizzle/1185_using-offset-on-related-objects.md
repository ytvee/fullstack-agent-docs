##### Using offset on related objects

<Callout title="❌ v1">
Was not supported in v1
</Callout>

<Callout title='✅ v2'>
```ts
await db.query.posts.findMany({
	limit: 5,
	offset: 2, // correct ✅
	with: {
		comments: {
			offset: 3, // correct ✅
			limit: 3,
		},
	},
});
```
</Callout>


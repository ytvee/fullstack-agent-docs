### Limit & Offset
Drizzle ORM provides `limit` & `offset` API for queries and for the nested entities.
  
**Find 5 posts:**
```typescript copy
await db._query.posts.findMany({
	limit: 5,
});
```

**Find posts and get 3 comments at most:**
```typescript copy
await db._query.posts.findMany({
	with: {
		comments: {
			limit: 3,
		},
	},
});
```

<Callout type="warning" emoji="⚠️">
  `offset` is only available for top level query.
</Callout>
```typescript 
await db._query.posts.findMany({
	limit: 5,
	offset: 2, // correct ✅
	with: {
		comments: {
			offset: 3, // incorrect ❌
			limit: 3,
		},
	},
});
```

Find posts with comments from the 5th to the 10th post:
```typescript copy
await db._query.posts.findMany({
	limit: 5,
  offset: 5,
	with: {
		comments: true,
	},
});
```


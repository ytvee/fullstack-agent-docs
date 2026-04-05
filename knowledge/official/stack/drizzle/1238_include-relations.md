### Include relations

`With` operator lets you combine data from multiple related tables and properly aggregate results.

**Getting all posts with comments:**
```typescript copy
const posts = await db.query.posts.findMany({
	with: {
		comments: true,
	},
});
```

**Getting first post with comments:**
```typescript copy
const post = await db.query.posts.findFirst({
	with: {
		comments: true,
	},
});
```

You can chain nested with statements as much as necessary.  
For any nested `with` queries Drizzle will infer types using [Core Type API](/docs/goodies#type-api).
  
**Get all users with posts. Each post should contain a list of comments:**
```typescript copy
const users = await db.query.users.findMany({
	with: {
		posts: {
			with: {
				comments: true,
			},
		},
	},
});
```


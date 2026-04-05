### Partial fields select
`columns` parameter lets you include or omit columns you want to get from the database.

<Callout type="info" emoji="ℹ️">
  Drizzle performs partial selects on the query level, no additional data is transferred from the database.

  Keep in mind that **a single SQL statement is outputted by Drizzle.**
</Callout>

**Get all posts with just `id`, `content` and include `comments`:**
```typescript copy
const posts = await db.query.posts.findMany({
	columns: {
		id: true,
		content: true,
	},
	with: {
		comments: true,
	}
});
```

**Get all posts without `content`:**
```typescript copy
const posts = await db.query.posts.findMany({
	columns: {
		content: false,
	},
});
```

<Callout type="info" emoji="ℹ️">
When both `true` and `false` select options are present, all `false` options are ignored.
</Callout>

If you include the `name` field and exclude the `id` field, `id` exclusion will be redundant, 
all fields apart from `name` would be excluded anyways.  
  
**Exclude and Include fields in the same query:**
<Section>
```typescript copy
const users = await db.query.users.findMany({
	columns: {
		name: true,
		id: false //ignored
	},
});
```
```ts
// result type
const users: {
	name: string;
};
```
</Section>

**Only include columns from nested relations:**
<Section>
```typescript copy
const res = await db.query.users.findMany({
	columns: {},
	with: {
		posts: true
	}
});
```
```ts
// result type
const res: {
	posts: {
		id: number,
		text: string
	}
}[];
```
</Section>


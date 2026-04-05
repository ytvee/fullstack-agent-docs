### Include custom fields
Relational query API lets you add custom additional fields. 
It's useful when you need to retrieve data and apply additional functions to it.
<Callout type="warning" emoji="⚠️">
	As of now aggregations are not supported in `extras`, please use **[`core queries`](/docs/select)** for that.
</Callout>

<Section>
```typescript copy {5}
import { sql } from 'drizzle-orm';

await db.query.users.findMany({
	extras: {
		loweredName: sql`lower(${users.name})`,
	},
})
```
```typescript copy {3}
await db.query.users.findMany({
	extras: {
		loweredName: (users, { sql }) => sql`lower(${users.name})`,
	},
})
```
</Section>

`lowerName` as a key will be included to all fields in returned object.

<Callout type="warning" emoji="⚠️">
  If you will specify `.as("<alias>")` for any extras field - drizzle will ignore it
</Callout>

To retrieve all users with groups, but with the fullName field included (which is a concatenation of firstName and lastName), 
you can use the following query with the Drizzle relational query builder.

<Section>
```typescript copy
const res = await db.query.users.findMany({
	extras: {
		fullName: (users, { sql }) => sql<string>`concat(${users.name}, " ", ${users.name})`,
	},
	with: {
		usersToGroups: {
			with: {
				group: true,
			},
		},
	},
});
```
```ts
// result type
const res: {
	id: number;
	name: string;
	verified: boolean;
	invitedBy: number | null;
	fullName: string;
	usersToGroups: {
			group: {
					id: number;
					name: string;
					description: string | null;
			};
	}[];
}[];

```
</Section>


To retrieve all posts with comments and add an additional field to calculate the size of the post content and the size of each comment content:
<Section>
```typescript copy
const res = await db.query.posts.findMany({
	extras: {
		contentLength: (table, { sql }) => sql<number>`length(${table.content})`,
	},
	with: {
		comments: {
			extras: {
				commentSize: (table, { sql }) => sql<number>`length(${table.content})`,
			},
		},
	},
});
```
```ts
// result type
const res: {
	id: number;
	createdAt: Date;
	content: string;
	authorId: number | null;
	contentLength: number;
	comments: {
			id: number;
			createdAt: Date;
			content: string;
			creator: number | null;
			postId: number | null;
			commentSize: number;
	}[];
};
```
</Section>


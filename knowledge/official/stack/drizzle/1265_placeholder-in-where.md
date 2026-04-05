##### **Placeholder in `where`**
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	where: ((users, { eq }) => eq(users.id, placeholder('id'))),
	with: {
		posts: {
			where: ((users, { eq }) => eq(users.id, placeholder('pid'))),
		},
	},
}).prepare('query_name');

const usersWithPosts = await prepared.execute({ id: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	where: ((users, { eq }) => eq(users.id, placeholder('id'))),
	with: {
		posts: {
			where: ((users, { eq }) => eq(users.id, placeholder('pid'))),
		},
	},
}).prepare();

const usersWithPosts = await prepared.execute({ id: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	where: ((users, { eq }) => eq(users.id, placeholder('id'))),
	with: {
		posts: {
			where: ((users, { eq }) => eq(users.id, placeholder('pid'))),
		},
	},
}).prepare();

const usersWithPosts = await prepared.execute({ id: 1 });
```
</Section>
</Tab>
</Tabs>



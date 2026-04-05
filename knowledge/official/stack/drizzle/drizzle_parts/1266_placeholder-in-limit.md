##### **Placeholder in `limit`**
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	with: {
		posts: {
			limit: placeholder('limit'),
		},
	},
}).prepare('query_name');

const usersWithPosts = await prepared.execute({ limit: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	with: {
		posts: {
			limit: placeholder('limit'),
		},
	},
}).prepare();

const usersWithPosts = await prepared.execute({ limit: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	with: {
		posts: {
			limit: placeholder('limit'),
		},
	},
}).prepare();

const usersWithPosts = await prepared.execute({ limit: 1 });
```
</Section>
</Tab>
</Tabs>



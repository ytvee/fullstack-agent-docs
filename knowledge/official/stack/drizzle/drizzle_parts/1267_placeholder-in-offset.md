##### **Placeholder in `offset`**
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	offset: placeholder('offset'),
	with: {
		posts: true,
	},
}).prepare('query_name');

const usersWithPosts = await prepared.execute({ offset: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	offset: placeholder('offset'),
	with: {
		posts: true,
	},
}).prepare();

const usersWithPosts = await prepared.execute({ offset: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	offset: placeholder('offset'),
	with: {
		posts: true,
	},
}).prepare();

const usersWithPosts = await prepared.execute({ offset: 1 });
```
</Section>
</Tab>
</Tabs>


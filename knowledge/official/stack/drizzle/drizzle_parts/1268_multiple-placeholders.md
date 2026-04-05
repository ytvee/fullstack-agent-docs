##### **Multiple placeholders**
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	limit: placeholder('uLimit'),
	offset: placeholder('uOffset'),
	where: ((users, { eq, or }) => or(eq(users.id, placeholder('id')), eq(users.id, 3))),
	with: {
		posts: {
			where: ((users, { eq }) => eq(users.id, placeholder('pid'))),
			limit: placeholder('pLimit'),
		},
	},
}).prepare('query_name');

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	limit: placeholder('uLimit'),
	offset: placeholder('uOffset'),
	where: ((users, { eq, or }) => or(eq(users.id, placeholder('id')), eq(users.id, 3))),
	with: {
		posts: {
			where: ((users, { eq }) => eq(users.id, placeholder('pid'))),
			limit: placeholder('pLimit'),
		},
	},
}).prepare();

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db._query.users.findMany({
	limit: placeholder('uLimit'),
	offset: placeholder('uOffset'),
	where: ((users, { eq, or }) => or(eq(users.id, placeholder('id')), eq(users.id, 3))),
	with: {
		posts: {
			where: ((users, { eq }) => eq(users.id, placeholder('pid'))),
			limit: placeholder('pLimit'),
		},
	},
}).prepare();

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```
</Section>
</Tab>
</Tabs>


Source: https://orm.drizzle.team/docs/schemas

import Tab from '@mdx/Tab.astro';
import Tabs from '@mdx/Tabs.astro';
import IsSupportedChipGroup from '@mdx/IsSupportedChipGroup.astro';
import Section from '@mdx/Section.astro';
import Callout from '@mdx/Callout.astro';


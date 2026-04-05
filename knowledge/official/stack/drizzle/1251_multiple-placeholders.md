##### **Multiple placeholders**
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
<Section>
```ts copy
const prepared = db.query.users.findMany({
    limit: sql.placeholder("uLimit"),
    offset: sql.placeholder("uOffset"),
    where: {
      OR: [{ id: { eq: sql.placeholder("id") } }, { id: 3 }],
    },
    with: {
      posts: {
        where: { id: { eq: sql.placeholder("pid") } },
        limit: sql.placeholder("pLimit"),
      },
    },
}).prepare("query_name");

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db.query.users.findMany({
    limit: sql.placeholder("uLimit"),
    offset: sql.placeholder("uOffset"),
    where: {
      OR: [{ id: { eq: sql.placeholder("id") } }, { id: 3 }],
    },
    with: {
      posts: {
        where: { id: { eq: sql.placeholder("pid") } },
        limit: sql.placeholder("pLimit"),
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
const prepared = db.query.users.findMany({
    limit: sql.placeholder("uLimit"),
    offset: sql.placeholder("uOffset"),
    where: {
      OR: [{ id: { eq: sql.placeholder("id") } }, { id: 3 }],
    },
    with: {
      posts: {
        where: { id: { eq: sql.placeholder("pid") } },
        limit: sql.placeholder("pLimit"),
      },
    },
}).prepare();

const usersWithPosts = await prepared.execute({ pLimit: 1, uLimit: 3, uOffset: 1, id: 2, pid: 6 });
```
</Section>
</Tab>
</Tabs>


Source: https://orm.drizzle.team/docs/rqb

import Tab from '@mdx/Tab.astro';
import Tabs from '@mdx/Tabs.astro';
import Callout from '@mdx/Callout.astro';
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Section from '@mdx/Section.astro';
import IsSupportedChipGroup from '@mdx/IsSupportedChipGroup.astro';


##### **Placeholder in `where`**
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
<Section>
```ts copy
const prepared = db.query.users.findMany({
    where: { id: { eq: sql.placeholder("id") } },
    with: {
      posts: {
        where: { id: 1 },
      },
    },
}).prepare("query_name");

const usersWithPosts = await prepared.execute({ id: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db.query.users.findMany({
    where: { id: { eq: sql.placeholder("id") } },
    with: {
      posts: {
        where: { id: 1 },
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
const prepared = db.query.users.findMany({
    where: { id: { eq: sql.placeholder("id") } },
    with: {
      posts: {
        where: { id: 1 },
      },
    },
}).prepare();

const usersWithPosts = await prepared.execute({ id: 1 });
```
</Section>
</Tab>
</Tabs>



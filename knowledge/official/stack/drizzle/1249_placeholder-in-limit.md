##### **Placeholder in `limit`**
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
<Section>
```ts copy
const prepared = db.query.users.findMany({
    with: {
      posts: {
        limit: sql.placeholder("limit"),
      },
    },
  }).prepare("query_name");

const usersWithPosts = await prepared.execute({ limit: 1 });
```
</Section>
</Tab>
<Tab>
<Section>
```ts copy
const prepared = db.query.users.findMany({
    with: {
      posts: {
        limit: sql.placeholder("limit"),
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
const prepared = db.query.users.findMany({
    with: {
      posts: {
        limit: sql.placeholder("limit"),
      },
    },
  }).prepare();

const usersWithPosts = await prepared.execute({ limit: 1 });
```
</Section>
</Tab>
</Tabs>



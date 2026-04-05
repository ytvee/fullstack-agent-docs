# Drizzle soft relations
The sole purpose of Drizzle relations is to let you query your relational data in the most simple and consise way:

<CodeTabs items={["Relational queries", "Select with joins"]}>
<Section>
```ts
import * as schema from './schema';
import { drizzle } from 'drizzle-orm/…';

const db = drizzle(client, { schema });

const result = db.query.users.findMany({
  with: {
    posts: true,
  },
});
```
```ts
[{
  id: 10,
  name: "Dan",
  posts: [
    {
      id: 1,
      content: "SQL is awesome",
      authorId: 10,
    },
    {
      id: 2,
      content: "But check relational queries",
      authorId: 10,
    }
  ]
}]
```
</Section>
<Section>
```ts
import { drizzle } from 'drizzle-orm/…';
import { eq } from 'drizzle-orm';
import { posts, users } from './schema';

const db = drizzle(client);

const res = await db.select()
                    .from(users)
                    .leftJoin(posts, eq(posts.authorId, users.id))
                    .orderBy(users.id)
const mappedResult =  
```
</Section>
</CodeTabs>



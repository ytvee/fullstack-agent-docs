### Include subqueries

You can also use subqueries within Relational Queries to leverage the power of custom SQL syntax

**Get users with posts and total posts count for each user**
```ts
import { posts } from './schema';
import { eq } from 'drizzle-orm';

await db.query.users.findMany({
  with: {
    posts: true
  },
  extras: {
    totalPostsCount: (table) => db.$count(posts, eq(posts.authorId, table.id)),
  }
});
```
```sql
select "d0"."id" as "id", "d0"."name" as "name", "posts"."r" as "posts", 
((select count(*) from "posts" where "posts"."author_id" = "d0"."id")) as "totalPostsCount" 
from "users" as "d0" 
left join lateral(
  select coalesce(json_agg(row_to_json("t".*)), '[]') as "r" 
  from (select "d1"."id" as "id", "d1"."content" as "content", "d1"."author_id" as "authorId" from "posts" as "d1" where "d0"."id" = "d1"."author_id") as "t"
) as "posts" on true
```


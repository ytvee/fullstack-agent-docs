### arrayContains
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': false, 'SQLite': false, 'SingleStore': false }} />
  
Test that a column or expression contains all elements of the list passed as the second argument

<Section>
```typescript
import { arrayContains } from "drizzle-orm";

const contains = await db.select({ id: posts.id }).from(posts)
  .where(arrayContains(posts.tags, ['Typescript', 'ORM']));

const withSubQuery = await db.select({ id: posts.id }).from(posts)
  .where(arrayContains(
    posts.tags,
    db.select({ tags: posts.tags }).from(posts).where(eq(posts.id, 1)),
  ));
```

```sql
select "id" from "posts" where "posts"."tags" @> {Typescript,ORM};
select "id" from "posts" where "posts"."tags" @> (select "tags" from "posts" where "posts"."id" = 1);
```
</Section>


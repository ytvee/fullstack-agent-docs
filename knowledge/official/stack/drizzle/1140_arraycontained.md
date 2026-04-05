### arrayContained
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': false, 'SQLite': false, 'SingleStore': false }} />
  
Test that the list passed as the second argument contains all elements of a column or expression

<Section>
```typescript
import { arrayContained } from "drizzle-orm";

const contained = await db.select({ id: posts.id }).from(posts)
  .where(arrayContained(posts.tags, ['Typescript', 'ORM']));
```

```sql
select "id" from "posts" where "posts"."tags" <@ {Typescript,ORM};
```
</Section>


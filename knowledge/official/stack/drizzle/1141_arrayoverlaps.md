### arrayOverlaps
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': false, 'SQLite': false, 'SingleStore': false }} />
  
Test that a column or expression contains any elements of the list passed as the second argument.

<Section>
```typescript
import { arrayOverlaps } from "drizzle-orm";

const overlaps = await db.select({ id: posts.id }).from(posts)
  .where(arrayOverlaps(posts.tags, ['Typescript', 'ORM']));
```

```sql
select "id" from "posts" where "posts"."tags" && {Typescript,ORM}
```
</Section>


Source: https://orm.drizzle.team/docs/overview

import Callout from '@mdx/Callout.astro';
import CodeTabs from '@mdx/CodeTabs.astro';
import YoutubeCards from '@mdx/YoutubeCards.astro';
import GetStartedLinks from '@mdx/GetStartedLinks/index.astro'


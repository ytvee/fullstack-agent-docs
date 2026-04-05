#### Indexes

With the available Drizzle indexes API, you should be able to write any indexes for PostGIS

**Examples**

```ts
// CREATE INDEX custom_idx ON table USING GIST (geom);

const table = pgTable('table', {
  	geo: geometry({ type: 'point' }),
}, (table) => [
  index('custom_idx').using('gist', table.geo)
])
```

Source: https://orm.drizzle.team/docs/extensions/singlestore


import Callout from '@mdx/Callout.astro';

<Callout>
Currently, there are no SingleStore extensions natively supported by Drizzle. Once those are added, we will have them here!
</Callout>

Source: https://orm.drizzle.team/docs/extensions/sqlite


import Callout from '@mdx/Callout.astro';

<Callout>
Currently, there are no SQLite extensions natively supported by Drizzle. Once those are added, we will have them here!
</Callout>

Source: https://orm.drizzle.team/docs/faq

import Callout from '@mdx/Callout.astro';


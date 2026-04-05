### Primary key
A primary key constraint indicates that a column, or group of columns, can be used as a unique identifier for rows in the table. 
This requires that the values be both unique and not null.
<Section>
```typescript
import { serial, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	id: serial().primaryKey(),
});
```

```sql
CREATE TABLE "table" (
	"id" serial PRIMARY KEY NOT NULL
);
```
</Section>


Source: https://orm.drizzle.team/docs/column-types/singlestore

import Section from '@mdx/Section.astro';
import Callout from '@mdx/Callout.astro';

We have native support for all of them, yet if that's not enough for you, feel free to create **[custom types](/docs/custom-types)**.

<Callout title='important' type='warning'>
All examples in this part of the documentation do not use database column name aliases, and column names are generated from TypeScript keys. 

You can use database aliases in column names if you want, and you can also use the `casing` parameter to define a mapping strategy for Drizzle. 

You can read more about it [here](/docs/sql-schema-declaration#shape-your-data-schema)
</Callout>


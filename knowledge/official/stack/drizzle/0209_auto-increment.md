### Auto increment

<Section>
```typescript
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	int: int().autoincrement(),
});
```

```sql
CREATE TABLE `table` (
	`int` int AUTO_INCREMENT
);
```
</Section>


Source: https://orm.drizzle.team/docs/column-types/sqlite


import Section from '@mdx/Section.astro';
import Callout from '@mdx/Callout.astro';

Based on the official **[SQLite docs](https://www.sqlite.org/datatype3.html)**,
each value stored in an SQLite database (or manipulated by the database engine)
has one of the following storage classes `NULL`, `INTEGER`, `REAL`, `TEXT` and `BLOB`.

We have native support for all of them, yet if that's not enough for you, feel free to create **[custom types](/docs/custom-types)**.

<Callout title='important' type='warning'>
All examples in this part of the documentation do not use database column name aliases, and column names are generated from TypeScript keys. 

You can use database aliases in column names if you want, and you can also use the `casing` parameter to define a mapping strategy for Drizzle. 

You can read more about it [here](/docs/sql-schema-declaration#shape-your-data-schema)
</Callout>


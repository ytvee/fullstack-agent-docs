### longblob

<Callout type='warning'>
Available starting from `drizzle-orm@1.0.0-beta.2`
</Callout>

A `LONGBLOB` is a binary large object that can hold a variable amount of data.
<Section>
```typescript
import { longblob, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	longblob: longblob()
});
```

```sql
CREATE TABLE `table` (
	`longblob` longblob
);
```
</Section>


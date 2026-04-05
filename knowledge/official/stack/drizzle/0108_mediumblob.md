### mediumblob

<Callout type='warning'>
Available starting from `drizzle-orm@1.0.0-beta.2`
</Callout>

A `MEDIUMBLOB` is a binary large object that can hold a variable amount of data.
<Section>
```typescript
import { mediumblob, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	mediumblob: mediumblob()
});
```

```sql
CREATE TABLE `table` (
	`mediumblob` mediumblob
);
```
</Section>


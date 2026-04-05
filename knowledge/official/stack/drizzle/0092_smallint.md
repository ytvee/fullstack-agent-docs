### smallint

<Section>
```typescript
import { smallint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	smallint: smallint()
});
```

```sql
CREATE TABLE `table` (
	`smallint` smallint
);
```
</Section>


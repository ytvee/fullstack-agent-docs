### mediumint

<Section>
```typescript
import { mediumint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	mediumint: mediumint()
});
```

```sql
CREATE TABLE `table` (
	`mediumint` mediumint
);
```
</Section>


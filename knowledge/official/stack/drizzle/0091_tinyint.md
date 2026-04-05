### tinyint

<Section>
```typescript
import { tinyint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	tinyint: tinyint()
});
```

```sql
CREATE TABLE `table` (
	`tinyint` tinyint
);
```
</Section>


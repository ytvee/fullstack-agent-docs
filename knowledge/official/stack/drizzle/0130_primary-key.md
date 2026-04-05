### Primary key 

<Section>
```typescript
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int().primaryKey(),
});
```

```sql
CREATE TABLE `table` (
	`int` int PRIMARY KEY NOT NULL
);
```
</Section>


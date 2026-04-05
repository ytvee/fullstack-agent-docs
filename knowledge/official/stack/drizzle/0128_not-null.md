### Not null
`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

<Section>
```typescript
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int().notNull(),
});
```

```sql
CREATE TABLE `table` (
	`int` int NOT NULL
);
```
</Section>


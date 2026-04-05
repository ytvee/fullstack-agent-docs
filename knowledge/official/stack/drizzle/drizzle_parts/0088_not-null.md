### Not null
`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

<Section>
```typescript
import { int, mssqlTable } from "drizzle-orm/mssql-core";

const table = mssqlTable('table', {
	int: int().notNull(),
});
```

```sql
CREATE TABLE [table] (
	[int] int NOT NULL
);
```
</Section>



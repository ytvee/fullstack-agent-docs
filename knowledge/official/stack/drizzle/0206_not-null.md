### Not null
`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

<Section>
```typescript
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	int: int().notNull(),
});
```

```sql
CREATE TABLE `table` (
	`int` int NOT NULL
);
```
</Section>


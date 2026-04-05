### Primary key 

<Section>
```typescript
import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	int: int().primaryKey(),
});
```

```sql
CREATE TABLE `table` (
	`int` int PRIMARY KEY NOT NULL
);
```
</Section>


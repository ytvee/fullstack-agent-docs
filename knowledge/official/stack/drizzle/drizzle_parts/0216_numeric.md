### Numeric

<Section>
```typescript
import { blob, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	numeric: numeric(),
	numericNum: numeric({ mode: 'number' }),
	numericBig: numeric({ mode: 'bigint' }),
});

```

```sql
CREATE TABLE `table` (
	`numeric` numeric,
	`numericNum` numeric,
	`numericBig` numeric
);
```
</Section>


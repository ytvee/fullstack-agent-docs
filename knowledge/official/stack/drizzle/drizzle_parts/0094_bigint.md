### bigint

<Section>
```typescript
import { bigint, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	bigint: bigint({ mode: 'number' })
	bigintUnsigned: bigint({ mode: 'number', unsigned: true })
});

bigint('...', { mode: 'number' | 'bigint' });

// You can also specify unsigned option for bigint
bigint('...', { mode: 'number' | 'bigint', unsigned: true })
```

```sql
CREATE TABLE `table` (
	`bigint` bigint,
	`bigintUnsigned` bigint unsigned
);
```
</Section>

We've omitted config of `M` in `bigint(M)`, since it indicates the display width of the numeric type 


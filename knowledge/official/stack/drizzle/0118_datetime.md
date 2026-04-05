### datetime

<Section>
```typescript
import { datetime, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	datetime: datetime(),
});

datetime('...', { mode: 'date' | "string"}),
datetime('...', { fsp : 0..6}),
```

```sql
CREATE TABLE `table` (
	`datetime` datetime
);
```
</Section>

<Section>
```typescript
import { datetime, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	datetime: datetime({ mode: 'date', fsp: 6 }),
});
```

```sql
CREATE TABLE `table` (
	`datetime` datetime(6)
);
```
</Section>


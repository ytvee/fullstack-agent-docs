### timestamp

<Section>
```typescript
import { timestamp, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	timestamp: timestamp(),
});

timestamp('...', { mode: 'date' | "string"}),
timestamp('...', { fsp : 0..6}),
```

```sql
CREATE TABLE `table` (
	`timestamp` timestamp
);
```
</Section>

<Section>
```typescript
import { timestamp, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	timestamp: timestamp({ mode: 'date', fsp: 6 }),
});
```

```sql
CREATE TABLE `table` (
	`timestamp` timestamp(6)
);
```
</Section>

<Section>
```typescript
import { timestamp, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	timestamp: timestamp().defaultNow(),
});
```

```sql
CREATE TABLE `table` (
	`timestamp` timestamp DEFAULT (now())
);
```
</Section>


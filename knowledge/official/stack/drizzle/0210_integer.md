### Integer

A signed integer, stored in `0`, `1`, `2`, `3`, `4`, `6`, or `8` bytes depending on the magnitude of the value.

<Section>
```typescript
import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	id: integer()
});

// you can customize integer mode to be number, boolean, timestamp, timestamp_ms
integer({ mode: 'number' })
integer({ mode: 'boolean' })
integer({ mode: 'timestamp_ms' })
integer({ mode: 'timestamp' }) // Date

```

```sql
CREATE TABLE `table` (
	`id` integer
);
```

</Section>

<Section>
```typescript
// to make integer primary key auto increment
integer({ mode: 'number' }).primaryKey({ autoIncrement: true })
```
```sql
CREATE TABLE `table` (
	`id` integer PRIMARY KEY AUTOINCREMENT NOT NULL
);
```
</Section>


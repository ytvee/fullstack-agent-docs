### Bigint

Since there is no `bigint` data type in SQLite, Drizzle offers a special `bigint` mode for `blob` columns. 
This mode allows you to work with BigInt instances in your code, and Drizzle stores them as blob values in the database.


<Section>
```typescript
import { blob, sqliteTable } from "drizzle-orm/sqlite-core";

const table = sqliteTable('table', {
	id: blob({ mode: 'bigint' })
});

```

```sql
CREATE TABLE `table` (
	`id` blob
);
```
</Section>


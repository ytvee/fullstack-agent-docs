### timestamp

<Section>
```typescript
import { timestamp, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	timestamp: timestamp(),
});

timestamp('...', { mode: 'date' | "string"}),
```

```sql
CREATE TABLE `table` (
	`timestamp` timestamp
);
```
</Section>

<Section>
```typescript
import { timestamp, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	timestamp: timestamp().defaultNow(),
});
```

```sql
CREATE TABLE `table` (
	`timestamp` timestamp DEFAULT (now())
);
```
</Section>


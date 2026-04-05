### datetime

<Section>
```typescript
import { datetime, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	datetime: datetime(),
});

datetime('...', { mode: 'date' | "string"}),
```

```sql
CREATE TABLE `table` (
	`datetime` datetime
);
```
</Section>


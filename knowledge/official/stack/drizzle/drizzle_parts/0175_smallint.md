### smallint

<Section>
```typescript
import { smallint, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	smallint: smallint()
});
```

```sql
CREATE TABLE `table` (
	`smallint` smallint
);
```
</Section>


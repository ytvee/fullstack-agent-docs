### tinyint

<Section>
```typescript
import { tinyint, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	tinyint: tinyint()
});
```

```sql
CREATE TABLE `table` (
	`tinyint` tinyint
);
```
</Section>


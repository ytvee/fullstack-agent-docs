### mediumint

<Section>
```typescript
import { mediumint, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	mediumint: mediumint()
});
```

```sql
CREATE TABLE `table` (
	`mediumint` mediumint
);
```
</Section>


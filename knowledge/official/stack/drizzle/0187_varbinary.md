### varbinary

<Section>
```typescript
import { varbinary, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	varbinary: varbinary({ length: 2}),
});
```

```sql
CREATE TABLE `table` (
	`varbinary` varbinary(2)
);
```
</Section>


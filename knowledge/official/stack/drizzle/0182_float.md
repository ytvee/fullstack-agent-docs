### float

<Section>
```typescript
import { float, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	float: float()
});
```

```sql
CREATE TABLE `table` (
	`float` float
);
```
</Section>


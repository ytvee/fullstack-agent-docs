### float

<Section>
```typescript
import { float, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	float: float()
});
```

```sql
CREATE TABLE `table` (
	`float` float
);
```
</Section>


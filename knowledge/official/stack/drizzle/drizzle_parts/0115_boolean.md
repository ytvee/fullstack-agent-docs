### boolean

<Section>
```typescript
import { boolean, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	boolean: boolean(),
});
```

```sql
CREATE TABLE `table` (
	`boolean` boolean
);
```
</Section>


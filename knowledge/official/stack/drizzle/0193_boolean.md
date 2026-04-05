### boolean

<Section>
```typescript
import { boolean, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	boolean: boolean(),
});
```

```sql
CREATE TABLE `table` (
	`boolean` boolean
);
```
</Section>


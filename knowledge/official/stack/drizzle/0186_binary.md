### binary

<Section>
```typescript
import { binary, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	binary: binary()
});
```

```sql
CREATE TABLE `table` (
	`binary` binary
);
```
</Section>


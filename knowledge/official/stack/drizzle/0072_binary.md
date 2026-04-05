### binary

Fixed-length binary data with a length of n bytes, where n is a value from 1 through 8,000. The storage size is n bytes.

<Section>
```typescript
import { binary, mssqlTable } from "drizzle-orm/mssql-core";

const table = mssqlTable('table', {
	binary: binary(),
	binary1: binary({ length: 256 })
});
```

```sql
CREATE TABLE [table] (
	[binary] binary,
	[binary1] binary(256)
);
```
</Section>


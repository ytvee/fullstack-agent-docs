### varbinary

Variable-length binary data. n can be a value from 1 through 8,000. max indicates that the maximum storage size is 2^31-1 bytes

<Section>
```typescript
import { varbinary, mssqlTable } from "drizzle-orm/mssql-core";

const table = mssqlTable('table', {
	varbinary: varbinary(),
	varbinary1: varbinary({ length: 256 }),
	varbinary2: varbinary({ length: 'max' })
});
```

```sql
CREATE TABLE [table] (
	[varbinary] varbinary,
	[varbinary1] varbinary(256),
	[varbinary2] varbinary(max)
);
```
</Section>


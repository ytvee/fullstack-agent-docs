### nchar
`nchar(n)`  

Fixed-size string data. n defines the string size in byte-pairs, and must be a value from 1 through 4,000

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql?view=sql-server-ver17#nchar---n--)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.

The `length` parameter is optional according to MSSQL docs.
<Section>
```typescript
import { nchar, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
  nchar1: nchar(),
  nchar2: nchar({ length: 256 }),
});

// will be inferred as text: "value1" | "value2" | null
nchar: nchar({ enum: ["value1", "value2"] }),
```

```sql
CREATE TABLE [table] (
	[nchar1] nchar,
	[nchar2] nchar(256)
);
```
</Section>


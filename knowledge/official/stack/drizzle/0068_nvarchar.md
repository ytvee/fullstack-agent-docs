### nvarchar
`nvarchar(n|max)`  
Variable-size string data. The value of n defines the string size in byte-pairs

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/nchar-and-nvarchar-transact-sql?view=sql-server-ver17#nvarchar---n--max--)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.

The `length` parameter is optional according to MSSQL docs.
<Section>
```typescript
import { nvarchar, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
  nvarchar1: nvarchar(),
  nvarchar2: nvarchar({ length: 256 }),
});

// will be inferred as text: "value1" | "value2" | null
nvarchar: nvarchar({ enum: ["value1", "value2"] }),

// will be inferred as `json`
nvarchar: nvarchar({ mode: 'json' })
```

```sql
CREATE TABLE [table] (
	[nvarchar1] nvarchar,
	[nvarchar2] nvarchar(256)
);
```
</Section>


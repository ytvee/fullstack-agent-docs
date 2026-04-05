### ntext
`text`  
Variable-length Unicode data with a maximum string length of 2^30 - 1 (1,073,741,823).

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/ntext-text-and-image-transact-sql?view=sql-server-ver17#text)**
  
You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.
<Section>
```typescript
import { text, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
  ntext: ntext()
});

// will be inferred as text: "value1" | "value2" | null
ntext: ntext({ enum: ["value1", "value2"] })
```

```sql
CREATE TABLE [table] (
	[ntext] ntext
);
```
</Section>


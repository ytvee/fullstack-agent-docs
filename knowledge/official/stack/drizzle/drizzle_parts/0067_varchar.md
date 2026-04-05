### varchar
`varchar(n|max)`  
Variable-size string data. Use n to define the string size in bytes and can be a value from 1 through 8,000

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/char-and-varchar-transact-sql?view=sql-server-ver17#varchar---n--max--)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.

The `length` parameter is optional according to MSSQL docs.
<Section>
```typescript
import { varchar, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
  varchar1: varchar(),
  varchar2: varchar({ length: 256 }),
  varchar3: varchar({ length: 'max' })
});

// will be inferred as text: "value1" | "value2" | null
varchar: varchar({ enum: ["value1", "value2"] }),
```

```sql
CREATE TABLE [table] (
	[varchar1] varchar,
	[varchar2] varchar(256),
	[varchar3] varchar(max)
);
```
</Section>


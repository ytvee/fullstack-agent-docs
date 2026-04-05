### numeric
`numeric`

Fixed precision and scale numbers. When maximum precision is used, valid values are from -10^38 + 1 through 10^38 - 1

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/decimal-and-numeric-transact-sql?view=sql-server-ver17#decimal---p---s----and-numeric---p---s---)**

<Section>
```typescript
import { numeric, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
  numeric1: numeric(),
  numeric2: numeric({ precision: 100 }),
  numeric3: numeric({ precision: 100, scale: 20 })
//   numericNum: numeric({ mode: 'number' }),
//   numericBig: numeric({ mode: 'bigint' }),
});
```

```sql
CREATE TABLE [table] (
	[numeric1] numeric,
	[numeric2] numeric(100),
	[numeric3] numeric(100, 20)
);
```
</Section>


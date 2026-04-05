### datetime2
`datetime2`  

Defines a date that is combined with a time of day that is based on 24-hour clock. datetime2 can be considered as an extension of the existing datetime type that has a larger date range, a larger default fractional precision, and optional user-specified precision.

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/datetime2-transact-sql?view=sql-server-ver17#datetime2-description)**
<Section>
```typescript
import { datetime2, mssqlTable } from "drizzle-orm/mssql-core";

const table = mssqlTable('table', {
	datetime2: datetime2(),
});
```

```sql
CREATE TABLE [table] (
	[datetime2] datetime2
);
```
</Section>
You can specify either `date` or `string` infer modes:
```typescript
// will infer as date
datetime2: datetime2({ mode: "date" }),

// will infer as string
datetime2: datetime2({ mode: "string" }),
```


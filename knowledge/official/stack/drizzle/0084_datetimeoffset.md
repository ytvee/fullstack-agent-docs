### datetimeoffset
`datetimeoffset`  

Defines a date that is combined with a time of a day based on a 24-hour clock like datetime2, and adds time zone awareness based on Coordinated Universal Time (UTC).

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/datetimeoffset-transact-sql?view=sql-server-ver17#datetimeoffset-description)**
<Section>
```typescript
import { datetimeoffset, mssqlTable } from "drizzle-orm/mssql-core";

const table = mssqlTable('table', {
	datetimeoffset: datetimeoffset(),
});
```

```sql
CREATE TABLE [table] (
	[datetimeoffset] datetimeoffset
);
```
</Section>
You can specify either `date` or `string` infer modes:
```typescript
// will infer as date
datetimeoffset: datetimeoffset({ mode: "date" }),

// will infer as string
datetimeoffset: datetimeoffset({ mode: "string" }),
```


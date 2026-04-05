### datetime
`datetime`  

Defines a date that is combined with a time of day with fractional seconds that is based on a 24-hour clock.

<Callout title='MSSQL docs'>
Avoid using datetime for new work. Instead, use the time, date, datetime2, and datetimeoffset data types. These types align with the SQL Standard, and are more portable. time, datetime2 and datetimeoffset provide more seconds precision. datetimeoffset provides time zone support for globally deployed applications.
</Callout>

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/datetime-transact-sql?view=sql-server-ver17#description)**
<Section>
```typescript
import { datetime, mssqlTable } from "drizzle-orm/mssql-core";

const table = mssqlTable('table', {
	datetime: datetime(),
});
```

```sql
CREATE TABLE [table] (
	[datetime] datetime
);
```
</Section>
You can specify either `date` or `string` infer modes:
```typescript
// will infer as date
datetime: datetime({ mode: "date" }),

// will infer as string
datetime: datetime({ mode: "string" }),
```


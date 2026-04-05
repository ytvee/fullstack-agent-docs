### float

float [ (n) ] Where n is the number of bits that are used to store the mantissa of the float number in scientific notation and, therefore, dictates the precision and storage size. If n is specified, it must be a value between 1 and 53. The default value of n is 53.

For more info please refer to the official MSSQL **[docs.](https://learn.microsoft.com/en-us/sql/t-sql/data-types/float-and-real-transact-sql?view=sql-server-ver17#syntax)**  

<Section>
```typescript
import { sql } from "drizzle-orm";
import { float, mssqlTable } from "drizzle-orm/mssql-core";

const table = mssqlTable('table', {
	float1: float(),
	float1: float({ precision: 16 })
});
```

```sql
CREATE TABLE [table] (
	[float1] float,
	[float2] float(16)
);
```
</Section>


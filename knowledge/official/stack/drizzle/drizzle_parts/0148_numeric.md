### numeric
`numeric` `decimal`  
Exact numeric of selectable precision. Can store numbers with a very large number of digits, up to 131072 digits before the decimal point and up to 16383 digits after the decimal point.

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-NUMERIC-DECIMAL)**

<Section>
```typescript
import { numeric, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
  numeric1: numeric(),
  numeric2: numeric({ precision: 100 }),
  numeric3: numeric({ precision: 100, scale: 20 }),
  numericNum: numeric({ mode: 'number' }),
  numericBig: numeric({ mode: 'bigint' }),
});
```

```sql
CREATE TABLE "table" (
	"numeric1" numeric,
	"numeric2" numeric(100),
	"numeric3" numeric(100, 20),
	"numericNum" numeric,
	"numericBig" numeric
);
```
</Section>


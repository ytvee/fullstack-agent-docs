### double precision
`double precision` `float8`  
Double precision floating-point number (8 bytes)

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-numeric.html)**  

<Section>
```typescript
import { sql } from "drizzle-orm";
import { doublePrecision, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	double1: doublePrecision(),
	double2: doublePrecision().default(10.10),
	double3: doublePrecision().default(sql`'10.10'::double precision`),
});
```

```sql
CREATE TABLE "table" (
	"double1" double precision,
	"double2" double precision default 10.10,
	"double3" double precision default '10.10'::double precision
);
```
</Section>


### smallserial
`smallserial` `serial2`  
Auto incrementing 2-bytes integer, notational convenience for creating unique identifier columns (similar to the `AUTO_INCREMENT` property supported by some other databases). 

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-SERIAL)**
<Section>
```typescript
import { smallserial, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
  smallserial: smallserial(),
});
```

```sql
CREATE TABLE "table" (
	"smallserial" smallserial NOT NULL
);
```
</Section>


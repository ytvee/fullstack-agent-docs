### serial
`serial` `serial4`  
Auto incrementing 4-bytes integer, notational convenience for creating unique identifier columns (similar to the `AUTO_INCREMENT` property supported by some other databases). 

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-SERIAL)**
<Section>
```typescript
import { serial, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
  serial: serial(),
});
```

```sql
CREATE TABLE "table" (
	"serial" serial NOT NULL
);
```
</Section>


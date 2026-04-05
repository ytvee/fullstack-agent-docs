### bigserial
`bigserial` `serial8`  
Auto incrementing 8-bytes integer, notational convenience for creating unique identifier columns (similar to the `AUTO_INCREMENT` property supported by some other databases).

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-SERIAL)**

If you're expecting values above 2^31 but below 2^53, you can utilise `mode: 'number'` and deal with javascript number as opposed to bigint.
<Section>
```typescript
import { bigserial, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
  bigserial: bigserial({ mode: 'number' }),
});
```

```sql
CREATE TABLE "table" (
	"bigserial" bigserial NOT NULL
);
```
</Section>


### boolean
PostgreSQL provides the standard SQL type boolean.

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-boolean.html)**

<Section>
```typescript
import { boolean, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
	boolean: boolean()
});

```

```sql
CREATE TABLE "table" (
	"boolean" boolean
);
```
</Section>


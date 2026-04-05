### bytea

PostgreSQL provides the standard SQL type bytea.

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-binary.html)**

<Section>
```typescript
import { bytea, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
	bytea: bytea()
});

```

```sql
CREATE TABLE IF NOT EXISTS "table" (
	"bytea" bytea,
);
```
</Section>


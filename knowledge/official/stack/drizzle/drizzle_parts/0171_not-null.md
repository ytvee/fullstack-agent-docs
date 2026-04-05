### Not null
`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.

<Section>
```typescript
import { integer, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	integer: integer().notNull(),
});
```

```sql
CREATE TABLE "table" (
	"integer" integer NOT NULL
);
```
</Section>



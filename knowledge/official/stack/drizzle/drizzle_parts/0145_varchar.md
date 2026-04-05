### varchar
`character varying(n)` `varchar(n)`  
Variable-length character string, can store strings up to **`n`** characters (not bytes). 

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-character.html)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.

The `length` parameter is optional according to PostgreSQL docs.
<Section>
```typescript
import { varchar, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
  varchar1: varchar(),
  varchar2: varchar({ length: 256 }),
});

// will be inferred as text: "value1" | "value2" | null
varchar: varchar({ enum: ["value1", "value2"] }),
```

```sql
CREATE TABLE "table" (
	"varchar1" varchar,
	"varchar2" varchar(256)
);
```
</Section>


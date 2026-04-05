### varchar
`character varying(n)` `varchar(n)`  

`STRING` alias used to stay compatible with PostgreSQL

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/string)**

You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.

The `length` parameter is optional according to PostgreSQL docs.
<Section>
```typescript
import { varchar, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
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


### smallint
`smallint` `int2`  
Small-range signed 2-byte integer   

<Section>
```typescript
import { smallint, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	smallint: smallint()
});
```

```sql
CREATE TABLE "table" (
	"smallint" smallint
);
```
</Section>

<Section>
```typescript
import { sql } from "drizzle-orm";
import { smallint, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	smallint1: smallint().default(10),
	smallint2: smallint().default(sql`'10'::smallint`)
});
```

```sql
CREATE TABLE "table" (
	"smallint1" smallint DEFAULT 10,
	"smallint2" smallint DEFAULT '10'::smallint
);
```
</Section>


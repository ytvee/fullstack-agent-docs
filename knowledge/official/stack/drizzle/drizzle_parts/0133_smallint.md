### smallint
`smallint` `int2`  
Small-range signed 2-byte integer   

If you need `smallint autoincrement` please refer to **[smallserial.](#smallserial)**
<Section>
```typescript
import { smallint, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
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
import { smallint, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
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


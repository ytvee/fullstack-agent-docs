### integer
`integer` `int` `int4`  
Signed 4-byte integer     

If you need `integer autoincrement` please refer to **[serial.](#serial)**

<Section>
```typescript
import { integer, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
	int: integer()
});

```

```sql
CREATE TABLE "table" (
	"int" integer
);
```
</Section>

<Section>
```typescript
import { sql } from "drizzle-orm";
import { integer, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
	int1: integer().default(10),
	int2: integer().default(sql`'10'::int`)
});

```

```sql
CREATE TABLE "table" (
	"int1" integer DEFAULT 10,
	"int2" integer DEFAULT '10'::int
);
```
</Section>


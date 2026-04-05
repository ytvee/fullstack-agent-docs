### bigint
`bigint` `int8`  
Signed 8-byte integer  

If you need `bigint autoincrement` please refer to **[bigserial.](#bigserial)**

If you're expecting values above 2^31 but below 2^53, you can utilise `mode: 'number'` and deal with javascript number as opposed to bigint.
<Section>
```typescript
import { bigint, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
	bigint: bigint({ mode: 'number' })
});

// will be inferred as `number`
bigint: bigint({ mode: 'number' })

// will be inferred as `bigint`
bigint: bigint({ mode: 'bigint' })
```

```sql
CREATE TABLE "table" (
	"bigint" bigint
);
```
</Section>

<Section>
```typescript
import { sql } from "drizzle-orm";
import { bigint, pgTable } from "drizzle-orm/pg-core";

export const table = pgTable('table', {
	bigint1: bigint().default(10),
	bigint2: bigint().default(sql`'10'::bigint`)
});
```

```sql
CREATE TABLE "table" (
	"bigint1" bigint DEFAULT 10,
	"bigint2" bigint DEFAULT '10'::bigint
);
```
</Section>


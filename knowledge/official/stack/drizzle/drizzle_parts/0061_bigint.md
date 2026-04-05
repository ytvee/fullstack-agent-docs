### bigint
`bigint`

Signed 8-byte integer  

If you're expecting values above 2^31 but below 2^53, you can utilise `mode: 'number'` and deal with javascript number as opposed to bigint.
<Section>
```typescript
import { bigint, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
	bigint: bigint({ mode: 'number' })
});

// will be inferred as `number`
bigint: bigint({ mode: 'number' })

// will be inferred as `bigint`
bigint: bigint({ mode: 'bigint' })

// will be inferred as `string`
bigint: bigint({ mode: 'string' })
```

```sql
CREATE TABLE [table] (
	[bigint] bigint
);
```
</Section>

<Section>
```typescript
import { sql } from "drizzle-orm";
import { bigint, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
	bigint1: bigint({ mode: 'number' }).default(10)
});
```

```sql
CREATE TABLE [table] (
	[bigint1] bigint DEFAULT 10
);
```
</Section>


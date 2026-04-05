### smallint
`smallint`

Small-range signed 2-byte integer   

<Section>
```typescript
import { smallint, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
	smallint: smallint()
});
```

```sql
CREATE TABLE [table] (
	[smallint] smallint
);
```
</Section>

<Section>
```typescript
import { sql } from "drizzle-orm";
import { smallint, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
	smallint1: smallint().default(10),
});
```

```sql
CREATE TABLE [table] (
	[smallint1] smallint DEFAULT 10
);
```
</Section>


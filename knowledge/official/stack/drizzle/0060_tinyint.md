### tinyint
`tinyint`

Small-range signed 1-byte integer   

<Section>
```typescript
import { tinyint, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
	tinyint: tinyint()
});
```

```sql
CREATE TABLE [table] (
	[tinyint] tinyint
);
```
</Section>

<Section>
```typescript
import { sql } from "drizzle-orm";
import { tinyint, mssqlTable } from "drizzle-orm/mssql-core";

export const table = mssqlTable('table', {
	tinyint1: tinyint().default(10),
});
```

```sql
CREATE TABLE [table] (
	[tinyint1] tinyint DEFAULT 10
);
```
</Section>


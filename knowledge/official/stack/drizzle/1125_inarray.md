### inArray
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': true, 'SQLite': true, 'SingleStore': true }} />
  
Value is in array of values
<Section>
```typescript
import { inArray } from "drizzle-orm";

db.select().from(table).where(inArray(table.column, [1, 2, 3, 4]));
```

```sql
SELECT * FROM table WHERE table.column in (1, 2, 3, 4)
```
</Section>

<Section>
```typescript
import { inArray } from "drizzle-orm";

const query = db.select({ data: table2.column }).from(table2);
db.select().from(table).where(inArray(table.column, query));
```

```sql
SELECT * FROM table WHERE table.column IN (SELECT table2.column FROM table2)
```
</Section>


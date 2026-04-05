### notInArray
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': true, 'SQLite': true, 'SingleStore': true }} />
  
Value is not in array of values
<Section>
```typescript
import { notInArray } from "drizzle-orm";

db.select().from(table).where(notInArray(table.column, [1, 2, 3, 4]));
```

```sql
SELECT * FROM table WHERE table.column NOT in (1, 2, 3, 4)
```
</Section>

<Section>
```typescript
import { notInArray } from "drizzle-orm";

const query = db.select({ data: table2.column }).from(table2);
db.select().from(table).where(notInArray(table.column, query));
```

```sql
SELECT * FROM table WHERE table.column NOT IN (SELECT table2.column FROM table2)
```
</Section>


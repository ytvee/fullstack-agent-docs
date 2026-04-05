### isNotNull
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': true, 'SQLite': true, 'SingleStore': true }} />
  
Value is not `null`
<Section>
```typescript
import { isNotNull } from "drizzle-orm";

db.select().from(table).where(isNotNull(table.column));
```

```sql
SELECT * FROM table WHERE table.column IS NOT NULL
```
</Section>


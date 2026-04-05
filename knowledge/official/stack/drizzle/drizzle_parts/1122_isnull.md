### isNull
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': true, 'SQLite': true, 'SingleStore': true }} />
  
Value is `null`
<Section>
```typescript
import { isNull } from "drizzle-orm";

db.select().from(table).where(isNull(table.column));
```

```sql
SELECT * FROM table WHERE table.column IS NULL
```
</Section>



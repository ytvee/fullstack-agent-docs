### notIlike
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': true, 'SQLite': true, 'SingleStore': true }} />
  
Value is not like some other value, case insensitive
<Section>
```typescript
import { notIlike } from "drizzle-orm";

db.select().from(table).where(notIlike(table.column, "%llo wor%"));
```

```sql
SELECT * FROM table WHERE table.column NOT ILIKE '%llo wor%'
```
</Section>


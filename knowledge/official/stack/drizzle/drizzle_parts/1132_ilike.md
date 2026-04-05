### ilike
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': false, 'SQLite': false, 'SingleStore': false }} />
  
Value is like some other value, case insensitive
<Section>
```typescript
import { ilike } from "drizzle-orm";

db.select().from(table).where(ilike(table.column, "%llo wor%"));
```

```sql
SELECT * FROM table WHERE table.column ILIKE '%llo wor%'
```
</Section>


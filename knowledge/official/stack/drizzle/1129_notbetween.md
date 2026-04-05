### notBetween
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': true, 'SQLite': true, 'SingleStore': true }} />
  
Value is not between two value
<Section>
```typescript
import { notBetween } from "drizzle-orm";

db.select().from(table).where(notBetween(table.column, 2, 7));
```

```sql
SELECT * FROM table WHERE table.column NOT BETWEEN 2 AND 7
```
</Section>


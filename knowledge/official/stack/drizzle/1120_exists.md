### exists
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': true, 'SQLite': true, 'SingleStore': true }} />
  
Value exists
<Section>
```typescript
import { exists } from "drizzle-orm";

const query = db.select().from(table2)
db.select().from(table).where(exists(query));
```

```sql
SELECT * FROM table WHERE EXISTS (SELECT * from table2)
```
</Section>


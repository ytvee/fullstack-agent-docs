### notExists

<Section>
```typescript
import { notExists } from "drizzle-orm";

const query = db.select().from(table2)
db.select().from(table).where(notExists(query));
```

```sql
SELECT * FROM table WHERE NOT EXISTS (SELECT * from table2)
```
</Section>


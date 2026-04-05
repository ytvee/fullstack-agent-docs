### interval
`interval`  
Time span

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-datetime.html)** 

<Section>
```typescript
import { interval, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	interval1: interval(),
  interval2: interval({ fields: 'day' }),
  interval3: interval({ fields: 'month' , precision: 6 }),
});

```

```sql
CREATE TABLE "table" (
	"interval1" interval,
	"interval2" interval day,
	"interval3" interval(6) month
);
```
</Section>


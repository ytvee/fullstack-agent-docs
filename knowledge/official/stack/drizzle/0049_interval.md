### interval
`interval`  

Stores a value that represents a span of time.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/interval)** 

<Section>
```typescript
import { interval, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
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


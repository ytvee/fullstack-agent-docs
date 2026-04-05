### float
`float` `float8` `double precision`  

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/float)**  

<Section>
```typescript
import { sql } from "drizzle-orm";
import { float, cockroachTable } from "drizzle-orm/cockroach-core";  

const table = cockroachTable('table', {
	float1: float(),
	float2: float().default(10.10),
	float3: float().default(sql`'10.10'::float`),
});
```

```sql
CREATE TABLE "table" (
	"float1" float,
	"float2" float default 10.10,
	"float3" float default '10.10'::float
);
```
</Section>


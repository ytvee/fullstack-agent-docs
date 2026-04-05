### decimal

`numeric` `decimal` `dec`
The DECIMAL data type stores exact, fixed-point numbers. This type is used when it is important to preserve exact precision, for example, with monetary data.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/decimal)**

<Section>
```typescript
import { decimal, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
  decimal1: decimal(),
  decimal2: decimal({ precision: 100 }),
  decimal3: decimal({ precision: 100, scale: 20 }),
  decimalNum: decimal({ mode: 'number' }),
  decimalBig: decimal({ mode: 'bigint' }),
});
```

```sql
CREATE TABLE "table" (
	"decimal1" decimal,
	"decimal2" decimal(100),
	"decimal3" decimal(100, 20),
	"decimalNum" decimal,
	"decimalBig" decimal
);
```
</Section>


### varbit
`varbit`

The VARBIT data types store bit arrays. With VARBIT, the length can be variable.

<br />

**Size**

The number of bits in a VARBIT value is determined as follows:

| Type&nbsp;declaration		| Logical&nbsp;size													|
|:------------------		|:--------------													|
| VARBIT					| variable&nbsp;with&nbsp;no&nbsp;maximum							|
| VARBIT(N)					| variable&nbsp;with&nbsp;a&nbsp;maximum&nbsp;of&nbsp;N&nbsp;bits	|

<br />

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/bit)**
<Section>
```typescript
import { sql } from "drizzle-orm";
import { cockroachTable, bit } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
	varbit1: varbit(),
	varbit2: varbit({ length: 15 }),
	varbit3: varbit({ length: 15 }).default('10011'),
	varbit4: varbit({ length: 15 }).default(sql`'10011'`)
});
```
```sql
CREATE TABLE "table" (
	"varbit1" varbit,
	"varbit2" varbit(15),
	"varbit3" varbit(15) DEFAULT '10011',
	"varbit4" varbit(15) DEFAULT '10011'
);
```

</Section>


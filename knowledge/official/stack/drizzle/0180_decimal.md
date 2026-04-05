### decimal

<Section>
```typescript
import { decimal, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	decimal: decimal(),
	decimalNum: decimal({ scale: 30, mode: 'number' }),
	decimalBig: decimal({ scale: 30, mode: 'bigint' }),
});
```

```sql
CREATE TABLE `table` (
	`decimal` decimal,
	`decimalNum` decimal(30),
	`decimalBig` decimal(30)
);
```
</Section>

<Section>
```typescript
import { decimal, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	decimalPrecision: decimal({ precision: 1,}),
	decimalPrecisionScale: decimal({ precision: 1, scale: 1,}),
});
```

```sql
CREATE TABLE `table` (
	`decimalPrecision` decimal(1),
	`decimalPrecisionScale` decimal(1, 1)
);
```
</Section>


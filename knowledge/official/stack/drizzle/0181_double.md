### double

<Section>
```typescript
import { double, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	double: double('double')
});
```

```sql
CREATE TABLE `table` (
	`double` double
);
```
</Section>

<Section>
```typescript
import { double, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	doublePrecision: double({ precision: 1,}),
	doublePrecisionScale: double({ precision: 1, scale: 1,}),
});
```

```sql
CREATE TABLE `table` (
	`doublePrecision` double(1),
	`doublePrecisionScale` double(1, 1)
);
```
</Section>


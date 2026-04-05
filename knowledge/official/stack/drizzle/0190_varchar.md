### varchar
You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.
<Section>
```typescript
import { varchar, singlestoreTable } from "drizzle-orm/singlestore-core";

const table = singlestoreTable('table', {
	varchar: varchar({ length: 2 }),
});

// will be inferred as text: "value1" | "value2" | null
varchar: varchar({ length: 6, enum: ["value1", "value2"] })
```

```sql
CREATE TABLE `table` (
	`varchar` varchar(2)
);
```
</Section>


### binary
`BINARY(M)` stores a fixed-length byte string of exactly M bytes.  
On insert, shorter values are right-padded with `0x00` bytes to reach M bytes; on retrieval, no padding is stripped.
All bytes—including trailing `0x00`—are significant in comparisons, `ORDER BY`, and `DISTINCT`
<Section>
```typescript
import { binary, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	binary: binary()
});
```

```sql
CREATE TABLE `table` (
	`binary` binary
);
```
</Section>


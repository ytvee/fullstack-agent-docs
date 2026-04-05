### string
`text` `varchar`, `char`

The `STRING` data type stores a string of Unicode characters.

<Callout>
For PostgreSQL compatibility, CockroachDB supports the following STRING-related types and their aliases:

`VARCHAR` (and alias `CHARACTER VARYING`)
`CHAR` (and alias `CHARACTER`)
`NAME`
</Callout>

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/string)**
  
You can define `{ enum: ["value1", "value2"] }` config to infer `insert` and `select` types, it **won't** check runtime values.
<Section>
```typescript
import { string, cockroachTable } from "drizzle-orm/cockroach-core";

export const table = cockroachTable('table', {
  stringColumn: string(), // equivalent to `text` PostgreSQL type
  stringColumn1: string({ length: 256 }), // equivalent to `varchar(256)` PostgreSQL type
});

// will be inferred as text: "value1" | "value2" | null
stringColumn: string({ enum: ["value1", "value2"] })
```

```sql
CREATE TABLE "table" (
	"stringColumn" string,
    "stringColumn1" string(256),
);
```
</Section>


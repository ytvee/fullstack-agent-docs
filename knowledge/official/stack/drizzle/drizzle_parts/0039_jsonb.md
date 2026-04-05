### jsonb
`jsonb`  

The JSONB data type stores JSON (JavaScript Object Notation) data as a binary representation of the JSONB value, which eliminates whitespace, duplicate keys, and key ordering

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/jsonb)**
<Section>
```typescript
import { jsonb, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
	jsonb1: jsonb(),
	jsonb2: jsonb().default({ foo: "bar" }),
	jsonb3: jsonb().default(sql`'{foo: "bar"}'::jsonb`),
});
```
```sql
CREATE TABLE "table" (
	"jsonb1" jsonb,
	"jsonb2" jsonb default '{"foo": "bar"}'::jsonb,
	"jsonb3" jsonb default '{"foo": "bar"}'::jsonb
);
```
</Section>

You can specify `.$type<..>()` for json object inference, it **won't** check runtime values. 
It provides compile time protection for default values, insert and select schemas.

```typescript
// will be inferred as { foo: string }
jsonb: jsonb().$type<{ foo: string }>();

// will be inferred as string[]
jsonb: jsonb().$type<string[]>();

// won't compile
jsonb: jsonb().$type<string[]>().default({});
```


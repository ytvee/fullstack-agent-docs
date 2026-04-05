### Default value
The `DEFAULT` clause specifies a default value to use for the column if no value
is explicitly provided by the user when doing an `INSERT`.
If there is no explicit `DEFAULT` clause attached to a column definition,
then the default value of the column is `NULL`.

An explicit `DEFAULT` clause may specify that the default value is `NULL`,
a string constant, a blob constant, a signed-number, or any constant expression enclosed in parentheses.

<Section>
```typescript
import { sql } from "drizzle-orm";
import { integer, pgTable, uuid } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	integer1: integer().default(42),
	integer2: integer().default(sql`'42'::integer`),
	uuid1: uuid().defaultRandom(),
	uuid2: uuid().default(sql`gen_random_uuid()`),
});
```

```sql
CREATE TABLE IF NOT EXISTS "table" (
	"integer1" integer DEFAULT 42,
	"integer2" integer DEFAULT '42'::integer,
	"uuid1" uuid DEFAULT gen_random_uuid(),
	"uuid2" uuid DEFAULT gen_random_uuid()
);
```
</Section>

When using `$default()` or `$defaultFn()`, which are simply different aliases for the same function, 
you can generate defaults at runtime and use these values in all insert queries. 

These functions can assist you in utilizing various implementations such as `uuid`, `cuid`, `cuid2`, and many more.

<Callout type="info" emoji="ℹ️">
	Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`
</Callout>

```ts
import { text, pgTable } from "drizzle-orm/pg-core";
import { createId } from '@paralleldrive/cuid2';

const table = pgTable('table', {
	id: text().$defaultFn(() => createId()),
});
```

When using `$onUpdate()` or `$onUpdateFn()`, which are simply different aliases for the same function, 
you can generate defaults at runtime and use these values in all update queries. 

Adds a dynamic update value to the column. The function will be called when the row is updated, 
and the returned value will be used as the column value if none is provided.
If no default (or $defaultFn) value is provided, the function will be called
when the row is inserted as well, and the returned value will be used as the column value.

<Callout type="info" emoji="ℹ️">
	Note: This value does not affect the `drizzle-kit` behavior, it is only used at runtime in `drizzle-orm`
</Callout>

```ts
import { integer, timestamp, text, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
	updateCounter: integer().default(sql`1`).$onUpdateFn((): SQL => sql`${table.update_counter} + 1`),
	updatedAt: timestamp({ mode: 'date', precision: 3 }).$onUpdate(() => new Date()),
    	alwaysNull: text().$type<string | null>().$onUpdate(() => null),
});
```



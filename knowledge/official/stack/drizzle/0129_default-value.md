### Default value

The `DEFAULT` clause specifies a default value to use for the column if no value
is explicitly provided by the user when doing an `INSERT`.
If there is no explicit `DEFAULT` clause attached to a column definition,
then the default value of the column is `NULL`.

An explicit `DEFAULT` clause may specify that the default value is `NULL`,
a string constant, a blob constant, a signed-number, or any constant expression enclosed in parentheses.

<Section>
```typescript
import { int, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
	int: int().default(3),
});
```

```sql
CREATE TABLE `table` (
	`int` int DEFAULT 3
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
import { varchar, mysqlTable } from "drizzle-orm/mysql-core";
import { createId } from '@paralleldrive/cuid2';

const table = mysqlTable('table', {
	id: varchar({ length: 128 }).$defaultFn(() => createId()),
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
import { text, mysqlTable } from "drizzle-orm/mysql-core";

const table = mysqlTable('table', {
    alwaysNull: text().$type<string | null>().$onUpdate(() => null),
});
```


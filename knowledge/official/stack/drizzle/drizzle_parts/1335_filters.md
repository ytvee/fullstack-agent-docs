### Filters

You can filter the query results using the [filter operators](/docs/operators) in the `.where()` method:

<Section>
```typescript copy
import { eq, lt, gte, ne } from 'drizzle-orm';

await db.select().from(users).where(eq(users.id, 42));
await db.select().from(users).where(lt(users.id, 42));
await db.select().from(users).where(gte(users.id, 42));
await db.select().from(users).where(ne(users.id, 42));
...
```
```sql
select "id", "name", "age" from "users" where "id" = 42;
select "id", "name", "age" from "users" where "id" < 42;
select "id", "name", "age" from "users" where "id" >= 42;
select "id", "name", "age" from "users" where "id" <> 42;
```
</Section>

All filter operators are implemented using the [`sql`](/docs/sql) function.
You can use it yourself to write arbitrary SQL filters, or build your own operators.
For inspiration, you can check how the operators provided by Drizzle are [implemented](https://github.com/drizzle-team/drizzle-orm/blob/main/drizzle-orm/src/sql/expressions/conditions.ts).
<Section>
```typescript copy
import { sql } from 'drizzle-orm';

function equals42(col: Column) {
  return sql`${col} = 42`;
}

await db.select().from(users).where(sql`${users.id} < 42`);
await db.select().from(users).where(sql`${users.id} = 42`);
await db.select().from(users).where(equals42(users.id));
await db.select().from(users).where(sql`${users.id} >= 42`);
await db.select().from(users).where(sql`${users.id} <> 42`);
await db.select().from(users).where(sql`lower(${users.name}) = 'aaron'`);
```
```sql
select "id", "name", "age" from "users" where 'id' < 42;
select "id", "name", "age" from "users" where 'id' = 42;
select "id", "name", "age" from "users" where 'id' = 42;
select "id", "name", "age" from "users" where 'id' >= 42;
select "id", "name", "age" from "users" where 'id' <> 42;
select "id", "name", "age" from "users" where lower("name") = 'aaron';
```
</Section>

<Callout type='info'>
All the values provided to filter operators and to the `sql` function are parameterized automatically.
For example, this query:
```ts
await db.select().from(users).where(eq(users.id, 42));
```
will be translated to:
```sql
select "id", "name", "age" from "users" where "id" = $1; -- params: [42]
```
</Callout>

Inverting condition with a `not` operator:
<Section>
```typescript copy
import { eq, not, sql } from 'drizzle-orm';

await db.select().from(users).where(not(eq(users.id, 42)));
await db.select().from(users).where(sql`not ${users.id} = 42`);
```
```sql
select "id", "name", "age" from "users" where not ("id" = 42);
select "id", "name", "age" from "users" where not ("id" = 42);
```
</Section>

<Callout type="info">
You can safely alter schema, rename tables and columns
and it will be automatically reflected in your queries because of template interpolation,
as opposed to hardcoding column or table names when writing raw SQL.
</Callout>


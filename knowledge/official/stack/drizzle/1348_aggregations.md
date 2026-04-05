### Aggregations
With Drizzle, you can do aggregations using functions like `sum`, `count`, `avg`, etc. by
grouping and filtering with `.groupBy()` and `.having()` respectfully, same as you would do in raw SQL:

<Section>
```typescript
import { gt } from 'drizzle-orm';

await db.select({
  age: users.age,
  count: sql<number>`cast(count(${users.id}) as int)`,
})
  .from(users)
  .groupBy(users.age);

await db.select({
  age: users.age,
  count: sql<number>`cast(count(${users.id}) as int)`,
})
  .from(users)
  .groupBy(users.age)
  .having(({ count }) => gt(count, 1));
```
```sql
select "age", cast(count("id") as int)
  from "users"
  group by "age";

select "age", cast(count("id") as int)
  from "users"
  group by "age"
  having cast(count("id") as int) > 1;
```
</Section>

<Callout type="info">
`cast(... as int)` is necessary because `count()` returns `bigint` in PostgreSQL and `decimal` in MySQL, which are treated as string values instead of numbers.
Alternatively, you can use [`.mapWith(Number)`](/docs/sql#sqlmapwith) to cast the value to a number at runtime.

If you need count aggregation - we recommend using our [`$count`](/docs/select#count) API
</Callout>


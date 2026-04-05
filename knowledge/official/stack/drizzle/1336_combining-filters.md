### Combining filters
You can logically combine filter operators with `and()` and `or()` operators:
<Section>
```typescript copy
import { eq, and, sql } from 'drizzle-orm';

await db.select().from(users).where(
  and(
    eq(users.id, 42),
    eq(users.name, 'Dan')
  )
);
await db.select().from(users).where(sql`${users.id} = 42 and ${users.name} = 'Dan'`);
```
```sql
select "id", "name", "age" from "users" where "id" = 42 and "name" = 'Dan';
select "id", "name", "age" from "users" where "id" = 42 and "name" = 'Dan';
```
</Section>

<Section>
```typescript copy
import { eq, or, sql } from 'drizzle-orm';

await db.select().from(users).where(
  or(
    eq(users.id, 42), 
    eq(users.name, 'Dan')
  )
);
await db.select().from(users).where(sql`${users.id} = 42 or ${users.name} = 'Dan'`);
```
```sql
select "id", "name", "age" from "users" where "id" = 42 or "name" = 'Dan';
select "id", "name", "age" from "users" where "id" = 42 or "name" = 'Dan';
```
</Section>


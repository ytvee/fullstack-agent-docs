### Order By
Use `.orderBy()` to add `order by` clause to the query, sorting the results by the specified fields:
<Section>
```typescript
import { asc, desc } from 'drizzle-orm';

await db.select().from(users).orderBy(users.name);
await db.select().from(users).orderBy(desc(users.name));

// order by multiple fields
await db.select().from(users).orderBy(users.name, users.name2);
await db.select().from(users).orderBy(asc(users.name), desc(users.name2));
```
```sql
select "id", "name", "age" from "users" order by "name";
select "id", "name", "age" from "users" order by "name" desc;

select "id", "name", "age" from "users" order by "name", "name2";
select "id", "name", "age" from "users" order by "name" asc, "name2" desc;
```
</Section>


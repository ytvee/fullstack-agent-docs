### Order By
Use `.orderBy()` to add `order by` clause to the query, sorting the results by the specified fields:
<Section>
```typescript
import { asc, desc } from 'drizzle-orm';

await db.delete(users).where(eq(users.name, 'Dan')).orderBy(users.name);
await db.delete(users).where(eq(users.name, 'Dan')).orderBy(desc(users.name));

// order by multiple fields
await db.delete(users).where(eq(users.name, 'Dan')).orderBy(users.name, users.name2);
await db.delete(users).where(eq(users.name, 'Dan')).orderBy(asc(users.name), desc(users.name2));
```
```sql
delete from "users" where "users"."name" = $1 order by "name";
delete from "users" where "users"."name" = $1 order by "name" desc;

delete from "users" where "users"."name" = $1 order by "name", "name2";
delete from "users" where "users"."name" = $1 order by "name" asc, "name2" desc;
```
</Section>


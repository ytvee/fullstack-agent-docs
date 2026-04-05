### Order By
Use `.orderBy()` to add `order by` clause to the query, sorting the results by the specified fields:
<Section>
```typescript
import { asc, desc } from 'drizzle-orm';

await db.update(usersTable).set({ verified: true }).orderBy(usersTable.name);
await db.update(usersTable).set({ verified: true }).orderBy(desc(usersTable.name));

// order by multiple fields
await db.update(usersTable).set({ verified: true }).orderBy(usersTable.name, usersTable.name2);
await db.update(usersTable).set({ verified: true }).orderBy(asc(usersTable.name), desc(usersTable.name2));
```
```sql
update "users" set "verified" = $1 order by "name";
update "users" set "verified" = $1 order by "name" desc;

update "users" set "verified" = $1 order by "name", "name2";
update "users" set "verified" = $1 order by "name" asc, "name2" desc;
```
</Section>


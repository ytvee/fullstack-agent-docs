### Select from subquery
Just like in SQL, you can embed queries into other queries by using the subquery API:
<Section>
```typescript copy
const sq = db.select().from(users).where(eq(users.id, 42)).as('sq');
const result = await db.select().from(sq);
```
```sql
select "id", "name", "age" from (select "id", "name", "age" from "users" where "id" = 42) "sq";
```
</Section>

Subqueries can be used in any place where a table can be used, for example in joins:
<Section>
```typescript copy
const sq = db.select().from(users).where(eq(users.id, 42)).as('sq');
const result = await db.select().from(users).leftJoin(sq, eq(users.id, sq.id));
```
```sql
select "users"."id", "users"."name", "users"."age", "sq"."id", "sq"."name", "sq"."age" from "users"
  left join (select "id", "name", "age" from "users" where "id" = 42) "sq"
    on "users"."id" = "sq"."id";
```
</Section>


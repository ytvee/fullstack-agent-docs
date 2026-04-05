### Left Join Lateral
<Section>
```typescript copy
const subquery = db.select().from(pets).where(gte(users.age, 16)).as('userPets')
const result = await db.select().from(users).leftJoinLateral(subquery, sql`true`)
```
```sql
select ... from "users" left join lateral (select ... from "pets" where "users"."age" >= 16) "userPets" on true
```
```typescript
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    userPets: {
        id: number;
        name: string;
        ownerId: number;
    } | null;
}[];
```
</Section>


### Cross Join Lateral
<Section>
```typescript copy
const subquery = db.select().from(pets).where(gte(users.age, 16)).as('userPets')
const result = await db.select().from(users).crossJoinLateral(subquery)
```
```sql
select ... from "users" cross join lateral (select ... from "pets" where "users"."age" >= 16) "userPets"
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
    };
}[];
```
</Section>


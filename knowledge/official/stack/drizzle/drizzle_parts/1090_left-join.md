### Left Join
<Section>
```typescript copy
const result = await db.select().from(users).leftJoin(pets, eq(users.id, pets.ownerId))
```
```sql
select ... from "users" left join "pets" on "users"."id" = "pets"."owner_id"
```
```typescript
// result type
const result: {
    user: {
        id: number;
        name: string;
    };
    pets: {
        id: number;
        name: string;
        ownerId: number;
    } | null;
}[];
```
</Section>


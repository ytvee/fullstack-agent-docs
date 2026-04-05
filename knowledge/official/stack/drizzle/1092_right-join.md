### Right Join
<Section>
```typescript copy
const result = await db.select().from(users).rightJoin(pets, eq(users.id, pets.ownerId))
```
```sql
select ... from "users" right join "pets" on "users"."id" = "pets"."owner_id"
```
```typescript
// result type
const result: {
    user: {
        id: number;
        name: string;
    } | null;
    pets: {
        id: number;
        name: string;
        ownerId: number;
    };
}[];
```
</Section>


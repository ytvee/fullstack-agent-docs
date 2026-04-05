### Cross Join
<Section>
```typescript copy
const result = await db.select().from(users).crossJoin(pets)
```
```sql
select ... from "users" cross join "pets"
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
    };
}[];
```
</Section>


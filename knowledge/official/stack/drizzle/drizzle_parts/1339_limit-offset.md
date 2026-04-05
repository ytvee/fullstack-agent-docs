### Limit & offset
<IsSupportedChipGroup chips={{ 'MSSQL': false }} />

Use `.limit()` and `.offset()` to add `limit` and `offset` clauses to the query - for example, to implement pagination:
<Section>
```typescript
await db.select().from(users).limit(10);
await db.select().from(users).limit(10).offset(10);
```
```sql
select "id", "name", "age" from "users" limit 10;
select "id", "name", "age" from "users" limit 10 offset 10;
```
</Section>


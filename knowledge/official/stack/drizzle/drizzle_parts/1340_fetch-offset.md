### Fetch & offset

<IsSupportedChipGroup chips={{ 'MSSQL': true }} />

<Callout>
In MSSQL, `FETCH` and `OFFSET` are part of the `ORDER BY` clause, so they can only be used after the `.orderBy()` function
</Callout>

<Section>
```typescript
await db.select().from(users).orderBy(asc(users.id)).offset(5);
await db.select().from(users).orderBy(asc(users.id)).offset(5).fetch(10);
```
```sql
select [id], [name], [age] from [users] offset 5 rows;
select [id], [name], [age] from [users] offset 5 rows fetch next 10 rows;
```
</Section>


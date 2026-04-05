### Limit

<IsSupportedChipGroup chips={{ 'PostgreSQL': false, 'MySQL': true, 'SQLite': true, 'SingleStore': true, 'MSSQL': false, 'CockroachDB': false }} />

Use `.limit()` to add `limit` clause to the query - for example:
<Section>
```typescript
await db.delete(users).where(eq(users.name, 'Dan')).limit(2);
```
```sql
delete from "users" where "users"."name" = $1 limit $2;
```
</Section>


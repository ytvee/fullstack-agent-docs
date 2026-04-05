### Limit

<IsSupportedChipGroup chips={{ 'PostgreSQL': false, 'MySQL': true, 'SQLite': true, 'SingleStore': true, 'MSSQL': false, 'CockroachDB': false }} />

Use `.limit()` to add `limit` clause to the query - for example:
<Section>
```typescript
await db.update(usersTable).set({ verified: true }).limit(2);
```
```sql
update "users" set "verified" = $1 limit $2;
```
</Section>


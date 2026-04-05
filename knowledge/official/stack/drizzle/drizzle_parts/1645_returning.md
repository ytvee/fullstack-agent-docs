### Returning
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'SQLite': true, 'MySQL': false , 'SingleStore': false, 'MSSQL': false, 'CockroachDB': true }} />
You can update a row and get it back in PostgreSQL and SQLite:
```typescript copy
const updatedUserId: { updatedId: number }[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .returning({ updatedId: users.id });
```


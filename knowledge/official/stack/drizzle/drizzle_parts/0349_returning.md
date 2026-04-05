### Returning
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'SQLite': true, 'MySQL': false, 'SingleStore': false, 'MSSQL': false, 'CockroachDB': true }} />
You can delete a row and get it back in PostgreSQL and SQLite:
```typescript copy
const deletedUser = await db.delete(users)
  .where(eq(users.name, 'Dan'))
  .returning();

// partial return
const deletedUserIds: { deletedId: number }[] = await db.delete(users)
  .where(eq(users.name, 'Dan'))
  .returning({ deletedId: users.id });
```


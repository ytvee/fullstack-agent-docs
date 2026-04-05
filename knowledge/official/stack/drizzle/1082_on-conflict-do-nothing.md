### On conflict do nothing
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'SQLite': true, 'MySQL': false, 'SingleStore': false, 'CockroachDB': true }} />

`onConflictDoNothing` will cancel the insert if there's a conflict:

```typescript copy
await db.insert(users)
  .values({ id: 1, name: 'John' })
  .onConflictDoNothing();

// explicitly specify conflict target
await db.insert(users)
  .values({ id: 1, name: 'John' })
  .onConflictDoNothing({ target: users.id });
```


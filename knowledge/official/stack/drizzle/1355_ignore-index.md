### Ignore Index

The `IGNORE INDEX` hint tells the optimizer to avoid using specific indexes for the query. MySQL will consider all other indexes (if any) or perform a full table scan if necessary.

<IsSupportedChipGroup chips={{ 'MySQL': true, 'PostgreSQL': false, 'SQLite': false, 'SingleStore': false, 'MSSQL': false, 'CockroachDB': false }} />

```ts copy
export const users = mysqlTable('users', {
	id: int('id').primaryKey(),
	name: varchar('name', { length: 100 }).notNull(),
}, () => [usersTableNameIndex]);

const usersTableNameIndex = index('users_name_index').on(users.name);

await db.select()
  .from(users, { ignoreIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```

You can also use this option on any join you want

```ts
await db.select()
  .from(users)
  .leftJoin(posts, eq(posts.userId, users.id), { useIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```



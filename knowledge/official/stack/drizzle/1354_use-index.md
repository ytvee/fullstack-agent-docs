### Use Index

The `USE INDEX` hint suggests to the optimizer which indexes to consider when processing the query. The optimizer is not forced to use these indexes but will prioritize them if they are suitable.

<IsSupportedChipGroup chips={{ 'MySQL': true, 'PostgreSQL': false, 'SQLite': false, 'SingleStore': false, 'MSSQL': false, 'CockroachDB': false }} />

```ts copy
export const users = mysqlTable('users', {
	id: int('id').primaryKey(),
	name: varchar('name', { length: 100 }).notNull(),
}, () => [usersTableNameIndex]);

const usersTableNameIndex = index('users_name_index').on(users.name);

await db.select()
  .from(users, { useIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```

You can also use this option on any join you want

```ts
await db.select()
  .from(users)
  .leftJoin(posts, eq(posts.userId, users.id), { useIndex: usersTableNameIndex })
  .where(eq(users.name, 'David'));
```


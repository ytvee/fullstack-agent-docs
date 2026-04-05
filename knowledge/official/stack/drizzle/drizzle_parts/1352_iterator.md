### Iterator

<IsSupportedChipGroup chips={{ 'MySQL': true, 'PostgreSQL[WIP]': false, 'SQLite[WIP]': false, 'SingleStore[WIP]': false, 'MSSQL': true, 'CockroachDB[WIP]': false }} />

If you need to return a very large amount of rows from a query and you don't want to load them all into memory, you can use `.iterator()` to convert the query into an async iterator:

```ts copy
const iterator = await db.select().from(users).iterator();

for await (const row of iterator) {
  console.log(row);
}
```

It also works with prepared statements:

```ts copy
const query = await db.select().from(users).prepare();
const iterator = await query.iterator();

for await (const row of iterator) {
  console.log(row);
}
```


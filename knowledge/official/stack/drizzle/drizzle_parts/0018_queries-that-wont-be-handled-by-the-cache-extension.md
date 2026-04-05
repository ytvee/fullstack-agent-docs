#### Queries that won't be handled by the `cache` extension:

- Using cache with raw queries, such as:

```ts
db.execute(sql`select 1`);
```

- Using cache with `batch` feature in `d1` and `libsql`

```ts
db.batch([
    db.insert(users).values(...),
    db.update(users).set(...).where()
])
```

- Using cache in transactions
```ts
await db.transaction(async (tx) => {
  await tx.update(accounts).set(...).where(...);
  await tx.update...
});
```


##### `orderBy` is now object

<Callout title="❌ v1">
```ts
const response = db._query.users.findMany({
  orderBy: (users, { asc }) => [asc(users.id)],
});
```
</Callout>

<Callout title="✅ v2">
```ts
const response = db.query.users.findMany({
  orderBy: { id: "asc" },
});
```
</Callout>


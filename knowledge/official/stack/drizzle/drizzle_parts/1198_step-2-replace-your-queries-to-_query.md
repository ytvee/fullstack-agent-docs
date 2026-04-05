##### Step 2: Replace your queries to `._query`

To use Relational Queries v1 you had to write `db.query.`

<Callout type='error' title='v1'>
```ts
await db.query.users.findMany();
```
</Callout>

In Relational Queries v2, we moved it to `db._query` so that `db.query` could be used for a new syntax, 
while still giving you the option to use the old syntax via `db._query`.

We had a long discussion about whether we should just deprecate `db.query` and replace it with 
something like `db.query2` or `db.queryV2`. In the end, we decided that all new APIs should remain 
as simple as `db.query`, and that requiring you to replace all of your queries with `db._query` if you
want to keep using the old syntax is preferable to forcing everyone in the future to use 
`db.queryV2`, `db.queryV3`, `db.queryV4`, etc.

<Callout title='v2'>
```ts
// Using RQBv1
await db._query.users.findMany();

// Using RQBv2
await db.query.users.findMany();
```
</Callout>


### Distinct select

You can use `.selectDistinct()` instead of `.select()` to retrieve only unique rows from a dataset:
<Section>
```ts
await db.selectDistinct().from(users).orderBy(users.id, users.name);

await db.selectDistinct({ id: users.id }).from(users).orderBy(users.id);
```
```sql
select distinct "id", "name" from "users" order by "id", "name";

select distinct "id" from "users" order by "id";
```
</Section>

In PostgreSQL, you can also use the `distinct on` clause to specify how the unique rows are determined:
<Callout type='warning'>
`distinct on` clause is only supported in PostgreSQL.
</Callout>
<Section>
```ts
await db.selectDistinctOn([users.id]).from(users).orderBy(users.id);
await db.selectDistinctOn([users.name], { name: users.name }).from(users).orderBy(users.name);
```
```sql
select distinct on ("id") "id", "name" from "users" order by "id";
select distinct on ("name") "name" from "users" order by "name";
```
</Section>




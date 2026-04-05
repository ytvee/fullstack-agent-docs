### WITH clause

<Callout>
  Check how to use WITH statement with [insert](/docs/insert#with-insert-clause), [update](/docs/update#with-update-clause), [delete](/docs/delete#with-delete-clause)
</Callout>

Using the `with` clause can help you simplify complex queries by splitting them into smaller subqueries called common table expressions (CTEs):
<Section>
```typescript copy
const sq = db.$with('sq').as(db.select().from(users).where(eq(users.id, 42)));

const result = await db.with(sq).select().from(sq);
```
```sql
with sq as (select "id", "name", "age" from "users" where "id" = 42)
select "id", "name", "age" from sq;
```
</Section>

You can also provide `insert`, `update` and `delete` statements inside `with`

<Section>
```typescript copy
const sq = db.$with('sq').as(
    db.insert(users).values({ name: 'John' }).returning(),
);

const result = await db.with(sq).select().from(sq);
```
```sql
with "sq" as (insert into "users" ("id", "name") values (default, 'John') returning "id", "name") 
select "id", "name" from "sq"
```
</Section>

<Section>
```typescript copy
const sq = db.$with('sq').as(
    db.update(users).set({ age: 25 }).where(eq(users.name, 'John')).returning(),
);
const result = await db.with(sq).select().from(sq);
```
```sql
with "sq" as (update "users" set "age" = 25 where "users"."name" = 'John' returning "id", "name", "age") 
select "id", "name", "age" from "sq"
```
</Section>

<Section>
```typescript copy
const sq = db.$with('sq').as(
  db.delete(users).where(eq(users.name, 'John')).returning(),
);

const result = await db.with(sq).select().from(sq);
```
```sql
with "sq" as (delete from "users" where "users"."name" = $1 returning "id", "name", "age") 
select "id", "name", "age" from "sq"
```
</Section>

To select arbitrary SQL values as fields in a CTE and reference them in other CTEs or in the main query,
you need to add aliases to them:
```typescript copy

const sq = db.$with('sq').as(db.select({ 
  name: sql<string>`upper(${users.name})`.as('name'),
})
.from(users));

const result = await db.with(sq).select({ name: sq.name }).from(sq);
```
If you don't provide an alias, the field type will become `DrizzleTypeError` and you won't be able to reference it in other queries.
If you ignore the type error and still try to use the field,
you will get a runtime error, since there's no way to reference that field without an alias.


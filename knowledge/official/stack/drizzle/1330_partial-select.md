### Partial select
In some cases, you might want to select only a subset of columns from a table.
You can do that by providing a selection object to the `.select()` method:
<Section>
```typescript copy
const result = await db.select({
  field1: users.id,
  field2: users.name,
}).from(users);

const { field1, field2 } = result[0];
```
```sql
select "id", "name" from "users";
```
</Section>

Like in SQL, you can use arbitrary expressions as selection fields, not just table columns:

<Section>
```typescript
const result = await db.select({
  id: users.id,
  lowerName: sql<string>`lower(${users.name})`,
}).from(users);
```
```sql
select "id", lower("name") from "users";
```
</Section>

<Callout type="warning">
By specifying `sql<string>`, you are telling Drizzle that the **expected** type of the field is `string`.<br />
If you specify it incorrectly (e.g. use `sql<number>` for a field that will be returned as a string), the runtime value won't match the expected type.
Drizzle cannot perform any type casts based on the provided type generic, because that information is not available at runtime.

If you need to apply runtime transformations to the returned value, you can use the [`.mapWith()`](/docs/sql#sqlmapwith) method.
</Callout>

<Callout title='Info'>
Starting from `v1.0.0-beta.1` you can use `.as()` for columns:

```ts
const result = await db.select({
  id: users.id,
  lowerName: users.name.as("lower"),
}).from(users);
```
</Callout>


### Basic select
Select all rows from a table including all columns:

<Section>
```typescript
const result = await db.select().from(users);
/*
  {
    id: number;
    name: string;
    age: number | null;
  }[]
*/
```
```sql
select "id", "name", "age" from "users";
```
</Section>

Notice that the result type is inferred automatically based on the table definition, including columns nullability.

<Callout type="info">
Drizzle always explicitly lists columns in the `select` clause instead of using `select *`.<br />
This is required internally to guarantee the fields order in the query result, and is also generally considered a good practice.
</Callout>


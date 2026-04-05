### Aggregations helpers

Drizzle has a set of wrapped `sql` functions, so you don't need to write
`sql` templates for common cases in your app

<Callout type="info">
 Remember, aggregation functions are often used with the GROUP BY clause of the SELECT statement. 
 So if you are selecting using aggregating functions and other columns in one query, 
 be sure to use the `.groupBy` clause
</Callout>


**count**

Returns the number of values in `expression`.
<Section>
```ts
import { count } from 'drizzle-orm'

await db.select({ value: count() }).from(users);
await db.select({ value: count(users.id) }).from(users);
```
```sql
select count("*") from "users";
select count("id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`count('*'))`.mapWith(Number) 
}).from(users);

await db.select({ 
  value: sql`count(${users.id})`.mapWith(Number) 
}).from(users);
```
</Section>

**countDistinct**

Returns the number of non-duplicate values in `expression`.
<Section>
```ts
import { countDistinct } from 'drizzle-orm'

await db.select({ value: countDistinct(users.id) }).from(users);
```
```sql
select count(distinct "id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`count(${users.id})`.mapWith(Number) 
}).from(users);
```
</Section>

**avg**

Returns the average (arithmetic mean) of all non-null values in `expression`.
<Section>
```ts
import { avg } from 'drizzle-orm'

await db.select({ value: avg(users.id) }).from(users);
```
```sql
select avg("id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`avg(${users.id})`.mapWith(String) 
}).from(users);
```
</Section>

**avgDistinct**

Returns the average (arithmetic mean) of all non-null values in `expression`.
<Section>
```ts
import { avgDistinct } from 'drizzle-orm'

await db.select({ value: avgDistinct(users.id) }).from(users);
```
```sql
select avg(distinct "id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`avg(distinct ${users.id})`.mapWith(String) 
}).from(users);
```
</Section>

**sum**

Returns the sum of all non-null values in `expression`.
<Section>
```ts
import { sum } from 'drizzle-orm'

await db.select({ value: sum(users.id) }).from(users);
```
```sql
select sum("id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`sum(${users.id})`.mapWith(String) 
}).from(users);
```
</Section>

**sumDistinct**

Returns the sum of all non-null and non-duplicate values in `expression`.
<Section>
```ts
import { sumDistinct } from 'drizzle-orm'

await db.select({ value: sumDistinct(users.id) }).from(users);
```
```sql
select sum(distinct "id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`sum(distinct ${users.id})`.mapWith(String) 
}).from(users);
```
</Section>

**max**

Returns the maximum value in `expression`.
<Section>
```ts
import { max } from 'drizzle-orm'

await db.select({ value: max(users.id) }).from(users);
```
```sql
select max("id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`max(${expression})`.mapWith(users.id) 
}).from(users);
```
</Section>

**min**

Returns the minimum value in `expression`.
<Section>
```ts
import { min } from 'drizzle-orm'

await db.select({ value: min(users.id) }).from(users);
```
```sql
select min("id") from "users";
```
```ts
// It's equivalent to writing
await db.select({ 
  value: sql`min(${users.id})`.mapWith(users.id) 
}).from(users);
```
</Section>

A more advanced example:

```typescript copy
const orders = sqliteTable('order', {
  id: integer('id').primaryKey(),
  orderDate: integer('order_date', { mode: 'timestamp' }).notNull(),
  requiredDate: integer('required_date', { mode: 'timestamp' }).notNull(),
  shippedDate: integer('shipped_date', { mode: 'timestamp' }),
  shipVia: integer('ship_via').notNull(),
  freight: numeric('freight').notNull(),
  shipName: text('ship_name').notNull(),
  shipCity: text('ship_city').notNull(),
  shipRegion: text('ship_region'),
  shipPostalCode: text('ship_postal_code'),
  shipCountry: text('ship_country').notNull(),
  customerId: text('customer_id').notNull(),
  employeeId: integer('employee_id').notNull(),
});

const details = sqliteTable('order_detail', {
  unitPrice: numeric('unit_price').notNull(),
  quantity: integer('quantity').notNull(),
  discount: numeric('discount').notNull(),
  orderId: integer('order_id').notNull(),
  productId: integer('product_id').notNull(),
});


db
  .select({
    id: orders.id,
    shippedDate: orders.shippedDate,
    shipName: orders.shipName,
    shipCity: orders.shipCity,
    shipCountry: orders.shipCountry,
    productsCount: sql<number>`cast(count(${details.productId}) as int)`,
    quantitySum: sql<number>`sum(${details.quantity})`,
    totalPrice: sql<number>`sum(${details.quantity} * ${details.unitPrice})`,
  })
  .from(orders)
  .leftJoin(details, eq(orders.id, details.orderId))
  .groupBy(orders.id)
  .orderBy(asc(orders.id))
  .all();
```


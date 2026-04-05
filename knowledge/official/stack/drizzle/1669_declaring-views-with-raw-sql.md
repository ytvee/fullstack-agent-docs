### Declaring views with raw SQL
Whenever you need to declare view using a syntax that is not supported by the query builder, 
you can directly use `sql` operator and explicitly specify view columns schema.

```ts copy
// regular view
const newYorkers = pgView('new_yorkers', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  cityId: integer('city_id').notNull(),
}).as(sql`select * from ${users} where ${eq(users.cityId, 1)}`);

// materialized view
const newYorkers = pgMaterializedView('new_yorkers', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  cityId: integer('city_id').notNull(),
}).as(sql`select * from ${users} where ${eq(users.cityId, 1)}`);
```


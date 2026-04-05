### point
`point`  
Geometric point type

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-geometric.html#DATATYPE-GEOMETRIC-POINTS)** 

Type `point` has 2 modes for mappings from the database: `tuple` and `xy`.

- `tuple` will be accepted for insert and mapped on select to a tuple. So, the database Point(1,2) will be typed as [1,2] with drizzle.

- `xy` will be accepted for insert and mapped on select to an object with x, y coordinates. So, the database Point(1,2) will be typed as `{ x: 1, y: 2 }` with drizzle

<Section>
```typescript
const items = pgTable('items', {
 point: point(),
 pointObj: point({ mode: 'xy' }),
});
```

```sql
CREATE TABLE "items" (
	"point" point,
	"pointObj" point
);
```
</Section>


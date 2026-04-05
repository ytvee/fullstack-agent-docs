#### Examples

Let's take a few examples of `pg_vector` queries from the `pg_vector` docs and translate them to Drizzle

```ts
import { l2Distance } from 'drizzle-orm';

// SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
db.select().from(items).orderBy(l2Distance(items.embedding, [3,1,2]))

// SELECT embedding <-> '[3,1,2]' AS distance FROM items;
db.select({ distance: l2Distance(items.embedding, [3,1,2]) })

// SELECT * FROM items ORDER BY embedding <-> (SELECT embedding FROM items WHERE id = 1) LIMIT 5;
const subquery = db.select({ embedding: items.embedding }).from(items).where(eq(items.id, 1));
db.select().from(items).orderBy(l2Distance(items.embedding, subquery)).limit(5)

// SELECT (embedding <#> '[3,1,2]') * -1 AS inner_product FROM items;
db.select({ innerProduct: sql`(${maxInnerProduct(items.embedding, [3,1,2])}) * -1` }).from(items)

// and more!
```


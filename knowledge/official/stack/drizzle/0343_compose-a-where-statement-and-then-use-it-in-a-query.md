#### Compose a WHERE statement and then use it in a query
```ts
async function getProductsBy({
  name,
  category,
  maxPrice,
}: {
  name?: string;
  category?: string;
  maxPrice?: string;
}) {
  const filters: SQL[] = [];

  if (name) filters.push(ilike(products.name, name));
  if (category) filters.push(eq(products.category, category));
  if (maxPrice) filters.push(lte(products.price, maxPrice));

  return db
    .select()
    .from(products)
    .where(and(...filters));
}
```


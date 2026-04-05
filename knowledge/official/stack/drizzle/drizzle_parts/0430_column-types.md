#### Column Types

**`vector`**

Store your vectors with the rest of your data

For more info please refer to the official pg_vector docs **[docs.](https://github.com/pgvector/pgvector)**


<Section>
```ts
const table = pgTable('table', {
    embedding: vector({ dimensions: 3 })
})
```

```sql
CREATE TABLE IF NOT EXISTS "table" (
	"embedding" vector(3)
);
```
</Section>


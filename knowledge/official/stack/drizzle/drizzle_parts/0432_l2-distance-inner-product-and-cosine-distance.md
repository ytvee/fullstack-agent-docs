#### L2 distance, Inner product and Cosine distance

```ts
// CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
// CREATE INDEX ON items USING hnsw (embedding vector_ip_ops);
// CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops);

const table = pgTable('items', {
    embedding: vector({ dimensions: 3 })
}, (table) => [
  index('l2_index').using('hnsw', table.embedding.op('vector_l2_ops'))
  index('ip_index').using('hnsw', table.embedding.op('vector_ip_ops'))
  index('cosine_index').using('hnsw', table.embedding.op('vector_cosine_ops'))
])
```


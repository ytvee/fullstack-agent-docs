#### L1 distance, Hamming distance and Jaccard distance - added in pg_vector 0.7.0 version

```ts
// CREATE INDEX ON items USING hnsw (embedding vector_l1_ops);
// CREATE INDEX ON items USING hnsw (embedding bit_hamming_ops);
// CREATE INDEX ON items USING hnsw (embedding bit_jaccard_ops);

const table = pgTable('table', {
    embedding: vector({ dimensions: 3 })
}, (table) => [
  index('l1_index').using('hnsw', table.embedding.op('vector_l1_ops'))
  index('hamming_index').using('hnsw', table.embedding.op('bit_hamming_ops'))
  index('bit_jaccard_index').using('hnsw', table.embedding.op('bit_jaccard_ops'))
])
```


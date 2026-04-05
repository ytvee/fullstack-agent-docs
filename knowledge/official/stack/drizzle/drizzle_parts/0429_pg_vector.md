### `pg_vector`

<Callout>
There is no specific code to create an extension inside the Drizzle schema. We assume that if you are using vector types, 
indexes, and queries, you have a PostgreSQL database with the pg_vector extension installed.
</Callout>

[`pg_vector`](https://github.com/pgvector/pgvector) is open-source vector similarity search for Postgres

Store your vectors with the rest of your data. Supports:

- exact and approximate nearest neighbor search
- single-precision, half-precision, binary, and sparse vectors
- L2 distance, inner product, cosine distance, L1 distance, Hamming distance, and Jaccard distance


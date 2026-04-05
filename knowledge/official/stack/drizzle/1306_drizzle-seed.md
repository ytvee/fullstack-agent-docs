# Drizzle Seed

<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'SQLite': true, 'MySQL': true, 'SingleStore': true, 'CockroachDB': true, 'MS SQL': true }} />

<Callout type='warning'>
  `drizzle-seed` can only be used with `drizzle-orm@0.36.4` or higher. Versions lower than this may work at runtime but could have type issues and identity column issues, as this patch was introduced in `drizzle-orm@0.36.4`
</Callout>

`drizzle-seed` is a TypeScript library that helps you generate deterministic, yet realistic,
fake data to populate your database. By leveraging a seedable pseudorandom number generator (pRNG),
it ensures that the data you generate is consistent and reproducible across different runs.
This is especially useful for testing, development, and debugging purposes.


#### Limitations that are temporary and will be handled soon:

- Using cache with Drizzle Relational Queries
```ts
await db.query.users.findMany();
```

- Using cache with `better-sqlite3`, `Durable Objects`, `expo sqlite`
- Using cache with AWS Data API drivers
- Using cache with views


Source: https://orm.drizzle.team/docs/column-types/cockroach


import Section from '@mdx/Section.astro';
import Callout from '@mdx/Callout.astro';
import Npm from '@mdx/Npm.astro';

<Callout type='error'>
This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.
</Callout>

<Npm>
drizzle-orm@beta
drizzle-kit@beta -D
</Npm>

<br/>

We have native support for all of them, yet if that's not enough for you, feel free to create **[custom types](/docs/custom-types)**.

<Callout title='important' type='warning'>
All examples in this part of the documentation do not use database column name aliases, and column names are generated from TypeScript keys. 

You can use database aliases in column names if you want, and you can also use the `casing` parameter to define a mapping strategy for Drizzle. 

You can read more about it [here](/docs/sql-schema-declaration#shape-your-data-schema)
</Callout>


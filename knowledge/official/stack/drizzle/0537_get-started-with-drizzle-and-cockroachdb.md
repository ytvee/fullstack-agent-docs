# Get Started with Drizzle and CockroachDB

<Callout type='error'>
This page explains concepts available on drizzle versions `1.0.0-beta.2` and higher.
</Callout>

<br/>

<Prerequisites>
  - **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
  - **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
  - **node-postgres** - package for querying your PostgreSQL database - [read here](https://node-postgres.com/)
</Prerequisites>

Drizzle has native support for CockroachDB connections with the `node-postgres` and `postgres.js` drivers.

We will use `node-postgres` for this get started example. But if you want to find more ways to connect to postgresql check
our [CockroachDB Connection](/docs/get-started-cockroach) page 

<FileStructure/>


# Get Started with Drizzle and SQLite in existing project

<Prerequisites>  
  - **dotenv** - package for managing environment variables - [read here](https://www.npmjs.com/package/dotenv)
  - **bun** - javaScript all-in-one toolkit - [read here](https://bun.sh/)
  - **Bun SQL** - native bindings for working with PostgreSQL databases - [read here](https://bun.sh/docs/api/sql)
</Prerequisites>

<Callout type='error'>
In version `1.2.0`, Bun has issues with executing concurrent statements, which may lead to errors if you try to run several queries simultaneously.
We've created a [github issue](https://github.com/oven-sh/bun/issues/16774) that you can track. Once it's fixed, you should no longer encounter any such errors on Bun's SQL side
</Callout>

<FileStructure />


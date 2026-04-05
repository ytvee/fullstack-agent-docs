# Getting started (/docs/v6/postgres/getting-started)



Quickstart [#quickstart]

To **bootstrap a new Prisma ORM project with a Prisma Postgres database**, run the following command in your terminal:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma init --db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma init --db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma init --db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma init --db
    ```
  </CodeBlockTab>
</CodeBlockTabs>

After running this command, the terminal will guide you with next steps. Follow [this page](/v6/prisma-postgres/from-the-cli) to complete the setup for your first Prisma Postgres project.

If you need a database quickly for testing, or want to try out Prisma Postgres, you can run the following command to spin up a temporary 24-hour database:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx create-db@latest
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx create-db@latest
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx create-db@latest
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun create-db@latest
    ```
  </CodeBlockTab>
</CodeBlockTabs>

You can learn more about `npx create-db` in [the dedicated documentation](/v6/postgres/introduction/npx-create-db).

Prisma ORM [#prisma-orm]

The easiest ways to get started with Prisma Postgres is by following these guides:

* [**Start from scratch**](/v6/prisma-postgres/quickstart/prisma-orm)
* [**Import data from an existing database**](/v6/prisma-postgres/import-from-existing-database-postgresql)

If you are looking to explore Prisma Postgres in a fullstack project, check out these resources:

* [**Build a fullstack app with Next.js 15**](/v6/guides/nextjs)
* [**Next.js 15 example app**](https://github.com/prisma/nextjs-prisma-postgres-demo) (including authentication)

Connect via any database library / tool [#connect-via-any-database-library--tool]

You can access Prisma Postgres with any ORM or database tool of your choice. Once you have the connection string, you can follow the setup docs for PostgreSQL of any ORM or database tool:

* [Drizzle ORM](https://orm.drizzle.team/docs/get-started/postgresql-new)
* [Kysely](https://kysely.dev/docs/getting-started)
* [TypeORM](https://typeorm.io/#installation)
* [Sequelize](https://sequelize.org/docs/v6/getting-started/)
* [MikroORM](https://mikro-orm.io/docs/quick-start)
* [node-postgres](https://node-postgres.com/)

Getting started [#getting-started]

* [Start from scratch](/v6/prisma-postgres/quickstart/prisma-orm) - Create a new Prisma ORM project with Prisma Postgres
* [Import from existing database](/v6/prisma-postgres/import-from-existing-database-postgresql) - Import data from an existing database
* [Build with Next.js 15](/v6/guides/nextjs) - Build a fullstack app with Next.js 15 and Prisma Postgres

You can either start with a fresh Prisma Postgres project or import data from an existing database to Prisma Postgres.



# TypeORM (/docs/v6/guides/migrate-from-typeorm)



Introduction [#introduction]

This guide shows you how to migrate your application from TypeORM to Prisma ORM. We'll use an extended version of the [TypeORM Express example](https://github.com/typeorm/typescript-express-example/) as a [sample project](https://github.com/prisma/migrate-from-typeorm-to-prisma) to demonstrate the migration steps.

This migration guide uses PostgreSQL as the example database, but it equally applies to any other relational database that's [supported by Prisma ORM](/v6/orm/reference/supported-databases). You can learn how Prisma ORM compares to TypeORM on the [Prisma ORM vs TypeORM](/v6/orm/more/comparisons/prisma-and-typeorm) page.

Prerequisites [#prerequisites]

Before starting this guide, make sure you have:

* A TypeORM project you want to migrate
* Node.js installed (version 16 or higher)
* PostgreSQL or another supported database
* Basic familiarity with TypeORM and Express.js

2. Prepare for migration [#2-prepare-for-migration]

2.1. Understand the migration process [#21-understand-the-migration-process]

The steps for migrating from TypeORM to Prisma ORM are always the same, no matter what kind of application or API layer you're building:

1. Install the Prisma CLI
2. Introspect your database
3. Create a baseline migration
4. Install Prisma Client
5. Gradually replace your TypeORM queries with Prisma Client

These steps apply whether you're building a REST API (e.g., with Express, Koa, or NestJS), a GraphQL API (e.g., with Apollo Server, TypeGraphQL, or Nexus), or any other kind of application that uses TypeORM for database access.

2.2. Set up Prisma configuration [#22-set-up-prisma-configuration]

Create a new Prisma schema file:

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
    npx prisma init --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma init --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma init --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma init --output ../generated/prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Update the `DATABASE_URL` in the `.env` file with your database connection string:

```text
DATABASE_URL="postgresql://USER:PASSWORD@HOST:PORT/DATABASE"
```

2.3. Configure Prisma [#23-configure-prisma]

Create a `prisma.config.ts` file in the root of your project with the following content:

```typescript title="prisma.config.ts"
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

<CalloutContainer type="info">
  <CalloutDescription>
    You'll need to install the `dotenv` package to load environment variables. If you haven't already, install it using your package manager:

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
        npm install dotenv
        ```
      </CodeBlockTab>

      <CodeBlockTab value="pnpm">
        ```bash
        pnpm add dotenv
        ```
      </CodeBlockTab>

      <CodeBlockTab value="yarn">
        ```bash
        yarn add dotenv
        ```
      </CodeBlockTab>

      <CodeBlockTab value="bun">
        ```bash
        bun add dotenv
        ```
      </CodeBlockTab>
    </CodeBlockTabs>
  </CalloutDescription>
</CalloutContainer>

3. Migrate the database schema [#3-migrate-the-database-schema]

3.1. Introspect your database [#31-introspect-your-database]

Run Prisma's introspection to create the Prisma schema from your existing database:

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
    npx prisma db pull
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db pull
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db pull
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db pull
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This will create a `schema.prisma` file with your database schema.

3.2. Create a baseline migration [#32-create-a-baseline-migration]

Create and apply a baseline migration to mark the current state of your database:

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
    npx prisma migrate diff --from-empty --to-schema prisma/schema.prisma --script > baseline.sql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate diff --from-empty --to-schema prisma/schema.prisma --script > baseline.sql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate diff --from-empty --to-schema prisma/schema.prisma --script > baseline.sql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate diff --from-empty --to-schema prisma/schema.prisma --script > baseline.sql
    ```
  </CodeBlockTab>
</CodeBlockTabs>

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
    npx prisma migrate resolve --applied "baseline"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate resolve --applied "baseline"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate resolve --applied "baseline"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate resolve --applied "baseline"
    ```
  </CodeBlockTab>
</CodeBlockTabs>

4. Update your application code [#4-update-your-application-code]

4.1. Install Prisma Client [#41-install-prisma-client]

Install the Prisma Client package:

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
    npm install @prisma/client
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add @prisma/client
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add @prisma/client
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add @prisma/client
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Generate Prisma Client:

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
    npx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma generate
    ```
  </CodeBlockTab>
</CodeBlockTabs>

4.2. Replace TypeORM queries [#42-replace-typeorm-queries]

Start replacing your TypeORM queries with Prisma Client. Here's an example of how to convert some common queries:

<CodeBlockTabs defaultValue="TypeORM">
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="TypeORM">
      TypeORM
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="Prisma Client">
      Prisma Client
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="TypeORM">
    ```typescript
    // Find one
    const user = await userRepository.findOne({
      where: { id: 1 },
    });

    // Create
    const user = await userRepository.save({
      email: "alice@prisma.io",
      name: "Alice",
    });

    // Update
    await userRepository.update(1, {
      name: "New name",
    });

    // Delete
    await userRepository.delete(1);
    ```
  </CodeBlockTab>

  <CodeBlockTab value="Prisma Client">
    ```typescript
    // Find one
    const user = await prisma.user.findUnique({
      where: { id: 1 },
    });

    // Create
    const user = await prisma.user.create({
      data: {
        email: "alice@prisma.io",
        name: "Alice",
      },
    });

    // Update
    await prisma.user.update({
      where: { id: 1 },
      data: { name: "New name" },
    });

    // Delete
    await prisma.user.delete({
      where: { id: 1 },
    });
    ```
  </CodeBlockTab>
</CodeBlockTabs>

4.3. Update your controllers [#43-update-your-controllers]

Update your Express controllers to use Prisma Client. For example, here's how to update the `CreateUserAction`:

```typescript
import { prisma } from "../client";

export class CreateUserAction {
  async run(req: Request, res: Response) {
    const { email, name } = req.body;

    const result = await prisma.user.create({
      data: {
        email,
        name,
      },
    });

    return res.json(result);
  }
}
```

5. Test and deploy [#5-test-and-deploy]

5.1. Test your changes [#51-test-your-changes]

Test all migrated endpoints to ensure they work as expected:

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
    npm test
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm test
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn test
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun run test
    ```
  </CodeBlockTab>
</CodeBlockTabs>

5.2. Deploy your changes [#52-deploy-your-changes]

1. Deploy your schema changes:

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
    npx prisma migrate deploy
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate deploy
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate deploy
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate deploy
    ```
  </CodeBlockTab>
</CodeBlockTabs>

2. Deploy your application code with the updated dependencies.

Next steps [#next-steps]

Now that you've migrated to Prisma ORM, you can:

* Add more complex queries using Prisma's powerful query API
* Set up Prisma Studio for database management
* Implement database monitoring
* Add automated tests using Prisma's testing utilities

For more information:

* [Prisma ORM documentation](/v6/orm)
* [Prisma Client API reference](/v6/orm/prisma-client/setup-and-configuration/introduction)



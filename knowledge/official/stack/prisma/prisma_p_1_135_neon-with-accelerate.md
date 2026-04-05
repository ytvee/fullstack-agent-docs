# Neon with Accelerate (/docs/guides/integrations/neon-accelerate)



Introduction [#introduction]

This guides teaches you how to add connection pooling to a PostgreSQL database hosted on [Neon](https://neon.tech/) using [Prisma Accelerate](/accelerate).

Prisma Accelerate is a robust and mature connection pooler enabling your database to function properly during traffic spikes and high load scenarios. Check out this [video](https://www.youtube.com/watch?v=cnL75if6Aq0) demonstrating how it performs in a load test or [learn why connection pooling is important](https://www.prisma.io/blog/saving-black-friday-with-connection-pooling).

Prerequisites [#prerequisites]

To successfully complete this guide, you need **a connection string for a PostgreSQL instance hosted on Neon**. It typically looks similar to this:

```bash no-copy
postgresql://neondb_owner:[YOUR-PASSWORD]@ep-lingering-hat-a2e7tkt3.eu-central-1.aws.neon.tech/neondb?sslmode=require
```

If you already have a project using Prisma ORM, you can skip the first two steps and jump ahead to [Step 3. Install the Accelerate extension](#3-install-the-accelerate-extension).

1. Set up Prisma ORM [#1-set-up-prisma-orm]

Start by installing the Prisma CLI in your project:

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
    npm install prisma --save-dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add prisma --save-dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add prisma --dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add prisma --dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Then, run the following command to initialize a new project:

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
    npx prisma init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma init
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This will create a new `prisma` directory with a `schema.prisma` file and add a `.env` file with the `DATABASE_URL` environment variable.

Update the file and set the `DATABASE_URL` to your Neon connection string:

```text title=".env"
DATABASE_URL="postgresql://neondb_owner:[YOUR-PASSWORD]@ep-lingering-hat-a2e7tkt3.eu-central-1.aws.neon.tech/neondb?sslmode=require"
```

Create a `prisma.config.ts` file to configure Prisma:

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
    You'll need to install the `dotenv` package to load environment variables:

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

2. Introspect your database [#2-introspect-your-database]

Next, run the following command to introspect your database and create your data model:

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

This command reads your database schema and creates new models in your `schema.prisma` file that match the tables in your database.

<CalloutContainer type="info">
  <CalloutDescription>
    If you want to use Prisma Migrate in the future, you also need to [baseline your database](/orm/prisma-migrate/workflows/baselining).
  </CalloutDescription>
</CalloutContainer>

3. Install the Accelerate extension [#3-install-the-accelerate-extension]

Install the Prisma Client extension for Accelerate:

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
    npm install @prisma/extension-accelerate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add @prisma/extension-accelerate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add @prisma/extension-accelerate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add @prisma/extension-accelerate
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This is needed to access Prisma Accelerate's connection pool.

4. Set up Accelerate in the Prisma Console [#4-set-up-accelerate-in-the-prisma-console]

To set up Accelerate in the Prisma Console, follow these steps:

1. Log into the [Prisma Console](https://console.prisma.io/?utm_source=docs\&utm_medium=content\&utm_content=guides).
2. Select **New project**
3. Choose a **Name** for your project
4. In the **Choose your starting product** section, find the **Accelerate** card and click **Get started**
5. In the field for your **Database connection string**, paste your Neon connection string
6. Select the **Region** that's closest to your database
7. Click **Create project**
8. On the next screen, click **Enable Accelerate**

Once you went through these steps, you'll be redirected to another page where you need to the click the **Generate API key** button.

You'll then be shown a new connection URL which enables you to connect to Prisma Accelerate's connection pool. This needs to be set as the new `DATABASE_URL` in your `.env` file:

```text title=".env"
DATABASE_URL="prisma://accelerate.prisma-data.net/?api_key=ey..."
```

<CalloutContainer type="info">
  <CalloutDescription>
    If you want to use Prisma Migrate with Prisma Accelerate, you need to provide a direct database URL in your `prisma.config.ts` file. The Accelerate URL (starting with `prisma://`) is used for queries via PrismaClient, while the direct database URL is used for migrations.

    Update your `prisma.config.ts`:

    ```typescript title="prisma.config.ts"
    import "dotenv/config";
    import { defineConfig, env } from "prisma/config";

    export default defineConfig({
      schema: "prisma/schema.prisma",
      migrations: {
        path: "prisma/migrations",
      },
      datasource: {
        url: env("DIRECT_URL"), // Direct database URL for migrations
      },
    });
    ```

    And add the `DIRECT_URL` to your `.env` file:

    ```text title=".env"
    DATABASE_URL="prisma://accelerate.prisma-data.net/?api_key=ey..."
    DIRECT_URL="postgresql://neondb_owner:[YOUR-PASSWORD]@ep-lingering-hat-a2e7tkt3.eu-central-1.aws.neon.tech/neondb?sslmode=require"
    ```
  </CalloutDescription>
</CalloutContainer>

5. Generate Prisma Client [#5-generate-prisma-client]

With your Prisma schema in place, you can go ahead and generate Prisma Client:

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

<CalloutContainer type="info">
  <CalloutDescription>
    In Prisma v7, the `--no-engine` flag is no longer required when using Prisma Accelerate. Previously, you would run `prisma generate --no-engine`, but now the standard `prisma generate` command works for all use cases.
  </CalloutDescription>
</CalloutContainer>

6. Send queries through the connection pool [#6-send-queries-through-the-connection-pool]

In your application code, you now need to apply the Accelerate extension to your Prisma Client instance:

```ts
import { PrismaClient } from "./generated/prisma/client";
import { withAccelerate } from "@prisma/extension-accelerate";

const prisma = new PrismaClient({
  accelerateUrl: process.env.DATABASE_URL,
}).$extends(withAccelerate());
```

At this point, you can now start sending queries which will be routed through the connection pool to your database.



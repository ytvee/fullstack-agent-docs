# push (/docs/cli/db/push)



The `prisma db push` command pushes the state of your Prisma schema to the database without using migrations. It creates the database if it does not exist.

This command is a good choice when you don't need to version schema changes, such as during prototyping and local development.

Usage [#usage]

```bash
prisma db push [options]
```

The datasource URL configuration is read from the Prisma config file (e.g., `prisma.config.ts`).

Prerequisites [#prerequisites]

Configure your database connection in `prisma.config.ts`:

```prisma file=schema.prisma
generator client {
  provider = "prisma-client"
  output   = "../generated/prisma"
}

datasource db {
  provider = "sqlite"
}
```

```typescript file=prisma.config.ts
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

Options [#options]

| Option               | Description                                             |
| -------------------- | ------------------------------------------------------- |
| `-h`, `--help`       | Display help message                                    |
| `--config`           | Custom path to your Prisma config file                  |
| `--schema`           | Custom path to your Prisma schema                       |
| `--url`              | Override the datasource URL from the Prisma config file |
| `--accept-data-loss` | Ignore data loss warnings                               |
| `--force-reset`      | Force a reset of the database before push               |

<CalloutContainer type="warning">
  <CalloutDescription>
    In Prisma v7, `db push` no longer runs `prisma generate` automatically. Run it explicitly if needed.
  </CalloutDescription>
</CalloutContainer>

Examples [#examples]

Push the schema to the database [#push-the-schema-to-the-database]

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
    npx prisma db push
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db push
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db push
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db push
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Accept data loss [#accept-data-loss]

Proceed even if the changes might result in data loss:

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
    npx prisma db push --accept-data-loss
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db push --accept-data-loss
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db push --accept-data-loss
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db push --accept-data-loss
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Specify a schema path [#specify-a-schema-path]

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
    npx prisma db push --schema=/tmp/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db push --schema=/tmp/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db push --schema=/tmp/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db push --schema=/tmp/schema.prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Force reset before push [#force-reset-before-push]

Reset the database before applying changes:

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
    npx prisma db push --force-reset
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db push --force-reset
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db push --force-reset
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db push --force-reset
    ```
  </CodeBlockTab>
</CodeBlockTabs>

See also [#see-also]

* [Conceptual overview of `db push` and when to use it over Prisma Migrate](/orm/prisma-migrate/workflows/prototyping-your-schema)
* [Schema prototyping with `db push`](/orm/prisma-migrate/workflows/prototyping-your-schema)



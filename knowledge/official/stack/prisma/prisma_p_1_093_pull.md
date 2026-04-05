# pull (/docs/cli/db/pull)



The `prisma db pull` command connects to your database and adds Prisma models to your Prisma schema that reflect the current database schema.

Usage [#usage]

```bash
prisma db pull [options]
```

The datasource URL configuration is read from the Prisma config file (e.g., `prisma.config.ts`).

<CalloutContainer type="warning">
  <CalloutDescription>
    This command will overwrite the current `schema.prisma` file with the new schema. Back up your current schema or commit to version control before running `db pull` if it contains important modifications.
  </CalloutDescription>
</CalloutContainer>

<CalloutContainer type="info">
  <CalloutDescription>
    Introspection with `db pull` on the [MongoDB connector](/orm/core-concepts/supported-databases/mongodb) samples the data instead of reading a schema.
  </CalloutDescription>
</CalloutContainer>

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

Flags [#flags]

| Flag           | Description                                    |
| -------------- | ---------------------------------------------- |
| `-h`, `--help` | Display help message                           |
| `--force`      | Ignore current Prisma schema file              |
| `--print`      | Print the introspected Prisma schema to stdout |

Options [#options]

| Option                   | Description                                                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `--config`               | Custom path to your Prisma config file                                                                                      |
| `--schema`               | Custom path to your Prisma schema                                                                                           |
| `--url`                  | Override the datasource URL from the Prisma config file                                                                     |
| `--composite-type-depth` | Depth for introspecting composite types (e.g., MongoDB Embedded Documents). Default `-1` for infinite depth, `0` to disable |
| `--schemas`              | Specify database schemas to introspect (overrides datasource block)                                                         |
| `--local-d1`             | Generate a Prisma schema from a local Cloudflare D1 database                                                                |

Examples [#examples]

Introspect the database [#introspect-the-database]

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

Output:

```text
Introspecting based on datasource defined in schema.prisma …

✔ Introspected 2 models and wrote them into schema.prisma in 38ms

Run prisma generate to generate Prisma Client.
```

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
    npx prisma db pull --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db pull --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db pull --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db pull --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Print to stdout instead of writing to file [#print-to-stdout-instead-of-writing-to-file]

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
    npx prisma db pull --print
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db pull --print
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db pull --print
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db pull --print
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Force overwrite existing schema [#force-overwrite-existing-schema]

Ignore any customizations in the current schema:

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
    npx prisma db pull --force
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db pull --force
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db pull --force
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db pull --force
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Set composite type depth for MongoDB [#set-composite-type-depth-for-mongodb]

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
    npx prisma db pull --composite-type-depth=2
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db pull --composite-type-depth=2
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db pull --composite-type-depth=2
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db pull --composite-type-depth=2
    ```
  </CodeBlockTab>
</CodeBlockTabs>



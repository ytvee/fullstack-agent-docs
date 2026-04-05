# execute (/docs/cli/db/execute)



The `prisma db execute` command applies a SQL script to the database without interacting with the Prisma migrations table.

<CalloutContainer type="warning">
  <CalloutDescription>
    This command is currently not supported on [MongoDB](/orm/core-concepts/supported-databases/mongodb).
  </CalloutDescription>
</CalloutContainer>

Usage [#usage]

```bash
prisma db execute [options]
```

The datasource URL configuration is read from the Prisma config file (e.g., `prisma.config.ts`).

The script input must be provided using either `--file` or `--stdin`. The whole script is sent as a single command to the database.

The output is connector-specific and reports success or failure only—it's not meant for returning data.

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

| Option         | Description                                     |
| -------------- | ----------------------------------------------- |
| `-h`, `--help` | Display help message                            |
| `--config`     | Custom path to your Prisma config file          |
| `--file`       | Path to a file containing the script to execute |

Flags [#flags]

| Flag      | Description                                          |
| --------- | ---------------------------------------------------- |
| `--stdin` | Use terminal standard input as the script to execute |

Either `--file` or `--stdin` is required.

<CalloutContainer type="info">
  <CalloutDescription>
    **Prisma v7 breaking change**: The `--schema` and `--url` options have been removed. Configure your database connection in `prisma.config.ts` instead.
  </CalloutDescription>
</CalloutContainer>

Examples [#examples]

Execute a SQL file [#execute-a-sql-file]

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
    npx prisma db execute --file ./script.sql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db execute --file ./script.sql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db execute --file ./script.sql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db execute --file ./script.sql
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Execute SQL from stdin [#execute-sql-from-stdin]

```bash
echo 'TRUNCATE TABLE dev;' | prisma db execute --stdin
```

See also [#see-also]

* [Migration troubleshooting in production](/orm/prisma-migrate/workflows/patching-and-hotfixing#fixing-failed-migrations-with-migrate-diff-and-db-execute)



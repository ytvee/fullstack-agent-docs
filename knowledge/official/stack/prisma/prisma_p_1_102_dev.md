# dev (/docs/cli/migrate/dev)



The `prisma migrate dev` command creates and applies migrations during development. It requires a [shadow database](/orm/prisma-migrate/understanding-prisma-migrate/shadow-database).

**For use in development environments only.**

<CalloutContainer type="warning">
  <CalloutDescription>
    This command is not supported on [MongoDB](/orm/core-concepts/supported-databases/mongodb). Use [`db push`](/cli/db/push) instead.
  </CalloutDescription>
</CalloutContainer>

Usage [#usage]

```bash
prisma migrate dev [options]
```

The datasource URL configuration is read from the Prisma config file (e.g., `prisma.config.ts`).

How it works [#how-it-works]

1. Reruns the existing migration history in the shadow database to detect schema drift
2. Applies pending migrations to the shadow database
3. Generates a new migration from any changes you made to the Prisma schema
4. Applies all unapplied migrations to the development database and updates the `_prisma_migrations` table

<CalloutContainer type="info">
  <CalloutDescription>
    **Prisma v7**: `migrate dev` no longer automatically triggers `prisma generate` or seed scripts. Run them explicitly if needed.
  </CalloutDescription>
</CalloutContainer>

Options [#options]

| Option          | Description                                             |
| --------------- | ------------------------------------------------------- |
| `-h`, `--help`  | Display help message                                    |
| `--config`      | Custom path to your Prisma config file                  |
| `--schema`      | Custom path to your Prisma schema                       |
| `--url`         | Override the datasource URL from the Prisma config file |
| `-n`, `--name`  | Name the migration                                      |
| `--create-only` | Create a new migration but do not apply it              |

<CalloutContainer type="info">
  <CalloutDescription>
    If a [schema drift](/orm/prisma-migrate/understanding-prisma-migrate/shadow-database#detecting-schema-drift) is detected while running with `--create-only`, you will be prompted to reset your database.
  </CalloutDescription>
</CalloutContainer>

Examples [#examples]

Create and apply migrations [#create-and-apply-migrations]

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
    npx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Name the migration [#name-the-migration]

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
    npx prisma migrate dev --name added_job_title
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev --name added_job_title
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev --name added_job_title
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev --name added_job_title
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Create migration without applying [#create-migration-without-applying]

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
    npx prisma migrate dev --create-only
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev --create-only
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev --create-only
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev --create-only
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This creates the migration file but doesn't apply it. Run `prisma migrate dev` again to apply.

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
    npx prisma migrate dev --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

See also [#see-also]

* [Conceptual overview of Prisma Migrate](/orm/prisma-migrate)
* [Developing with Prisma Migrate](/orm/prisma-migrate)



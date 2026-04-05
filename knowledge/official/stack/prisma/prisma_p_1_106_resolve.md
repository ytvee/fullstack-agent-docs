# resolve (/docs/cli/migrate/resolve)



The `prisma migrate resolve` command allows you to solve migration history issues in production by marking a failed migration as already applied (supports baselining) or rolled back.

<CalloutContainer type="warning">
  <CalloutDescription>
    This command is not supported on [MongoDB](/orm/core-concepts/supported-databases/mongodb). Use [`db push`](/cli/db/push) instead.
  </CalloutDescription>
</CalloutContainer>

Usage [#usage]

```bash
prisma migrate resolve [options]
```

The datasource URL configuration is read from the Prisma config file (e.g., `prisma.config.ts`).

<CalloutContainer type="info">
  <CalloutDescription>
    This command can only be used with a failed migration. Using it with a successful migration results in an error.
  </CalloutDescription>
</CalloutContainer>

Use cases [#use-cases]

* Recover from failed migrations
* Baseline databases when starting to use Prisma Migrate on existing databases
* Reconcile hotfixes done manually on databases with your migration history

Run `prisma migrate status` to identify if you need to use `resolve`.

Options [#options]

| Option          | Description                                |
| --------------- | ------------------------------------------ |
| `-h`, `--help`  | Display help message                       |
| `--config`      | Custom path to your Prisma config file     |
| `--schema`      | Custom path to your Prisma schema          |
| `--applied`     | Record a specific migration as applied     |
| `--rolled-back` | Record a specific migration as rolled back |

You must specify either `--applied` or `--rolled-back`.

Examples [#examples]

Mark a migration as applied [#mark-a-migration-as-applied]

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
    npx prisma migrate resolve --applied 20201231000000_add_users_table
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate resolve --applied 20201231000000_add_users_table
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate resolve --applied 20201231000000_add_users_table
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate resolve --applied 20201231000000_add_users_table
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Mark a migration as rolled back [#mark-a-migration-as-rolled-back]

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
    npx prisma migrate resolve --rolled-back 20201231000000_add_users_table
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate resolve --rolled-back 20201231000000_add_users_table
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate resolve --rolled-back 20201231000000_add_users_table
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate resolve --rolled-back 20201231000000_add_users_table
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
    npx prisma migrate resolve --rolled-back 20201231000000_add_users_table --schema=./schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate resolve --rolled-back 20201231000000_add_users_table --schema=./schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate resolve --rolled-back 20201231000000_add_users_table --schema=./schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate resolve --rolled-back 20201231000000_add_users_table --schema=./schema.prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

See also [#see-also]

* [Resolving migration history issues](https://pris.ly/d/migrate-resolve)



# reset (/docs/cli/migrate/reset)



The `prisma migrate reset` command resets your database and re-applies all migrations.

**For use in development environments only.**

<CalloutContainer type="warning">
  <CalloutDescription>
    This command is not supported on [MongoDB](/orm/core-concepts/supported-databases/mongodb). Use [`db push`](/cli/db/push) instead.
  </CalloutDescription>
</CalloutContainer>

Usage [#usage]

```bash
prisma migrate reset [options]
```

The datasource URL configuration is read from the Prisma config file (e.g., `prisma.config.ts`).

How it works [#how-it-works]

1. Drops the database/schema if possible, or performs a soft reset if the environment doesn't allow it
2. Creates a new database/schema with the same name
3. Applies all migrations
4. Runs seed scripts

Options [#options]

| Option          | Description                            |
| --------------- | -------------------------------------- |
| `-h`, `--help`  | Display help message                   |
| `--config`      | Custom path to your Prisma config file |
| `--schema`      | Custom path to your Prisma schema      |
| `-f`, `--force` | Skip the confirmation prompt           |

Examples [#examples]

Reset the database [#reset-the-database]

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
    npx prisma migrate reset
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate reset
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate reset
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate reset
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Skip confirmation prompt [#skip-confirmation-prompt]

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
    npx prisma migrate reset --force
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate reset --force
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate reset --force
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate reset --force
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
    npx prisma migrate reset --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate reset --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate reset --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate reset --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

AI safety guardrails [#ai-safety-guardrails]

Prisma ORM includes built-in safety checks to prevent accidental destructive commands when run through AI coding assistants.

When AI agents like Claude Code, Cursor, Gemini CLI, or others attempt `prisma migrate reset --force`, Prisma blocks execution and shows a protective error message.

To proceed, you must provide explicit consent. The AI agent will:

1. Explain what action it's attempting
2. Warn that this action irreversibly destroys all data
3. Confirm whether this is a development or production database
4. Ask for your explicit consent before proceeding

After consent, the AI sets the `PRISMA_USER_CONSENT_FOR_DANGEROUS_AI_ACTION` environment variable and reruns the command.



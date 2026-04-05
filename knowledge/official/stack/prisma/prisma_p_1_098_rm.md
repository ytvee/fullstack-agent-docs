# rm (/docs/cli/dev/rm)



The `prisma dev rm` command removes the data of one or more [local Prisma Postgres](/postgres/database/local-development) databases from your file system.

Usage [#usage]

```bash
prisma dev rm [options] <name>
```

Arguments [#arguments]

| Argument | Description                                           |
| -------- | ----------------------------------------------------- |
| `<name>` | Name(s) or glob pattern(s) of the server(s) to remove |

Options [#options]

| Option    | Description                                   | Default |
| --------- | --------------------------------------------- | ------- |
| `--debug` | Enable debug logging                          | `false` |
| `--force` | Stop any running servers before removing them | `false` |

Without `--force`, the command fails if any server is running.

Examples [#examples]

Remove a specific database [#remove-a-specific-database]

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
    npx prisma dev rm mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev rm mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev rm mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev rm mydb
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Remove multiple databases with a pattern [#remove-multiple-databases-with-a-pattern]

Remove all databases starting with `mydb`:

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
    npx prisma dev rm mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev rm mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev rm mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev rm mydb*
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Force remove a running database [#force-remove-a-running-database]

Stop and remove a database in one command:

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
    npx prisma dev rm --force mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev rm --force mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev rm --force mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev rm --force mydb
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CalloutContainer type="info">
  <CalloutDescription>
    The `rm` command is interactive and includes safety prompts to prevent accidental data loss.
  </CalloutDescription>
</CalloutContainer>



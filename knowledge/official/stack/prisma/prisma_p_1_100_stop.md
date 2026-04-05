# stop (/docs/cli/dev/stop)



The `prisma dev stop` command stops one or more [local Prisma Postgres](/postgres/database/local-development) databases.

Usage [#usage]

```bash
prisma dev stop [options] <name>
```

Arguments [#arguments]

| Argument | Description                                         |
| -------- | --------------------------------------------------- |
| `<name>` | Name(s) or glob pattern(s) of the server(s) to stop |

Options [#options]

| Option    | Description          | Default |
| --------- | -------------------- | ------- |
| `--debug` | Enable debug logging | `false` |

Examples [#examples]

Stop a specific database [#stop-a-specific-database]

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
    npx prisma dev stop mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev stop mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev stop mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev stop mydb
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Stop multiple databases with a pattern [#stop-multiple-databases-with-a-pattern]

Stop all databases starting with `mydb`:

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
    npx prisma dev stop mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev stop mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev stop mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev stop mydb*
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CalloutContainer type="info">
  <CalloutDescription>
    The `stop` command is interactive and includes safety prompts to prevent accidental operations.
  </CalloutDescription>
</CalloutContainer>



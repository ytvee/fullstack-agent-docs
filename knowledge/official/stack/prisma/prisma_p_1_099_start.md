# start (/docs/cli/dev/start)



The `prisma dev start` command starts existing [local Prisma Postgres](/postgres/database/local-development) instances in the background.

Usage [#usage]

```bash
prisma dev start [options] <name>
```

Arguments [#arguments]

| Argument | Description                                          |
| -------- | ---------------------------------------------------- |
| `<name>` | Name(s) or glob pattern(s) of the server(s) to start |

Options [#options]

| Option    | Description          | Default |
| --------- | -------------------- | ------- |
| `--debug` | Enable debug logging | `false` |

<CalloutContainer type="info">
  <CalloutDescription>
    This command only works with instances that already exist. Use `prisma dev` to create a new instance.
  </CalloutDescription>
</CalloutContainer>

Examples [#examples]

Start a specific database [#start-a-specific-database]

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
    npx prisma dev start mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev start mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev start mydb
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev start mydb
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Start multiple databases with a pattern [#start-multiple-databases-with-a-pattern]

Start all databases starting with `mydb`:

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
    npx prisma dev start mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev start mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev start mydb*
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev start mydb*
    ```
  </CodeBlockTab>
</CodeBlockTabs>



# ls (/docs/cli/dev/ls)



The `prisma dev ls` command lists all available [local Prisma Postgres](/postgres/database/local-development) instances on your system.

Usage [#usage]

```bash
prisma dev ls [options]
```

Options [#options]

| Option    | Description          | Default |
| --------- | -------------------- | ------- |
| `--debug` | Enable debug logging | `false` |

Examples [#examples]

List all servers [#list-all-servers]

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
    npx prisma dev ls
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev ls
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev ls
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev ls
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This shows all instances on your system with their current status and configuration.



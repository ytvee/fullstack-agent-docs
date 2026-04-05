# debug (/docs/cli/debug)



The `prisma debug` command prints information helpful for debugging and bug reports.

<CalloutContainer type="info">
  <CalloutDescription>
    Available from version 5.6.0 and newer.
  </CalloutDescription>
</CalloutContainer>

Usage [#usage]

```bash
prisma debug [options]
```

Options [#options]

| Option         | Description                            |
| -------------- | -------------------------------------- |
| `-h`, `--help` | Display help message                   |
| `--config`     | Custom path to your Prisma config file |
| `--schema`     | Custom path to your Prisma schema      |

Examples [#examples]

Display debug information [#display-debug-information]

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
    npx prisma debug
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma debug
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma debug
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma debug
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Output:

```text
-- Prisma schema --
Path: /prisma/schema.prisma

-- Local cache directory for engines files --
Path: /.cache/prisma

-- Environment variables --
When not set, the line is dimmed and no value is displayed.
When set, the line is bold and the value is inside the `` backticks.

For general debugging
 - CI:
 - DEBUG:
 - NODE_ENV:
 - RUST_LOG:
 - RUST_BACKTRACE:
 - NO_COLOR:
 - TERM: `xterm-256color`
 - NODE_TLS_REJECT_UNAUTHORIZED:
 - NO_PROXY:
 - http_proxy:
 - HTTP_PROXY:
 - https_proxy:
 - HTTPS_PROXY:

For hiding messages
 - PRISMA_DISABLE_WARNINGS:
 - PRISMA_HIDE_PREVIEW_FLAG_WARNINGS:
 - PRISMA_HIDE_UPDATE_MESSAGE:

For downloading engines
 - PRISMA_ENGINES_MIRROR:
 - PRISMA_BINARIES_MIRROR (deprecated):
 - PRISMA_ENGINES_CHECKSUM_IGNORE_MISSING:
 - BINARY_DOWNLOAD_VERSION:

For custom engines
 - PRISMA_SCHEMA_ENGINE_BINARY:
 - PRISMA_MIGRATION_ENGINE_BINARY:

For Prisma Client
 - PRISMA_SHOW_ALL_TRACES:

For Prisma Migrate
 - PRISMA_SCHEMA_DISABLE_ADVISORY_LOCK:

For Prisma Studio
 - BROWSER:

-- Terminal is interactive? --
true

-- CI detected? --
false
```

Use with older versions [#use-with-older-versions]

If using an older Prisma version:

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
    npx prisma@latest debug
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma@latest debug
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma@latest debug
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma@latest debug
    ```
  </CodeBlockTab>
</CodeBlockTabs>



# version (/docs/cli/version)



The `prisma version` command outputs information about your current Prisma version, platform, and engine binaries.

Usage [#usage]

```bash
prisma version [options]
```

Or use the shorthand:

```bash
prisma -v [options]
```

Options [#options]

| Option         | Description                               |
| -------------- | ----------------------------------------- |
| `-h`, `--help` | Display help message                      |
| `--json`       | Output version information in JSON format |

Examples [#examples]

Display version information [#display-version-information]

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
    npx prisma version
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma version
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma version
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma version
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Output:

```text
Environment variables loaded from .env
prisma               : 2.21.0-dev.4
@prisma/client       : 2.21.0-dev.4
Current platform     : windows
Query Engine         : query-engine 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6
Migration Engine     : migration-engine-cli 2fb8f444d9cdf7c0beee7b041194b42d7a9ce1e6
Format Binary        : prisma-fmt 60ba6551f29b17d7d6ce479e5733c70d9c00860e
Default Engines Hash : 60ba6551f29b17d7d6ce479e5733c70d9c00860e
Studio               : 0.365.0
```

Display version using shorthand [#display-version-using-shorthand]

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
    npx prisma -v
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma -v
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma -v
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma -v
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Display version as JSON [#display-version-as-json]

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
    npx prisma version --json
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma version --json
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma version --json
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma version --json
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Output:

```json
{
  "prisma": "2.21.0-dev.4",
  "@prisma/client": "2.21.0-dev.4",
  "current-platform": "windows",
  "query-engine": "query-engine 60ba6551f29b17d7d6ce479e5733c70d9c00860e",
  "migration-engine": "migration-engine-cli 60ba6551f29b17d7d6ce479e5733c70d9c00860e",
  "format-binary": "prisma-fmt 60ba6551f29b17d7d6ce479e5733c70d9c00860e",
  "default-engines-hash": "60ba6551f29b17d7d6ce479e5733c70d9c00860e",
  "studio": "0.365.0"
}
```



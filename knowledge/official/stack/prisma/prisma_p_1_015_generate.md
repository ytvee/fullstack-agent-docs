# generate (/docs/cli/generate)



The `prisma generate` command generates assets like Prisma Client based on the [`generator`](/orm/prisma-schema/overview/generators) and [`data model`](/orm/prisma-schema/data-model/models) blocks defined in your `schema.prisma` file.

Usage [#usage]

```bash
prisma generate [options]
```

How it works [#how-it-works]

1. Inspects the current directory to find a Prisma schema
2. Generates a customized Prisma Client based on your schema into the output directory specified in the generator block

Prerequisites [#prerequisites]

Add a generator definition in your `schema.prisma` file:

```prisma
generator client {
  provider = "prisma-client"
  output   = "./generated"
}
```

Options [#options]

| Option             | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `-h`, `--help`     | Display help message                                   |
| `--config`         | Custom path to your Prisma config file                 |
| `--schema`         | Custom path to your Prisma schema                      |
| `--sql`            | Generate typed SQL module                              |
| `--watch`          | Watch the Prisma schema and regenerate after changes   |
| `--generator`      | Generator to use (can be provided multiple times)      |
| `--no-hints`       | Hide hint messages (still outputs errors and warnings) |
| `--require-models` | Do not allow generating a client without models        |

Examples [#examples]

Generate Prisma Client [#generate-prisma-client]

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
    npx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma generate
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma generate
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Output:

```text
✔ Generated Prisma Client to ./node_modules/.prisma/client in 61ms

You can now start using Prisma Client in your code:

import { PrismaClient } from '../prisma/generated/client'

const prisma = new PrismaClient()
```

Generate with a custom schema path [#generate-with-a-custom-schema-path]

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
    npx prisma generate --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma generate --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma generate --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma generate --schema=./alternative/schema.prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Watch mode [#watch-mode]

Automatically regenerate when the schema changes:

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
    npx prisma generate --watch
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma generate --watch
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma generate --watch
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma generate --watch
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Output:

```text
Watching... /home/prismauser/prisma/schema.prisma

✔ Generated Prisma Client to ./node_modules/.prisma/client in 45ms
```

Generate specific generators [#generate-specific-generators]

Run only specific generators:

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
    npx prisma generate --generator client
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma generate --generator client
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma generate --generator client
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma generate --generator client
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Multiple generators:

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
    npx prisma generate --generator client --generator zod_schemas
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma generate --generator client --generator zod_schemas
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma generate --generator client --generator zod_schemas
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma generate --generator client --generator zod_schemas
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Generated assets [#generated-assets]

The `prisma-client` generator creates a customized client for working with your database. You can [customize the output folder](/orm/reference/prisma-schema-reference#fields-for-prisma-client-provider) using the `output` field in the generator block.



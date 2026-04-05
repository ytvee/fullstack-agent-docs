# Prisma Studio (/docs/studio)



[Prisma Studio](https://www.prisma.io/studio) works with or without Prisma ORM and supports the following workflows:

* Viewing and editing data in a spreadsheet-like interface
* Real-time schema introspection
* Embedding directly into your Next.js applications
* VS Code integration for in-editor database management

Supported databases [#supported-databases]

* PostgreSQL
* MySQL
* SQLite

Quick start [#quick-start]

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
    # With Prisma project
    npx prisma studio

    # With direct database connection
    npx prisma studio --url="postgresql://user:password@localhost:5432/dbname"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    # With Prisma project
    pnpm dlx prisma studio

    # With direct database connection
    pnpm dlx prisma studio --url="postgresql://user:password@localhost:5432/dbname"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    # With Prisma project
    yarn dlx prisma studio

    # With direct database connection
    yarn dlx prisma studio --url="postgresql://user:password@localhost:5432/dbname"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    # With Prisma project
    bun x prisma studio

    # With direct database connection
    bun x prisma studio --url="postgresql://user:password@localhost:5432/dbname"
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Getting started [#getting-started]

* [Getting Started](/studio/getting-started) - Learn how to set up and use Prisma Studio to manage your database
* [Embed Studio](/studio/integrations/embedding) - Learn how to embed Prisma Studio in your own applications
* [Studio in VS Code](/studio/integrations/vscode-integration) - Learn how to use Prisma Studio directly in VS Code



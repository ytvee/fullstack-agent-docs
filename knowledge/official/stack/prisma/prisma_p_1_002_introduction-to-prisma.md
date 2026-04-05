# Introduction to Prisma (/docs)



[**Prisma ORM**](/orm) is an open-source ORM that provides fast, type-safe access to Postgres, MySQL, SQLite, and other databases, and runs smoothly across Node.js, Bun, and Deno.

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
    npx prisma init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma init
    ```
  </CodeBlockTab>
</CodeBlockTabs>

[**Prisma Postgres**](/postgres) is a fully managed PostgreSQL database that scales to zero, integrates with [Prisma ORM](/orm) and [Prisma Studio](/studio), and includes a [generous free tier](https://www.prisma.io/pricing).

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
    npx create-db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx create-db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx create-db
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun create-db
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<Cards>
  <Card
    href="/prisma-orm/quickstart/prisma-postgres"
    title="Use Prisma Postgres"
    icon={<div className="text-primary"><svg xmlns="http://www.w3.org/2000/svg" width="159" height="195" viewBox="0 0 640 640" fill="none"><path d="M355.2 85C348.2 72.1 334.7 64 320 64C305.3 64 291.8 72.1 284.8 85L209.7 224L430.2 224L355.1 85zM123.3 384L516.6 384L456.1 272L183.7 272L123.2 384zM97.4 432L68.8 485C62.1 497.4 62.4 512.4 69.6 524.5C76.8 536.6 89.9 544 104 544L536 544C550.1 544 563.1 536.6 570.4 524.5C577.7 512.4 577.9 497.4 571.2 485L542.6 432L97.4 432z" fill="currentColor"/></svg></div>
}
  >
    **Need a database?** Get started with your favorite framework and Prisma Postgres.
  </Card>

  <Card href="/prisma-postgres/quickstart/prisma-orm" title="Bring your own database" icon={<Database className="text-primary" />}>
    **Already have a database?** Use Prisma ORM for a type-safe developer experience and automated migrations.
  </Card>
</Cards>



# Schema management in teams (/docs/v6/guides/implementing-schema-changes)



Introduction [#introduction]

When working in a team, managing database schema changes can be challenging. This guide shows you how to effectively collaborate on schema changes using Prisma Migrate, ensuring that all team members can safely contribute to and incorporate schema changes.

Prerequisites [#prerequisites]

Before starting this guide, make sure you have:

* Node.js installed (version 20 or higher)
* A Prisma project set up with migrations
* A relational database (PostgreSQL, MySQL, SQLite, SQL Server, etc.)
* Basic understanding of Git
* Basic familiarity with Prisma Migrate

<CalloutContainer type="warning">
  <CalloutDescription>
    This guide **does not apply for MongoDB**.<br />
    Instead of `migrate dev`, [`db push`](/v6/orm/prisma-migrate/workflows/prototyping-your-schema) is used for [MongoDB](/v6/orm/overview/databases/mongodb).
  </CalloutDescription>
</CalloutContainer>

1. Understand migration basics [#1-understand-migration-basics]

1.1. Migration order [#11-migration-order]

Migrations are **applied in the same order as they were created**. The creation date is part of the migration subfolder name - for example, `20210316081837-updated-fields` was created on `2021-03-16-08:18:37`.

1.2. Source control requirements [#12-source-control-requirements]

You should commit the following files to source control:

* The contents of the `.prisma/migrations` folder, including the `migration_lock.toml` file
* The Prisma Schema (`schema.prisma`)

Source-controlling the `schema.prisma` file is not enough - you must include your migration history because:

* Customized migrations contain information that cannot be represented in the Prisma schema
* The `prisma migrate deploy` command only runs migration files

1.3. Configure Prisma [#13-configure-prisma]

Create a `prisma.config.ts` file in the root of your project with the following content:

```typescript title="prisma.config.ts"
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

<CalloutContainer type="info">
  <CalloutDescription>
    You'll need to install the `dotenv` package to load environment variables. If you haven't already, install it using your package manager:

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
        npm install dotenv
        ```
      </CodeBlockTab>

      <CodeBlockTab value="pnpm">
        ```bash
        pnpm add dotenv
        ```
      </CodeBlockTab>

      <CodeBlockTab value="yarn">
        ```bash
        yarn add dotenv
        ```
      </CodeBlockTab>

      <CodeBlockTab value="bun">
        ```bash
        bun add dotenv
        ```
      </CodeBlockTab>
    </CodeBlockTabs>
  </CalloutDescription>
</CalloutContainer>

2. Incorporate team changes [#2-incorporate-team-changes]

2.1. Pull latest changes [#21-pull-latest-changes]

To incorporate changes from collaborators:

1. Pull the changed Prisma schema and `./prisma/migrations` folder
2. Run the migrate command:

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
    npx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

2.2. Example scenario [#22-example-scenario]

Let's walk through a sample scenario with three developers sharing schema changes:

<CodeBlockTabs defaultValue="Before">
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="Before">
      Before
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="After">
      After
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="Before">
    ```prisma title="schema.prisma" 
    model Post {
      id        Int     @id @default(autoincrement())
      title     String
      content   String?
      published Boolean @default(false)
      author    User?   @relation(fields: [authorId], references: [id])
      authorId  Int?
    }

    model User {
      id    Int     @id @default(autoincrement())
      email String  @unique
      name  String?
      posts Post[]
    }
    ```
  </CodeBlockTab>

  <CodeBlockTab value="After">
    ```prisma title="schema.prisma" 
    model Post {
      id        Int     @id @default(autoincrement())
      title     String
      content   String?
      published Boolean @default(false)
      author    User?   @relation(fields: [authorId], references: [id])
      authorId  Int?
    }

    model User {
      id              Int     @id @default(autoincrement())
      email           String  @unique
      name            String?
      favoriteColor   String? // Added by Ania // [!code ++]
      bestPacmanScore Int? // Added by you // [!code ++]
      posts           Post[]
    }

    // Added by Javier // [!code ++]
    model Tag { // [!code ++]
      tagName     String   @id // [!code ++]
      tagCategory Category // [!code ++]
    } // [!code ++]
    ```
  </CodeBlockTab>
</CodeBlockTabs>

3. Handle concurrent changes [#3-handle-concurrent-changes]

3.1. Developer A's changes [#31-developer-as-changes]

Ania adds a new field:

```prisma
model User {
  /* ... */
  favoriteColor String?
}
```

And generates a migration:

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
    npx prisma migrate dev --name new-field
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev --name new-field
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev --name new-field
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev --name new-field
    ```
  </CodeBlockTab>
</CodeBlockTabs>

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

3.2. Developer B's changes [#32-developer-bs-changes]

Javier adds a new model:

```prisma
model Tag {
  tagName     String   @id
  tagCategory Category
}
```

And generates a migration:

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
    npx prisma migrate dev --name new-model
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev --name new-model
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev --name new-model
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev --name new-model
    ```
  </CodeBlockTab>
</CodeBlockTabs>

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

3.3. Merge changes [#33-merge-changes]

The migration history now has two new migrations:

<img alt="A diagram showing changes by two separate developers converging in a single migration history." src="/img/guides/migrate-team-dev.png" width="1600" height="1690" />

4. Integrate your changes [#4-integrate-your-changes]

4.1. Pull team changes [#41-pull-team-changes]

1. Pull the most recent changes:
   * Two new migrations
   * Updated schema file

2. Review the merged schema:

```prisma
model User {
  /* ... */
  favoriteColor   String?
  bestPacmanScore Int?
}

model Tag {
  tagName     String   @id
  tagCategory Category
  posts       Post[]
}
```

4.2. Generate your migration [#42-generate-your-migration]

Run the migrate command:

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
    npx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

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

This will:

1. Apply your team's migrations
2. Create a new migration for your changes
3. Apply your new migration

4.3. Commit changes [#43-commit-changes]

Commit:

* The merged `schema.prisma`
* Your new migration file

Next steps [#next-steps]

Now that you understand team schema management, you can:

* Learn about [customizing migrations](/v6/orm/prisma-migrate/workflows/customizing-migrations)
* Explore [deployment workflows](/v6/orm/prisma-migrate/workflows/development-and-production)

For more information:

* [Prisma Migrate documentation](/v6/orm/prisma-migrate/getting-started)
* [Team development workflows](/v6/orm/prisma-migrate/workflows/team-development)



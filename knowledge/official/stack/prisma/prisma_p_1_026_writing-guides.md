# Writing guides (/docs/guides/making-guides)



Introduction [#introduction]

This guide shows you how to write guides for Prisma ORM documentation. It covers the required structure, formatting, and style conventions to ensure consistency across all guides. You'll learn about frontmatter requirements, section organization, and writing style.

Prerequisites [#prerequisites]

Before writing a guide, make sure you have:

* A clear understanding of the topic you're writing about
* Access to the Prisma documentation repository
* Familiarity with Markdown and MDX
* Knowledge of the target audience for your guide

Guide structure [#guide-structure]

Required frontmatter [#required-frontmatter]

Every guide must include the following frontmatter at the top of the file:

```mdx
---
title: '[Descriptive title]'
description: '[One-sentence summary of what the guide covers]'
---
```

* `title`: A clear, descriptive title (e.g., "Next.js", "Multiple databases", "GitHub Actions")
* `description`: A one-sentence summary that describes what you'll learn or accomplish
* `image`: A unique header image for social media sharing (coordinate with the design team)

All frontmatter fields should use sentence case.

Required sections [#required-sections]

1. **Introduction** (H2: `##`)
   * Brief overview of what the guide covers
   * What the reader will learn/accomplish
   * Link to any example repositories or related resources on GitHub

2. **Prerequisites** (H2: `##`)
   * Required software/tools with version numbers (e.g., "Node.js 20+")
   * Required accounts (e.g., "A Prisma Data Platform account")
   * Keep it concise - only list what's truly necessary

3. **Main content sections** (H2: `##`)
   * Use numbered steps (e.g., "## 1. Set up your project", "## 2. Install and Configure Prisma")
   * Use numbered subsections (e.g., "### 2.1. Install dependencies", "### 2.2. Define your Prisma Schema")
   * Each step should build on previous steps
   * Include all commands and code snippets needed

4. **Next steps** (H2: `##`)
   * What to do after completing the guide
   * Related guides or documentation (with links)
   * Additional resources

Writing style and voice [#writing-style-and-voice]

General principles [#general-principles]

* Write in a clear, conversational tone
* Use active voice and present tense
* Address the reader directly using "you" (e.g., "You'll learn how to...")
* Avoid jargon and explain technical terms when necessary
* Be concise but thorough
* Guide readers step-by-step through the process

Code examples [#code-examples]

* Include complete, runnable code examples
* Use syntax highlighting with language specification
* Include file paths in code block metadata using `title=`
* Use ` ```bash title=".env" ` for `.env` files so inline `# [!code ++]`, `# [!code --]`, and `# [!code highlight]` annotations render correctly
* Reserve ` ```text ` for other plain-text files that do not need Fumadocs code annotations
* Use comments sparingly - only when needed to explain complex logic
* Use ` ```npm ` for package manager commands (auto-converts to pnpm/yarn/bun)
* Use ` ```bash ` for shell commands and `.env` files
* Use ` ```text ` for other plain text files
* Use ` ```typescript `, ` ```prisma `, ` ```json ` for respective languages

Example with file path:

```typescript title="src/lib/prisma.ts"
import { PrismaClient } from "../generated/prisma";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

const prisma = new PrismaClient({
  adapter,
});

export default prisma;
```

Example showing changes:

```typescript title="prisma.config.ts"
import "dotenv/config"; // [!code ++]
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

Formatting conventions [#formatting-conventions]

* Use backticks for inline code:
  * File names: `` `schema.prisma` ``
  * Directory names: `` `prisma/` ``
  * Code elements: `` `PrismaClient` ``
  * Package manager commands: Use ` ```npm ` blocks (see [Package manager commands](#package-manager-commands))
* Use admonitions for important information:
  ```markdown
  :::info
  Context or background information
  :::

  :::note
  Important details to remember
  :::

  :::warning
  Critical information or gotchas
  :::

  :::tip
  Helpful suggestions or best practices
  :::
  ```
* Use proper heading hierarchy (never skip levels)
* Use numbered sections (e.g., "## 1. Setup", "### 1.1. Install")
* Link to other documentation pages using relative paths (e.g., `[Database drivers](/orm/core-concepts/supported-databases/database-drivers)`)

Guide categories [#guide-categories]

| Category            | Directory                      | Description                         | Examples                                                                                                                                                                              |
| ------------------- | ------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Framework**       | `guides/frameworks/`           | Integrate Prisma with frameworks    | [Next.js](/guides/frameworks/nextjs), [NestJS](/guides/frameworks/nestjs), [SvelteKit](/guides/frameworks/sveltekit)                                                                  |
| **Deployment**      | `guides/deployment/`           | Deploy apps and set up monorepos    | [Turborepo](/guides/deployment/turborepo), [Cloudflare Workers](/guides/deployment/cloudflare-workers)                                                                                |
| **Integration**     | `guides/integrations/`         | Use Prisma with platforms and tools | [GitHub Actions](/guides/integrations/github-actions), [Supabase](/guides/integrations/supabase-accelerate)                                                                           |
| **Database**        | `guides/database/`             | Database patterns and migrations    | [Multiple databases](/guides/database/multiple-databases), [Data migration](/guides/database/data-migration)                                                                          |
| **Authentication**  | `guides/authentication/`       | Authentication patterns with Prisma | [Auth.js + Next.js](/guides/authentication/authjs/nextjs), [Better Auth + Next.js](/guides/authentication/better-auth/nextjs), [Clerk + Next.js](/guides/authentication/clerk/nextjs) |
| **Prisma Postgres** | `guides/postgres/`             | Prisma Postgres features            | [Vercel](/guides/postgres/vercel), [Netlify](/guides/postgres/netlify), [Viewing data](/guides/postgres/viewing-data)                                                                 |
| **Migration**       | `guides/switch-to-prisma-orm/` | Switch from other ORMs              | [From Mongoose](/guides/switch-to-prisma-orm/from-mongoose), [From Drizzle](/guides/switch-to-prisma-orm/from-drizzle)                                                                |

Common patterns [#common-patterns]

Package manager commands [#package-manager-commands]

Use ` ```npm ` code blocks for package manager commands. These automatically convert to other package managers (pnpm, yarn, bun) in the UI:

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
    npm install prisma --save-dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add prisma --save-dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add prisma --dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add prisma --dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Environment variables [#environment-variables]

Show `.env` file examples using ` ```bash title=".env" ` blocks:

```bash title=".env"
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
```

If you need to show changes in an `.env` file, use bash comments for the Fumadocs annotations:

```bash title=".env"
DATABASE_URL="postgresql://user:password@localhost:5432/mydb" # [!code --]

DATABASE_URL="postgresql://user:password@db.example.com:5432/mydb" # [!code ++]
```

Database provider compatibility [#database-provider-compatibility]

Include an info admonition when commands or code are PostgreSQL-specific:

```markdown
:::info

If you are using a different database provider (MySQL, SQL Server, SQLite), install the corresponding driver adapter package instead of `@prisma/adapter-pg`. For more information, see [Database drivers](/orm/core-concepts/supported-databases/database-drivers).

:::
```

Prisma Client instantiation [#prisma-client-instantiation]

Show the standard pattern for creating a Prisma Client with database adapters:

```typescript title="lib/prisma.ts"
import { PrismaClient } from "../generated/prisma";
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

const prisma = new PrismaClient({
  adapter,
});

export default prisma;
```

Include a warning about connection pooling:

```markdown
:::warning
We recommend using a connection pooler (like [Prisma Accelerate](https://www.prisma.io/accelerate)) to manage database connections efficiently.
:::
```

Best practices [#best-practices]

1. **Keep it focused**
   * Each guide should cover one main topic
   * Break complex topics into multiple guides
   * Link to related guides instead of duplicating content

2. **Show don't tell**
   * Include practical, real-world examples
   * Provide complete, working code samples
   * Explain why certain approaches are recommended

3. **Consider the context**
   * Explain prerequisites clearly
   * Don't assume prior knowledge
   * Link to foundational concepts within or outside of our docs when needed

4. **Maintain consistency**
   * Follow the established guide structure
   * Use consistent terminology
   * Match the style of existing guides

5. **Think about maintenance**
   * Use version numbers where appropriate
   * Avoid time-sensitive references
   * Consider future updates when structuring content

Guide template [#guide-template]

Use this template as a starting point for new guides. The template includes common sections and patterns used across Prisma guides.

Basic template structure [#basic-template-structure]

Copy this template for a new guide:

````markdown
---
title: '[Your guide title]'
description: '[One-sentence summary of what you'll learn]'
image: '/img/guides/[guide-name]-cover.png'
---

## Introduction

[Brief overview of what this guide covers and what you'll accomplish. Include a link to an example repository if available.]

## Prerequisites

- [Node.js 20+](https://nodejs.org)
- [Any other prerequisites]

## 1. Set up your project

[Instructions for creating or setting up the project]

```npm

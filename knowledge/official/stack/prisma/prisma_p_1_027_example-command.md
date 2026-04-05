# Example command
npx create-next-app@latest my-app
cd my-app
```

## 2. Install and Configure Prisma

### 2.1. Install dependencies

To get started with Prisma, you'll need to install a few dependencies:

```npm
npm install prisma tsx @types/pg --save-dev
```

```npm
npm install @prisma/client @prisma/adapter-pg dotenv pg
```

:::info

If you are using a different database provider (MySQL, SQL Server, SQLite), install the corresponding driver adapter package instead of `@prisma/adapter-pg`. For more information, see [Database drivers](/orm/core-concepts/supported-databases/database-drivers).

:::

Once installed, initialize Prisma in your project:

```npm
npx prisma init --output ../generated/prisma
```

:::info

`prisma init` creates the Prisma scaffolding and a local `DATABASE_URL`. In the next step, you will create a Prisma Postgres database and replace that value with a direct `postgres://...` connection string.

:::

This will create:

- A `prisma` directory with a `schema.prisma` file
- A Prisma Postgres database
- A `.env` file containing the `DATABASE_URL`
- A `prisma.config.ts` file for configuration

Create a Prisma Postgres database and replace the generated `DATABASE_URL` in your `.env` file with the `postgres://...` connection string from the CLI output:

```npm
npx create-db
```

### 2.2. Define your Prisma Schema

In the `prisma/schema.prisma` file, add your models:

```prisma title="prisma/schema.prisma"
generator client {
  provider = "prisma-client"
  output   = "../generated/prisma"
}

datasource db {
  provider = "postgresql"
}

model User { // [!code ++]
  id    Int     @id @default(autoincrement()) // [!code ++]
  email String  @unique // [!code ++]
  name  String? // [!code ++]
  posts Post[] // [!code ++]
} // [!code ++]

model Post { // [!code ++]
  id        Int     @id @default(autoincrement()) // [!code ++]
  title     String // [!code ++]
  content   String? // [!code ++]
  published Boolean @default(false) // [!code ++]
  authorId  Int // [!code ++]
  author    User    @relation(fields: [authorId], references: [id]) // [!code ++]
} // [!code ++]
```

### 2.3. Run migrations and generate Prisma Client

Create the database tables:

```npm
npx prisma migrate dev --name init
```

Then generate Prisma Client:

```npm
npx prisma generate
```

## 3. [Integration-specific steps]

[Add framework or platform-specific integration steps here]

## Next steps

Now that you've completed this guide, you can:

- [Suggestion 1]
- [Suggestion 2]
- [Related guide 1](/path/to/guide)
- [Related guide 2](/path/to/guide)

For more information:

- [Prisma documentation](/orm)
- [Related documentation]
````

Adding guides to navigation [#adding-guides-to-navigation]

Guides are organized by category in subdirectories. To add a guide to the navigation, you need to update the appropriate `meta.json` file.

Main categories [#main-categories]

The main guide categories are listed in `meta.json`:

```json title="apps/docs/content/docs/guides/meta.json"
{
  "title": "Guides",
  "root": true,
  "icon": "NotebookTabs",
  "pages": [
    "index",
    "frameworks",
    "deployment",
    "authentication",
    "integrations",
    "postgres",
    "database",
    "switch-to-prisma-orm",
    "upgrade-prisma-orm"
  ]
}
```

Adding a guide to a category [#adding-a-guide-to-a-category]

To add a guide to a category (e.g., `frameworks`), edit the category's `meta.json` file:

```json title="apps/docs/content/docs/guides/frameworks/meta.json"
{
  "title": "Frameworks",
  "defaultOpen": true,
  "pages": [
    "nextjs",
    "astro",
    "nuxt",
    "your-new-guide" // [!code ++]
  ]
}
```

The page name should match your `.mdx` filename without the extension. For example, if your file is `your-new-guide.mdx`, add `"your-new-guide"` to the `pages` array.

Next steps [#next-steps]

After reading this guide, you can:

* Start writing your own guide using the provided template
* Review existing guides in the category you're contributing to
* Coordinate with the design team for a unique header image
* Submit your guide for review



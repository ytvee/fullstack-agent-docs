# PlanetScale (/docs/prisma-orm/quickstart/planetscale)



[PlanetScale](https://planetscale.com) is a serverless database platform. This guide covers both **PlanetScale MySQL** and **PlanetScale Postgres**. In this guide, you will learn how to set up a new TypeScript project from scratch, connect it to PlanetScale using Prisma ORM, and generate a Prisma Client for easy, type-safe access to your database.

Prerequisites [#prerequisites]

You also need:

* A [PlanetScale](https://planetscale.com) account
* A PlanetScale database (MySQL or Postgres)
* Database connection credentials from PlanetScale

1. Create a new project [#1-create-a-new-project]

```shell
mkdir hello-prisma
cd hello-prisma
```

Initialize a TypeScript project:

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
    npm init
    npm install typescript tsx @types/node --save-dev
    npx tsc --init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm init
    pnpm add typescript tsx @types/node --save-dev
    pnpm dlx tsc --init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn init
    yarn add typescript tsx @types/node --dev
    yarn dlx tsc --init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun init
    bun add typescript tsx @types/node --dev
    bun x tsc --init
    ```
  </CodeBlockTab>
</CodeBlockTabs>

2. Install required dependencies [#2-install-required-dependencies]

Install the packages needed for this quickstart:

MySQL [#mysql]

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
    npm install @prisma/client @prisma/adapter-planetscale undici dotenv
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add prisma --save-dev
    pnpm add @prisma/client @prisma/adapter-planetscale undici dotenv
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add prisma --dev
    yarn add @prisma/client @prisma/adapter-planetscale undici dotenv
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add prisma --dev
    bun add @prisma/client @prisma/adapter-planetscale undici dotenv
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Postgres [#postgres]

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
    npm install prisma @types/pg --save-dev
    npm install @prisma/client @prisma/adapter-pg pg dotenv
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add prisma @types/pg --save-dev
    pnpm add @prisma/client @prisma/adapter-pg pg dotenv
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add prisma @types/pg --dev
    yarn add @prisma/client @prisma/adapter-pg pg dotenv
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add prisma @types/pg --dev
    bun add @prisma/client @prisma/adapter-pg pg dotenv
    ```
  </CodeBlockTab>
</CodeBlockTabs>

3. Configure ESM support [#3-configure-esm-support]

Update `tsconfig.json` for ESM compatibility:

```json title="tsconfig.json"
{
  "compilerOptions": {
    "module": "ESNext",
    "moduleResolution": "bundler",
    "target": "ES2023",
    "strict": true,
    "esModuleInterop": true,
    "ignoreDeprecations": "6.0"
  }
}
```

Update `package.json` to enable ESM:

```json title="package.json"
{
  "type": "module" // [!code ++]
}
```

4. Initialize Prisma ORM [#4-initialize-prisma-orm]

You can now invoke the Prisma CLI by prefixing it with `npx`:

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
    npx prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Next, set up your Prisma ORM project by creating your [Prisma Schema](/orm/prisma-schema/overview) file with the following command:

MySQL [#mysql-1]

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
    npx prisma init --datasource-provider mysql --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma init --datasource-provider mysql --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma init --datasource-provider mysql --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma init --datasource-provider mysql --output ../generated/prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Postgres [#postgres-1]

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
    npx prisma init --datasource-provider postgresql --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma init --datasource-provider postgresql --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma init --datasource-provider postgresql --output ../generated/prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma init --datasource-provider postgresql --output ../generated/prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This command does a few things:

* Creates a `prisma/` directory with a `schema.prisma` file containing your database connection and schema models
* Creates a `.env` file in the root directory for environment variables
* Creates a `prisma.config.ts` file for Prisma configuration

The generated `prisma.config.ts` file looks like this:

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

The generated schema uses [the ESM-first `prisma-client` generator](/orm/prisma-schema/overview/generators#prisma-client) with a custom output path:

<CodeBlockTabs defaultValue="MySQL">
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="MySQL">
      MySQL
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="Postgres">
      Postgres
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="MySQL">
    ```prisma title="prisma/schema.prisma" 
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider     = "mysql"
      relationMode = "prisma"
    }
    ```
  </CodeBlockTab>

  <CodeBlockTab value="Postgres">
    ```prisma title="prisma/schema.prisma" 
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider = "postgresql"
    }
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CalloutContainer type="info">
  <CalloutDescription>
    **PlanetScale MySQL** requires `relationMode = "prisma"` because it doesn't support foreign key constraints.
  </CalloutDescription>
</CalloutContainer>

5. Configure your connection [#5-configure-your-connection]

Update your `.env` file with your PlanetScale connection string:

<CodeBlockTabs defaultValue="MySQL">
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="MySQL">
      MySQL
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="Postgres">
      Postgres
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="MySQL">
    ```text title=".env" 
    DATABASE_URL="mysql://username:password@host.connect.psdb.cloud/mydb?sslaccept=strict"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="Postgres">
    ```text title=".env" 
    DATABASE_URL="postgresql://{username}:{password}@{host}:6432/postgres?sslmode=verify-full"
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Replace with your actual PlanetScale credentials from your database dashboard.

<CalloutContainer type="info">
  <CalloutDescription>
    **PlanetScale Postgres connection types:**

    | Type          | Port   | Use case                                                       |
    | ------------- | ------ | -------------------------------------------------------------- |
    | **Direct**    | `5432` | Prisma CLI commands (migrations, introspection), Prisma Studio |
    | **PgBouncer** | `6432` | Application connections, serverless environments               |

    For production applications, we recommend using PgBouncer (port 6432) for application connections while keeping a direct connection for Prisma CLI commands.
  </CalloutDescription>
</CalloutContainer>

6. Define your data model [#6-define-your-data-model]

Open `prisma/schema.prisma` and add the following models:

<CodeBlockTabs defaultValue="MySQL">
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="MySQL">
      MySQL
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="Postgres">
      Postgres
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="MySQL">
    ```prisma title="prisma/schema.prisma" 
    generator client {
      provider = "prisma-client"
      output   = "../generated/prisma"
    }

    datasource db {
      provider     = "mysql"
      relationMode = "prisma"
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
      content   String? @db.Text // [!code ++]
      published Boolean @default(false) // [!code ++]
      author    User    @relation(fields: [authorId], references: [id]) // [!code ++]
      authorId  Int // [!code ++]

      @@index([authorId]) // [!code ++]
    } // [!code ++]
    ```
  </CodeBlockTab>

  <CodeBlockTab value="Postgres">
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
      author    User    @relation(fields: [authorId], references: [id]) // [!code ++]
      authorId  Int // [!code ++]
    } // [!code ++]
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<CalloutContainer type="info">
  <CalloutDescription>
    Note the `@@index([authorId])` on the `Post` model for MySQL. PlanetScale MySQL requires indexes on foreign keys when using `relationMode = "prisma"`.
  </CalloutDescription>
</CalloutContainer>

7. Apply your schema to the database [#7-apply-your-schema-to-the-database]

MySQL [#mysql-2]

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
    npx prisma db push
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma db push
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma db push
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma db push
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Postgres [#postgres-2]

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
    npx prisma migrate dev --name init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma migrate dev --name init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma migrate dev --name init
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma migrate dev --name init
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This command creates the database tables based on your schema.

Now run the following command to generate the Prisma Client:

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

<CalloutContainer type="info">
  <CalloutDescription>
    **PlanetScale MySQL** uses a branching workflow instead of traditional migrations, so we use `prisma db push`. **PlanetScale Postgres** supports standard migrations with `prisma migrate dev`.
  </CalloutDescription>
</CalloutContainer>

8. Instantiate Prisma Client [#8-instantiate-prisma-client]

Now that you have all the dependencies installed, you can instantiate Prisma Client. You need to pass an instance of the Prisma ORM driver adapter adapter to the `PrismaClient` constructor:

<CodeBlockTabs defaultValue="MySQL">
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="MySQL">
      MySQL
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="Postgres">
      Postgres
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="MySQL">
    ```typescript title="lib/prisma.ts" 
    import "dotenv/config";
    import { PrismaPlanetScale } from "@prisma/adapter-planetscale";
    import { PrismaClient } from "../generated/prisma/client";
    import { fetch as undiciFetch } from "undici";

    const adapter = new PrismaPlanetScale({ url: process.env.DATABASE_URL, fetch: undiciFetch });
    const prisma = new PrismaClient({ adapter });

    export { prisma };
    ```
  </CodeBlockTab>

  <CodeBlockTab value="Postgres">
    ```typescript title="lib/prisma.ts" 
    import "dotenv/config";
    import { PrismaPg } from "@prisma/adapter-pg";
    import { PrismaClient } from '../generated/prisma/client'

    const connectionString = `${process.env.DATABASE_URL}`;

    const adapter = new PrismaPg({ connectionString });
    const prisma = new PrismaClient({ adapter });

    export { prisma };
    ```
  </CodeBlockTab>
</CodeBlockTabs>

9. Write your first query [#9-write-your-first-query]

Create a `script.ts` file to test your setup:

```typescript title="script.ts"
import { prisma } from "./lib/prisma";

async function main() {
  // Create a new user with a post
  const user = await prisma.user.create({
    data: {
      name: "Alice",
      email: "alice@prisma.io",
      posts: {
        create: {
          title: "Hello World",
          content: "This is my first post!",
          published: true,
        },
      },
    },
    include: {
      posts: true,
    },
  });
  console.log("Created user:", user);

  // Fetch all users with their posts
  const allUsers = await prisma.user.findMany({
    include: {
      posts: true,
    },
  });
  console.log("All users:", JSON.stringify(allUsers, null, 2));
}

main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
```

Run the script:

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
    npx tsx script.ts
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx tsx script.ts
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx tsx script.ts
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun tsx script.ts
    ```
  </CodeBlockTab>
</CodeBlockTabs>

You should see the created user and all users printed to the console!

10. Explore your data with Prisma Studio [#10-explore-your-data-with-prisma-studio]

Prisma Studio is a visual editor for your database. Launch it with:

```shell
npx prisma studio
```

Next steps [#next-steps]

You've successfully set up Prisma ORM. Here's what you can explore next:

* **Learn more about Prisma Client**: Explore the [Prisma Client API](/orm/prisma-client/setup-and-configuration/introduction) for advanced querying, filtering, and relations
* **Database migrations**: Learn about [Prisma Migrate](/orm/prisma-migrate) for evolving your database schema
* **Performance optimization**: Discover [query optimization techniques](/orm/prisma-client/queries/advanced/query-optimization-performance)
* **Build a full application**: Check out our [framework guides](/guides) to integrate Prisma ORM with Next.js, Express, and more
* **Join the community**: Connect with other developers on [Discord](https://pris.ly/discord)

More info [#more-info]

* [Prisma Config reference](/orm/reference/prisma-config-reference)
* [Database connection management](/orm/prisma-client/setup-and-configuration/databases-connections)
* [PlanetScale documentation](https://planetscale.com/docs)



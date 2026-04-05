# Prisma v7
npm install prisma tsx --save-dev
npm install @prisma/client dotenv
```

If using Prisma Postgres:

```npm
npm install @prisma/adapter-pg
```

---

## Initialize Prisma inside `packages/db`

```bash
cd packages/db
npx prisma init
```

This creates:

```
packages/db/
  prisma/
    schema.prisma
  prisma.config.ts
```

---

## Prisma v7 config (`packages/db/prisma.config.ts`)

**CRITICAL:** load env vars at the top.

```ts
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

---

## Prisma schema (`packages/db/prisma/schema.prisma`)

```prisma
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}

datasource db {
  provider = "postgresql"
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

---

## Shared Prisma client singleton (`packages/db/src/client.ts`)

```ts
import { PrismaClient } from "../generated/prisma/client";

//Prisma Driver Adapter for Postgres
import { PrismaPg } from "@prisma/adapter-pg";

// Create a new Driver Adapter instance for PrismaPostgres
const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

const globalForPrisma = globalThis as unknown as {
  prisma?: PrismaClient;
};

export const prisma = globalForPrisma.prisma ?? new PrismaClient({ adapter });

if (process.env.NODE_ENV !== "production") {
  globalForPrisma.prisma = prisma;
}

export default prisma;
```

---

## Export DB package API (`packages/db/src/index.ts`)

```ts
export { prisma } from "./client";
export * from "../generated/prisma";
```

And in `packages/db/package.json`:

```json
{
  "name": "@repo/db",
  "private": true,
  "main": "src/index.ts",
  "types": "src/index.ts",
  "scripts": {
    "db:generate": "prisma generate",
    "db:push": "prisma db push",
    "db:migrate": "prisma migrate dev",
    "db:studio": "prisma studio",
    "db:test": "tsx scripts/test-database.ts"
  }
}
```

---

## Root Turbo pipeline (`turbo.json`)

```json
{
  "globalEnv": ["DATABASE_URL"],
  "tasks": {
    "dev": {
      "cache": false,
      "persistent": true,
      "dependsOn": ["^db:generate"]
    },
    "build": {
      "dependsOn": ["^db:generate"],
      "outputs": [".next/**", "dist/**"]
    },
    "db:generate": {
      "cache": false
    },
    "db:migrate": {
      "cache": false
    },
    "db:studio": {
      "cache": false
    },
    "db:test": {
      "cache": false,
      "dependsOn": ["db:generate"]
    }
  }
}
```

---

## Root scripts (`package.json`)

```json
{
  "scripts": {
    "dev": "turbo dev",
    "build": "turbo build",
    "lint": "turbo lint",
    "db:generate": "turbo run db:generate",
    "db:push": "turbo run db:push",
    "db:migrate": "turbo run db:migrate",
    "db:studio": "turbo run db:studio",
    "db:test": "turbo run db:test"
  }
}
```

---

## Shared test script (`packages/db/scripts/test-database.ts`)

```ts
import "dotenv/config";
import prisma from "../src/client";

async function testDatabase() {
  console.log("🔍 Testing Prisma Postgres connection...\n");

  try {
    console.log("✅ Connected to database!");

    console.log("\n📝 Creating a test user...");
    const newUser = await prisma.user.create({
      data: {
        email: "demo@example.com",
        name: "Demo User",
      },
    });
    console.log("✅ Created user:", newUser);

    console.log("\n📋 Fetching all users...");
    const allUsers = await prisma.user.findMany();
    console.log(`✅ Found ${allUsers.length} user(s):`);
    allUsers.forEach((user) => {
      console.log(`   - ${user.name} (${user.email})`);
    });

    console.log("\n🎉 All tests passed! Your database is working.\n");
  } catch (error) {
    console.error("❌ Error:", error);
    process.exit(1);
  } finally {
    await prisma.$disconnect();
  }
}

testDatabase();
```

---

## Using Prisma in apps (example: `apps/web` Next.js)

In any app, add a dependency on `@repo/db` (workspace):

```json
{
  "dependencies": {
    "@repo/db": "*"
  }
}
```

Then in server-side code:

```ts
import { prisma } from "@repo/db";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const users = await prisma.user.findMany();
    return NextResponse.json(users);
  } catch (e) {
    console.error(e);
    return NextResponse.json({ error: "Failed to fetch users" }, { status: 500 });
  }
}
```

---

## Complete setup workflow

1. **Create Turborepo** (or use existing):

   ```npm
   npx create-turbo@latest
   ```

2. **Add `packages/db`**, install Prisma v7 deps.

3. **Initialize Prisma in `packages/db`**:

   ```bash
   cd packages/db
   npx prisma init
   ```

4. **Update `prisma.config.ts`** to include `import "dotenv/config"`.

5. **Update schema** with Prisma v7 generator + output.

6. **Create `src/client.ts`** singleton and export via `src/index.ts`.

7. **Wire Turbo tasks** in `turbo.json`.

8. **Add `.env`** at root **and/or** `packages/db/.env`.

9. **Push schema**:

   ```bash
   npm run db:push
   ```

10. **Test**:

    ```bash
    npm run db:test
    ```

11. **Start dev**:
    ```bash
    npm run dev
    ```

---

## AI Model verification checklist

Before generating any code, verify:

1. `provider = "prisma-client"`?
2. `output   = "../src/generated/prisma"` present?
3. All Prisma files in `packages/db`?
4. Client imports from `../generated/prisma/client` (or via `@repo/db`)?
5. `import "dotenv/config"` in `packages/db/prisma.config.ts`?
6. Turbo tasks depend on `db:generate`?
7. `DATABASE_URL` listed in `globalEnv`?
8. All DB ops wrapped in try/catch?
9. Test script exists in `packages/db/scripts/test-database.ts`?

No exceptions. If any check fails, STOP and FIX.

---

## AI MODEL RESPONSE TEMPLATE (UPDATED FOR TURBOREPO + PRISMA v7)

When asked about implementing Prisma v7 inside a Turborepo monorepo (with any framework such as Next.js, Node, etc.), you MUST:

1. **Assume Prisma lives in a shared package**
   - Always place schema, config, and migrations in `packages/db`.
   - Never suggest adding Prisma directly into an app unless the user explicitly says they don’t want a shared package.

2. **Use only Prisma v7 generator patterns**
   - The schema MUST include:
     ```prisma
     generator client {
       provider = "prisma-client"
       output   = "./generated/prisma"
     }
     ```
   - Never use `prisma-client-js`.

3. **Use correct import paths for custom output**
   - Any PrismaClient import MUST come from the generated output:
     ```ts
     import { PrismaClient } from "./generated/prisma/client";
     ```
   - If importing from apps, you MUST import via the package boundary:
     ```ts
     import { prisma } from "@repo/db";
     ```
   - Never import from `@prisma/client` in this setup.

4. **Always include a shared singleton client in `packages/db`**
   - Provide a `packages/db/src/client.ts` with global caching for dev hot-reload.
   - If Accelerate is requested or implied, use `$extends(withAccelerate())`.
   - If Accelerate is not requested, omit it.

5. **Always load environment variables properly**
   - `packages/db/prisma.config.ts` MUST start with `import "dotenv/config"`.
   - Use `process.env.DATABASE_URL` in runtime code.
   - Remind users that `.env` should exist at root and/or `packages/db`.

6. **Always wire Turbo dependencies**
   - Turbo tasks `dev` and `build` MUST depend on `^db:generate`.
   - `DATABASE_URL` MUST be listed in `globalEnv` to ensure correct task hashing.

7. **Provide correct repo-level scripts**
   - Root scripts should proxy to Turbo (`turbo run db:*`).
   - The Prisma package `packages/db` should own `db:generate`, `db:migrate`, `db:studio`, and `db:test`.

8. **Include a real verification step**
   - Provide (or reference) `packages/db/scripts/test-database.ts`.
   - Ensure it imports dotenv and disconnects Prisma on completion.

9. **Use safe runtime patterns**
   - All DB calls in apps MUST be wrapped in try/catch.
   - In Next.js App Router examples, use server-only imports and return `NextResponse`.

10. **Self-verify before replying**

- Re-check all items in the “AI Model verification checklist.”
- If any item is missing or incorrect, STOP and FIX before responding.

Remember: There are NO exceptions to these rules. Every requirement is mandatory for a correct Turborepo + Prisma v7 setup.
````

Running the application [#running-the-application]

Get your application running locally in three quick steps:

**1. Generate the Prisma Client:**

```bash
npx turbo db:generate
```

**2. View your database in Prisma Studio:**

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
    npx turbo db:studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx turbo db:studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx turbo db:studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun turbo db:studio
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Prisma Studio opens at `localhost:5555` where you can inspect your `User` table and see the test user stored in your database.



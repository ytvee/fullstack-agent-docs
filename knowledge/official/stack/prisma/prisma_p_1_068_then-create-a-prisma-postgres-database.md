# Then create a Prisma Postgres database
npx create-db
```

This step:

- Generates `prisma/schema.prisma` with the correct output path
- Generates `prisma.config.ts`
- Generates `.env` with a local `DATABASE_URL`
- Requires `npx create-db` if you want a real Prisma Postgres database

**IMPORTANT**: After `npx create-db`, replace the generated `DATABASE_URL` in `.env` with the returned `postgres://...` connection string.

```text
DATABASE_URL="postgres://..."
```

## CORRECT PRISMA CONFIG (prisma.config.ts)

When using `npx prisma init`, the `prisma.config.ts` is **auto-generated** with the correct configuration:

```typescript
import "dotenv/config"; // ✅ Auto-included by prisma init
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
    seed: "tsx ./prisma/seed.ts",
  },
  // ✅ NO engine property - removed in Prisma v7
  datasource: {
    url: env("DATABASE_URL"),
  },
});
```

**Note**: If you need to manually create this file, ensure `import "dotenv/config"` is at the top.

## CORRECT SCHEMA CONFIGURATION (prisma/schema.prisma)

Update the generated `prisma/schema.prisma` file:

```prisma
generator client {
  provider = "prisma-client"
  output   = "./generated"
}

datasource db {
  provider = "postgresql"
  // ✅ NO url here - now configured in prisma.config.ts
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User?    @relation(fields: [authorId], references: [id])
  authorId  Int?
}
```

## CORRECT GLOBAL PRISMA CLIENT

Create `server/utils/db.ts` file. Nuxt auto-imports exports from `server/utils/`, making `prisma` available in all server API routes without explicit imports:

```typescript
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../../prisma/generated/client"; // ✅ CRITICAL: Include /client

const prismaClientSingleton = () => {
  const pool = new PrismaPg({ connectionString: process.env.DATABASE_URL! });
  return new PrismaClient({ adapter: pool });
};

type PrismaClientSingleton = ReturnType<typeof prismaClientSingleton>;

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClientSingleton | undefined;
};

export const prisma = globalForPrisma.prisma ?? prismaClientSingleton();

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
```

## ADD NPM SCRIPTS TO PACKAGE.JSON

Update your `package.json` to include these scripts:

```json
{
  "scripts": {
    "build": "nuxt build",
    "dev": "nuxt dev",
    "generate": "nuxt generate",
    "preview": "nuxt preview",
    "postinstall": "prisma generate && nuxt prepare",
    "db:test": "tsx scripts/test-database.ts",
    "db:studio": "prisma studio"
  }
}
```

## CREATE TEST SCRIPT

Create `scripts/test-database.ts` to verify your setup:

```typescript
import "dotenv/config"; // ✅ CRITICAL: Load environment variables
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../prisma/generated/client";

const pool = new PrismaPg({ connectionString: process.env.DATABASE_URL! });
const prisma = new PrismaClient({ adapter: pool });

async function testDatabase() {
  console.log("🔍 Testing Prisma Postgres connection...\n");

  try {
    // Test 1: Check connection
    console.log("✅ Connected to database!");

    // Test 2: Create a test user
    console.log("\n📝 Creating a test user...");
    const newUser = await prisma.user.create({
      data: {
        email: "demo@example.com",
        name: "Demo User",
      },
    });
    console.log("✅ Created user:", newUser);

    // Test 3: Fetch all users
    console.log("\n📋 Fetching all users...");
    const allUsers = await prisma.user.findMany();
    console.log(`✅ Found ${allUsers.length} user(s):`);
    allUsers.forEach((user) => {
      console.log(`   - ${user.name} (${user.email})`);
    });

    console.log("\n🎉 All tests passed! Your database is working perfectly.\n");
  } catch (error) {
    console.error("❌ Error:", error);
    process.exit(1);
  }
}

testDatabase();
```

## CORRECT API ROUTE IMPLEMENTATION

Nuxt uses file-based API routing in `server/api/`. The `prisma` instance is auto-imported from `server/utils/db.ts`.

Create `server/api/users.get.ts` to fetch users:

```typescript
export default defineEventHandler(async () => {
  try {
    const users = await prisma.user.findMany({
      include: { posts: true },
    });
    return users;
  } catch (error) {
    console.error("Error fetching users:", error);
    throw createError({
      statusCode: 500,
      statusMessage: "Failed to fetch users",
    });
  }
});
```

Create `server/api/users.post.ts` to create a user:

```typescript
export default defineEventHandler(async (event) => {
  try {
    const body = await readBody<{ name: string; email: string }>(event);

    if (!body.email) {
      throw createError({
        statusCode: 400,
        statusMessage: "Email is required",
      });
    }

    const user = await prisma.user.create({
      data: {
        name: body.name,
        email: body.email,
      },
    });

    return user;
  } catch (error) {
    console.error("Error creating user:", error);
    throw createError({
      statusCode: 500,
      statusMessage: "Failed to create user",
    });
  }
});
```

## CORRECT USAGE IN VUE PAGES

Update `app.vue` to display users from the database:

```html
<template>
  <div>
    <h1>Users</h1>
    <ul v-if="users?.length">
      <li v-for="user in users" :key="user.id">
        {{ user.name }} ({{ user.email }})
      </li>
    </ul>
    <p v-else>No users yet.</p>
  </div>
</template>

<script setup>
const { data: users } = await useFetch("/api/users");
</script>
```

## COMPLETE SETUP WORKFLOW

User should follow these steps (AI should provide these instructions):

1. **Ensure a Nuxt project exists** — check for `nuxt.config.ts`. If missing, create one:

   ```bash
   npx nuxi@latest init hello-prisma
   cd hello-prisma
   ```

2. **Install dependencies**:

   ```bash
   npm install @prisma/client @prisma/adapter-pg pg dotenv
   ```

   ```bash
   npm install -D prisma @types/pg tsx
   ```

3. **Initialize Prisma AND create Prisma Postgres database** (⚠️ USER MUST RUN MANUALLY):

   > **AI ASSISTANT**: You can run `npx prisma init` yourself. If you should not provision cloud resources automatically, ask the user to run `npx create-db` and update `DATABASE_URL` before continuing.

   ```bash
   npx prisma init --output ./generated
   npx create-db
   ```

   This creates `prisma/schema.prisma`, `prisma.config.ts`, and `.env`, then returns a `postgres://...` connection string for Prisma Postgres.

   **If you asked the user to run `npx create-db`, wait for them to share or paste the returned connection string before proceeding.**

4. **Verify `.env` was created** — Replace the generated `DATABASE_URL` with the `postgres://...` connection string returned by `npx create-db`.

   ```text
   DATABASE_URL="postgres://..."
   ```

   **Do NOT invent this URL. Use the one returned by `npx create-db`.**

5. **Update `prisma/schema.prisma`** — Add the User and Post models (generator and datasource are already configured):

   ```prisma
   model User {
     id    Int     @id @default(autoincrement())
     email String  @unique
     name  String?
     posts Post[]
   }

   model Post {
     id        Int      @id @default(autoincrement())
     title     String
     content   String?
     published Boolean  @default(false)
     author    User?    @relation(fields: [authorId], references: [id])
     authorId  Int?
   }
   ```

6. **Create `server/utils/db.ts`** with correct import path including `/client` and using `@prisma/adapter-pg`.

7. **Add npm scripts** to `package.json` for `db:test`, `db:studio`, and `postinstall`

8. **Create `scripts/test-database.ts`** test script

9. **Create API routes** — `server/api/users.get.ts` and `server/api/users.post.ts`

10. **Update `app.vue`** to display users

11. **Push schema to database**:

    ```bash
    npx prisma db push
    ```

12. **Generate Prisma Client**:

    ```bash
    npx prisma generate
    ```

13. **Test the setup**:

    ```bash
    npm run db:test
    ```

14. **Start development server**:

    ```bash
    npm run dev
    ```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Does the current directory contain `nuxt.config.ts`? If not, create the project first.
2. Are you using `provider = "prisma-client"` (not "prisma-client-js")? If not, STOP and FIX.
3. Are you using `output = "./generated"`? If not, STOP and FIX.
4. Are you importing from `'../../prisma/generated/client'` (with `/client`)? If not, STOP and FIX.
5. Did you add `import "dotenv/config"` to `prisma.config.ts`? If not, STOP and FIX.
6. Did you add `import "dotenv/config"` to `scripts/test-database.ts`? If not, STOP and FIX.
7. Are you using `@prisma/adapter-pg` with `PrismaPg`? If not, STOP and FIX.
8. Are you using `adapter` property in PrismaClient constructor? If not, STOP and FIX.
9. Are you wrapping database operations in try-catch? If not, STOP and FIX.
10. Did you create the Prisma client in `server/utils/db.ts` (not `lib/prisma.ts`)? If not, STOP and FIX.
11. Did you create the test script at `scripts/test-database.ts`? If not, STOP and FIX.
12. Did you add `db:test` and `db:studio` scripts to package.json? If not, STOP and FIX.
13. Did you remove `url` from the datasource block in `schema.prisma`? If not, STOP and FIX.
14. Did you remove `engine` property from `prisma.config.ts`? If not, STOP and FIX.
15. Did you run `npx prisma init` with the documented output path? If not, STOP and FIX.
16. Is the DATABASE_URL a TCP URL (`postgres://...`)? If it's a `prisma+postgres://` URL, STOP and FIX.
17. Did Prisma generate the `.env` file? If you invented the URL manually, STOP and FIX.
18. Are you using Nuxt auto-imports (`defineEventHandler`, `readBody`, `createError`, `prisma`)? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code using:

- `prisma-client-js` provider → **CLIENT GENERATION FAILS**
- Wrong import path (missing `/client`) → **MODULE NOT FOUND ERROR**
- Missing `import "dotenv/config"` in prisma.config.ts → **DATABASE_URL NOT FOUND ERROR**
- Missing `import "dotenv/config"` in test scripts → **ENVIRONMENT VARIABLE ERROR**
- Default import from `@prisma/client` → **IMPORT ERROR**
- Using `accelerateUrl` or `withAccelerate` → **UNNECESSARY ACCELERATE DEPENDENCY / CONFIG ERROR**
- Missing custom output path → **WRONG CLIENT GENERATED**
- Including `url` in datasource block → **DEPRECATED CONFIGURATION ERROR**
- Including `engine` property → **DEPRECATED CONFIGURATION ERROR**
- Using local URL (`postgres://localhost:...`) → **VERSION INCOMPATIBILITY ERRORS WITH Prisma v7**
- Using `npx prisma init` without `--db` → **NO DATABASE CREATED, ONLY LOCAL FILES**
- Manually inventing DATABASE_URL → **INVALID CONNECTION STRING ERRORS**
- Creating client in `lib/prisma.ts` instead of `server/utils/db.ts` → **NOT AUTO-IMPORTED IN NUXT SERVER ROUTES**
- Missing `pg` dependency → **ADAPTER INITIALIZATION FAILURE**

The implementation will:

1. Break immediately with module errors
2. Fail to read environment variables
3. Cause connection pool exhaustion in production
4. Result in import errors that prevent compilation
5. Cause performance issues and connection failures
6. Fail with "HTTP connection string is not supported" errors when using local URLs

## USEFUL COMMANDS

```bash

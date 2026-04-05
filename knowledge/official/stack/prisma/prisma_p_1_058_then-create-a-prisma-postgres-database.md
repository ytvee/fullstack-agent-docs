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
  output   = "../app/generated/prisma"
}

datasource db {
  provider = "postgresql"
  // ✅ NO url here - now configured in prisma.config.ts
}

// Example User model for testing
model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

## CORRECT GLOBAL PRISMA CLIENT

Create `lib/prisma.ts` file:

```typescript
import { PrismaClient } from "../app/generated/prisma/client"; // ✅ CRITICAL: Include /client
import { PrismaPg } from "@prisma/adapter-pg";

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
});

const globalForPrisma = global as unknown as { prisma: PrismaClient };

const prisma =
  globalForPrisma.prisma ||
  new PrismaClient({
    adapter,
  });

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;

export default prisma;
```

## ADD NPM SCRIPTS TO PACKAGE.JSON

Update your `package.json` to include these scripts:

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "db:test": "tsx scripts/test-database.ts",
    "db:studio": "prisma studio"
  }
}
```

## CREATE TEST SCRIPT

Create `scripts/test-database.ts` to verify your setup:

```typescript
import "dotenv/config"; // ✅ CRITICAL: Load environment variables
import prisma from "../lib/prisma";

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

## CORRECT API ROUTE IMPLEMENTATION (App Router)

Create `app/api/users/route.ts` with GET and POST handlers:

```typescript
import { NextRequest, NextResponse } from "next/server";
import prisma from "../../../lib/prisma";

export async function GET(request: NextRequest) {
  try {
    const users = await prisma.user.findMany();
    return NextResponse.json(users);
  } catch (error) {
    console.error("Error fetching users:", error);
    return NextResponse.json({ error: "Failed to fetch users" }, { status: 500 });
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const user = await prisma.user.create({
      data: {
        email: body.email,
        name: body.name,
      },
    });
    return NextResponse.json(user, { status: 201 });
  } catch (error) {
    console.error("Error creating user:", error);
    return NextResponse.json({ error: "Failed to create user" }, { status: 500 });
  }
}
```

## CORRECT USAGE IN SERVER COMPONENTS

Update `app/page.tsx` to display users from the database:

```typescript
import prisma from "../lib/prisma";

export default async function Home() {
    let users: Array<{
        id: number;
        email: string;
        name: string | null;
        createdAt: Date;
        updatedAt: Date;
    }> = [];
    let error = null;

    try {
        users = await prisma.user.findMany({
            orderBy: {
                createdAt: "desc",
            },
        });
    } catch (e) {
        console.error("Error fetching users:", e);
        error =
            "Failed to load users. Make sure your DATABASE_URL is configured.";
    }

    return (
        <main className="p-8">
            <h1 className="text-2xl font-bold mb-4">Users from Database</h1>
            {error ? (
                <p className="text-red-500">{error}</p>
            ) : users.length === 0 ? (
                <p>No users yet. Create one using the API at /api/users</p>
            ) : (
                <ul className="space-y-2">
                    {users.map((user) => (
                        <li key={user.id} className="border p-4 rounded">
                            <p className="font-semibold">
                                {user.name || "No name"}
                            </p>
                            <p className="text-sm text-gray-600">
                                {user.email}
                            </p>
                        </li>
                    ))}
                </ul>
            )}
        </main>
    );
}
```

## COMPLETE SETUP WORKFLOW

User should follow these steps (AI should provide these instructions):

1. **Install dependencies**:

   ```npm
   npm install prisma tsx --save-dev
   ```

   ```npm
   npm install @prisma/adapter-pg @prisma/client dotenv
   ```

2. **Initialize Prisma, then create Prisma Postgres:**

   > **AI ASSISTANT**: You can run `npx prisma init` yourself. If you should not provision cloud resources automatically, ask the user to run `npx create-db` and update `DATABASE_URL` before continuing.

   ```npm
   npx prisma init --output ../app/generated/prisma
   npx create-db
   ```

   This creates `prisma/schema.prisma`, `prisma.config.ts`, and `.env`, then returns a `postgres://...` connection string for Prisma Postgres.

   **If you asked the user to run `npx create-db`, wait for them to share or paste the returned connection string before proceeding.**

3. **Verify `.env` was created** - Replace the generated `DATABASE_URL` with the `postgres://...` connection string returned by `npx create-db`.

   ```text
   DATABASE_URL="postgres://..."
   ```

   **Do NOT invent this URL. Use the one returned by `npx create-db`.**

4. **Update `prisma/schema.prisma`** - Add the User model (generator and datasource are already configured):

   ```prisma
   model User {
     id        Int      @id @default(autoincrement())
     email     String   @unique
     name      String?
     createdAt DateTime @default(now())
     updatedAt DateTime @updatedAt
   }
   ```

5. **Create `lib/prisma.ts`** with correct import path including `/client` and using `@prisma/adapter-pg`.

6. **Add npm scripts** to `package.json` for `db:test` and `db:studio`

7. **Create `scripts/test-database.ts`** test script

8. **Push schema to database**:

   ```npm
   npx prisma db push
   ```

9. **Generate Prisma Client**:

   ```npm
   npx prisma generate
   ```

10. **Test the setup**:

    ```bash
    npm run db:test
    ```

11. **Start development server**:
    ```bash
    npm run dev
    ```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using `provider = "prisma-client"` (not "prisma-client-js")? If not, STOP and FIX.
2. Are you using `output = "../app/generated/prisma"`? If not, STOP and FIX.
3. Are you importing from `'../app/generated/prisma/client'` (with `/client`)? If not, STOP and FIX.
4. Did you add `import "dotenv/config"` to `prisma.config.ts`? If not, STOP and FIX.
5. Did you add `import "dotenv/config"` to `scripts/test-database.ts`? If not, STOP and FIX.
6. Are you using `@prisma/adapter-pg`? If not, STOP and FIX.
7. Are you using `adapter` property in PrismaClient constructor? If not, STOP and FIX.
8. Are you wrapping database operations in try-catch? If not, STOP and FIX.
9. Did you create the test script at `scripts/test-database.ts`? If not, STOP and FIX.
10. Did you add `db:test` and `db:studio` scripts to package.json? If not, STOP and FIX.
11. Did you remove `url` from the datasource block in `schema.prisma`? If not, STOP and FIX.
12. Did you remove `engine` property from `prisma.config.ts`? If not, STOP and FIX.
13. Did you run `npx prisma init` with the documented output path? If not, STOP and FIX.
14. Is the DATABASE_URL a TCP URL (`postgres://...`)? If it's a `prisma+postgres://` URL, STOP and FIX.
15. Did Prisma generate the `.env` file? If you invented the URL manually, STOP and FIX.

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

The implementation will:

1. Break immediately with module errors
2. Fail to read environment variables
3. Cause connection pool exhaustion in production
4. Result in import errors that prevent compilation
5. Cause performance issues and connection failures
6. Fail with "HTTP connection string is not supported" errors when using local URLs

## USEFUL COMMANDS

```bash

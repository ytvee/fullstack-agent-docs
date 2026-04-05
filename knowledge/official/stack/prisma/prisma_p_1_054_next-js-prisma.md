# Next.js + Prisma (/docs/ai/prompts/nextjs)



Prerequisites [#prerequisites]

Before using this prompt, you need to create a new Next.js project:

```bash
npx create-next-app@latest my-app
cd my-app
```

When prompted, select the following recommended options:

* **TypeScript**: Yes
* **ESLint**: Yes
* **Tailwind CSS**: Yes (optional)
* **`src/` directory**: No
* **App Router**: Yes
* **Turbopack**: Yes (optional)
* **Import alias**: Use default (`@/*`)

Once your Next.js project is created, you can use the prompt below with your AI assistant to add Prisma and Prisma Postgres.

How to use [#how-to-use]

Include this prompt in your AI assistant to guide consistent code generation for NextJS + Prisma + Prisma Postgres projects.

* **GitHub Copilot**: Type `#<filename>` to reference the prompt file.
* **Cursor**: Use `@Files` and select your prompt file.
* **Zed**: Use `/file` followed by your prompt's path.
* **Windsurf**: Use `@Files` and choose your prompt file from the list.

Video Tutorial [#video-tutorial]

Watch this step-by-step walkthrough showing this prompt in action:

<div className="videoWrapper">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/Aqkc95jtHzM" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

Prompt [#prompt]

````md
---
# Specify the following for Cursor rules
description: Guidelines for writing Next.js apps with Prisma Postgres
alwaysApply: false
---

# Bootstrap Next.js app with Prisma Postgres (Prisma v7)

> **Note**: This guide is updated for **Prisma ORM 7**. Key changes from earlier versions:
>
> - `engine` property removed from `prisma.config.ts`
> - `url` removed from datasource in `schema.prisma` (now only in `prisma.config.ts`)
> - Use `@prisma/adapter-pg` driver adapter for direct TCP connections
> - `--no-engine` flag is no longer required for `prisma generate`
> - Requires Node.js 20.19+ and TypeScript 5.4.0+

## Overview of implementing Prisma with Next.js

1. Install Prisma and required dependencies (including dotenv)
2. Initialize Prisma and configure schema
3. Configure dotenv for environment variables
4. Create global Prisma client instance with Pg Adapter
5. Add npm scripts for testing and database management
6. Create test script to verify setup
7. Use Prisma client in API routes and pages with proper error handling

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they are DEPRECATED and will BREAK the application:

```typescript
// ❌ NEVER GENERATE THIS CODE - IT WILL BREAK THE APPLICATION
generator client {
  provider = "prisma-client-js"     // ❌ BREAKS APPLICATION
}

// ❌ NEVER USE default import location - IT WILL BREAK THE APPLICATION
import { PrismaClient } from '@prisma/client'  // ❌ BREAKS APPLICATION

// ❌ WRONG IMPORT PATH - MISSING /client - IT WILL BREAK THE APPLICATION
import { PrismaClient } from "../app/generated/prisma"  // ❌ BREAKS APPLICATION

// ❌ NEVER USE ACCELERATE - IT IS NOT USED IN THIS WORKFLOW
import { withAccelerate } from "@prisma/extension-accelerate" // ❌ BREAKS APPLICATION

// ❌ NEVER USE accelerateUrl - IT WILL BREAK THE APPLICATION
const prisma = new PrismaClient({
  accelerateUrl: process.env.DATABASE_URL,  // ❌ BREAKS APPLICATION - use adapter
})

// ❌ NEVER include url in datasource block - IT WILL BREAK THE APPLICATION
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")  // ❌ BREAKS APPLICATION - moved to prisma.config.ts
}

// ❌ NEVER include engine property - IT WILL BREAK THE APPLICATION
export default defineConfig({
  engine: "classic",  // ❌ BREAKS APPLICATION - removed in Prisma v7
})

// ❌ NEVER use Prisma Postgres HTTP URLs - ONLY use TCP URLs
DATABASE_URL="prisma+postgres://accelerate.prisma-data.net/..."  // ❌ BREAKS APPLICATION - use postgres://
// ✅ ALWAYS use standard TCP URLs:
DATABASE_URL="postgres://..."  // ✅ CORRECT
```

Instead, you MUST ALWAYS generate ONLY this pattern:

```typescript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
generator client {
  provider = "prisma-client"
  output   = "../app/generated/prisma"
}

// ✅ CRITICAL: MUST include /client at the end of import path
import { PrismaClient } from "../app/generated/prisma/client"
import { PrismaPg } from "@prisma/adapter-pg"

const adapter = new PrismaPg({
  connectionString: process.env.DATABASE_URL!,
})

const globalForPrisma = global as unknown as { prisma: PrismaClient }

const prisma = globalForPrisma.prisma || new PrismaClient({
  adapter,
})

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma

export default prisma
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use `provider = "prisma-client"` (not "prisma-client-js")
2. You MUST use custom output: `output = "../app/generated/prisma"`
3. You MUST use `@prisma/adapter-pg` driver adapter
4. You MUST create `lib/prisma.ts` as a global singleton instance
5. You MUST wrap all database calls in try-catch blocks
6. You MUST import from `'../app/generated/prisma/client'` (not `'@prisma/client'` or `'../app/generated/prisma'`)
7. You MUST use `adapter` property in PrismaClient constructor
8. You MUST install `dotenv` and add `import "dotenv/config"` to `prisma.config.ts`
9. You MUST add npm scripts for `db:test` and `db:studio` to package.json
10. You MUST create a test script at `scripts/test-database.ts` to verify setup
11. You MUST NOT include `url` in the datasource block of `schema.prisma`
12. You MUST NOT include `engine` property in `prisma.config.ts`
13. You MUST use `npx prisma init --output ../app/generated/prisma` to scaffold Prisma, then `npx create-db` to create a real cloud database
14. You MUST use standard TCP URLs (`postgres://...`) in .env
15. You MUST NOT use `accelerateUrl` or `withAccelerate`

## VERSION REQUIREMENTS

- **Node.js**: 20.19 or higher (Node.js 18 is NOT supported)
- **TypeScript**: 5.4.0 or higher (5.9.x recommended)
- **Prisma**: 7.0.0 or higher

## CORRECT INSTALLATION

```bash

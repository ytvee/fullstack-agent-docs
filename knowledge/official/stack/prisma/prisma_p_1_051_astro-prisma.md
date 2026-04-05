# Astro + Prisma (/docs/ai/prompts/astro)



How to use [#how-to-use]

Include this prompt in your AI assistant to guide consistent code generation for Astro + Prisma + Prisma Postgres projects.

* **GitHub Copilot**: Type `#<filename>` to reference the prompt file.
* **Cursor**: Use `@Files` and select your prompt file.
* **Zed**: Use `/file` followed by your prompt's path.
* **Windsurf**: Use `@Files` and choose your prompt file from the list.

Prompt [#prompt]

````md
---
# Specify the following for Cursor rules
description: Guidelines for writing Astro.js apps with Prisma Postgres
alwaysApply: false
---

# Bootstrap Astro app with Prisma Postgres

## Overview of implementing Prisma with Astro

1. Install Prisma and required dependencies
2. Initialize Prisma with custom output path
3. Configure schema with correct provider
4. Create global Prisma client instance with Accelerate
5. Use Prisma client in API routes with proper error handling

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any of the following code patterns, as they are DEPRECATED and will BREAK the application:

```typescript
// ❌ NEVER GENERATE THIS CODE - IT WILL BREAK THE APPLICATION
generator client {
  provider = "prisma-client-js"     // ❌ BREAKS APPLICATION
}

// ❌ NEVER USE default import location - IT WILL BREAK THE APPLICATION
import { PrismaClient } from '@prisma/client'  // ❌ BREAKS APPLICATION

// ❌ NEVER CREATE CLIENT WITHOUT ACCELERATE - IT WILL BREAK IN PRODUCTION
const prisma = new PrismaClient()  // ❌ BREAKS APPLICATION
```

Instead, you MUST ALWAYS generate ONLY this pattern:

```typescript
// ✅ ALWAYS GENERATE THIS EXACT PATTERN
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}

// ✅ ALWAYS USE THIS IMPORT PATH
import { PrismaClient } from "../generated/prisma/client"
import { withAccelerate } from "@prisma/extension-accelerate"

// ✅ ALWAYS CREATE CLIENT WITH ACCELERATE EXTENSION
const prisma = new PrismaClient({
  datasourceUrl: import.meta.env.DATABASE_URL,
}).$extends(withAccelerate())

export default prisma
```

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use `provider = "prisma-client"` (not "prisma-client-js")
2. You MUST use custom output: `output = "../src/generated/prisma"`
3. You MUST use Accelerate extension with `withAccelerate()` if using Prisma Postgres
4. You MUST create `lib/prisma.ts` as a global singleton instance
5. You MUST wrap all database calls in try-catch blocks
6. You MUST import from `'../generated/prisma/client'` (not `'@prisma/client'`)
7. You MUST use `import.meta.env.DATABASE_URL` in Astro (not `process.env`)
8. You MUST use `npx prisma init --output ../src/generated/prisma` before editing the Prisma schema. If you need Prisma Postgres, run `npx create-db` and update `.env` with the returned `postgres://...` value

## CORRECT INSTALLATION

```bash

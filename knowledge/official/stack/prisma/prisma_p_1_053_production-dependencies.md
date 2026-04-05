# Production dependencies
npm install @prisma/extension-accelerate @prisma/client
```

## CORRECT PRISMA INITIALIZATION

```npm
npx prisma init --output ../src/generated/prisma
```

## CORRECT SCHEMA CONFIGURATION

```prisma
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model YourModel {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

## CORRECT GLOBAL PRISMA CLIENT

**src/lib/prisma.ts**:

```typescript
import { PrismaClient } from "../generated/prisma/client";
import { withAccelerate } from "@prisma/extension-accelerate";

const prisma = new PrismaClient({
  datasourceUrl: import.meta.env.DATABASE_URL,
}).$extends(withAccelerate());

export default prisma;
```

## CORRECT API ROUTE IMPLEMENTATION

All API routes MUST follow this pattern with proper error handling:

```typescript
import type { APIRoute } from "astro";
import prisma from "../../../lib/prisma";

export const GET: APIRoute = async () => {
  try {
    const data = await prisma.yourModel.findMany();
    return new Response(JSON.stringify(data), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  } catch (error) {
    console.error("Error:", error);
    return new Response(JSON.stringify({ error: "Failed to fetch data" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
};

export const POST: APIRoute = async ({ request }) => {
  try {
    const body = await request.json();

    // Validate required fields
    if (!body.requiredField) {
      return new Response(JSON.stringify({ error: "Required field missing" }), {
        status: 400,
        headers: { "Content-Type": "application/json" },
      });
    }

    const result = await prisma.yourModel.create({
      data: body,
    });

    return new Response(JSON.stringify(result), {
      status: 201,
      headers: { "Content-Type": "application/json" },
    });
  } catch (error) {
    console.error("Error:", error);
    return new Response(JSON.stringify({ error: "Failed to create data" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
};
```

## CORRECT USAGE IN ASTRO PAGES

Server-side data fetching in Astro pages:

```astro
---
import prisma from '../lib/prisma'

// Fetch data on the server
const data = await prisma.yourModel.findMany()
---

<html>
  <body>
    {data.map(item => (
      <div>{item.name}</div>
    ))}
  </body>
</html>
```

## AI MODEL VERIFICATION STEPS

Before generating any code, you MUST verify:

1. Are you using `provider = "prisma-client"` (not "prisma-client-js")? If not, STOP and FIX.
2. Are you using `output = "../src/generated/prisma"`? If not, STOP and FIX.
3. Are you importing from `'../generated/prisma/client'`? If not, STOP and FIX.
4. Are you using `withAccelerate()` extension? If not, STOP and FIX.
5. Are you wrapping database operations in try-catch? If not, STOP and FIX.
6. Are you using `import.meta.env` (not `process.env`)? If not, STOP and FIX.
7. Did you use `--generator-provider prisma-client` (NOT `postgresql`)? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate code using:

- `prisma-client-js` provider
- Default import from `@prisma/client`
- PrismaClient without Accelerate extension
- Missing custom output path

The implementation will:

1. Break in production
2. Cause connection pool exhaustion
3. Fail to maintain proper database connections
4. Result in import errors
5. Cause performance issues

## USEFUL COMMANDS

```npm
npx prisma generate              # Regenerate client after schema changes
```

```npm
npx prisma migrate dev --name X  # Create and apply migration
```

```npm
npx prisma studio                # Open visual database editor
```

```npm
npx prisma db push               # Push schema without migration
```

## AI MODEL RESPONSE TEMPLATE

When asked about Prisma + Astro implementation, you MUST:

1. ONLY use code from this guide
2. NEVER suggest deprecated approaches
3. ALWAYS use the exact patterns shown above
4. VERIFY your response against the patterns shown here
5. ALWAYS include error handling in API routes
6. ALWAYS use the global prisma instance from `lib/prisma.ts`

Remember: There are NO EXCEPTIONS to these rules.
````

Running the application [#running-the-application]

Get your application running locally in three quick steps:

**1. Generate the Prisma Client:**

```bash
npx prisma generate --no-engine
```

**2. View your database in Prisma Studio:**

```bash
npm run db:studio
```

Prisma Studio opens at `localhost:5555` where you can inspect your `User` table and see the test user stored in your database.

**3. Start your Next.js development server:**

```bash
npm run dev
```

Visit `http://localhost:3000` to see your Next.js application live, displaying your first user fetched directly from your Prisma Postgres database!



---
category: architecture
topic: api-design
status: draft
---

## Проблема / Контекст

Next.js App Router offers two ways to handle mutations and data operations: **Route Handlers** (the `route.ts` files under `app/api/`) and **Server Actions** (async functions marked with `'use server'`). Choosing the wrong tool for the job leads to unnecessary complexity: building REST endpoints that only your own frontend calls, or using Server Actions for webhook receivers that need raw body access.

Additionally, inconsistent error formats, missing Zod validation on inputs, and ad-hoc auth checks scattered across handlers create security gaps and make APIs unpredictable for consumers.

## Решение

### Decision Rule: Route Handler vs Server Action

| Criterion | Route Handler (`route.ts`) | Server Action |
|---|---|---|
| Called by external clients (Stripe webhooks, mobile apps) | Yes | No |
| Needs raw request body (webhook signature verification) | Yes | No |
| Mutation from a Client Component form | No | **Yes** |
| Progressive enhancement (works without JS) | No | **Yes** |
| Returns streaming response | Yes | Limited |
| Called by Server Component | No (fetch overhead) | **Yes** |
| Needs custom HTTP status codes for external consumers | Yes | No |
| File uploads from browser | Either | Either |

**Heuristic**: If only your own Next.js app calls it, use a Server Action. If anything outside your app calls it, use a Route Handler.

### Route Handler Conventions

Route handlers live under `src/app/api/` and follow REST conventions.

**File structure:**
```
src/app/api/
├── webhooks/
│   ├── stripe/route.ts        # POST only — no auth, raw body
│   └── uploadthing/route.ts   # GET + POST — UploadThing SDK
└── v1/                        # Versioned public API (if needed)
    └── projects/
        ├── route.ts           # GET (list), POST (create)
        └── [id]/
            └── route.ts       # GET, PUT, DELETE
```

**Standard response helper:**
```typescript
// src/lib/api-response.ts
import { NextResponse } from 'next/server'
import type { ApiResponse } from '@/types/api'

export function ok<T>(data: T, status = 200): NextResponse<ApiResponse<T>> {
  return NextResponse.json({ success: true, data }, { status })
}

export function err(
  error: string,
  status = 400,
  code?: string
): NextResponse<ApiResponse<never>> {
  return NextResponse.json({ success: false, error, code }, { status })
}
```

**GET — list resources with pagination:**
```typescript
// src/app/api/v1/projects/route.ts
import { auth } from '@/server/auth'
import { db } from '@/server/db'
import { projects } from '@/server/db/schema'
import { eq, desc, count } from 'drizzle-orm'
import { z } from 'zod'
import { ok, err } from '@/lib/api-response'
import type { NextRequest } from 'next/server'

const listQuerySchema = z.object({
  page: z.coerce.number().int().min(1).default(1),
  pageSize: z.coerce.number().int().min(1).max(100).default(20),
})

export async function GET(request: NextRequest) {
  const session = await auth()
  if (!session?.user?.id) return err('Unauthorized', 401)

  const { searchParams } = request.nextUrl
  const parsed = listQuerySchema.safeParse(Object.fromEntries(searchParams))
  if (!parsed.success) return err('Invalid query parameters', 400)

  const { page, pageSize } = parsed.data
  const offset = (page - 1) * pageSize

  const [rows, [{ value: total }]] = await Promise.all([
    db.query.projects.findMany({
      where: eq(projects.userId, session.user.id),
      orderBy: [desc(projects.createdAt)],
      limit: pageSize,
      offset,
    }),
    db.select({ value: count() }).from(projects).where(eq(projects.userId, session.user.id)),
  ])

  return ok({
    data: rows,
    total,
    page,
    pageSize,
    totalPages: Math.ceil(total / pageSize),
  })
}
```

**POST — create resource:**
```typescript
import { createProjectSchema } from '@/features/project-create/schemas'

export async function POST(request: NextRequest) {
  const session = await auth()
  if (!session?.user?.id) return err('Unauthorized', 401)

  let body: unknown
  try {
    body = await request.json()
  } catch {
    return err('Invalid JSON body', 400)
  }

  const parsed = createProjectSchema.safeParse(body)
  if (!parsed.success) {
    return err('Validation failed', 422, 'VALIDATION_ERROR')
    // For detailed field errors, return parsed.error.flatten()
  }

  const [project] = await db
    .insert(projects)
    .values({ ...parsed.data, userId: session.user.id })
    .returning()

  return ok(project, 201)
}
```

**DELETE — remove resource:**
```typescript
// src/app/api/v1/projects/[id]/route.ts
export async function DELETE(
  _request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth()
  if (!session?.user?.id) return err('Unauthorized', 401)

  const { id } = await params

  const existing = await db.query.projects.findFirst({
    where: eq(projects.id, id),
  })
  if (!existing) return err('Not found', 404)
  if (existing.userId !== session.user.id) return err('Forbidden', 403)

  await db.delete(projects).where(eq(projects.id, id))
  return ok({ deleted: true })
}
```

**Webhook Route Handler — raw body, signature verification:**
```typescript
// src/app/api/webhooks/stripe/route.ts
import { stripe } from '@/lib/stripe'
import { db } from '@/server/db'
import { subscriptions } from '@/server/db/schema'
import { eq } from 'drizzle-orm'
import { headers } from 'next/headers'
import type Stripe from 'stripe'

export async function POST(request: Request) {
  const body = await request.text() // Raw body required for signature
  const headersList = await headers()
  const sig = headersList.get('stripe-signature')

  if (!sig) {
    return new Response('Missing stripe-signature header', { status: 400 })
  }

  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(
      body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET!
    )
  } catch {
    return new Response('Webhook signature verification failed', { status: 400 })
  }

  switch (event.type) {
    case 'customer.subscription.created':
    case 'customer.subscription.updated': {
      const sub = event.data.object as Stripe.Subscription
      const userId = sub.metadata.userId
      if (!userId) break

      await db
        .insert(subscriptions)
        .values({
          userId,
          stripeSubscriptionId: sub.id,
          stripeCustomerId: sub.customer as string,
          plan: sub.items.data[0]?.price.lookup_key ?? 'pro',
          status: sub.status,
          currentPeriodEnd: new Date(sub.current_period_end * 1000),
          trialEndsAt: sub.trial_end ? new Date(sub.trial_end * 1000) : null,
        })
        .onConflictDoUpdate({
          target: subscriptions.userId,
          set: {
            status: sub.status,
            plan: sub.items.data[0]?.price.lookup_key ?? 'pro',
            currentPeriodEnd: new Date(sub.current_period_end * 1000),
            trialEndsAt: sub.trial_end ? new Date(sub.trial_end * 1000) : null,
          },
        })
      break
    }
    case 'customer.subscription.deleted': {
      const sub = event.data.object as Stripe.Subscription
      const userId = sub.metadata.userId
      if (userId) {
        await db
          .update(subscriptions)
          .set({ status: 'canceled' })
          .where(eq(subscriptions.userId, userId))
      }
      break
    }
  }

  return new Response(null, { status: 200 })
}
```

### Server Actions for Mutations

Server Actions are the default for any mutation initiated from your own UI.

**Standard Server Action pattern:**
```typescript
// src/features/projects/actions.ts
'use server'

import { auth } from '@/server/auth'
import { db } from '@/server/db'
import { projects } from '@/server/db/schema'
import { eq } from 'drizzle-orm'
import { revalidatePath } from 'next/cache'
import { z } from 'zod'
import type { ActionResult } from '@/types/api'
import { createProjectSchema, updateProjectSchema } from './schemas'

export async function createProject(
  input: z.infer<typeof createProjectSchema>
): Promise<ActionResult<{ id: string }>> {
  const session = await auth()
  if (!session?.user?.id) {
    return { success: false, error: 'Unauthorized' }
  }

  const parsed = createProjectSchema.safeParse(input)
  if (!parsed.success) {
    return {
      success: false,
      error: 'Validation failed',
      fieldErrors: parsed.error.flatten().fieldErrors as Record<string, string[]>,
    }
  }

  try {
    const [project] = await db
      .insert(projects)
      .values({ ...parsed.data, userId: session.user.id })
      .returning({ id: projects.id })

    revalidatePath('/projects')
    return { success: true, data: { id: project.id } }
  } catch (error) {
    console.error('createProject error:', error)
    return { success: false, error: 'Failed to create project' }
  }
}

export async function deleteProject(projectId: string): Promise<ActionResult> {
  const session = await auth()
  if (!session?.user?.id) {
    return { success: false, error: 'Unauthorized' }
  }

  const existing = await db.query.projects.findFirst({
    where: eq(projects.id, projectId),
    columns: { userId: true },
  })

  if (!existing) return { success: false, error: 'Not found' }
  if (existing.userId !== session.user.id) return { success: false, error: 'Forbidden' }

  await db.delete(projects).where(eq(projects.id, projectId))
  revalidatePath('/projects')
  return { success: true, data: undefined }
}
```

### Zod Schemas — Shared Between Client and Server

Define schemas in the feature's `schemas.ts` — imported by both the form (client) and the action (server):

```typescript
// src/features/projects/schemas.ts
import { z } from 'zod'

export const createProjectSchema = z.object({
  name: z
    .string()
    .min(1, 'Name is required')
    .max(100, 'Name must be 100 characters or less'),
  description: z.string().max(500).optional(),
  visibility: z.enum(['public', 'private']).default('private'),
})

export const updateProjectSchema = createProjectSchema.partial().extend({
  id: z.string().cuid2(),
})

export type CreateProjectInput = z.infer<typeof createProjectSchema>
export type UpdateProjectInput = z.infer<typeof updateProjectSchema>
```

### Middleware for Auth — Edge-Level Route Protection

`middleware.ts` runs at the edge before the route is served. Use it for broad auth checks, not fine-grained authorization (roles/permissions belong in the layout or action).

```typescript
// src/middleware.ts
import { auth } from '@/server/auth'
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

const PUBLIC_PATHS = ['/', '/pricing', '/blog', '/login', '/register', '/forgot-password']
const API_AUTH_FREE = ['/api/webhooks'] // webhooks skip session auth

export default auth((request: NextRequest & { auth: unknown }) => {
  const { pathname } = request.nextUrl
  const session = (request as { auth: { user?: unknown } | null }).auth

  // Allow public paths
  if (PUBLIC_PATHS.some((p) => pathname === p || pathname.startsWith(p + '/'))) {
    return NextResponse.next()
  }

  // Allow webhook endpoints without auth
  if (API_AUTH_FREE.some((p) => pathname.startsWith(p))) {
    return NextResponse.next()
  }

  // Redirect unauthenticated users to login
  if (!session?.user) {
    const loginUrl = new URL('/login', request.url)
    loginUrl.searchParams.set('callbackUrl', pathname)
    return NextResponse.redirect(loginUrl)
  }

  return NextResponse.next()
})

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)'],
}
```

### Standardized Error Response Format

All errors from both Route Handlers and Server Actions use the same shape:

```typescript
// Errors from Route Handlers (external consumers)
{
  "success": false,
  "error": "Human-readable message",
  "code": "MACHINE_READABLE_CODE"   // optional, for programmatic handling
}

// Validation errors include field errors
{
  "success": false,
  "error": "Validation failed",
  "code": "VALIDATION_ERROR",
  "fieldErrors": {
    "name": ["Name is required"],
    "email": ["Invalid email address"]
  }
}

// Success responses
{
  "success": true,
  "data": { ... }
}
```

HTTP status code conventions:
- `200` — successful GET, PUT, DELETE
- `201` — successful POST (resource created)
- `400` — bad request (malformed JSON, missing required fields)
- `401` — unauthenticated (no valid session/token)
- `403` — authenticated but not authorized for this resource
- `404` — resource not found
- `422` — validation failed (valid JSON, invalid values)
- `429` — rate limited
- `500` — server error (never expose internals)

## Антипаттерн

```typescript
// BAD 1: Using Route Handler for a mutation only called by your own frontend
// src/app/api/update-profile/route.ts — UNNECESSARY
export async function POST(request: NextRequest) {
  const body = await request.json()
  // ... update user ...
}
// Client then does: await fetch('/api/update-profile', { method: 'POST', body: JSON.stringify(data) })
// USE A SERVER ACTION INSTEAD

// BAD 2: No Zod validation in Server Action — trusting client input
export async function createProject(name: string, description: string) {
  'use server'
  // Directly inserting without validation — type safety alone is not enough at runtime
  await db.insert(projects).values({ name, description, userId: '...' })
}

// BAD 3: Throwing errors from Server Actions — breaks error handling in Client Components
export async function deleteProject(id: string) {
  'use server'
  const project = await db.query.projects.findFirst(...)
  if (!project) throw new Error('Not found')  // Unhandled in the client
  // Return { success: false, error: 'Not found' } instead
}

// BAD 4: Auth check missing in Server Action — assuming middleware is enough
export async function adminDeleteUser(userId: string) {
  'use server'
  // No session check — middleware only protects page routes, not direct action calls
  await db.delete(users).where(eq(users.id, userId))
}
```

## Связанные документы

- `01-architecture/data-flow.md` — When to fetch in Server Components vs Server Actions
- `02-patterns/crud-pattern.md` — Full CRUD using Server Actions
- `02-patterns/auth-flow.md` — Auth.js session in Route Handlers and Server Actions
- `06-security/input-validation.md` — Zod patterns for server-side validation

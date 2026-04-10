# 30 - Security

> **Scope:** All project files
>
> **Relationship:** Extends `00-context.md`. Core rules (env vars, Git) are defined there. This file covers security architecture, patterns, and configurations.

## 1. Next.js 15 threat model

Before implementing any data-related feature — explicitly answer three questions:

1. Who can call this code? (Server Action / Route Handler = public HTTP endpoint)
2. Can the response leak to the client? (Server Component → Client Component boundary)
3. Is authorization checked near the data, not only in middleware?

Middleware is not a security boundary. Use it only for redirects and UX optimizations. Real authorization checks must live in the Data Access Layer.

> **CVE-2025-29927:** In March 2025, a critical vulnerability (CVSS 9.1) was disclosed in Next.js 11.1.4–15.2.2. An attacker could pass the `x-middleware-subrequest` header to completely bypass middleware, including all authentication checks. Fixed in Next.js **15.2.3+**. Verify the version is up to date.

---

## 2. Data Access Layer (DAL)

The official Next.js recommendation for new projects: all data access logic lives in a dedicated layer at `src/lib/dal.ts` or `src/features/*/queries.ts`.

Every DAL file must start with:

```typescript
import 'server-only'
```

This causes a build error if the DAL module is imported in a Client Component.

### DAL function structure

```typescript
// src/lib/dal.ts
import 'server-only'
import { cache } from 'react'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import { db } from '@/lib/db'

// cache() — one session check per render pass, no duplicate DB requests
export const verifySession = cache(async () => {
  const cookieStore = await cookies()
  const token = cookieStore.get('session')?.value
  if (!token) redirect('/login')

  const session = await validateToken(token)
  if (!session) redirect('/login')

  return session
})

// Never return a raw ORM object — return only a DTO with the required fields
export async function getUserProfile(targetUserId: string) {
  const session = await verifySession()

  // Authorization check near the data (authorization, not just authentication)
  if (session.userId !== targetUserId && session.role !== 'admin') {
    return null
  }

  return db.user.findUnique({
    where: { id: targetUserId },
    select: { id: true, name: true, email: true }, // only needed fields
  })
}
```

### DAL rules

- `import 'server-only'` — required in every DAL file.
- Session verification — via `cache()` from React. One `verifySession` function is called everywhere.
- Authorization is checked inside the DAL function, not in the component.
- Return DTOs — only the fields the UI needs. Never return raw Prisma objects with fields like `passwordHash`, `internalNotes`.
- Direct DAL calls from Server Components — do not call `fetch('http://localhost/api/...')`.

---

## 3. Server Action security

A Server Action is a public HTTP POST endpoint. Check every one against this template:

```typescript
// features/posts/actions.ts
'use server'

import { z } from 'zod'
import { revalidatePath } from 'next/cache'
import { verifySession } from '@/lib/dal'
import { db } from '@/lib/db'

const UpdatePostSchema = z.object({
  postId: z.string().cuid(),
  title: z.string().min(1).max(200),
  content: z.string().min(1),
})

export async function updatePost(formData: FormData) {
  // 1. Authentication — who is calling?
  const session = await verifySession()

  // 2. Input validation with Zod
  const parsed = UpdatePostSchema.safeParse({
    postId: formData.get('postId'),
    title: formData.get('title'),
    content: formData.get('content'),
  })
  if (!parsed.success) return { error: parsed.error.flatten() }

  // 3. Authorization — does this user have the right to perform this action?
  // Resource ownership check prevents IDOR attacks
  const post = await db.post.findUnique({ where: { id: parsed.data.postId } })
  if (!post) return { error: 'Not found' }
  if (post.authorId !== session.userId) return { error: 'Forbidden' }

  // 4. Mutation
  await db.post.update({
    where: { id: parsed.data.postId },
    data: { title: parsed.data.title, content: parsed.data.content },
  })

  revalidatePath('/posts')
}
```

### Forbidden in Server Actions

- Checking permissions only at the page level — the Action is called directly, independent of the UI.
- Returning full objects from the database — only the needed fields.
- Throwing uncaught errors — log server-side, return `{ error: string }`.
- Trusting any data from `formData` without Zod validation.

---

## 4. Environment variables

```
# Server-only (secure)
DATABASE_URL=
AUTH_SECRET=
STRIPE_SECRET_KEY=

# Visible to the client in the JS bundle (public data only)
NEXT_PUBLIC_APP_URL=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
```

Rules:

- Secrets (API keys, DB passwords, tokens) — never with the `NEXT_PUBLIC_` prefix.
- Read `process.env.SECRET` only in DAL, Server Actions, and Route Handlers — not in components.
- In responses, logs, comments, and git diffs — never expose `.env` values.
- `.env.local` in `.gitignore`. Only `.env.example` with placeholder values may be committed.

---

## 5. Cookies and sessions

```typescript
// lib/session.ts
import 'server-only'
import { cookies } from 'next/headers'

export async function setSessionCookie(token: string) {
  const cookieStore = await cookies()
  cookieStore.set('session', token, {
    httpOnly: true,   // not accessible via document.cookie (XSS protection)
    secure: true,     // HTTPS only
    sameSite: 'lax',  // CSRF protection; 'strict' if no cross-site navigation
    path: '/',
    maxAge: 60 * 60 * 24, // 24 hours
  })
}
```

Forbidden:

- Storing session tokens in `localStorage` or `sessionStorage` — readable by any JS on the page.
- Using `sameSite: 'none'` without a clear justification.
- Sessions without `maxAge` — they do not expire on the server side when the browser closes.

---

## 6. HTTP Security Headers

Add via `next.config.ts`. For CSP with nonce — use middleware.

### Static headers (next.config.ts)

```typescript
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          { key: 'X-Content-Type-Options', value: 'nosniff' },
          { key: 'X-Frame-Options', value: 'DENY' },
          { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
          { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
          {
            key: 'Strict-Transport-Security',
            value: 'max-age=31536000; includeSubDomains',
          },
        ],
      },
    ]
  },
}

export default nextConfig
```

### CSP with nonce (middleware.ts)

Use when inline scripts are needed (analytics, GTM). The nonce is generated per-request:

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server'

export function middleware(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const isDev = process.env.NODE_ENV === 'development'

  const csp = [
    "default-src 'self'",
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${isDev ? " 'unsafe-eval'" : ''}`,
    `style-src 'self' 'nonce-${nonce}'`,
    "img-src 'self' blob: data:",
    "font-src 'self'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
    "upgrade-insecure-requests",
  ].join('; ')

  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)
  requestHeaders.set('Content-Security-Policy', csp)

  const response = NextResponse.next({ request: { headers: requestHeaders } })
  response.headers.set('Content-Security-Policy', csp)

  return response
}

export const config = {
  matcher: [
    {
      source: '/((?!_next/static|_next/image|favicon.ico).*)',
      missing: [
        { type: 'header', key: 'next-router-prefetch' },
        { type: 'header', key: 'purpose', value: 'prefetch' },
      ],
    },
  ],
}
```

Read the nonce in a Server Component:

```typescript
import { headers } from 'next/headers'

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const nonce = (await headers()).get('x-nonce') ?? ''
  // pass nonce to <Script nonce={nonce} />
}
```

| Header | Value | Protects against |
|---|---|---|
| `X-Content-Type-Options` | `nosniff` | MIME-sniffing attacks |
| `X-Frame-Options` | `DENY` | Clickjacking |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | URL leaks in the Referer header |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Downgrade attacks (HTTPS-only) |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | Unauthorized browser API access |
| `Content-Security-Policy` | nonce + strict-dynamic | XSS |

---

## 7. Middleware: optimizations only, not security

Middleware is suitable for:

- Redirecting unauthenticated users (UX, not security).
- Setting security headers.
- Rewrites and localization.

Middleware is not suitable for:

- Being the sole authorization check — after CVE-2025-29927, this is an unacceptable pattern.
- Direct database access (Prisma etc.) in Edge Runtime.
- Business logic and heavy computation.

If middleware redirects — the DAL still checks permissions when data is accessed.

---

## 8. Route Handlers

```typescript
// app/api/posts/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { verifySession } from '@/lib/dal'
import { z } from 'zod'

const QuerySchema = z.object({
  page: z.coerce.number().int().positive().default(1),
})

export async function GET(request: NextRequest) {
  // Authenticate even in GET if data is not public
  const session = await verifySession()

  const { searchParams } = request.nextUrl
  const parsed = QuerySchema.safeParse({ page: searchParams.get('page') })
  if (!parsed.success) {
    return NextResponse.json({ error: 'Invalid params' }, { status: 400 })
  }

  // ... logic
}
```

Rules:

- A Route Handler is a public endpoint. Check auth even if called only from your own frontend.
- Parameters from `searchParams` and `params` — always validate with Zod.
- Do not log the full `request.body` — it may contain passwords and tokens.
- Return identical errors for non-existent and forbidden resources (`404`, not `403`) when the existence of a resource must be hidden.

---

## 9. Security checklist

Before committing any data-related feature, verify:

**Server Actions:**

- Authentication (`verifySession()`) — called first.
- Authorization on the specific resource (not just "is the user logged in").
- All input validated with Zod before use.

**Data Access Layer:**

- File starts with `import 'server-only'`.
- Returns a DTO, not a raw ORM object.
- `verifySession` is wrapped in `cache()`.

**Environment variables:**

- Secrets have no `NEXT_PUBLIC_` prefix.
- `.env.local` is in `.gitignore`.

**Cookies:**

- `httpOnly: true`, `secure: true`, `sameSite: 'lax'` or `'strict'`.
- Tokens not in `localStorage`.

**Middleware:**

- Is not the sole access control point.
- No database calls in Edge Runtime.

**Next.js version:**

- Not below 15.2.3 (CVE-2025-29927 patch).

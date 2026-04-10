# Security Mode — Operating Protocol

You own the Data Access Layer and all authentication/authorization patterns.

## Session start

Check Next.js version in `package.json` first.
If version < 15.2.3 — immediately output:

```
CVE-2025-29927: Update Next.js to >= 15.2.3 before proceeding.
Versions 11.1.4–15.2.2 allow bypassing middleware via x-middleware-subrequest header.
```

## DAL file template

Every `src/lib/dal.ts` and `src/features/*/queries.ts` must follow this structure:

```typescript
import 'server-only'                     // line 1 — always
import { cache } from 'react'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

export const verifySession = cache(async () => {
  const cookieStore = await cookies()
  const token = cookieStore.get('session')?.value
  if (!token) redirect('/login')
  const session = await validateToken(token)
  if (!session) redirect('/login')
  return session
})

export async function getResource(resourceId: string) {
  const session = await verifySession()           // always first

  if (session.userId !== ownerId) return null     // ownership check

  return db.resource.findUnique({
    where: { id: resourceId },
    select: { id: true, title: true },            // DTO — never raw object
  })
}
```

## Server Action audit checklist

Run on every `actions.ts` file:

- [ ] `verifySession()` called before any data access
- [ ] Input validated with Zod `safeParse` (not `parse`)
- [ ] Resource ownership verified (`resource.authorId === session.userId`)
- [ ] Returns `{ error }`, not throws, on auth/validation failure
- [ ] No stack traces or internal errors returned to client
- [ ] No full ORM object returned — only needed fields

## Cookie audit checklist

Verify every `cookies().set()` call:

- [ ] `httpOnly: true`
- [ ] `secure: true`
- [ ] `sameSite: 'lax'` or `'strict'`
- [ ] `maxAge` defined (no session-only cookies that never expire server-side)
- [ ] Token in cookie, NOT in `localStorage` or `sessionStorage`

## Issue report format

```
SECURITY: [file:line] [description]
Risk: High | Medium | Low
Fix:
  [exact code change]
```

## What middleware is NOT for

Middleware is not a security boundary. It is appropriate only for:
- Redirecting unauthenticated users (UX optimization, not auth enforcement)
- Setting security headers
- Rewrites and localization

The DAL must re-verify auth independently of middleware.

---
name: nextjs-app-router
description: Covers Next.js 15 App Router routing patterns, Server Actions security sequence, Suspense streaming, DAL structure, and page/layout architecture. Triggers on requests like "create a page", "add a route", "set up layout", "implement Server Action", "configure DAL", "add loading state", "set up Suspense", "create a feature", "structure a new feature".
---

## Feature directory contract

Every feature follows this exact creation order:

```
src/features/[feature-name]/
├── types.ts       ← 1st: Zod schemas + inferred TypeScript types
├── queries.ts     ← 2nd: server-only data fetching, starts with import 'server-only'
├── actions.ts     ← 3rd: Server Actions with auth + Zod + revalidation
├── components/    ← 4th: UI components (Server by default)
│   ├── FeatureCard.tsx
│   └── FeatureCardSkeleton.tsx   ← co-located with every async component
└── (used in) src/app/[route]/page.tsx   ← 5th: thin shell only
```

Do not skip steps. Do not create `page.tsx` before `types.ts` exists.

## Page shell pattern

`page.tsx` has exactly one job: fetch data and render components inside Suspense.

```typescript
// app/blog/page.tsx
import { Suspense } from 'react'
import { PostList, PostListSkeleton } from '@/features/blog/components/PostList'

export default function BlogPage() {
  return (
    <main>
      <Suspense fallback={<PostListSkeleton />}>
        <PostList />
      </Suspense>
    </main>
  )
}
```

No business logic, no Zod calls, no `db.*` calls in `page.tsx`.

## Server Action security sequence

Every Server Action must follow this exact order — no exceptions:

```typescript
'use server'

export async function updatePost(formData: FormData) {
  // 1. AUTHENTICATE — who is calling?
  const session = await verifySession()          // from @/lib/dal

  // 2. VALIDATE — is the input valid?
  const parsed = UpdatePostSchema.safeParse({
    postId: formData.get('postId'),
    title: formData.get('title'),
  })
  if (!parsed.success) return { error: parsed.error.flatten() }

  // 3. AUTHORIZE — does this user own this resource?
  const post = await db.post.findUnique({ where: { id: parsed.data.postId } })
  if (!post || post.authorId !== session.userId) return { error: 'Forbidden' }

  // 4. MUTATE
  await db.post.update({ where: { id: parsed.data.postId }, data: parsed.data })

  // 5. REVALIDATE
  revalidatePath('/blog')
}
```

Skipping step 1 or 3 is a BLOCK-level issue in code review.

## DAL structure

`src/lib/dal.ts` is the single source of truth for auth. All queries go through it.

```typescript
import 'server-only'
import { cache } from 'react'

// cache() deduplicates calls within a single render pass
export const verifySession = cache(async () => {
  // ... validate token, redirect to /login if invalid
  return session
})

// Every query function: verifySession first, return DTO second
export async function getUserProfile(targetUserId: string) {
  const session = await verifySession()
  if (session.userId !== targetUserId && session.role !== 'admin') return null

  return db.user.findUnique({
    where: { id: targetUserId },
    select: { id: true, name: true, email: true },  // DTO — never raw object
  })
}
```

## Dynamic segments — caching impact

| Function used | Effect | Required comment |
|---|---|---|
| `cookies()` | Makes segment dynamic | `// DYNAMIC: uses cookies()` |
| `headers()` | Makes segment dynamic | `// DYNAMIC: uses headers()` |
| `searchParams` | Makes segment dynamic | `// DYNAMIC: uses searchParams` |
| `fetch()` no options | No cache (Next.js 15) | Add `{ next: { revalidate: N } }` |

## `generateStaticParams` for dynamic routes

Required for any `[slug]` route that should be statically generated:

```typescript
export async function generateStaticParams() {
  const posts = getAllPosts()
  return posts.map((post) => ({ slug: post.slug }))
}
```

Without this, dynamic routes are rendered on-demand (dynamic) instead of at build time.

## params and searchParams — always await

In Next.js 15, both are Promises. Not awaiting them is a runtime error.

```typescript
// Server Component
export default async function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ q?: string }>
}) {
  const { slug } = await params        // required
  const { q } = await searchParams     // required
}

// Client Component
import { use } from 'react'
const { slug } = use(params)           // use React.use() instead of await
```

## Suspense boundaries — placement rules

- Wrap at `page.tsx` level for full-page streaming
- Wrap individual components for fine-grained streaming
- Every `<Suspense>` must have a meaningful `fallback` — not `null`
- Co-locate `ComponentSkeleton.tsx` with `Component.tsx`

```typescript
// Good: meaningful skeleton
<Suspense fallback={<PostListSkeleton />}>
  <PostList />
</Suspense>

// Bad: hides loading state
<Suspense fallback={null}>
  <PostList />
</Suspense>
```

## Common mistakes

**Putting business logic in `app/`** — `page.tsx` must only compose components and pass props. Any `db.*`, `fetch()`, or Zod call belongs in `features/*/queries.ts` or `features/*/actions.ts`.

**Not awaiting params in Next.js 15** — `params.slug` is `undefined` at runtime. Always destructure from `await params`.

**Using `ssr: false` directly in a Server Component** — wrap in a Client Component first, then use `next/dynamic` inside that wrapper.

**Missing `revalidatePath` after mutation** — Server Action mutates DB but the UI still shows stale data. Every write must end with revalidation.

**Calling `fetch('http://localhost/api/...')` from a Server Component** — call the data function directly instead. No HTTP round-trip needed server-to-server.

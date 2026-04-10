# 10 - Next.js Conventions (App Router)

> **Scope:** All files and components in the Next.js project
>
> **Next.js version:** 15+ (with React 19)
>
> **Relationship:** Extends `00-context.md`. In case of conflict, this file takes precedence on Next.js-specific details.

## 1. Routing and `app/` structure

Project structure and `features/` separation are described in `00-context.md`. This file covers routing specifics only.

Special file segments:

| File | Purpose |
|---|---|
| `layout.tsx` | Persistent segment wrapper |
| `page.tsx` | Public route |
| `loading.tsx` | Suspense fallback at segment level |
| `error.tsx` | Error boundary (must be `'use client'`) |
| `not-found.tsx` | 404 for the segment |
| `route.ts` | Route Handler (REST / webhooks) |
| `template.tsx` | Like layout, but re-created on navigation |

Conventions:

- Route groups: `(kebab-case)` — do not affect the URL
- Dynamic segments: `[slug]`, `[...catchAll]`, `[[...optional]]`
- Private folders (not exposed as routes): `_components/`, `_lib/`

### `params` is a Promise in Next.js 15

All dynamic parameters must be awaited in Next.js 15:

```typescript
// app/blog/[slug]/page.tsx
type Props = {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ q?: string }>
}

export default async function BlogPost({ params, searchParams }: Props) {
  const { slug } = await params
  const { q } = await searchParams
  // ...
}

// In Client Components use React.use()
import { use } from 'react'

export default function ClientPage(props: Props) {
  const { slug } = use(props.params)
  // ...
}
```

## 2. Server vs Client Components — nuances

Core rules in `00-context.md`. This section covers Next.js-specific behavior only.

### Forbidden in Next.js 15

`ssr: false` cannot be used with `next/dynamic` inside Server Components:

```typescript
// Wrong: ssr: false inside a Server Component
const Chart = dynamic(() => import('./Chart'), { ssr: false }) // build error

// Correct: wrap in a Client Component
// components/ChartWrapper.tsx
'use client'
import dynamic from 'next/dynamic'

const Chart = dynamic(() => import('./Chart'), {
  ssr: false,
  loading: () => <Skeleton />,
})

export { Chart }
```

### Server + Client composition

```typescript
// Server Component passes data via props or children
export default async function Page() {
  const user = await getUser()
  return (
    <ClientShell>          {/* Client Component */}
      <UserCard user={user} />   {/* Server Component as children */}
    </ClientShell>
  )
}
```

## 3. Navigation

### `<Link>` (preferred for internal navigation)

```typescript
import Link from 'next/link'

// Static route
<Link href="/dashboard">Dashboard</Link>

// External link
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  External
</a>
```

### `useRouter` (Client Components only)

```typescript
'use client'
import { useRouter } from 'next/navigation'

const router = useRouter()
router.push('/dashboard')    // navigate
router.replace('/login')     // no history entry
router.refresh()             // refresh Server Component data
```

### `next/form` (new in Next.js 15)

```typescript
import Form from 'next/form'

// Extends <form>: client-side navigation, prefetches action URL
<Form action="/search">
  <input name="q" />
  <button type="submit">Search</button>
</Form>
```

## 4. Data Fetching

### Direct data access in Server Components

```typescript
// app/products/page.tsx
import { db } from '@/lib/db'

export default async function ProductsPage() {
  const products = await db.product.findMany()
  return <ProductList products={products} />
}
```

### `generateStaticParams` for static dynamic routes

```typescript
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await db.post.findMany({ select: { slug: true } })
  return posts.map((post) => ({ slug: post.slug }))
}
```

### Streaming with Suspense

```typescript
// app/dashboard/page.tsx
import { Suspense } from 'react'
import { UserCard, UserCardSkeleton } from '@/features/user/components/UserCard'
import { OrderList, OrderListSkeleton } from '@/features/orders/components/OrderList'

export default function Dashboard() {
  return (
    <>
      <Suspense fallback={<UserCardSkeleton />}>
        <UserCard />
      </Suspense>
      <Suspense fallback={<OrderListSkeleton />}>
        <OrderList />
      </Suspense>
    </>
  )
}
```

### Server Actions and client-side handling

The Action pattern is described in `00-context.md`. Here — `useActionState` only:

```typescript
// features/newsletter/actions.ts
'use server'
import { z } from 'zod'
import { revalidatePath } from 'next/cache'

const Schema = z.object({ email: z.string().email() })

export async function subscribeEmail(
  prevState: { error?: string; success?: boolean } | null,
  formData: FormData,
) {
  const parsed = Schema.safeParse({ email: formData.get('email') })
  if (!parsed.success) return { error: 'Invalid email' }

  await db.subscriber.create({ data: parsed.data })
  revalidatePath('/newsletter')
  return { success: true }
}
```

```typescript
// features/newsletter/components/SubscribeForm.tsx
'use client'
import { useActionState } from 'react'
import { subscribeEmail } from '../actions'

export function SubscribeForm() {
  const [state, action, isPending] = useActionState(subscribeEmail, null)

  return (
    <form action={action}>
      <input name="email" type="email" disabled={isPending} />
      {state?.error && <p>{state.error}</p>}
      <button type="submit" disabled={isPending}>
        {isPending ? 'Sending...' : 'Subscribe'}
      </button>
    </form>
  )
}
```

## 5. Performance

### `next/image`

```typescript
import Image from 'next/image'

// Always specify width + height, or fill + sizes
<Image src="/hero.jpg" alt="Hero" width={1200} height={600} />

// LCP image — priority is required
<Image src="/hero.jpg" alt="Hero" width={1200} height={600} priority />

// External sources — configure in next.config.ts
<Image src="https://cdn.example.com/photo.jpg" alt="Photo" fill sizes="100vw" />
```

### `next/font`

```typescript
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',   // required
})
```

### Dynamic import for heavy Client Components

```typescript
// Only inside a Client Component wrapper
'use client'
import dynamic from 'next/dynamic'

const HeavyChart = dynamic(() => import('./HeavyChart'), {
  loading: () => <Skeleton />,
  // ssr: false — only inside a Client Component
})
```

## 6. Partial Prerendering (PPR)

PPR is an experimental feature in Next.js 15. Not recommended for production.

Enable in `next.config.ts`:

```typescript
const nextConfig: NextConfig = {
  experimental: {
    ppr: 'incremental',  // not 'true' — only incremental in stable 15.x
  },
}
```

Enable for a specific route:

```typescript
// app/dashboard/page.tsx
import { Suspense } from 'react'
import { StaticContent } from '@/features/dashboard/components/StaticContent'
import { DynamicFeed } from '@/features/dashboard/components/DynamicFeed'

export const experimental_ppr = true  // opt-in for this segment

export default function Dashboard() {
  return (
    <>
      <StaticContent />
      <Suspense fallback={<Skeleton />}>
        <DynamicFeed />   {/* streamed dynamically */}
      </Suspense>
    </>
  )
}
```

`experimental_ppr = true` propagates to all child layouts and pages. No need to add it to every file.

## 7. View Transitions

Experimental feature. Enable in `next.config.ts`:

```typescript
const nextConfig: NextConfig = {
  experimental: {
    viewTransition: true,
  },
}
```

`<ViewTransition>` is imported directly from React — no third-party packages needed:

```typescript
import { ViewTransition } from 'react'
import Image from 'next/image'
import Link from 'next/link'

function PhotoGrid({ photos }: { photos: Photo[] }) {
  return (
    <div>
      {photos.map((photo) => (
        <Link key={photo.id} href={`/photo/${photo.id}`}>
          <ViewTransition name={`photo-${photo.id}`}>
            <Image src={photo.src} alt={photo.title} />
          </ViewTransition>
        </Link>
      ))}
    </div>
  )
}
```

## 8. Middleware

Edge Runtime by default. Node.js runtime became stable in Next.js 15.5:

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server'

export function middleware(request: NextRequest) {
  // logic
  return NextResponse.next()
}

export const config = {
  matcher: ['/dashboard/:path*', '/admin/:path*'],
  runtime: 'nodejs',  // stable since Next.js 15.5; omit for Edge Runtime
}
```

Rules for Middleware:

- No business logic or heavy computation
- No direct database access (Prisma etc.) in Edge Runtime
- Use only for auth token checks, redirects, and rewrites

## 9. Edge cases

### `error.tsx` — must be a Client Component

```typescript
'use client'
import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // log server-side, never expose stack trace to the user
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong</h2>
      <button onClick={reset}>Try again</button>
    </div>
  )
}
```

### `not-found.tsx`

```typescript
// In a Server Component, call notFound() from next/navigation
import { notFound } from 'next/navigation'

export default async function ProductPage({ params }: Props) {
  const { id } = await params
  const product = await getProduct(id)
  if (!product) notFound()
  // ...
}
```

## 10. `next.config.ts` configuration

```typescript
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'cdn.example.com' },
    ],
  },
  experimental: {
    ppr: 'incremental',       // PPR — incremental only in stable 15.x
    viewTransition: true,     // View Transitions API (experimental)
    // dynamicIO: true        // canary only, not in stable
  },
  eslint: { ignoreDuringBuilds: false },
  typescript: { ignoreBuildErrors: false },
  output: 'standalone',       // for Docker
}

export default nextConfig
```

## 11. Pre-commit checklist

- No unnecessary `'use client'`
- `params` and `searchParams` are awaited (they are Promises in Next.js 15)
- `ssr: false` in `next/dynamic` — only inside a Client Component
- All images use `next/image` with required dimensions
- Server Actions: Zod validation + `revalidatePath` / `revalidateTag`
- Routes with async data have `loading.tsx` or `<Suspense>`
- `generateStaticParams` implemented for static dynamic routes
- `tsc --noEmit` and `next lint` pass without errors

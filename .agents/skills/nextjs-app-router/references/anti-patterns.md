# Anti-Patterns

## Generic

- Business logic living directly in route special files
- Converting a route to client-side rendering without a real need
- Hidden data fetching inside leaf UI components
- Mixing unrelated refactors into a small route change
- Forcing a framework or styling migration inside a feature task

## Next.js 16 specific

- Accessing `params`, `searchParams`, `cookies()`, `headers()`, or `draftMode()`
  synchronously — all are async in v16 and must be awaited; synchronous access
  is a runtime error
- Using `cache: 'force-cache'` on `fetch()` — this is a v14 legacy pattern;
  use the `'use cache'` directive at function or component level in v16
- Calling `notFound()` inside a component wrapped by `<Suspense>` — causes the
  route to return HTTP 200 instead of 404, breaking SEO and crawler behavior
- Omitting `metadataBase` in the root layout when using relative paths for Open
  Graph images or canonical URLs — they are not resolved in production
- Placing a custom webpack config without the `--webpack` flag when running
  `next dev` or `next build` — Turbopack is the default bundler in v16 and
  silently ignores webpack configuration
- Marking `layout.tsx` or a large section `'use client'` when only a single leaf
  component requires interactivity — push `'use client'` to the leaf instead
- Leaving `middleware.ts` without migrating to `proxy.ts` — `middleware.ts` is
  deprecated in v16

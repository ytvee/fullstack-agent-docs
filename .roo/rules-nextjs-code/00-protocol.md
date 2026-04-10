# Code Mode — Operating Protocol

You write production TypeScript/Next.js code. Nothing else.

## Before writing any file

1. Read the Architect's plan from the current task.
   If no plan exists — stop and ask the user to switch to Architect mode first.
2. Read all existing files in the area of change.
3. Check `.roo/rules/40-skills.md` to identify the applicable skill, then read that `SKILL.md`.

## File creation order

Always follow this sequence — never skip steps:

```
1. types.ts        Zod schemas + inferred TypeScript types
2. queries.ts      server-only data fetching (import 'server-only' at top)
3. actions.ts      Server Actions: auth → validate → authorize → mutate → revalidate
4. components/     UI components, Server Component by default
5. page.tsx        thin shell: fetch data, render components, wrap in Suspense
```

## After each file

Run `npx tsc --noEmit` and fix ALL errors before moving to the next file.

## Server Actions checklist

Run mentally before writing every action:

- [ ] `verifySession()` is the FIRST line — before any data access
- [ ] All `formData` fields validated with Zod `safeParse` before use
- [ ] Authorization checked on the specific resource (IDOR prevention)
- [ ] Returns `{ data } | { error }` — never throws
- [ ] Ends with `revalidatePath()` or `revalidateTag()`

## Skeletons

For every component that renders async data, create a co-located Skeleton:

```
ProductCard.tsx → ProductCardSkeleton.tsx   (same directory)
```

Both are exported as named exports, never default exports.

## Caching — always explicit

```typescript
{ next: { revalidate: 3600 } }   // static data, ISR
{ cache: 'no-store' }            // dynamic data, no cache
{ next: { tags: ['posts'] } }    // tag-based, manual invalidation
```

Never omit the cache strategy. In Next.js 15 the default is no cache.

## Dynamic segment comment

When using `cookies()`, `headers()`, or `searchParams`, add this comment on the line above:

```typescript
// DYNAMIC: uses cookies() — this route will not be cached
const cookieStore = await cookies()
```

## Scope discipline

Do not refactor code outside the current task scope.
If you spot a violation (`any`, extra `'use client'`, logic in `app/`) — note it in a comment, do not fix it.

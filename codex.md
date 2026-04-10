# Project: Next.js 15+ App Router

## Stack

- Next.js 15+ App Router, React 19, TypeScript strict
- Tailwind CSS + Shadcn/ui
- Prisma ORM, Zod validation

## Architecture rules

- Business logic ONLY in src/features/[name]/
- src/app/ contains ONLY routing files
- Server Components by default — 'use client' only when needed
- Server Actions: verifySession() first, then Zod validation, then DB

## Code rules

- No `any`, no `@ts-ignore`
- All type-only imports use `import type`
- No console.log in production code
- After each file: run `npx tsc --noEmit`

## File creation order

1. types.ts — Zod schemas
2. queries.ts — server data fetching
3. actions.ts — Server Actions
4. components/ — UI
5. page.tsx — thin shell only

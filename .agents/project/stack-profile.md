# Stack Profile

This file is the repo-specific overlay for the current application.

## Framework

- Next.js `16.2.1` (App Router, Turbopack is the default bundler)
- React `19.2.4`
- Node.js `≥ 20.9` required (Next.js 16 dropped Node 18)

## Project Type

- Default classification: `frontend-only`
- No auth, database, Route Handlers, or Server Actions are present today

## Language and Tooling

- TypeScript with `strict: true`
- ESLint flat config
- Prettier as the single formatter
- Zod `^4.3.6` for boundary validation (v4 API — see `frontend-zod-schema` skill)

## Runtime Dependencies

- `date-fns ^4.1.0` — date formatting utilities
- `next-mdx-remote ^6.0.0` — MDX rendering
- `gray-matter ^4.0.3` — frontmatter parsing
- `server-only ^0.0.1` — enforces server-only module boundaries at build time

## Content and Data

- Filesystem-backed MDX content under `src/app/content/`
- Frontmatter schema and parser: `src/lib/mdx.ts`
- Reading time utility: `src/lib/readingTime.ts`
- Content listings: `src/features/posts/queries.ts`, `src/features/essays/queries.ts`

## Testing

- No dedicated test runner is configured
- Validation relies on TypeScript, ESLint, Prettier, and `next build`

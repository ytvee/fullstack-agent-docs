# Stack Profile

This file is the repo-specific overlay for the current application.

## Framework

- Next.js `16.2.1`
- App Router
- React `19`

## Project Type

- Default classification: `frontend-only`
- No auth, database, Route Handlers, or Server Actions are present today

## Language and Tooling

- TypeScript with `strict: true`
- ESLint flat config
- Prettier as the single formatter
- Zod available for boundary validation

## Content and Data

- Filesystem-backed MDX content under `src/app/content/`
- Frontmatter parsed in `src/lib/mdx.ts`
- Reading time utility in `src/lib/readingTime.ts`
- Content listings currently come from `src/features/*/queries.ts`

## Testing

- No dedicated test runner is configured
- Validation relies on TypeScript, ESLint, Prettier, and `next build`

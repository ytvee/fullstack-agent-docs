# Project Anti-Patterns

Treat the following as local anti-patterns unless the user explicitly asks for a
change in direction.

- Introducing Tailwind, shadcn/ui, or another styling stack into CSS Modules areas
- Putting business logic directly into `page.tsx`, `layout.tsx`, or other route files
- Converting Server Components to Client Components without a concrete need
- Using `any`, `@ts-ignore`, or untyped boundary parsing
- Fetching your own route handlers from server-side code when direct code access exists
- Hardcoding Figma-derived spacing, colors, or type styles when existing tokens cover them
- Refactoring unrelated files just because they are nearby

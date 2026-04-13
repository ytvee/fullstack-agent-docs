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
- Choosing terse or clever syntax over straightforward control flow when readability drops
- Using one-letter, cryptic, or over-abbreviated names outside narrow conventional cases
- Naming values with generic placeholders such as `data`, `value`, `item`, `obj`, `elem`, `str`, or `num` when a domain name exists
- Using visually similar names for different things, or mixing transliterated and English identifiers for the same concept
- Using multiple synonyms for the same behavior, or the same verb for different behavior, without a real semantic distinction
- Reusing the same variable name for different meanings within a function or reassigning parameters to unrelated values
- Shadowing outer-scope variables when a clearer local name would avoid ambiguity
- Adding `_` or `__` prefixes or suffixes without a consistent project-level meaning
- Naming symbols with decorative adjectives such as `super`, `mega`, or `nice` instead of concrete intent
- Giving query-style helpers such as `is*`, `has*`, `can*`, `check*`, or `find*` hidden side effects or non-obvious return shapes
- Combining multiple unrelated actions into one "power function" when separate helpers would keep the contract explicit

# AGENTS.md

This repository uses `AGENTS.md` as the repo entrypoint, `.agents/skills/` for
reusable workflows, and `.agents/project/` for repo-specific overlay docs.

## Inspect First

Before implementation work:

1. Read `AGENTS.md`.
2. Load the relevant skill from `.agents/skills/`.
3. Read the relevant project overlay docs from `.agents/project/`.
4. Read the affected source files and configs before changing anything.

Do not skip this order when the task changes code or project instructions.

## Project Classification

Default classification for this repository: `frontend-only`.

Why:

- Content-driven Next.js application
- No auth, database, Route Handlers, or Server Actions in the current app
- Primary work is routing, UI composition, MDX content rendering, and styling

Only switch to `fullstack` when the task introduces or modifies server-side
domain logic such as auth, persistence, protected mutations, backend validation,
Route Handlers, or Server Actions.

## React vs Next

- Use `nextjs-app-router` when the task touches routes, layouts, metadata,
  loading states, dynamic segments, or server/client boundaries in the app.
- Use `react-component-workflow` when the task is primarily component structure,
  props/state flow, hooks discipline, or reusable UI behavior not driven by
  Next.js routing concerns.
- Add `frontend-typescript-rules` for strict typing and safe refactors.
- Add `frontend-zod-schema` when the task parses or validates boundary input.
- End implementation work with `frontend-review-and-fix`.

## Stack Snapshot

- Next.js `16.2.1` with App Router
- React `19`
- TypeScript strict mode
- ESLint flat config
- Prettier
- CSS Modules plus global token CSS
- Zod for schema validation
- MDX content parsed with `gray-matter` and `next-mdx-remote`
- No test runner configured in `package.json`

If a prompt includes a Figma URL, use the built-in Figma capabilities before
implementing UI. Then adapt the design to the existing tokens, layout patterns,
and breakpoints documented in `.agents/project/figma-profile.md`.

## Code Style

- Prefer consistency with the current codebase over idealized refactors.
- Keep route files thin and focused on composition.
- Prefer Server Components by default; add `'use client'` only when needed.
- Use CSS Modules where the touched area already uses them.
- Do not introduce Tailwind, shadcn/ui, or a new styling system unless asked.
- No `any`, no `@ts-ignore`, and use `import type` for type-only imports.
- Avoid unrelated refactors while implementing the requested task.

## Validation Commands

Run relevant checks after implementation work:

1. `npx tsc --noEmit`
2. `npx eslint .`
3. `npx prettier --check .`
4. `npm run build` for structural Next.js changes

There is currently no test runner in `package.json`. Report that plainly instead
of inventing one.

## Skill Map

- Task classification and workflow routing -> `webapp-task-protocol`
- Next.js App Router work -> `nextjs-app-router`
- React component architecture and implementation -> `react-component-workflow`
- TypeScript rules and safe refactors -> `frontend-typescript-rules`
- Zod validation and boundary parsing -> `frontend-zod-schema`
- Review pass and verification -> `frontend-review-and-fix`
- Manual technical SEO audit/fixes -> `technical-seo-app`
- Manual security audit/reporting -> `frontend-security-inspector`
- Manual refresh of `.agents/project/*` docs -> `project-context-adapter`

This repo does not keep a content-authoring skill. For MDX/frontmatter rules,
use `src/app/content/README.md` and `src/lib/mdx.ts`.

## Project Overlay Docs

Use these files as the current repo profile:

- `.agents/project/stack-profile.md`
- `.agents/project/architecture-map.md`
- `.agents/project/styling-profile.md`
- `.agents/project/verification-profile.md`
- `.agents/project/anti-patterns.md`
- `.agents/project/figma-profile.md`

## Dev Workflow

- Branch names: `feat/*`, `fix/*`, `refactor/*`, `chore/*`
- Commits: Conventional Commit style, e.g. `feat(posts): add reading time`
- PRs:
    - Keep one concern per PR
    - Include a short validation summary
    - Use draft PRs until local checks pass
    - Do not mix unrelated cleanup into feature work

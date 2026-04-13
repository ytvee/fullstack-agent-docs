---
name: nextjs-app-router
description: Use when working on Next.js App Router routes, layouts, metadata,
    server/client boundaries, dynamic segments, and route-level UX states.
---

# Next.js App Router

## When to use

- Add or edit routes, layouts, loading states, or metadata
- Work with dynamic segments and static params
- Adjust server/client boundaries in a Next.js app
- Implement Figma-driven pages or sections inside a Next.js repository

## Required context

Before editing:

1. Read `AGENTS.md`.
2. Read `.agents/project/stack-profile.md` — framework version and project type.
3. Read `.agents/project/architecture-map.md` — route tree and shared code locations.
4. Read `.agents/project/anti-patterns.md` — project-specific patterns to avoid.
5. Read `.agents/project/styling-profile.md` — token system and styling conventions.
6. Read `.agents/project/figma-profile.md` — only when the task starts from design.

## Core rules

- Keep route special files focused on composition.
- Move reusable logic into helpers, feature modules, or shared code.
- Choose server/client boundaries intentionally; default to server-first.
- Derive metadata from validated or trusted data sources.
- Handle loading, error, and empty states intentionally.
- Reuse the project's existing styling system instead of introducing a new one.

## Figma

When a task starts from a Figma URL:

1. Use the built-in Figma capabilities first.
2. Inspect component structure, variables, spacing, and layout behavior.
3. Rebuild the UI with the repo's existing patterns, tokens, and breakpoints.
4. Avoid one-off hardcoded values when a reusable token or pattern fits.

## Reference map

- `references/route-patterns.md`
- `references/server-client-boundaries.md`
- `references/metadata-patterns.md`
- `references/anti-patterns.md`
- `references/figma-implementation.md`

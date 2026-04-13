---
name: webapp-task-protocol
description: Use to classify React and Next.js application tasks, detect project
    type, choose the right skill chain, and enforce inspect -> plan -> implement
    -> verify.
---

# Webapp Task Protocol

## When to use

- New feature work
- Refactors
- Bug fixes
- Code review or follow-up fixes
- SEO or security audits
- Design implementation tasks that may start from a Figma URL

## Required context order

1. Read `AGENTS.md`.
2. Read overlay files based on task type:
   - Always: `.agents/project/stack-profile.md`
   - Routing / layout / server-client work: `.agents/project/architecture-map.md`
   - Styling or design-driven work: `.agents/project/styling-profile.md`
   - Figma URL present: `.agents/project/figma-profile.md`
   - Any implementation work: `.agents/project/anti-patterns.md`
3. Read the affected source files and configuration files.
4. Then choose the skill chain.

## Routing workflow

1. Classify the task: `feature`, `refactor`, `bugfix`, `review`, or `audit`.
2. Detect the framework boundary:
    - Next.js routing/layout/metadata/server-client work -> `nextjs-app-router`
    - React component/state/hooks work -> `react-component-workflow`
3. Detect the project type:
    - `frontend-only`
    - `fullstack`
4. Add cross-cutting skills as needed:
    - `frontend-typescript-rules`
    - `frontend-zod-schema`
5. End implementation work with `frontend-review-and-fix`.

## Manual-only skills

- Use `technical-seo-app` only when the user explicitly asks for SEO work.
- Use `frontend-security-inspector` only when the user explicitly asks for a
  security audit.
- Use `project-context-adapter` only when the user asks to refresh or adapt the
  repo overlay docs.

## Figma trigger

If the prompt includes a Figma URL, node, or explicit design implementation
request:

1. Use the built-in Figma capabilities first.
2. Read `.agents/project/figma-profile.md`.
3. Continue implementation with the appropriate domain skill.

## Reference map

- `references/classification-rules.md`
- `references/task-routing.md`

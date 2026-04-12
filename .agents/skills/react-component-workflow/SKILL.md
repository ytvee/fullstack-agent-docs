---
name: react-component-workflow
description: Use when working on React component structure, props and state
    flow, hooks discipline, rendering logic, and reusable UI behavior.
---

# React Component Workflow

## When to use

- Build or refactor components
- Improve props, state, or render flow
- Split orchestration and presentation concerns
- Implement Figma-derived UI that is not primarily a routing task

## Required context

Before editing:

1. Read `AGENTS.md`.
2. Read `.agents/project/stack-profile.md`.
3. Read `.agents/project/architecture-map.md`.
4. Read `.agents/project/styling-profile.md`.
5. Read `.agents/project/figma-profile.md` when the work starts from design.

## Core rules

- Prefer small, focused components with one clear responsibility.
- Keep data flow explicit through props and clear ownership.
- Derive state when possible instead of duplicating it.
- Use effects only for true side effects, not for routine render logic.
- Reuse the established styling system and component patterns of the repo.

## Figma

When implementing from Figma:

1. Inspect the design first with the built-in Figma capabilities.
2. Recreate structure and responsive behavior with existing repo patterns.
3. Avoid hardcoded values when existing tokens or abstractions fit.

## Reference map

- `references/component-patterns.md`
- `references/hooks-rules.md`
- `references/anti-patterns.md`
- `references/figma-implementation.md`

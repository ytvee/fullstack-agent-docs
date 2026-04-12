---
name: project-context-adapter
description: Use only when explicitly requested to adapt the repo overlay docs to
    the current project without rewriting the reusable core skills.
---

# Project Context Adapter

## Mode

Manual only. Do not invoke unless the user explicitly asks to adapt or refresh
the repo overlay docs.

## Goal

Refresh the factual repo-specific documentation in `.agents/project/` so the
generic skills can be reused in this repository without embedding project
details inside the skills themselves.

## Required workflow

1. Read `AGENTS.md`.
2. Inspect the project:
    - `package.json`
    - `tsconfig.json`
    - ESLint and Prettier config
    - route tree
    - styling system
    - component structure
    - validation stack
3. Update only `.agents/project/*.md`.
4. Do not rewrite core reusable skills for repo-specific details.

## Outputs

- `stack-profile.md`
- `architecture-map.md`
- `styling-profile.md`
- `verification-profile.md`
- `anti-patterns.md`
- `figma-profile.md`

## Reference map

- `references/sync-procedure.md`
- `references/extraction-checklist.md`

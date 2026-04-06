# Project Context

## Repository Role

`fullstack-agent-docs` is a docs-only knowledge repository for RAG and coding agents working in a Next.js-centered fullstack stack. It is not an application, not a starter template, and not an automation-heavy build system. Its main job is to provide retrieval-friendly documentation plus a curated rules layer for AI-assisted engineering.

## Current Structure

- `knowledge/custom/` is the internal policy layer: architecture, patterns, antipatterns, linting, testing, security, performance, accessibility, SEO, DevOps, and agent rules.
- `knowledge/official/` is the upstream snapshot layer: Vercel, Next.js, React, React Hook Form, shadcn/ui, Tailwind CSS, Drizzle, Prisma, Resend, TypeScript, Zustand, and Vitest.
- `scripts/` contains source registries, metadata prompts, normalization utilities, and prompt files.
- `.vscode/` contains editor preferences only.
- `.codex` currently exists as an empty top-level control file.

## Primary Knowledge Corpus

- `knowledge/custom/`: 40 curated markdown documents across 11 sections.
- `knowledge/official/`: 4983 upstream markdown documents across 12 source families before generated context artifacts.
- Format heterogeneity is significant:
  - `vercel` is heavily normalized with rich frontmatter.
  - `vitest` is well split and uses lightweight `url` frontmatter.
  - `nextjs`, `typescript`, `drizzle`, `prisma`, and `zustand` are partially normalized.
  - `react`, `react-hook-form`, `shadcn`, `tailwindcss`, and much of `resend` are close to raw upstream export formats.

## Working-Tree State Notes

- The current root working tree contains `.codex`, `.gitignore`, `.vscode/`, `knowledge/`, and `scripts/`.
- Local version-control state reports `README.md` and `todo` as tracked deletions. They are relevant historical context, but they are not present in the current working tree.

## Source-of-Truth Rules

1. Real file contents and current working-tree structure come first.
2. `knowledge/custom/` defines project preferences and AI operating rules.
3. `knowledge/official/` defines upstream factual behavior for frameworks and tools.
4. `scripts/` explains ingestion, normalization, and metadata strategy.
5. Deleted tracked files matter as state discrepancies, not as active working-tree files.

## Recommended Starting Context For AI

1. Read `knowledge/custom/01-architecture`, `02-patterns`, and `11-agent-rules` first.
2. Use `knowledge/custom/06-security`, `07-performance`, `05-testing`, and `09-seo` as policy overlays.
3. Use `knowledge/official/nextjs`, `drizzle`, `vercel`, `vitest`, `typescript`, and `react` as primary upstream references.
4. Prefer split official files for retrieval precision and root aggregate files for source-wide orientation.

## Retrieval Guidance

- Use `knowledge/custom/*` first when the question is about preferred implementation style.
- Use `knowledge/official/*` first when the question is about exact framework or library behavior.
- Watch for aggregate-vs-split duplication in `vercel`, `nextjs`, `drizzle`, `prisma`, `resend`, `typescript`, `zustand`, and `react-hook-form`.
- Treat `guide.md` as the entrypoint for `knowledge/official/testing/vitest/`.

## Generated Context Artifacts

- This file provides the repository-wide context.
- Each relevant folder now has its own `FOLDER_CONTEXT.md` summarizing purpose, structure, and AI usage guidance.

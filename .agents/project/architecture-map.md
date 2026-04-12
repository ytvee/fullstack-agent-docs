# Architecture Map

Use this file to adapt generic skills to the current repository structure.

## Routing

- `src/app/` owns routes and Next.js special files
- Static sections currently include `about`, `posts`, `essays`, and `services`
- Dynamic content pages use `[slug]` segments under `posts` and `essays`

## Shared Code

- `src/components/` holds shared UI pieces such as header, footer, and loader
- `src/features/posts/queries.ts` and `src/features/essays/queries.ts` handle
  content collection reads
- `src/lib/` holds shared runtime helpers such as MDX parsing and reading time

## Current Data Flow

- Route files compose page UI and call server-side query helpers
- MDX files are parsed from the filesystem rather than fetched from an API
- Listing pages sort content by date and filter on `published`

## Guidance for Changes

- Prefer keeping logic out of route special files when a helper or feature module
  already owns that concern
- Reuse the existing `src/features/*/queries.ts` pattern for content reads
- Add new shared runtime helpers to `src/lib/` unless the touched area already
  follows a different local convention

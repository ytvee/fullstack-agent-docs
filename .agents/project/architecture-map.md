# Architecture Map

Use this file to adapt generic skills to the current repository structure.

## Routing

- `src/app/` owns routes and Next.js special files
- Static sections: `about`, `posts`, `essays`, `services`
- Dynamic content pages use `[slug]` segments under `posts` and `essays`

## Shared UI Components

- `src/components/header/Header.tsx` — server shell; imports `HeaderNavigation`
- `src/components/header/HeaderNavigation.tsx` — client component (`'use client'`);
  owns `usePathname`, mobile menu `useState`, and active-link logic
- `src/components/footer/Footer.tsx` — server shell; imports `FooterCopyEmail`
- `src/components/footer/FooterCopyEmail.tsx` — client component (`'use client'`);
  owns clipboard copy logic, timeout cleanup, and toast state
- `src/components/loader/Loader.tsx` — named export `Loader`; used in loading files

## Shared Code

- `src/lib/mdx.ts` — frontmatter Zod schema, `parseMdxFile`, `getContentPath`,
  `formatMdxDate`; imports `server-only`
- `src/lib/readingTime.ts` — `calculateReadingTime(content, wpm?)` utility
- `src/styles/tokens/` — global CSS custom properties (colors, typography)

## Feature Modules

- `src/features/posts/queries.ts` — `getPosts`, `getPostBySlug`, `getAllPostSlugs`
- `src/features/essays/queries.ts` — `getEssays`, `getEssayBySlug`, `getAllEssaySlugs`

## Current Data Flow

- Route files compose page UI and call server-side query helpers
- MDX files are parsed from the filesystem; no external API or database
- Listing pages filter on `published: true` and sort by date descending
- Parse errors in content files surface as thrown exceptions (not silent skips)

## Guidance for Changes

- Keep logic out of route special files — delegate to helpers or feature modules
- Reuse `src/features/*/queries.ts` pattern for content reads
- Add new shared runtime utilities to `src/lib/`
- Keep client-side interactivity isolated in leaf client components;
  do not mark parent layouts or server shells as `'use client'`

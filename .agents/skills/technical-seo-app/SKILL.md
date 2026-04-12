---
name: technical-seo-app
description: Use only when explicitly requested to audit or improve technical SEO
    in a React or Next.js application.
---

# Technical SEO App

## Mode

Manual only. Do not invoke unless the user explicitly asks for SEO work.

## Default workflow

1. Audit the current metadata and crawlability setup.
2. Compare current behavior with the affected routes or pages.
3. Report one of:
    - everything is already aligned, or
    - concrete SEO risks and recommended fixes
4. Apply fixes only when the user asks for implementation.

## Scope

- titles and descriptions
- canonical URLs
- robots and sitemap behavior
- Open Graph / social metadata
- crawlability and indexability
- structured data when appropriate

## Reference map

- `references/metadata-rules.md`
- `references/crawling-indexing.md`
- `references/structured-data.md`

---
name: frontend-zod-schema
description: Use when validating boundary input with Zod in React or Next.js
    apps, including forms, search params, config parsing, and payload validation.
---

# Frontend Zod Schema

## When to use

- Search params
- Form submissions
- Config parsing
- Route or action payload validation
- Schema-driven typing at input boundaries

## Core rules

- Treat user or external input as untrusted.
- Define the schema and inferred type together.
- Use `safeParse` where invalid input is expected.
- Normalize input at the boundary instead of scattering coercion downstream.

## Reference map

- `references/schema-patterns.md`
- `references/boundary-validation.md`

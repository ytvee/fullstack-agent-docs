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

## Zod version

This project uses **Zod v4**. Key v4 differences from v3:

- Error customization uses a single unified `error` parameter instead of the
  separate `message`, `invalid_type_error`, `required_error`, and `errorMap`
  options from v3.
- `z.input<typeof schema>` and `z.output<typeof schema>` are the correct way to
  get the pre-transform and post-transform types when a schema uses `.transform()`.
- `z.discriminatedUnion()` now supports nested unions and pipes.
- `.brand()` adds nominal typing to a schema output.
- New top-level format helpers: `z.email()`, `z.uuid()`, `z.url()`.
- `z.literal([200, 201, 202])` accepts an array for multiple literal values.

## Reference map

- `references/schema-patterns.md`
- `references/boundary-validation.md`

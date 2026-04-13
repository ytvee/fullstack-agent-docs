# Schema Patterns

## Core patterns

- Export the schema and inferred type together.
- Use coercion only where stringly typed input actually exists (e.g. query params,
  form fields that always arrive as strings).
- Use transforms for normalization (trimming, lowercasing, date parsing).
- Use refinements for cross-field rules that cannot be expressed structurally.

## Input vs output types

When a schema includes `.transform()`, the inferred type differs before and after
the transform. Use the correct helper to avoid type mismatches:

```ts
const DateSchema = z.string().transform((s) => new Date(s))

type DateInput  = z.input<typeof DateSchema>   // string
type DateOutput = z.output<typeof DateSchema>  // Date
```

Always use `z.infer<typeof Schema>` only when there is no transform. With
transforms, prefer `z.input<>` / `z.output<>` explicitly.

## Discriminated unions

Use `z.discriminatedUnion()` when objects share a discriminant field:

```ts
const EventSchema = z.discriminatedUnion('type', [
    z.object({ type: z.literal('click'), x: z.number(), y: z.number() }),
    z.object({ type: z.literal('keydown'), key: z.string() }),
])
```

In Zod v4, `discriminatedUnion` supports nested unions and pipes.

## Nominal typing with `.brand()`

Use `.brand()` to create types that are structurally identical but
semantically distinct:

```ts
const UserId = z.string().brand('UserId')
type UserId = z.infer<typeof UserId>
// UserId is a string, but not assignable from a plain string without parsing
```

## Error customization (Zod v4)

Use the unified `error` parameter instead of the v3-style separate options:

```ts
// v4
z.string().min(1, { error: 'Required' })

// v3 (do not use in this project)
z.string().min(1, { message: 'Required' })
```

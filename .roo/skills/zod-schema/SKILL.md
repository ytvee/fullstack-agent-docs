---
name: zod-schema
description: Creates Zod validation schemas and infers TypeScript types for Next.js applications. Handles form data validation, search params coercion, Server Action error handling with safeParse, and environment variable schemas. Triggers on requests like "validate form data", "parse search params", "add Zod schema", "validate Server Action input", "type-safe env vars", "validate query string", "schema for form".
---

## Base pattern

Always define the schema and infer the TypeScript type together. The type is derived from the schema, never defined separately:

```typescript
import { z } from 'zod'

export const PostFilterSchema = z.object({
  tag: z.string().optional(),
  page: z.coerce.number().int().positive().default(1),
})

export type PostFilter = z.infer<typeof PostFilterSchema>
```

Install: `npm install zod`

## Search params (query strings)

URL search params arrive as strings regardless of intended type. Use `z.coerce` to convert:

```typescript
export const BlogSearchParamsSchema = z.object({
  q: z.string().min(1).max(100).optional(),
  page: z.coerce.number().int().positive().default(1),
  tag: z.string().optional(),
  sort: z.enum(['date', 'title']).default('date'),
})

export type BlogSearchParams = z.infer<typeof BlogSearchParamsSchema>
```

Use in a Server Component page:

```typescript
export default async function BlogPage({
  searchParams,
}: {
  searchParams: Promise<Record<string, string | string[] | undefined>>
}) {
  const params = BlogSearchParamsSchema.parse(await searchParams)
  // params.page is number, params.sort is 'date' | 'title'
}
```

`z.coerce.number()` calls `Number()` on the value. An empty string becomes `0`, which may fail `.positive()` — this is usually the correct behavior for pagination.

## Form data

`formData.get()` returns `FormDataEntryValue | null`. Zod coerces `null` to a string, so validate presence explicitly:

```typescript
export const ContactFormSchema = z.object({
  email: z.string().email('Invalid email address'),
  subject: z.string().min(3).max(100),
  message: z.string().min(10, 'Message must be at least 10 characters').max(1000),
})

export type ContactForm = z.infer<typeof ContactFormSchema>
```

Server Action:

```typescript
'use server'
import { ContactFormSchema } from '@/lib/schemas'

export async function submitContact(formData: FormData) {
  const parsed = ContactFormSchema.safeParse({
    email: formData.get('email'),
    subject: formData.get('subject'),
    message: formData.get('message'),
  })

  if (!parsed.success) {
    return { error: parsed.error.flatten() }
  }

  // parsed.data is fully typed
  await sendEmail(parsed.data)
  return { success: true }
}
```

## safeParse vs parse

**`safeParse`** — returns `{ success: true, data } | { success: false, error }`. Never throws. Use in:
- Server Actions (caller handles error response)
- Route Handlers (return 400 response on failure)
- Any boundary where invalid input is an expected condition

**`parse`** — throws `ZodError` on failure. Use in:
- Utility functions where invalid input is a developer bug
- Application startup (environment variable validation)
- Tests

## Handling errors in the UI

`parsed.error.flatten()` shapes errors for form display:

```typescript
// Shape returned by flatten():
{
  formErrors: string[],      // object-level errors (from .refine())
  fieldErrors: {
    email: string[],
    subject: string[],
    message: string[],
  }
}
```

In a React component with `useActionState`:

```typescript
'use client'
import { useActionState } from 'react'
import { submitContact } from '@/actions/contact'

export function ContactForm() {
  const [state, action] = useActionState(submitContact, null)

  return (
    <form action={action}>
      <input name="email" />
      {state?.error?.fieldErrors.email?.map((err) => (
        <p key={err} className="text-red-500 text-sm">{err}</p>
      ))}
      <button type="submit">Send</button>
    </form>
  )
}
```

## Useful methods

```typescript
// .transform() — modify data after validation
const SlugSchema = z.string().transform((val) => val.toLowerCase().replace(/\s+/g, '-'))

// .refine() — custom validation with error message
const PasswordSchema = z.string().refine(
  (val) => /[A-Z]/.test(val),
  { message: 'Password must contain at least one uppercase letter' }
)

// .default() — value when field is absent
const PaginationSchema = z.object({
  page: z.coerce.number().default(1),
  limit: z.coerce.number().max(100).default(20),
})

// .optional() — field may be absent (undefined)
// .nullable() — field may be null
// .nullish() — field may be null or undefined

// z.enum() — strict union of string literals
const SortSchema = z.enum(['asc', 'desc'])
type Sort = z.infer<typeof SortSchema>  // 'asc' | 'desc'

// z.union() — one of several schemas
const IdSchema = z.union([z.string().uuid(), z.number().int().positive()])

// z.array() — typed arrays
const TagsSchema = z.array(z.string()).min(1).max(10)

// z.discriminatedUnion() — union with a discriminant field
const ActionSchema = z.discriminatedUnion('type', [
  z.object({ type: z.literal('create'), title: z.string() }),
  z.object({ type: z.literal('delete'), id: z.string().uuid() }),
])
```

## Schema composition

```typescript
const BasePostSchema = z.object({
  title: z.string().min(1).max(200),
  description: z.string().max(500),
  tags: z.array(z.string()).default([]),
})

// Extend with additional fields
const CreatePostSchema = BasePostSchema.extend({
  content: z.string().min(1),
  published: z.boolean().default(false),
})

// Pick a subset
const PostPreviewSchema = BasePostSchema.pick({
  title: true,
  description: true,
})

// Omit fields
const PostUpdateSchema = CreatePostSchema.omit({ published: true }).partial()
```

See [docs/patterns.md](docs/patterns.md) for environment variable schemas and advanced patterns.

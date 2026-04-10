# Zod advanced patterns

## Environment variables

Validate all environment variables at startup in `src/lib/env.ts`. This fails the build immediately if a required variable is missing, rather than causing runtime errors in production.

```typescript
import { z } from 'zod'

const EnvSchema = z.object({
  // Node
  NODE_ENV: z.enum(['development', 'production', 'test']).default('development'),

  // App
  NEXT_PUBLIC_APP_URL: z.string().url(),

  // External services
  DATABASE_URL: z.string().url().optional(),
  RESEND_API_KEY: z.string().startsWith('re_'),
  STRIPE_SECRET_KEY: z.string().startsWith('sk_'),

  // Optional with defaults
  LOG_LEVEL: z.enum(['debug', 'info', 'warn', 'error']).default('info'),
})

export const env = EnvSchema.parse(process.env)
```

Import `env` instead of accessing `process.env` directly:

```typescript
// Correct
import { env } from '@/lib/env'
console.log(env.RESEND_API_KEY)

// Wrong — no validation, no type safety
process.env.RESEND_API_KEY
```

For `NEXT_PUBLIC_*` variables, ensure they are in the schema. Next.js inlines them at build time.

## Nested objects

```typescript
const UserProfileSchema = z.object({
  name: z.string().min(1).max(100),
  address: z.object({
    street: z.string(),
    city: z.string(),
    country: z.string().length(2),  // ISO country code
  }),
  preferences: z.object({
    newsletter: z.boolean().default(false),
    theme: z.enum(['light', 'dark', 'system']).default('system'),
  }).optional(),
})
```

## Arrays with validation

```typescript
const TagListSchema = z.array(
  z.string().min(1).max(30).regex(/^[a-z0-9-]+$/, 'Only lowercase letters, numbers and hyphens')
).min(1, 'At least one tag required').max(5, 'Maximum 5 tags')

// Tuple — fixed length array with typed positions
const CoordinateSchema = z.tuple([
  z.number().min(-180).max(180),  // longitude
  z.number().min(-90).max(90),    // latitude
])
```

## Discriminated unions

Use when objects share a `type` field. More efficient than `z.union()` and produces better error messages:

```typescript
const NotificationSchema = z.discriminatedUnion('type', [
  z.object({
    type: z.literal('email'),
    to: z.string().email(),
    subject: z.string(),
    body: z.string(),
  }),
  z.object({
    type: z.literal('sms'),
    to: z.string().regex(/^\+[1-9]\d{1,14}$/),
    body: z.string().max(160),
  }),
  z.object({
    type: z.literal('push'),
    deviceToken: z.string(),
    title: z.string(),
    body: z.string(),
  }),
])

type Notification = z.infer<typeof NotificationSchema>
```

## Cross-field validation with .refine()

```typescript
const DateRangeSchema = z.object({
  startDate: z.string().date(),
  endDate: z.string().date(),
}).refine(
  (data) => data.endDate >= data.startDate,
  {
    message: 'End date must be after start date',
    path: ['endDate'],  // attach error to endDate field
  }
)

const PasswordConfirmSchema = z.object({
  password: z.string().min(8),
  confirmPassword: z.string(),
}).refine(
  (data) => data.password === data.confirmPassword,
  {
    message: 'Passwords do not match',
    path: ['confirmPassword'],
  }
)
```

## Transforming data

```typescript
// Parse a comma-separated tag string from query params
const TagQuerySchema = z.string()
  .optional()
  .transform((val) => val ? val.split(',').map((t) => t.trim()).filter(Boolean) : [])

// Normalize whitespace in user input
const NameSchema = z.string()
  .transform((val) => val.trim().replace(/\s+/g, ' '))
  .pipe(z.string().min(1).max(100))

// Convert string date to Date object
const DateSchema = z.string().date().transform((val) => new Date(val))
```

## Reusing schemas across boundaries

```typescript
// src/lib/schemas/post.ts

// Database shape
export const PostDBSchema = z.object({
  id: z.string().uuid(),
  title: z.string(),
  content: z.string(),
  published: z.boolean(),
  createdAt: z.date(),
  updatedAt: z.date(),
  authorId: z.string().uuid(),
})

// API input — subset of fields, no server-generated fields
export const CreatePostInputSchema = PostDBSchema.pick({
  title: true,
  content: true,
}).extend({
  published: z.boolean().default(false),
  tags: z.array(z.string()).default([]),
})

// Update — all fields optional except id
export const UpdatePostInputSchema = PostDBSchema
  .pick({ id: true })
  .merge(CreatePostInputSchema.partial())

// Public API response — omit internal fields
export const PostResponseSchema = PostDBSchema.omit({
  authorId: true,
}).extend({
  tags: z.array(z.string()),
})

export type Post = z.infer<typeof PostDBSchema>
export type CreatePostInput = z.infer<typeof CreatePostInputSchema>
export type UpdatePostInput = z.infer<typeof UpdatePostInputSchema>
export type PostResponse = z.infer<typeof PostResponseSchema>
```

## Route Handler validation

```typescript
// src/app/api/posts/route.ts
import { NextResponse } from 'next/server'
import { CreatePostInputSchema } from '@/lib/schemas/post'

export async function POST(request: Request) {
  const body = await request.json().catch(() => null)

  if (body === null) {
    return NextResponse.json({ error: 'Invalid JSON' }, { status: 400 })
  }

  const parsed = CreatePostInputSchema.safeParse(body)

  if (!parsed.success) {
    return NextResponse.json(
      { error: parsed.error.flatten() },
      { status: 422 }
    )
  }

  // parsed.data is typed as CreatePostInput
  const post = await createPost(parsed.data)
  return NextResponse.json(post, { status: 201 })
}
```

## Async validation with .refineAsync()

Use for database uniqueness checks or external API validation:

```typescript
const UniqueEmailSchema = z.string().email().refineAsync(
  async (email) => {
    const exists = await checkEmailExists(email)
    return !exists
  },
  { message: 'Email already registered' }
)

// Must use parseAsync / safeParseAsync
const result = await UniqueEmailSchema.safeParseAsync(email)
```

---
category: security
topic: server-action-validation
status: draft
---

## Проблема / Контекст

Server Actions are `POST` requests under the hood. Any client — including `curl`, Postman, or a malicious browser extension — can call them directly, bypassing all client-side validation. The Next.js framework provides no automatic validation layer. Without explicit server-side validation, a Server Action is an unauthenticated, unvalidated HTTP endpoint.

The validation stack for every mutating Server Action must be: **Auth check → Zod parse → Ownership check → DB write → Typed return**.

---

## Решение

### The validation pipeline in order

1. **Authentication** — is there a session? Return early if not.
2. **Zod validation** — parse and coerce input. Return `fieldErrors` if invalid.
3. **Authorization / Ownership** — does this user own the resource they're mutating?
4. **Rate limiting** — prevent brute force and spam.
5. **Business logic** — the actual DB operation.
6. **Typed Result return** — never throw to the client.

### Typed Result pattern

```typescript
// src/lib/action-result.ts
export type ActionResult<T = void> =
  | { success: true; data: T }
  | { success: false; error: string; fieldErrors?: Record<string, string[]> };

export function ok<T>(data: T): ActionResult<T> {
  return { success: true, data };
}

export function err(
  message: string,
  fieldErrors?: Record<string, string[]>
): ActionResult<never> {
  return { success: false, error: message, fieldErrors };
}
```

### Full validation example — createPost Server Action

```typescript
// src/actions/post.ts
"use server";

import { z } from "zod";
import { auth } from "@/auth";
import { db } from "@/db";
import { posts } from "@/db/schema";
import { ok, err, type ActionResult } from "@/lib/action-result";
import { checkRateLimit } from "@/lib/rate-limit";
import { revalidatePath } from "next/cache";

const createPostSchema = z.object({
  title: z
    .string()
    .min(3, "Title must be at least 3 characters")
    .max(200, "Title must be under 200 characters")
    .trim(),
  content: z
    .string()
    .min(10, "Content must be at least 10 characters")
    .max(50_000, "Content too long")
    .trim(),
  published: z.boolean().default(false),
});

type CreatePostInput = z.infer<typeof createPostSchema>;

export async function createPost(
  input: unknown // Accept unknown — Zod will validate
): Promise<ActionResult<{ id: string; slug: string }>> {
  // Step 1: Authentication
  const session = await auth();
  if (!session?.user?.id) {
    return err("Unauthorized");
  }

  // Step 2: Rate limiting (5 posts per minute per user)
  const rateLimitResult = await checkRateLimit(`create-post:${session.user.id}`, {
    limit: 5,
    windowMs: 60_000,
  });
  if (!rateLimitResult.allowed) {
    return err("Too many requests. Please wait before creating another post.");
  }

  // Step 3: Zod validation — parse unknown input
  const parsed = createPostSchema.safeParse(input);
  if (!parsed.success) {
    return err("Validation failed", parsed.error.flatten().fieldErrors);
  }

  const { title, content, published } = parsed.data;

  // Step 4: Sanitize for XSS if content will be rendered as HTML
  // (If using a markdown renderer, sanitize the rendered HTML output instead)
  // const sanitizedContent = DOMPurify.sanitize(content, { ALLOWED_TAGS: [] });

  // Step 5: DB write
  try {
    const [post] = await db.insert(posts).values({
      title,
      content,
      published,
      authorId: session.user.id, // always set from session, never from input
      createdAt: new Date(),
    }).returning({ id: posts.id, slug: posts.slug });

    revalidatePath("/posts");
    return ok({ id: post.id, slug: post.slug });
  } catch (error) {
    // Log to Sentry but return a generic message — never leak DB errors to client
    console.error("[createPost] DB error:", error);
    return err("Failed to create post. Please try again.");
  }
}
```

### Ownership verification — updatePost

```typescript
// src/actions/post.ts (continued)

const updatePostSchema = z.object({
  postId: z.string().uuid("Invalid post ID"),
  title: z.string().min(3).max(200).trim().optional(),
  content: z.string().min(10).max(50_000).trim().optional(),
  published: z.boolean().optional(),
});

export async function updatePost(
  input: unknown
): Promise<ActionResult<{ id: string }>> {
  const session = await auth();
  if (!session?.user?.id) return err("Unauthorized");

  const parsed = updatePostSchema.safeParse(input);
  if (!parsed.success) return err("Validation failed", parsed.error.flatten().fieldErrors);

  const { postId, ...updates } = parsed.data;

  // Ownership check: fetch the post and verify authorId
  const existing = await db.query.posts.findFirst({
    where: and(
      eq(posts.id, postId),
      // Admins can edit any post; regular users only their own
      session.user.role === "admin"
        ? undefined
        : eq(posts.authorId, session.user.id)
    ),
    columns: { id: true, authorId: true },
  });

  if (!existing) {
    // Return "Not found" — don't reveal whether the post exists but belongs to someone else
    return err("Post not found");
  }

  await db.update(posts).set({ ...updates, updatedAt: new Date() }).where(eq(posts.id, postId));

  revalidatePath(`/posts/${postId}`);
  return ok({ id: postId });
}
```

### Rate limiting with Upstash Redis

```typescript
// src/lib/rate-limit.ts
import { Ratelimit } from "@upstash/ratelimit";
import { Redis } from "@upstash/redis";

// Initialize once at module level — the client is stateless
const redis = Redis.fromEnv();

const limiters = new Map<string, Ratelimit>();

function getLimiter(key: string, limit: number, windowMs: number): Ratelimit {
  const cacheKey = `${limit}:${windowMs}`;
  if (!limiters.has(cacheKey)) {
    limiters.set(
      cacheKey,
      new Ratelimit({
        redis,
        limiter: Ratelimit.slidingWindow(limit, `${windowMs}ms`),
        analytics: true,
        prefix: "rl",
      })
    );
  }
  return limiters.get(cacheKey)!;
}

export async function checkRateLimit(
  identifier: string,
  options: { limit: number; windowMs: number }
): Promise<{ allowed: boolean; remaining: number; resetAt: Date }> {
  if (process.env.NODE_ENV === "test") {
    return { allowed: true, remaining: 999, resetAt: new Date() };
  }

  const limiter = getLimiter(identifier, options.limit, options.windowMs);
  const { success, remaining, reset } = await limiter.limit(identifier);

  return {
    allowed: success,
    remaining,
    resetAt: new Date(reset),
  };
}
```

### Simple in-memory rate limiter for development / low-traffic

```typescript
// src/lib/rate-limit-memory.ts
// Use this only for low-traffic apps or when Upstash is not available.
// Does NOT work correctly across multiple server instances (serverless).

interface RateLimitEntry {
  count: number;
  resetAt: number;
}

const store = new Map<string, RateLimitEntry>();

export function checkRateLimitMemory(
  key: string,
  limit: number,
  windowMs: number
): { allowed: boolean; remaining: number } {
  const now = Date.now();
  const entry = store.get(key);

  if (!entry || now > entry.resetAt) {
    store.set(key, { count: 1, resetAt: now + windowMs });
    return { allowed: true, remaining: limit - 1 };
  }

  if (entry.count >= limit) {
    return { allowed: false, remaining: 0 };
  }

  entry.count++;
  return { allowed: true, remaining: limit - entry.count };
}
```

### CSRF considerations

```typescript
// Next.js 15 Server Actions are protected against CSRF by default:
// - They only accept POST requests
// - They include an Origin header check for same-origin requests
// - next-csrf is NOT needed for Server Actions called from Next.js <form> or useTransition

// When you DO need extra CSRF protection:
// 1. Route Handlers accepting cross-origin POST requests
// 2. Server Actions called from external services
// 3. Older browsers that send cookies cross-origin

// For Route Handlers that must accept cross-origin requests:
// src/app/api/webhook/stripe/route.ts
export async function POST(request: Request) {
  // Stripe signs its webhooks — verify the signature instead of CSRF token
  const signature = request.headers.get("stripe-signature");
  if (!signature) return new Response("No signature", { status: 400 });

  const body = await request.text();
  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(body, signature, process.env.STRIPE_WEBHOOK_SECRET!);
  } catch {
    return new Response("Invalid signature", { status: 400 });
  }
  // process event...
}
```

### Input sanitization helper

```typescript
// src/lib/sanitize.ts
import DOMPurify from "isomorphic-dompurify";

// Strip all HTML from text fields
export function sanitizeText(input: string): string {
  return DOMPurify.sanitize(input, { ALLOWED_TAGS: [], ALLOWED_ATTR: [] });
}

// Allow limited safe HTML for rich text fields
export function sanitizeRichText(html: string): string {
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ["p", "br", "b", "i", "em", "strong", "ul", "ol", "li", "a", "h2", "h3"],
    ALLOWED_ATTR: ["href", "target", "rel"],
    FORCE_BODY: true,
    ADD_ATTR: ["rel"], // force rel="noopener noreferrer" on all links
    FORBID_ATTR: ["style", "class", "id"],
  });
}
```

---

## Антипаттерн

```typescript
// BAD 1: Trusting client-validated data without re-validating on server
export async function createOrder(validatedData: OrderData) {
  // validatedData came from client — treat it as unknown
  const session = await auth();
  await db.insert(orders).values({ ...validatedData, userId: validatedData.userId }); // ← userId from client!
}

// BAD 2: Throwing errors that bubble to the client
export async function deletePost(postId: string) {
  const session = await auth();
  if (!session) throw new Error("Unauthorized"); // ← React renders "Error: Unauthorized" on client
  // DB errors thrown here expose schema details
  await db.delete(posts).where(eq(posts.id, postId));
}

// BAD 3: Accepting typed input (bypasses Zod for extra fields / coercion attacks)
export async function updateProfile(input: ProfileData) { // ← input is already "typed", right?
  // An attacker passes { role: "admin" } — TypeScript types don't exist at runtime!
  await db.update(users).set(input).where(eq(users.id, session.user.id)); // ← privilege escalation
}

// GOOD: Always parse unknown, always return typed Result
export async function updateProfile(input: unknown): Promise<ActionResult<void>> {
  const session = await auth();
  if (!session?.user?.id) return err("Unauthorized");

  const parsed = profileSchema.safeParse(input);
  if (!parsed.success) return err("Validation failed", parsed.error.flatten().fieldErrors);

  // Only update fields that the schema allows — no role, no id, no email
  await db.update(users)
    .set({ displayName: parsed.data.displayName, bio: parsed.data.bio })
    .where(eq(users.id, session.user.id));

  return ok(undefined);
}
```

---

## Связанные документы

- `knowledge/custom/06-security/owasp-nextjs.md` — OWASP Top 10 overview
- `knowledge/custom/06-security/auth-security.md` — Auth.js v5 hardening
- `knowledge/custom/02-patterns/server-actions.md` — Server Action patterns
- `knowledge/custom/05-testing/test-strategy.md` — integration tests for Server Actions

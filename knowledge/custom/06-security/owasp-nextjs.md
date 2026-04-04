---
category: security
topic: owasp-nextjs
status: draft
---

## Проблема / Контекст

The OWASP Top 10 is the canonical checklist of the most critical web application security risks. Next.js 15 App Router changes *where* code runs (server vs. client) in ways that affect how each OWASP category manifests. A Server Action that fetches data based on an unchecked user ID is a Broken Access Control bug even though it looks like a harmless server function. This document maps each relevant OWASP category to concrete Next.js patterns and provides real mitigation code.

---

## Решение

### A01 — Broken Access Control

**In Next.js App Router:** Server Actions and Route Handlers execute on the server but receive user-supplied input. The most common mistake is fetching by ID without verifying the requesting user *owns* that resource.

```typescript
// src/actions/order.ts
"use server";

import { auth } from "@/auth";
import { db } from "@/db";
import { orders } from "@/db/schema";
import { eq, and } from "drizzle-orm";

// BAD — fetches order by ID without ownership check
// Any authenticated user can see any order by guessing the ID
export async function getOrderBad(orderId: string) {
  const session = await auth();
  if (!session) return { error: "Unauthorized" };

  const order = await db.query.orders.findFirst({
    where: eq(orders.id, orderId), // ← IDOR vulnerability
  });
  return { data: order };
}

// GOOD — always add ownership condition to the WHERE clause
export async function getOrder(orderId: string) {
  const session = await auth();
  if (!session?.user?.id) return { error: "Unauthorized" };

  const order = await db.query.orders.findFirst({
    where: and(
      eq(orders.id, orderId),
      eq(orders.userId, session.user.id) // ← ownership enforced at DB level
    ),
  });

  if (!order) return { error: "Not found" }; // same message for not-found and forbidden
  return { data: order };
}
```

**Admin-only routes** — protect at both middleware AND action level:

```typescript
// src/middleware.ts
import { auth } from "@/auth";
import { NextResponse } from "next/server";

export default auth((req) => {
  const isAdmin = req.auth?.user?.role === "admin";
  const isAdminRoute = req.nextUrl.pathname.startsWith("/admin");

  if (isAdminRoute && !isAdmin) {
    return NextResponse.redirect(new URL("/", req.url));
  }
});

// src/actions/admin.ts — double-check even though middleware exists
// Middleware can be bypassed if someone calls the action directly
export async function deleteUser(userId: string) {
  const session = await auth();
  if (session?.user?.role !== "admin") {
    return { error: "Forbidden" };
  }
  // ...
}
```

---

### A02 — Cryptographic Failures

**Passwords:** Auth.js v5 Credentials provider handles hashing, but if you implement custom auth you must use bcrypt.

```typescript
// src/lib/password.ts
import bcrypt from "bcryptjs";

const SALT_ROUNDS = 12; // 12 is the current recommended minimum

export async function hashPassword(plain: string): Promise<string> {
  return bcrypt.hash(plain, SALT_ROUNDS);
}

export async function verifyPassword(plain: string, hashed: string): Promise<boolean> {
  return bcrypt.compare(plain, hashed);
}

// NEVER do this:
// const stored = sha256(password)  — not a KDF, trivially reversed with rainbow tables
// const stored = md5(password)     — broken, collision attacks exist
// const stored = password          — plaintext, catastrophic on DB breach
```

**Sensitive tokens:** use `crypto.randomBytes` for password reset and email verification tokens.

```typescript
// src/lib/tokens.ts
import crypto from "crypto";

export function generateSecureToken(bytes: number = 32): string {
  return crypto.randomBytes(bytes).toString("hex"); // 64 hex chars = 256-bit entropy
}

// Store the HASH of the token in the DB, not the token itself
// This way a DB breach doesn't give attackers valid tokens
export async function hashToken(token: string): Promise<string> {
  return crypto.createHash("sha256").update(token).digest("hex");
}
```

**HTTPS enforcement in next.config.ts:**

```typescript
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          {
            key: "Strict-Transport-Security",
            value: "max-age=63072000; includeSubDomains; preload",
          },
        ],
      },
    ];
  },
};
export default nextConfig;
```

---

### A03 — Injection

**SQL Injection:** Drizzle ORM uses parameterized queries by default. Using the typed query builder is safe. The only risk is `sql` template literals with unescaped interpolation.

```typescript
import { db } from "@/db";
import { products } from "@/db/schema";
import { ilike } from "drizzle-orm";
import { sql } from "drizzle-orm";

// SAFE — parameterized, Drizzle generates: WHERE name ILIKE $1
const results = await db.query.products.findMany({
  where: ilike(products.name, `%${searchTerm}%`),
});

// DANGEROUS — do NOT interpolate user input into sql`` template
// If searchTerm = "'; DROP TABLE products; --" this is a live SQL injection
const results2 = await db.execute(
  sql`SELECT * FROM products WHERE name = '${searchTerm}'` // ← NEVER do this
);

// SAFE way to use sql`` when needed — use sql.placeholder or pass as param
const results3 = await db.execute(
  sql`SELECT * FROM products WHERE name ILIKE ${"%" + searchTerm + "%"}` // Drizzle auto-parameterizes
);
```

**XSS:** React escapes JSX content by default. The only XSS risk is `dangerouslySetInnerHTML`.

```typescript
// BAD — renders raw HTML from user input
<div dangerouslySetInnerHTML={{ __html: userBio }} />

// GOOD — sanitize with DOMPurify before setting inner HTML (if rich text is truly needed)
import DOMPurify from "isomorphic-dompurify";

const sanitized = DOMPurify.sanitize(userBio, {
  ALLOWED_TAGS: ["b", "i", "em", "strong", "p", "br"],
  ALLOWED_ATTR: [],
});
<div dangerouslySetInnerHTML={{ __html: sanitized }} />

// BEST — avoid dangerouslySetInnerHTML entirely; render structured data instead
```

---

### A05 — Security Misconfiguration

**Security headers in next.config.ts:**

```typescript
// next.config.ts
import type { NextConfig } from "next";

const isDev = process.env.NODE_ENV === "development";

const securityHeaders = [
  {
    key: "X-DNS-Prefetch-Control",
    value: "on",
  },
  {
    key: "X-Frame-Options",
    value: "SAMEORIGIN", // prevents clickjacking
  },
  {
    key: "X-Content-Type-Options",
    value: "nosniff", // prevents MIME sniffing
  },
  {
    key: "Referrer-Policy",
    value: "strict-origin-when-cross-origin",
  },
  {
    key: "Permissions-Policy",
    value: "camera=(), microphone=(), geolocation=()",
  },
  {
    key: "Content-Security-Policy",
    // In production, tighten this significantly
    value: isDev
      ? "default-src 'self' 'unsafe-eval' 'unsafe-inline' *"
      : [
          "default-src 'self'",
          "script-src 'self' 'unsafe-inline' https://js.stripe.com", // Stripe requires unsafe-inline
          "style-src 'self' 'unsafe-inline'", // Tailwind requires unsafe-inline
          "img-src 'self' data: https:",
          "font-src 'self'",
          "connect-src 'self' https://api.stripe.com https://api.resend.com",
          "frame-src https://js.stripe.com https://hooks.stripe.com",
          "object-src 'none'",
          "base-uri 'self'",
          "form-action 'self'",
        ].join("; "),
  },
  {
    key: "Strict-Transport-Security",
    value: "max-age=63072000; includeSubDomains; preload",
  },
];

const nextConfig: NextConfig = {
  async headers() {
    return [{ source: "/(.*)", headers: securityHeaders }];
  },
  // Prevent exposing server internals in error messages
  serverRuntimeConfig: {
    // Only available server-side
  },
  // Never expose secrets in public env vars
  // BAD: NEXT_PUBLIC_DB_URL — this leaks to the browser bundle
  // GOOD: DATABASE_URL — only accessible server-side
};

export default nextConfig;
```

**Environment variable discipline:**

```bash
# .env.local — NEVER commit this file
DATABASE_URL=postgresql://...          # server-only
NEXTAUTH_SECRET=...                    # server-only
STRIPE_SECRET_KEY=sk_live_...          # server-only
STRIPE_WEBHOOK_SECRET=whsec_...        # server-only
RESEND_API_KEY=re_...                  # server-only

# These are safe to expose (NEXT_PUBLIC_ prefix)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...
NEXT_PUBLIC_APP_URL=https://myapp.com
```

---

### A07 — Identification and Authentication Failures

**Auth.js v5 secure configuration:**

```typescript
// auth.ts
import NextAuth from "next-auth";
import { DrizzleAdapter } from "@auth/drizzle-adapter";
import { db } from "@/db";
import Google from "next-auth/providers/google";
import Credentials from "next-auth/providers/credentials";
import { verifyPassword } from "@/lib/password";
import { findUserByEmail } from "@/db/queries/user";

export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: DrizzleAdapter(db),
  providers: [
    Google({
      clientId: process.env.AUTH_GOOGLE_ID!,
      clientSecret: process.env.AUTH_GOOGLE_SECRET!,
    }),
    Credentials({
      async authorize(credentials) {
        // Always do constant-time comparison to prevent timing attacks
        const user = await findUserByEmail(credentials.email as string);
        if (!user?.passwordHash) return null; // don't reveal whether email exists

        const valid = await verifyPassword(
          credentials.password as string,
          user.passwordHash
        );
        if (!valid) return null;

        return { id: user.id, email: user.email, role: user.role };
      },
    }),
  ],
  session: {
    strategy: "database", // database sessions > JWT for revocation support
    maxAge: 30 * 24 * 60 * 60, // 30 days
    updateAge: 24 * 60 * 60,   // refresh session every 24h
  },
  cookies: {
    sessionToken: {
      options: {
        httpOnly: true,  // not accessible from JS
        sameSite: "lax", // CSRF protection
        secure: process.env.NODE_ENV === "production", // HTTPS only in prod
        path: "/",
      },
    },
  },
  callbacks: {
    session({ session, user }) {
      session.user.id = user.id;
      session.user.role = user.role as string;
      return session;
    },
  },
});
```

---

### A09 — Security Logging and Monitoring Failures

**Sentry without leaking sensitive data:**

```typescript
// src/lib/sentry.ts
import * as Sentry from "@sentry/nextjs";

// Scrub sensitive fields before they reach Sentry
Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  beforeSend(event) {
    // Remove sensitive headers
    if (event.request?.headers) {
      delete event.request.headers["authorization"];
      delete event.request.headers["cookie"];
    }
    // Remove sensitive body fields
    if (event.request?.data) {
      const data = event.request.data as Record<string, unknown>;
      delete data["password"];
      delete data["creditCard"];
      delete data["ssn"];
    }
    return event;
  },
  // Don't send user IP addresses
  sendDefaultPii: false,
});

// src/lib/audit-log.ts — security-relevant events
export async function logSecurityEvent(
  event: "login_failed" | "password_reset" | "suspicious_activity" | "admin_action",
  metadata: {
    userId?: string;
    ip?: string;
    userAgent?: string;
    details?: string;
  }
) {
  // Write to a separate audit_logs table — never delete these
  await db.insert(auditLogs).values({
    event,
    userId: metadata.userId,
    // Truncate/hash PII in logs
    ip: metadata.ip ? hashIp(metadata.ip) : null,
    details: metadata.details,
    createdAt: new Date(),
  });
}
```

---

## Антипаттерн

```typescript
// A01 — IDOR: trusting client-supplied IDs without ownership check
export async function deleteItem(itemId: string) {
  const session = await auth();
  if (!session) return { error: "Unauthorized" };
  await db.delete(items).where(eq(items.id, itemId)); // ← any user deletes any item
}

// A02 — Storing password in plain text or with weak hash
await db.insert(users).values({ email, password: md5(password) });

// A03 — Raw SQL with string interpolation
await db.execute(sql.raw(`SELECT * FROM users WHERE email = '${email}'`));

// A05 — Exposing DB URL in client bundle
// In next.config.ts env section or component:
const url = process.env.NEXT_PUBLIC_DATABASE_URL; // ← sends DB creds to browser

// A07 — JWT with weak secret
// In auth.ts:
secret: "secret" // ← trivially brute-forced; use 32+ random bytes
```

---

## Связанные документы

- `knowledge/custom/06-security/server-action-validation.md` — input validation in Server Actions
- `knowledge/custom/06-security/auth-security.md` — Auth.js v5 hardening
- `knowledge/custom/02-patterns/server-actions.md` — Server Action patterns

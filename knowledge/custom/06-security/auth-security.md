---
category: security
topic: auth-security
status: draft
---

## Проблема / Контекст

Auth.js v5 (next-auth v5) ships with sensible defaults but leaves many security decisions to the developer. Default session duration is 30 days with no rotation. The Credentials provider has no built-in brute force protection. Email verification is optional. Password reset tokens are not provided — you build them yourself. Without deliberate hardening, an Auth.js deployment is functional but not production-hardened.

---

## Решение

### Secure session configuration

```typescript
// auth.ts
import NextAuth from "next-auth";
import { DrizzleAdapter } from "@auth/drizzle-adapter";
import { db } from "@/db";

export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: DrizzleAdapter(db),

  session: {
    strategy: "database", // Prefer database sessions over JWT for production
    // Database sessions can be revoked instantly (e.g., on logout-everywhere)
    // JWT sessions cannot be invalidated until they expire

    maxAge: 30 * 24 * 60 * 60,  // 30 days absolute expiry
    updateAge: 24 * 60 * 60,     // Extend session by 30 days every 24h of activity
    // With these settings: a session expires 30 days after the LAST activity
    // A user who doesn't visit for 30 days is logged out automatically
  },

  cookies: {
    sessionToken: {
      name: process.env.NODE_ENV === "production"
        ? "__Secure-next-auth.session-token"
        : "next-auth.session-token",
      options: {
        httpOnly: true,          // Inaccessible to document.cookie
        sameSite: "lax",         // Sent on top-level navigations, not cross-site
        secure: process.env.NODE_ENV === "production", // HTTPS-only in prod
        path: "/",
      },
    },
  },

  callbacks: {
    session({ session, user }) {
      // Extend the session type to include custom fields
      session.user.id = user.id;
      session.user.role = (user as { role: string }).role ?? "user";
      session.user.emailVerified = user.emailVerified;
      return session;
    },
    signIn({ user, account }) {
      // Block sign-in if email is not verified (for Credentials provider)
      if (account?.provider === "credentials" && !user.emailVerified) {
        return "/sign-in?error=EmailNotVerified";
      }
      return true;
    },
  },

  events: {
    async signIn({ user, account, isNewUser }) {
      // Log all sign-in events for security audit
      await logSecurityEvent("sign_in", {
        userId: user.id,
        provider: account?.provider,
        isNewUser,
      });
    },
    async signOut({ session }) {
      await logSecurityEvent("sign_out", {
        userId: (session as { userId?: string }).userId,
      });
    },
  },

  pages: {
    signIn: "/sign-in",
    error: "/sign-in",  // Don't use a separate error page — leaks auth info
    verifyRequest: "/verify-email",
  },
});
```

### JWT secret rotation

```typescript
// auth.ts — when using JWT strategy (e.g., for Edge runtime compatibility)
import NextAuth from "next-auth";
import { type JWT } from "next-auth/jwt";

export const { handlers, auth } = NextAuth({
  session: { strategy: "jwt" },

  jwt: {
    // Use the longest non-deprecated algorithm: HS512 > HS256
    // Key rotation: add the new secret as first, keep old as second for existing sessions
    secret: process.env.NEXTAUTH_SECRET,

    // Custom encode/decode allows handling multiple secrets during rotation
    async encode({ token, secret, maxAge }) {
      // During rotation: sign with new secret
      const secrets = Array.isArray(secret) ? secret : [secret];
      return await new SignJWT(token as Record<string, unknown>)
        .setProtectedHeader({ alg: "HS256" })
        .setIssuedAt()
        .setExpirationTime(Math.floor(Date.now() / 1000) + (maxAge ?? 30 * 24 * 60 * 60))
        .sign(new TextEncoder().encode(secrets[0] as string));
    },

    async decode({ token, secret }) {
      // During rotation: try new secret first, fall back to old secret
      const secrets = Array.isArray(secret) ? secret : [secret];
      for (const s of secrets) {
        try {
          const { payload } = await jwtVerify(
            token!,
            new TextEncoder().encode(s as string)
          );
          return payload as JWT;
        } catch {
          continue;
        }
      }
      return null;
    },
  },
});

// Key rotation process:
// 1. Generate new secret: openssl rand -base64 32
// 2. Set NEXTAUTH_SECRET="new_secret old_secret" (space-separated)
// 3. Deploy — existing JWTs signed with old_secret still work
// 4. After maxAge (30 days), all old tokens expired; remove old_secret
```

### Brute force protection for Credentials provider

```typescript
// src/lib/auth/brute-force.ts
import { db } from "@/db";
import { loginAttempts } from "@/db/schema";
import { eq, and, gt } from "drizzle-orm";

const MAX_ATTEMPTS = 5;
const LOCKOUT_DURATION_MS = 15 * 60 * 1000; // 15 minutes

export async function checkBruteForce(
  email: string,
  ip: string
): Promise<{ blocked: boolean; attemptsRemaining: number }> {
  const windowStart = new Date(Date.now() - LOCKOUT_DURATION_MS);

  const attempts = await db.query.loginAttempts.findMany({
    where: and(
      eq(loginAttempts.email, email.toLowerCase()),
      gt(loginAttempts.createdAt, windowStart)
    ),
  });

  const blocked = attempts.length >= MAX_ATTEMPTS;
  return {
    blocked,
    attemptsRemaining: Math.max(0, MAX_ATTEMPTS - attempts.length),
  };
}

export async function recordFailedAttempt(email: string, ip: string) {
  await db.insert(loginAttempts).values({
    email: email.toLowerCase(),
    ip,
    createdAt: new Date(),
  });
}

export async function clearFailedAttempts(email: string) {
  await db.delete(loginAttempts).where(
    eq(loginAttempts.email, email.toLowerCase())
  );
}

// auth.ts — Credentials provider with brute force check
Credentials({
  async authorize(credentials, req) {
    const ip = req.headers?.get("x-forwarded-for") ?? "unknown";
    const email = credentials.email as string;

    // Check brute force before querying DB
    const { blocked } = await checkBruteForce(email, ip);
    if (blocked) {
      // Same error message — don't confirm whether the account exists
      return null;
    }

    const user = await findUserByEmail(email);
    if (!user?.passwordHash) {
      await recordFailedAttempt(email, ip);
      return null;
    }

    const valid = await verifyPassword(credentials.password as string, user.passwordHash);
    if (!valid) {
      await recordFailedAttempt(email, ip);
      return null;
    }

    await clearFailedAttempts(email); // Reset on success
    return { id: user.id, email: user.email, role: user.role };
  },
}),
```

### Email verification flow

```typescript
// src/actions/auth/send-verification.ts
"use server";

import { generateSecureToken, hashToken } from "@/lib/tokens";
import { db } from "@/db";
import { verificationTokens, users } from "@/db/schema";
import { resend } from "@/lib/resend";
import { VerificationEmail } from "@/emails/verification";
import { eq } from "drizzle-orm";

export async function sendVerificationEmail(email: string) {
  const user = await db.query.users.findFirst({
    where: eq(users.email, email.toLowerCase()),
    columns: { id: true, emailVerified: true },
  });

  // Always return success — don't confirm whether email is registered
  if (!user || user.emailVerified) return { success: true };

  const token = generateSecureToken(32);
  const hashedToken = await hashToken(token);
  const expiresAt = new Date(Date.now() + 24 * 60 * 60 * 1000); // 24 hours

  // Delete any existing token for this email (one at a time)
  await db.delete(verificationTokens).where(eq(verificationTokens.identifier, email));

  await db.insert(verificationTokens).values({
    identifier: email,
    token: hashedToken, // store hash, send plain
    expires: expiresAt,
  });

  await resend.emails.send({
    from: "noreply@myapp.com",
    to: email,
    subject: "Verify your email",
    react: VerificationEmail({
      url: `${process.env.NEXT_PUBLIC_APP_URL}/verify-email?token=${token}&email=${encodeURIComponent(email)}`,
      expiresIn: "24 hours",
    }),
  });

  return { success: true };
}

// src/actions/auth/verify-email.ts
export async function verifyEmail(token: string, email: string) {
  const hashedToken = await hashToken(token);

  const record = await db.query.verificationTokens.findFirst({
    where: and(
      eq(verificationTokens.identifier, email),
      eq(verificationTokens.token, hashedToken),
      gt(verificationTokens.expires, new Date())
    ),
  });

  if (!record) {
    return { error: "Invalid or expired verification link" };
  }

  await db.transaction(async (tx) => {
    await tx.update(users)
      .set({ emailVerified: new Date() })
      .where(eq(users.email, email));

    await tx.delete(verificationTokens)
      .where(eq(verificationTokens.identifier, email));
  });

  return { success: true };
}
```

### Password reset with short-lived tokens

```typescript
// src/actions/auth/password-reset.ts
"use server";

const RESET_TOKEN_EXPIRY_MS = 60 * 60 * 1000; // 1 hour — NOT 24h like email verification

export async function requestPasswordReset(email: string) {
  // Always respond the same way — don't leak whether email exists
  const user = await db.query.users.findFirst({
    where: eq(users.email, email.toLowerCase()),
    columns: { id: true, passwordHash: true },
  });

  // If user has no passwordHash, they signed up with OAuth — can't reset
  if (!user?.passwordHash) return { success: true }; // silent

  const token = generateSecureToken(32);
  const hashedToken = await hashToken(token);

  // Invalidate all existing reset tokens for this user
  await db.delete(passwordResetTokens).where(eq(passwordResetTokens.userId, user.id));

  await db.insert(passwordResetTokens).values({
    userId: user.id,
    token: hashedToken,
    expires: new Date(Date.now() + RESET_TOKEN_EXPIRY_MS),
    used: false,
  });

  await resend.emails.send({
    from: "noreply@myapp.com",
    to: email,
    subject: "Reset your password",
    react: PasswordResetEmail({
      url: `${process.env.NEXT_PUBLIC_APP_URL}/reset-password?token=${token}`,
      expiresIn: "1 hour",
    }),
  });

  return { success: true };
}

const resetPasswordSchema = z.object({
  token: z.string().min(64).max(64), // 32 bytes = 64 hex chars
  password: z.string().min(8).max(128),
});

export async function resetPassword(input: unknown) {
  const parsed = resetPasswordSchema.safeParse(input);
  if (!parsed.success) return { error: "Invalid request" };

  const { token, password } = parsed.data;
  const hashedToken = await hashToken(token);

  const record = await db.query.passwordResetTokens.findFirst({
    where: and(
      eq(passwordResetTokens.token, hashedToken),
      eq(passwordResetTokens.used, false),
      gt(passwordResetTokens.expires, new Date())
    ),
    columns: { id: true, userId: true },
  });

  if (!record) return { error: "Invalid or expired reset link" };

  const newHash = await hashPassword(password);

  await db.transaction(async (tx) => {
    await tx.update(users)
      .set({ passwordHash: newHash, updatedAt: new Date() })
      .where(eq(users.id, record.userId));

    // Mark token as used (don't delete — useful for audit)
    await tx.update(passwordResetTokens)
      .set({ used: true, usedAt: new Date() })
      .where(eq(passwordResetTokens.id, record.id));

    // Invalidate ALL active sessions for this user
    await tx.delete(sessions).where(eq(sessions.userId, record.userId));
  });

  return { success: true };
}
```

### Logout everywhere

```typescript
// src/actions/auth/logout-everywhere.ts
"use server";

import { auth } from "@/auth";
import { db } from "@/db";
import { sessions } from "@/db/schema";
import { eq } from "drizzle-orm";

export async function logoutEverywhere() {
  const session = await auth();
  if (!session?.user?.id) return { error: "Unauthorized" };

  // Delete all DB sessions for this user
  await db.delete(sessions).where(eq(sessions.userId, session.user.id));

  // The current request's session cookie is now invalid
  // Client should call signOut() after this to clear the cookie
  return { success: true };
}
```

### Suspicious login detection

```typescript
// src/lib/auth/suspicious-login.ts
import { auth } from "@/auth";
import { headers } from "next/headers";

interface LoginContext {
  userId: string;
  ip: string;
  userAgent: string;
  country?: string;
}

export async function detectSuspiciousLogin(
  current: LoginContext,
  previous: LoginContext | null
): Promise<boolean> {
  if (!previous) return false; // First login — not suspicious

  // Different country within 1 hour — impossible travel
  if (current.country && previous.country && current.country !== previous.country) {
    const hourAgo = Date.now() - 60 * 60 * 1000;
    const lastLoginTime = await getLastLoginTime(current.userId);
    if (lastLoginTime && lastLoginTime.getTime() > hourAgo) {
      return true;
    }
  }

  // Drastically different user agent (new OS/browser combo)
  const prevBrowser = parseBrowser(previous.userAgent);
  const currBrowser = parseBrowser(current.userAgent);
  if (prevBrowser !== currBrowser) {
    return true; // Could be a new device — flag for notification
  }

  return false;
}

// In the signIn event:
events: {
  async signIn({ user, account }) {
    const headersList = await headers();
    const ip = headersList.get("x-forwarded-for") ?? "unknown";
    const userAgent = headersList.get("user-agent") ?? "unknown";

    const suspicious = await detectSuspiciousLogin(
      { userId: user.id!, ip, userAgent },
      await getLastLoginContext(user.id!)
    );

    if (suspicious) {
      // Send "new sign-in" notification email
      await resend.emails.send({
        from: "security@myapp.com",
        to: user.email!,
        subject: "New sign-in detected",
        react: SuspiciousLoginEmail({ ip, userAgent, time: new Date() }),
      });
    }

    await recordLoginContext(user.id!, { ip, userAgent });
  },
}
```

---

## Антипаттерн

```typescript
// BAD 1: JWT strategy with no way to revoke sessions
session: { strategy: "jwt", maxAge: 30 * 24 * 60 * 60 }
// If a user's account is compromised, you cannot invalidate their token
// until it naturally expires 30 days later.

// BAD 2: Storing the reset token directly (not its hash)
await db.insert(passwordResetTokens).values({ token: plainToken });
// A DB breach gives attackers valid reset tokens for all users.

// BAD 3: Password reset tokens valid for 24 hours
expires: new Date(Date.now() + 24 * 60 * 60 * 1000),
// Use 1 hour — password reset tokens should be short-lived.

// BAD 4: Revealing whether an email is registered
if (!user) return { error: "No account with that email" };
// Instead: always return { success: true } regardless.

// BAD 5: Not invalidating sessions after password change
await db.update(users).set({ passwordHash: newHash }).where(...);
// The attacker who triggered the reset still has a valid session!
// Always delete all sessions after a password change.

// BAD 6: No email verification — allows spam accounts and fake signups
// signIn callback should block unverified Credentials sign-ins.
```

---

## Связанные документы

- `knowledge/custom/06-security/owasp-nextjs.md` — OWASP A07 auth failures
- `knowledge/custom/06-security/server-action-validation.md` — validation in auth actions
- `knowledge/custom/02-patterns/server-actions.md` — Server Action patterns

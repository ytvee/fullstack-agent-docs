---
category: patterns
topic: auth-flow
status: draft
---

## Проблема / Контекст

Auth.js v5 (formerly NextAuth.js) has breaking changes from v4: the config is now in a single `auth.ts` file, the Drizzle adapter API changed, middleware integration works differently, and the `getServerSession()` function is replaced by `auth()`. Many online examples still show v4 patterns.

Common issues in production auth implementations:
- Session checks duplicated in every Server Component instead of centralized in middleware + layout
- JWT vs database sessions chosen without understanding the trade-offs
- No type augmentation for custom user fields (role, orgId, etc.)
- Credentials provider storing plaintext passwords
- OAuth callback not creating users in the database correctly
- Role-based access implemented with fragile pathname string matching

## Решение

### 1. Install and Configure Drizzle Adapter

```bash
pnpm add next-auth@beta @auth/drizzle-adapter bcryptjs
pnpm add -D @types/bcryptjs
```

**Drizzle schema for Auth.js tables:**

```typescript
// src/server/db/schema.ts (auth tables section)
import {
  pgTable, text, timestamp, integer, boolean, primaryKey
} from 'drizzle-orm/pg-core'
import { createId } from '@paralleldrive/cuid2'

export const users = pgTable('users', {
  id: text('id').primaryKey().$defaultFn(() => createId()),
  name: text('name'),
  email: text('email').unique().notNull(),
  emailVerified: timestamp('email_verified', { mode: 'date' }),
  image: text('image'),
  password: text('password'),  // null for OAuth-only users
  role: text('role', { enum: ['user', 'admin'] }).notNull().default('user'),
  createdAt: timestamp('created_at').defaultNow().notNull(),
})

export const accounts = pgTable(
  'accounts',
  {
    userId: text('user_id').notNull().references(() => users.id, { onDelete: 'cascade' }),
    type: text('type').notNull(),
    provider: text('provider').notNull(),
    providerAccountId: text('provider_account_id').notNull(),
    refresh_token: text('refresh_token'),
    access_token: text('access_token'),
    expires_at: integer('expires_at'),
    token_type: text('token_type'),
    scope: text('scope'),
    id_token: text('id_token'),
    session_state: text('session_state'),
  },
  (table) => ({
    pk: primaryKey({ columns: [table.provider, table.providerAccountId] }),
  })
)

export const sessions = pgTable('sessions', {
  sessionToken: text('session_token').primaryKey(),
  userId: text('user_id').notNull().references(() => users.id, { onDelete: 'cascade' }),
  expires: timestamp('expires', { mode: 'date' }).notNull(),
})

export const verificationTokens = pgTable(
  'verification_tokens',
  {
    identifier: text('identifier').notNull(),
    token: text('token').notNull(),
    expires: timestamp('expires', { mode: 'date' }).notNull(),
  },
  (table) => ({
    pk: primaryKey({ columns: [table.identifier, table.token] }),
  })
)

// Type exports for use in application code
export type User = typeof users.$inferSelect
export type NewUser = typeof users.$inferInsert
```

### 2. Auth.js v5 Configuration

```typescript
// src/server/auth.ts
import NextAuth from 'next-auth'
import { DrizzleAdapter } from '@auth/drizzle-adapter'
import GitHub from 'next-auth/providers/github'
import Google from 'next-auth/providers/google'
import Credentials from 'next-auth/providers/credentials'
import { db } from '@/server/db'
import { users, accounts, sessions, verificationTokens } from '@/server/db/schema'
import { eq } from 'drizzle-orm'
import bcrypt from 'bcryptjs'
import { z } from 'zod'

const credentialsSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
})

export const { handlers, signIn, signOut, auth } = NextAuth({
  adapter: DrizzleAdapter(db, {
    usersTable: users,
    accountsTable: accounts,
    sessionsTable: sessions,
    verificationTokensTable: verificationTokens,
  }),

  // JWT strategy: session data stored in cookie, no DB lookup on each request
  // Database strategy: session stored in DB, one DB query per request
  // Use JWT for most apps; database sessions if you need instant revocation
  session: { strategy: 'jwt' },

  providers: [
    GitHub({
      clientId: process.env.AUTH_GITHUB_ID!,
      clientSecret: process.env.AUTH_GITHUB_SECRET!,
    }),
    Google({
      clientId: process.env.AUTH_GOOGLE_ID!,
      clientSecret: process.env.AUTH_GOOGLE_SECRET!,
    }),
    Credentials({
      credentials: {
        email: { label: 'Email', type: 'email' },
        password: { label: 'Password', type: 'password' },
      },
      async authorize(credentials) {
        const parsed = credentialsSchema.safeParse(credentials)
        if (!parsed.success) return null

        const user = await db.query.users.findFirst({
          where: eq(users.email, parsed.data.email),
        })
        if (!user?.password) return null

        const passwordMatch = await bcrypt.compare(parsed.data.password, user.password)
        if (!passwordMatch) return null

        return {
          id: user.id,
          email: user.email,
          name: user.name,
          image: user.image,
          role: user.role,
        }
      },
    }),
  ],

  callbacks: {
    // Runs when JWT is created/updated. Add custom fields here.
    async jwt({ token, user }) {
      if (user) {
        // `user` is only available on initial sign-in
        token.id = user.id
        token.role = (user as { role?: string }).role ?? 'user'
      }
      return token
    },

    // Runs when session is accessed. Expose JWT fields to session.
    async session({ session, token }) {
      if (token) {
        session.user.id = token.id as string
        session.user.role = token.role as string
      }
      return session
    },
  },

  pages: {
    signIn: '/login',
    error: '/login',       // Auth errors redirect here with ?error=...
    verifyRequest: '/verify-email',
  },

  events: {
    // Called after a new user is created via OAuth
    async createUser({ user }) {
      // Send welcome email, create org, etc.
      console.log('New user created:', user.email)
    },
  },
})
```

### 3. TypeScript Augmentation for Session

Auth.js v5 session types don't include custom fields by default. Augment them:

```typescript
// src/types/auth.ts
import type { DefaultSession } from 'next-auth'

declare module 'next-auth' {
  interface Session {
    user: {
      id: string
      role: 'user' | 'admin'
    } & DefaultSession['user']
  }

  interface User {
    role: 'user' | 'admin'
  }
}

declare module 'next-auth/jwt' {
  interface JWT {
    id: string
    role: 'user' | 'admin'
  }
}
```

### 4. Route Handlers for Auth Endpoints

```typescript
// src/app/api/auth/[...nextauth]/route.ts
import { handlers } from '@/server/auth'
export const { GET, POST } = handlers
```

### 5. Middleware — Broad Route Protection

```typescript
// src/middleware.ts
import { auth } from '@/server/auth'
import type { NextRequest } from 'next/server'
import { NextResponse } from 'next/server'

const PROTECTED_PREFIXES = ['/dashboard', '/projects', '/settings', '/admin']
const AUTH_PAGES = ['/login', '/register', '/forgot-password']

export default auth((request) => {
  const { pathname } = request.nextUrl
  const session = request.auth

  const isProtected = PROTECTED_PREFIXES.some((p) => pathname.startsWith(p))
  const isAuthPage = AUTH_PAGES.some((p) => pathname.startsWith(p))

  // Redirect unauthenticated users attempting to access protected routes
  if (isProtected && !session?.user) {
    const url = new URL('/login', request.url)
    url.searchParams.set('callbackUrl', pathname)
    return NextResponse.redirect(url)
  }

  // Redirect authenticated users away from auth pages
  if (isAuthPage && session?.user) {
    return NextResponse.redirect(new URL('/dashboard', request.url))
  }

  return NextResponse.next()
})

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
}
```

### 6. Using `auth()` in Server Components

```typescript
// src/app/(dashboard)/settings/profile/page.tsx
import { auth } from '@/server/auth'
import { redirect } from 'next/navigation'
import { db } from '@/server/db'
import { users } from '@/server/db/schema'
import { eq } from 'drizzle-orm'
import { ProfileForm } from '@/features/auth/components/profile-form'

export default async function ProfilePage() {
  const session = await auth()

  // Layout already checks auth, but double-check for safety in sensitive pages
  if (!session?.user?.id) redirect('/login')

  const user = await db.query.users.findFirst({
    where: eq(users.id, session.user.id),
    columns: { id: true, name: true, email: true, image: true },
  })

  if (!user) redirect('/login')

  return <ProfileForm user={user} />
}
```

### 7. Using `useSession` in Client Components

```typescript
// src/components/layout/user-menu.tsx
'use client'

import { useSession, signOut } from 'next-auth/react'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

export function UserMenu() {
  const { data: session, status } = useSession()

  if (status === 'loading') {
    return <div className="h-8 w-8 animate-pulse rounded-full bg-muted" />
  }

  if (!session?.user) return null

  const initials = session.user.name
    ?.split(' ')
    .map((n) => n[0])
    .join('')
    .toUpperCase()
    .slice(0, 2) ?? 'U'

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <button className="rounded-full outline-none ring-offset-2 focus-visible:ring-2">
          <Avatar className="h-8 w-8">
            <AvatarImage src={session.user.image ?? undefined} alt={session.user.name ?? ''} />
            <AvatarFallback>{initials}</AvatarFallback>
          </Avatar>
        </button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-48">
        <DropdownMenuItem className="text-sm font-medium">
          {session.user.email}
        </DropdownMenuItem>
        <DropdownMenuItem asChild>
          <a href="/settings/profile">Settings</a>
        </DropdownMenuItem>
        <DropdownMenuItem
          className="text-destructive"
          onClick={() => signOut({ redirectTo: '/login' })}
        >
          Sign out
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

### 8. SessionProvider in Root Layout

```typescript
// src/app/layout.tsx
import { SessionProvider } from 'next-auth/react'
import { auth } from '@/server/auth'

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const session = await auth()

  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        {/* Pass server session to avoid client-side refetch on mount */}
        <SessionProvider session={session}>
          {children}
        </SessionProvider>
      </body>
    </html>
  )
}
```

### 9. Credentials Registration Action

```typescript
// src/features/auth/register/actions.ts
'use server'

import { db } from '@/server/db'
import { users } from '@/server/db/schema'
import { eq } from 'drizzle-orm'
import bcrypt from 'bcryptjs'
import { z } from 'zod'
import { signIn } from '@/server/auth'
import { AuthError } from 'next-auth'
import type { ActionResult } from '@/types/api'

const registerSchema = z.object({
  name: z.string().min(2, 'Name must be at least 2 characters'),
  email: z.string().email('Invalid email'),
  password: z
    .string()
    .min(8, 'Password must be at least 8 characters')
    .regex(/[A-Z]/, 'Must contain an uppercase letter')
    .regex(/[0-9]/, 'Must contain a number'),
})

export async function registerUser(
  input: z.infer<typeof registerSchema>
): Promise<ActionResult> {
  const parsed = registerSchema.safeParse(input)
  if (!parsed.success) {
    return {
      success: false,
      error: 'Validation failed',
      fieldErrors: parsed.error.flatten().fieldErrors as Record<string, string[]>,
    }
  }

  const { name, email, password } = parsed.data

  const existing = await db.query.users.findFirst({
    where: eq(users.email, email),
    columns: { id: true },
  })
  if (existing) {
    return { success: false, error: 'An account with this email already exists' }
  }

  const hashedPassword = await bcrypt.hash(password, 12)

  await db.insert(users).values({ name, email, password: hashedPassword })

  // Immediately sign in after registration
  try {
    await signIn('credentials', { email, password, redirect: false })
  } catch (error) {
    if (error instanceof AuthError) {
      return { success: false, error: 'Account created but sign-in failed. Please log in.' }
    }
    throw error
  }

  return { success: true, data: undefined }
}
```

### 10. Role-Based Access Control

```typescript
// src/lib/auth-utils.ts
import { auth } from '@/server/auth'
import { redirect } from 'next/navigation'

export async function requireAuth() {
  const session = await auth()
  if (!session?.user?.id) redirect('/login')
  return session
}

export async function requireAdmin() {
  const session = await requireAuth()
  if (session.user.role !== 'admin') redirect('/dashboard')
  return session
}

// Usage in admin pages:
// src/app/(admin)/admin/users/page.tsx
import { requireAdmin } from '@/lib/auth-utils'

export default async function AdminUsersPage() {
  const session = await requireAdmin()
  // Only admins reach this line
  return <AdminUserList />
}
```

## Антипаттерн

```typescript
// BAD 1: Checking auth in every page — redundant when layout already checks
// src/app/(dashboard)/projects/page.tsx
export default async function ProjectsPage() {
  const session = await auth()
  if (!session) redirect('/login')  // Layout already did this!
  // ...
}
// Exception: very sensitive pages (delete account, admin) should double-check

// BAD 2: Storing sensitive data in JWT token (it's base64, not encrypted)
callbacks: {
  async jwt({ token, user }) {
    if (user) {
      token.password = user.password          // NEVER
      token.creditCardNumber = user.card      // NEVER
      token.socialSecurityNumber = user.ssn   // NEVER
    }
    return token
  }
}

// BAD 3: Using useSession in Server Components
// 'use client' is implied, but this pattern kills RSC benefits
async function ProfilePage() {
  const { data: session } = useSession()  // only works in Client Components
  // Use auth() instead in Server Components
}

// BAD 4: Plaintext password storage
await db.insert(users).values({ email, password: rawPassword })
// Always bcrypt.hash(password, 12) — cost factor 12 is the production minimum

// BAD 5: Not handling signIn redirect properly
// This causes an unhandled NEXT_REDIRECT error in try/catch
try {
  await signIn('credentials', { email, password, redirectTo: '/dashboard' })
} catch (error) {
  // redirect() throws internally — this catch will swallow it
}
// Use redirect: false then manually redirect, or let the error propagate
```

## Связанные документы

- `01-architecture/api-design.md` — Middleware auth pattern
- `01-architecture/route-groups.md` — Auth vs dashboard layout separation
- `02-patterns/crud-pattern.md` — Using session in CRUD operations
- `06-security/input-validation.md` — Zod validation for auth inputs

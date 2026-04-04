---
category: architecture
topic: folder-structure
status: draft
---

## Проблема / Контекст

Next.js 15 App Router projects quickly become unmaintainable when there is no clear convention for where code lives. The App Router introduces new primitives (Server Components, Client Components, Route Handlers, Server Actions) that do not map cleanly onto old Pages Router conventions. Without a canonical structure, teams end up with logic scattered across `app/`, utility functions duplicated in multiple routes, and unclear boundaries between server-only and client-safe code.

The goal is a folder structure that:
- Makes co-location the default for route-specific code
- Provides a clear home for shared utilities, components, and types
- Enforces the server/client boundary at the filesystem level
- Scales from a solo project to a team of 10+ without reorganization

## Решение

### Top-Level Layout (with `src/`)

Always use `src/` to separate application code from config files at the root.

```
my-app/
├── src/
│   ├── app/                    # Next.js App Router — routes only
│   ├── components/             # Shared UI components
│   ├── features/               # Feature slices (domain logic)
│   ├── lib/                    # Pure utilities, third-party wrappers
│   ├── server/                 # Server-only code (never imported by client)
│   ├── hooks/                  # Client-side React hooks
│   ├── store/                  # Zustand stores
│   ├── types/                  # Global TypeScript types and interfaces
│   └── styles/                 # Global CSS, Tailwind base
├── public/                     # Static assets
├── drizzle/                    # Drizzle migrations and schema
├── .env.local
├── next.config.ts
├── tailwind.config.ts
├── drizzle.config.ts
└── tsconfig.json
```

### `app/` Directory — Routes Only

The `app/` directory should contain **only routing concerns**: layouts, pages, loading/error boundaries, and route handlers. Business logic belongs in `features/` or `server/`.

```
src/app/
├── (marketing)/                # Route group: public marketing pages
│   ├── layout.tsx              # Marketing layout (navbar + footer)
│   ├── page.tsx                # Landing page /
│   ├── pricing/
│   │   └── page.tsx            # /pricing
│   └── blog/
│       ├── page.tsx            # /blog
│       └── [slug]/
│           └── page.tsx        # /blog/:slug
│
├── (auth)/                     # Route group: unauthenticated flows
│   ├── layout.tsx              # Centered card layout, no nav
│   ├── login/
│   │   └── page.tsx
│   ├── register/
│   │   └── page.tsx
│   └── forgot-password/
│       └── page.tsx
│
├── (dashboard)/                # Route group: authenticated app
│   ├── layout.tsx              # Dashboard shell: sidebar + header
│   ├── dashboard/
│   │   └── page.tsx            # /dashboard
│   ├── settings/
│   │   ├── layout.tsx          # Settings sub-nav
│   │   ├── profile/
│   │   │   └── page.tsx        # /settings/profile
│   │   └── billing/
│   │       └── page.tsx        # /settings/billing
│   └── projects/
│       ├── page.tsx            # /projects
│       ├── new/
│       │   └── page.tsx        # /projects/new
│       └── [projectId]/
│           ├── page.tsx        # /projects/:id
│           └── edit/
│               └── page.tsx    # /projects/:id/edit
│
├── api/                        # Route Handlers (REST API)
│   ├── webhooks/
│   │   ├── stripe/
│   │   │   └── route.ts
│   │   └── uploadthing/
│   │       └── route.ts
│   └── uploadthing/
│       └── route.ts
│
├── layout.tsx                  # Root layout (html, body, providers)
├── not-found.tsx
└── error.tsx
```

### `components/` — Shared UI

Split into `ui/` (primitive, stateless) and `features/` (domain-aware, may use hooks/stores).

```
src/components/
├── ui/                         # shadcn/ui primitives + custom atoms
│   ├── button.tsx
│   ├── dialog.tsx
│   ├── form.tsx
│   ├── input.tsx
│   └── ...                     # All shadcn components live here
│
└── layout/                     # App-wide layout primitives
    ├── navbar.tsx
    ├── sidebar.tsx
    ├── footer.tsx
    └── page-header.tsx
```

Feature-specific components (e.g., `ProjectCard`, `BillingForm`) live inside `features/`, not here.

### `features/` — Domain Logic

Each feature is a self-contained slice: components, actions, queries, schemas.

```
src/features/
├── auth/
│   ├── components/
│   │   ├── login-form.tsx
│   │   └── register-form.tsx
│   ├── actions.ts              # Server Actions: signIn, signUp, signOut
│   └── schemas.ts              # Zod schemas for auth forms
│
├── projects/
│   ├── components/
│   │   ├── project-card.tsx
│   │   ├── project-list.tsx
│   │   └── project-form.tsx
│   ├── actions.ts              # createProject, updateProject, deleteProject
│   ├── queries.ts              # getProjects, getProjectById (Drizzle)
│   └── schemas.ts
│
└── billing/
    ├── components/
    │   ├── pricing-table.tsx
    │   ├── billing-portal-button.tsx
    │   └── subscription-status.tsx
    ├── actions.ts              # createCheckoutSession, createPortalSession
    └── schemas.ts
```

### `lib/` — Pure Utilities and Third-Party Wrappers

No business logic. No database calls. Safe to import from both server and client (unless explicitly in a `lib/server/` subfolder).

```
src/lib/
├── utils.ts                    # cn(), formatDate(), truncate()
├── validations.ts              # Shared Zod schemas (email, phone, etc.)
├── constants.ts                # APP_URL, PLANS, LIMITS
└── stripe.ts                   # Stripe client initialization (server-safe)
```

### `server/` — Server-Only Code

Files here must never be imported by Client Components. Use `server-only` package to enforce at build time.

```
src/server/
├── db/
│   ├── index.ts                # Drizzle client export
│   ├── schema.ts               # All Drizzle table definitions
│   └── seed.ts                 # Database seeding script
├── auth.ts                     # Auth.js config (auth(), handlers, signIn, signOut)
├── email.ts                    # Resend client + email-sending functions
└── uploadthing.ts              # UploadThing server config
```

`src/server/db/index.ts`:
```typescript
import 'server-only'
import { drizzle } from 'drizzle-orm/neon-http'
import { neon } from '@neondatabase/serverless'
import * as schema from './schema'

const sql = neon(process.env.DATABASE_URL!)
export const db = drizzle(sql, { schema })
```

### `hooks/` — Client-Side Hooks

Only hooks that require `"use client"` context (browser APIs, Zustand, event listeners).

```
src/hooks/
├── use-debounce.ts
├── use-media-query.ts
├── use-outside-click.ts
└── use-upload.ts               # UploadThing client hook wrapper
```

### `store/` — Zustand Stores

One file per domain. Never put server data in Zustand — only ephemeral UI state.

```
src/store/
├── ui-store.ts                 # sidebar open/close, theme, modals
├── upload-store.ts             # upload progress state
└── notification-store.ts      # toast queue (if not using a library)
```

### `types/` — Global TypeScript Types

Shared types that do not belong to a single feature.

```
src/types/
├── index.ts                    # Re-exports all types
├── db.ts                       # Inferred types from Drizzle schema
├── auth.ts                     # Augmented Session, User types
└── api.ts                      # ApiResponse<T>, PaginatedResponse<T>
```

`src/types/api.ts`:
```typescript
export type ApiResponse<T> =
  | { success: true; data: T }
  | { success: false; error: string; code?: string }

export type PaginatedResponse<T> = {
  data: T[]
  total: number
  page: number
  pageSize: number
  totalPages: number
}

export type ActionResult<T = void> =
  | { success: true; data: T }
  | { success: false; error: string; fieldErrors?: Record<string, string[]> }
```

### Co-location vs Centralization

**Co-locate** when:
- A component is only used by one route → put it in `app/(group)/route/_components/`
- A schema is only used by one feature → keep it in `features/feature/schemas.ts`
- A hook is only used by one feature → keep it in `features/feature/hooks.ts`

**Centralize** when:
- A component is used by 2+ unrelated features → move to `components/`
- A utility is used across 3+ files → move to `lib/utils.ts`
- A type is referenced in both feature code and API responses → move to `types/`

**The rule**: start co-located, centralize when the second independent consumer appears.

### Private Folders and Barrel Files

Prefix route-adjacent folders with `_` to exclude them from routing:

```
src/app/(dashboard)/projects/
├── _components/               # NOT a route, just co-located components
│   ├── project-table.tsx
│   └── delete-button.tsx
├── _actions.ts                # Co-located Server Actions for this route
└── page.tsx
```

Avoid barrel files (`index.ts`) inside `features/` — they cause circular dependency issues and slow down TypeScript. Import directly from the module file.

## Антипаттерн

```
# BAD: Flat structure, everything in app/
src/app/
├── components/           # Mixed server and client components with no clear ownership
│   ├── Button.tsx
│   ├── ProjectCard.tsx
│   └── BillingModal.tsx
├── utils/
│   ├── db.ts             # Database calls mixed with pure utilities
│   └── helpers.ts
└── (routes)/
    └── dashboard/
        └── page.tsx      # 400-line file with data fetching, forms, and business logic

# BAD: Putting everything in lib/
src/lib/
├── db.ts
├── auth.ts
├── stripe.ts
├── email.ts
├── utils.ts
├── ProjectCard.tsx       # Components in lib???
└── actions.ts            # ALL server actions in one file
```

Symptoms of a broken structure:
- `page.tsx` files over 100 lines
- Importing from `../../../../../../lib/db`
- Client Components importing from `server/` (build-time error with `server-only`)
- No clear answer to "where does this new file go?"

## Связанные документы

- `01-architecture/feature-sliced.md` — Feature-Sliced Design mapping
- `01-architecture/route-groups.md` — Route group conventions
- `01-architecture/data-flow.md` — Where data fetching happens
- `02-patterns/crud-pattern.md` — Full CRUD implementation using this structure

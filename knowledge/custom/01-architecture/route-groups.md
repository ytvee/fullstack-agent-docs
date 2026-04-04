---
category: architecture
topic: route-groups
status: draft
---

## Проблема / Контекст

A production Next.js 15 app typically has multiple distinct layout contexts: a public marketing site, a full-screen auth flow, a dashboard with sidebar navigation, and possibly an admin panel. Without route groups, all of these must share a single root layout or developers resort to conditional rendering inside `layout.tsx` based on the pathname — which is fragile, hard to test, and leaks concerns across layout boundaries.

Additionally, Next.js App Router supports **parallel routes** (rendering multiple page slots simultaneously) and **intercepting routes** (showing a modal route while preserving the background URL). These are powerful but often misused. This document establishes when and how to use all three patterns.

## Решение

### Route Groups Fundamentals

A route group is a directory wrapped in parentheses: `(group-name)`. It does **not** appear in the URL path but creates a layout boundary. Each group can have its own `layout.tsx`, `loading.tsx`, `error.tsx`, and `template.tsx`.

```
src/app/
├── (marketing)/         # URL: /  /pricing  /blog/:slug
├── (auth)/              # URL: /login  /register  /forgot-password
├── (dashboard)/         # URL: /dashboard  /projects  /settings
└── (admin)/             # URL: /admin  /admin/users  /admin/billing
```

None of `(marketing)`, `(auth)`, `(dashboard)`, or `(admin)` appear in any URL.

### Layout Isolation Per Group

**Marketing layout** — minimal, no auth dependency, optimized for SEO and public access:

```typescript
// src/app/(marketing)/layout.tsx
import { MarketingNav } from '@/widgets/marketing-nav/ui/marketing-nav'
import { Footer } from '@/components/layout/footer'

export default function MarketingLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
      <MarketingNav />
      <main>{children}</main>
      <Footer />
    </>
  )
}
```

**Auth layout** — centered card, no navigation, no footer:

```typescript
// src/app/(auth)/layout.tsx
import { auth } from '@/server/auth'
import { redirect } from 'next/navigation'

export default async function AuthLayout({
  children,
}: {
  children: React.ReactNode
}) {
  // Redirect already-authenticated users away from auth pages
  const session = await auth()
  if (session?.user) redirect('/dashboard')

  return (
    <div className="flex min-h-screen items-center justify-center bg-muted/40">
      <div className="w-full max-w-md">{children}</div>
    </div>
  )
}
```

**Dashboard layout** — authenticated, sidebar + topbar, protects all child routes:

```typescript
// src/app/(dashboard)/layout.tsx
import { auth } from '@/server/auth'
import { redirect } from 'next/navigation'
import { Sidebar } from '@/widgets/sidebar/ui/sidebar'
import { Topbar } from '@/widgets/topbar/ui/topbar'

export default async function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const session = await auth()
  if (!session?.user) redirect('/login')

  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar user={session.user} />
      <div className="flex flex-1 flex-col overflow-hidden">
        <Topbar user={session.user} />
        <main className="flex-1 overflow-y-auto p-6">{children}</main>
      </div>
    </div>
  )
}
```

**Admin layout** — extends auth check with role guard:

```typescript
// src/app/(admin)/layout.tsx
import { auth } from '@/server/auth'
import { redirect } from 'next/navigation'
import { AdminSidebar } from '@/widgets/admin-sidebar/ui/admin-sidebar'

export default async function AdminLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const session = await auth()
  if (!session?.user) redirect('/login')
  if (session.user.role !== 'admin') redirect('/dashboard')

  return (
    <div className="flex h-screen">
      <AdminSidebar />
      <main className="flex-1 overflow-y-auto p-8">{children}</main>
    </div>
  )
}
```

### Full Route Group Folder Structure

```
src/app/
├── (marketing)/
│   ├── layout.tsx
│   ├── page.tsx                      # /
│   ├── pricing/
│   │   └── page.tsx                  # /pricing
│   ├── blog/
│   │   ├── page.tsx                  # /blog
│   │   └── [slug]/
│   │       ├── page.tsx              # /blog/:slug
│   │       └── opengraph-image.tsx   # OG image for blog posts
│   └── changelog/
│       └── page.tsx                  # /changelog
│
├── (auth)/
│   ├── layout.tsx
│   ├── login/
│   │   └── page.tsx                  # /login
│   ├── register/
│   │   └── page.tsx                  # /register
│   ├── forgot-password/
│   │   └── page.tsx                  # /forgot-password
│   └── verify-email/
│       └── page.tsx                  # /verify-email?token=...
│
├── (dashboard)/
│   ├── layout.tsx
│   ├── dashboard/
│   │   ├── page.tsx                  # /dashboard
│   │   └── loading.tsx
│   ├── projects/
│   │   ├── page.tsx                  # /projects
│   │   ├── new/
│   │   │   └── page.tsx              # /projects/new
│   │   └── [projectId]/
│   │       ├── page.tsx              # /projects/:id
│   │       └── edit/
│   │           └── page.tsx          # /projects/:id/edit
│   └── settings/
│       ├── layout.tsx                # Settings sub-nav (nested layout)
│       ├── page.tsx                  # /settings (redirects to /settings/profile)
│       ├── profile/
│       │   └── page.tsx              # /settings/profile
│       ├── billing/
│       │   └── page.tsx              # /settings/billing
│       └── team/
│           └── page.tsx              # /settings/team
│
├── (admin)/
│   ├── layout.tsx
│   └── admin/
│       ├── page.tsx                  # /admin
│       └── users/
│           └── page.tsx              # /admin/users
│
├── api/
│   └── webhooks/
│       └── stripe/
│           └── route.ts
│
├── layout.tsx                        # Root layout (html, body, ThemeProvider)
└── not-found.tsx
```

### Parallel Routes

Parallel routes render **multiple pages simultaneously in the same layout** using named slots (`@slotName`). Use them for dashboards with independent loading states, or side panels alongside main content.

```
src/app/(dashboard)/dashboard/
├── @main/
│   ├── page.tsx       # Main content area
│   └── loading.tsx
├── @activity/
│   ├── page.tsx       # Activity feed — loads independently
│   └── loading.tsx
└── layout.tsx         # Receives both slots as props
```

```typescript
// src/app/(dashboard)/dashboard/layout.tsx
export default function DashboardLayout({
  children,
  main,
  activity,
}: {
  children: React.ReactNode
  main: React.ReactNode
  activity: React.ReactNode
}) {
  return (
    <div className="grid grid-cols-[1fr_320px] gap-6">
      <div>{main}</div>
      <aside>{activity}</aside>
    </div>
  )
}
```

Each slot streams independently — `@activity` loading doesn't block `@main`.

**Unmatched slots**: add a `default.tsx` in each slot folder to handle navigations where the slot has no matching page (e.g., navigating to a sub-route from a different entry point).

```typescript
// src/app/(dashboard)/dashboard/@activity/default.tsx
export default function ActivityDefault() {
  return null // or a skeleton
}
```

### Intercepting Routes

Intercepting routes allow a URL to be **rendered as a modal on top of the current page** when navigated to from within the app, but as a full page when accessed directly (e.g., via direct URL, refresh, or link share).

Common use case: photo gallery, post preview, or project detail modal.

Syntax:
- `(.)route` — intercepts a route at the same level
- `(..)route` — intercepts one level up
- `(...)route` — intercepts from the root

```
src/app/(dashboard)/projects/
├── page.tsx                          # /projects — shows project grid
├── [projectId]/
│   └── page.tsx                      # /projects/:id — full page view (for direct access)
├── @modal/
│   ├── default.tsx                   # null — no modal by default
│   └── (.)projects/[projectId]/
│       └── page.tsx                  # Intercepted: renders as modal over /projects
└── layout.tsx                        # Receives @modal slot
```

```typescript
// src/app/(dashboard)/projects/layout.tsx
export default function ProjectsLayout({
  children,
  modal,
}: {
  children: React.ReactNode
  modal: React.ReactNode
}) {
  return (
    <>
      {children}
      {modal}
    </>
  )
}
```

```typescript
// src/app/(dashboard)/projects/@modal/(.)projects/[projectId]/page.tsx
import { ProjectDetailModal } from '@/features/projects/ui/project-detail-modal'
import { getProjectById } from '@/entities/project/queries'
import { notFound } from 'next/navigation'

export default async function ProjectModalPage({
  params,
}: {
  params: Promise<{ projectId: string }>
}) {
  const { projectId } = await params
  const project = await getProjectById(projectId)
  if (!project) notFound()

  return <ProjectDetailModal project={project} />
}
```

```typescript
// src/app/(dashboard)/projects/@modal/default.tsx
export default function ModalDefault() {
  return null
}
```

The modal component uses `useRouter().back()` to close:

```typescript
// src/features/projects/ui/project-detail-modal.tsx
'use client'

import { useRouter } from 'next/navigation'
import { Dialog, DialogContent } from '@/components/ui/dialog'
import type { Project } from '@/entities/project/model'

export function ProjectDetailModal({ project }: { project: Project }) {
  const router = useRouter()

  return (
    <Dialog open onOpenChange={() => router.back()}>
      <DialogContent className="max-w-2xl">
        <h1 className="text-xl font-semibold">{project.name}</h1>
        <p className="text-muted-foreground">{project.description}</p>
      </DialogContent>
    </Dialog>
  )
}
```

### Nested Layouts Within a Group

Route groups can have nested layouts without creating additional URL segments:

```
src/app/(dashboard)/settings/
├── layout.tsx          # Settings sub-navigation
├── profile/
│   └── page.tsx        # /settings/profile
└── billing/
    └── page.tsx        # /settings/billing
```

```typescript
// src/app/(dashboard)/settings/layout.tsx
import { SettingsNav } from '@/widgets/settings-nav/ui/settings-nav'

export default function SettingsLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex gap-8">
      <SettingsNav />
      <div className="flex-1 max-w-2xl">{children}</div>
    </div>
  )
}
```

## Антипаттерн

```typescript
// BAD: Checking pathname in root layout to conditionally render nav
// src/app/layout.tsx
'use client'
import { usePathname } from 'next/navigation'

export default function RootLayout({ children }) {
  const pathname = usePathname()
  const showNav = !pathname.startsWith('/login') && !pathname.startsWith('/register')
  // This forces the entire root layout to be a Client Component
  // Breaks streaming, loses RSC benefits, adds flash of incorrect UI
  return (
    <html>
      <body>
        {showNav && <Navbar />}
        {children}
      </body>
    </html>
  )
}

// BAD: Route groups without purpose — just for grouping files
// (this creates confusion about whether the group is meaningful)
src/app/
├── (pages)/           # Not a real layout boundary, just nesting for its own sake
│   ├── home/
│   └── about/
```

## Связанные документы

- `01-architecture/folder-structure.md` — Complete directory layout
- `01-architecture/data-flow.md` — How auth checks flow through layouts
- `02-patterns/auth-flow.md` — Auth.js middleware vs layout-level checks
- `02-patterns/crud-pattern.md` — Intercepting routes for create/edit modals

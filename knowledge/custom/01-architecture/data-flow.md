---
category: architecture
topic: data-flow
status: draft
---

## Проблема / Контекст

The Next.js App Router fundamentally changes how data flows through a React application. With Pages Router and client-side React, the pattern was: component mounts → `useEffect` fires → fetch from API → set state → re-render. This created waterfalls, loading spinners everywhere, and the need for TanStack Query or SWR to manage server state on the client.

App Router's default is that **components are Server Components** — they run on the server and can directly `await` database calls, without any HTTP layer. This means data flow must be rethought from first principles.

The common mistakes: adding a `useEffect` to fetch data that a Server Component could fetch directly, using Zustand to cache server data (it should only hold ephemeral UI state), and triggering full re-renders for optimistic operations that should use `useOptimistic`.

## Решение

### The Four Data Flow Patterns

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA FLOW DECISION TREE                      │
│                                                                   │
│  Is this a READ operation?                                        │
│  └─► YES → Is the data needed on initial render?                 │
│            └─► YES → Server Component, fetch directly from DB    │
│            └─► NO  → Not needed (lazy load via Suspense or skip) │
│                                                                   │
│  Is this a WRITE/MUTATION?                                        │
│  └─► YES → Is it triggered by user interaction in the browser?   │
│            └─► YES → Server Action (called from Client Component)│
│            └─► NO  → Server Component or Route Handler           │
│                                                                   │
│  Does the state affect ONLY UI? (open/close, tabs, theme)        │
│  └─► YES → Zustand store or useState                              │
│  └─► NO  → It's server state, don't put it in Zustand            │
└─────────────────────────────────────────────────────────────────┘
```

### Pattern 1: Server Component Reads Data Directly

The default and preferred pattern. No API layer. No loading state management. No caching library.

```
Browser Request
     │
     ▼
Next.js Server
     │
     ▼
┌────────────────────────────────────┐
│         layout.tsx (RSC)           │◄── awaits auth()
│                                    │
│  ┌─────────────────────────────┐   │
│  │       page.tsx (RSC)        │◄──┼── awaits db.query.projects...
│  │                             │   │
│  │  ┌──────────────────────┐  │   │
│  │  │ ProjectList (RSC)    │◄─┼───┼── receives projects as props
│  │  │                      │  │   │
│  │  │  ┌───────────────┐   │  │   │
│  │  │  │ ProjectCard   │   │  │   │
│  │  │  │ (RSC or CC)   │   │  │   │
│  │  │  └───────────────┘   │  │   │
│  │  └──────────────────────┘  │   │
│  └─────────────────────────────┘   │
└────────────────────────────────────┘
     │
     ▼
  HTML + RSC Payload → Browser
```

```typescript
// src/app/(dashboard)/projects/page.tsx
import { auth } from '@/server/auth'
import { getProjectsByUserId } from '@/entities/project/queries'
import { ProjectList } from '@/features/projects/ui/project-list'
import { redirect } from 'next/navigation'

export default async function ProjectsPage() {
  const session = await auth()
  if (!session?.user?.id) redirect('/login')

  // Direct DB call — no fetch(), no useSWR, no TanStack Query
  const projects = await getProjectsByUserId(session.user.id)

  return (
    <div>
      <h1 className="text-2xl font-bold">Projects</h1>
      <ProjectList projects={projects} />
    </div>
  )
}
```

```typescript
// src/entities/project/queries.ts
import 'server-only'
import { db } from '@/server/db'
import { projects } from '@/server/db/schema'
import { eq, desc } from 'drizzle-orm'

export async function getProjectsByUserId(userId: string) {
  return db.query.projects.findMany({
    where: eq(projects.userId, userId),
    orderBy: [desc(projects.createdAt)],
    with: { members: true },
  })
}
```

### Pattern 2: Parallel Data Fetching to Avoid Waterfalls

Multiple independent data needs in one page: use `Promise.all`.

```
WITHOUT Promise.all (waterfall):
────────────────────────────────►
await getUser()          [200ms]
                         await getProjects()    [150ms]
                                                await getSubscription() [100ms]
Total: 450ms

WITH Promise.all (parallel):
────────────────────────────────►
await getUser()     [200ms]─────────────────────┐
await getProjects() [150ms]──────────┐          │
await getSubscription() [100ms]──┐  │          │
                                  ▼  ▼          ▼
Total: 200ms (limited by slowest)
```

```typescript
// src/app/(dashboard)/dashboard/page.tsx
import { auth } from '@/server/auth'
import { getProjectsByUserId } from '@/entities/project/queries'
import { getSubscriptionByUserId } from '@/entities/subscription/queries'
import { getRecentActivity } from '@/entities/activity/queries'
import { redirect } from 'next/navigation'

export default async function DashboardPage() {
  const session = await auth()
  if (!session?.user?.id) redirect('/login')

  // All three queries run in parallel
  const [projects, subscription, activity] = await Promise.all([
    getProjectsByUserId(session.user.id),
    getSubscriptionByUserId(session.user.id),
    getRecentActivity(session.user.id, { limit: 10 }),
  ])

  return (
    <div className="grid grid-cols-3 gap-6">
      <ProjectStats projects={projects} />
      <SubscriptionStatus subscription={subscription} />
      <ActivityFeed activity={activity} />
    </div>
  )
}
```

### Pattern 3: Streaming with Suspense

For slow data that should not block the initial render, wrap in `<Suspense>`. The fast parts stream immediately; slow parts stream when ready.

```
Initial Response (fast):
┌──────────────────────────────┐
│  Layout, Header, Shell HTML  │  → streams immediately
│  <Suspense fallback={...}>   │
│    [skeleton placeholder]    │  → visible while waiting
│  </Suspense>                 │
└──────────────────────────────┘

Streamed Later (slow data ready):
┌──────────────────────────────┐
│  [actual component HTML]     │  → replaces skeleton
└──────────────────────────────┘
```

```typescript
// src/app/(dashboard)/dashboard/page.tsx
import { Suspense } from 'react'
import { ProjectListSkeleton } from '@/features/projects/ui/project-list-skeleton'
import { SlowAnalyticsWidget } from '@/widgets/analytics/ui/analytics-widget'
import { FastProjectList } from '@/widgets/project-list/ui/project-list'

export default async function DashboardPage() {
  // FastProjectList fetches its own data internally (no prop drilling needed)
  return (
    <div className="space-y-6">
      {/* Renders immediately — fast query */}
      <Suspense fallback={<ProjectListSkeleton />}>
        <FastProjectList />
      </Suspense>

      {/* Streams in later — slow aggregation query */}
      <Suspense fallback={<div className="h-32 animate-pulse rounded-lg bg-muted" />}>
        <SlowAnalyticsWidget />
      </Suspense>
    </div>
  )
}
```

```typescript
// The component fetches its own data — colocated data fetching
// src/widgets/project-list/ui/project-list.tsx
import { auth } from '@/server/auth'
import { getProjectsByUserId } from '@/entities/project/queries'
import { ProjectCard } from '@/entities/project/ui/project-card'
import { redirect } from 'next/navigation'

export async function FastProjectList() {
  const session = await auth()
  if (!session?.user?.id) redirect('/login')
  const projects = await getProjectsByUserId(session.user.id)
  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {projects.map((p) => <ProjectCard key={p.id} project={p} />)}
    </div>
  )
}
```

### Pattern 4: Server Actions for Mutations

Client Components call Server Actions. The action runs on the server, mutates the DB, then invalidates the cache.

```
Client Component
     │
     │  calls action (RPC-like, no fetch needed)
     ▼
┌────────────────────────────────┐
│      Server Action             │
│  1. auth() — verify session    │
│  2. zod.parse — validate input │
│  3. db.insert/update/delete    │
│  4. revalidatePath/Tag         │
│  5. return ActionResult<T>     │
└────────────────────────────────┘
     │
     │  returns to client
     ▼
Client Component
  - receives { success, data } or { success: false, error }
  - updates local UI state if needed
  - Next.js router auto-refreshes the page segment
```

```typescript
// src/features/projects/actions.ts
'use server'
import { auth } from '@/server/auth'
import { db } from '@/server/db'
import { projects } from '@/server/db/schema'
import { revalidatePath } from 'next/cache'
import { createProjectSchema } from './schemas'
import type { ActionResult } from '@/types/api'
import { z } from 'zod'

export async function createProject(
  input: z.infer<typeof createProjectSchema>
): Promise<ActionResult<{ id: string }>> {
  const session = await auth()
  if (!session?.user?.id) return { success: false, error: 'Unauthorized' }

  const parsed = createProjectSchema.safeParse(input)
  if (!parsed.success) {
    return {
      success: false,
      error: 'Validation failed',
      fieldErrors: parsed.error.flatten().fieldErrors as Record<string, string[]>,
    }
  }

  const [project] = await db
    .insert(projects)
    .values({ ...parsed.data, userId: session.user.id })
    .returning({ id: projects.id })

  // Invalidate the projects list — Next.js will refetch on next visit
  revalidatePath('/projects')

  return { success: true, data: { id: project.id } }
}
```

### Cache Invalidation Strategy

```
revalidatePath('/projects')
  → Marks the cached RSC output for /projects as stale
  → Next request to /projects will re-run the Server Component

revalidatePath('/projects', 'layout')
  → Invalidates the layout.tsx and all its children

revalidateTag('projects')
  → Invalidates all fetch() calls tagged with 'projects'
  → Use with: fetch(url, { next: { tags: ['projects'] } })

When to use which:
  revalidatePath  → after mutations that affect a specific page
  revalidateTag   → for shared data used across multiple pages
                    (e.g., subscription status shown in navbar + settings)
```

```typescript
// Tagging fetch calls (for external APIs, not Drizzle)
const data = await fetch('https://api.github.com/repos/...', {
  next: { tags: ['github-repo'], revalidate: 3600 }
})

// Invalidating a tag from a Server Action
import { revalidateTag } from 'next/cache'
revalidateTag('github-repo') // refreshes all fetches with this tag
```

### Zustand — UI State Only

Zustand is for ephemeral browser state that has no server representation. Never put database-derived data into Zustand.

```typescript
// src/store/ui-store.ts
import { create } from 'zustand'

// CORRECT: UI-only state
interface UIStore {
  sidebarOpen: boolean
  setSidebarOpen: (open: boolean) => void
  toggleSidebar: () => void

  activeModal: string | null
  openModal: (id: string) => void
  closeModal: () => void
}

export const useUIStore = create<UIStore>((set) => ({
  sidebarOpen: true,
  setSidebarOpen: (open) => set({ sidebarOpen: open }),
  toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),

  activeModal: null,
  openModal: (id) => set({ activeModal: id }),
  closeModal: () => set({ activeModal: null }),
}))
```

```typescript
// WRONG: server data in Zustand
interface ProjectStore {
  projects: Project[]           // ❌ This is server state
  fetchProjects: () => void     // ❌ useEffect + fetch anti-pattern
  setProjects: (p: Project[]) => void
}
// Projects should come from Server Component props, not a Zustand fetch
```

### Passing Server Data to Client Components

Server Components fetch the data; Client Components receive it as props. This is the correct boundary.

```typescript
// Server Component — fetches data
// src/app/(dashboard)/projects/page.tsx
import { getProjectsByUserId } from '@/entities/project/queries'
import { ProjectFilters } from '@/features/projects/ui/project-filters' // 'use client'

export default async function ProjectsPage() {
  const session = await auth()
  const projects = await getProjectsByUserId(session!.user.id)

  // Pass serializable data (plain objects, no class instances) to Client Component
  return <ProjectFilters initialProjects={projects} />
}
```

```typescript
// Client Component — manages UI state with received data
// src/features/projects/ui/project-filters.tsx
'use client'
import { useState } from 'react'
import type { Project } from '@/entities/project/model'

interface ProjectFiltersProps {
  initialProjects: Project[]
}

export function ProjectFilters({ initialProjects }: ProjectFiltersProps) {
  const [filter, setFilter] = useState<'all' | 'active' | 'archived'>('all')

  const filtered = initialProjects.filter((p) => {
    if (filter === 'all') return true
    return p.status === filter
  })

  // filter state is local UI state — no Zustand, no server call needed
  return (
    <div>
      <FilterTabs value={filter} onChange={setFilter} />
      <ProjectGrid projects={filtered} />
    </div>
  )
}
```

## Антипаттерн

```typescript
// BAD 1: useEffect + fetch in a component that could be a Server Component
'use client'
export default function ProjectsPage() {
  const [projects, setProjects] = useState([])
  useEffect(() => {
    fetch('/api/projects').then(r => r.json()).then(setProjects)
  }, [])
  // This causes: loading flicker, extra round-trip, SEO issues, waterfall
}

// BAD 2: Storing server data in Zustand
const useProjectStore = create((set) => ({
  projects: [],
  fetchProjects: async () => {
    const res = await fetch('/api/projects')
    set({ projects: await res.json() })
  }
}))
// This duplicates cache management Next.js already handles

// BAD 3: Sequential awaits when parallel is possible
export default async function DashboardPage() {
  const user = await getUser()          // waits 200ms
  const projects = await getProjects()  // waits AFTER user (150ms)
  const sub = await getSub()            // waits AFTER projects (100ms)
  // Total: 450ms instead of 200ms
}

// BAD 4: Calling a Server Action from a Server Component
// src/app/(dashboard)/projects/page.tsx
export default async function ProjectsPage() {
  await createProject({ name: 'Default' }) // Server Actions are for CLIENT→SERVER calls
  // Fetch data with Drizzle directly, or call the query function
}
```

## Связанные документы

- `01-architecture/api-design.md` — Route Handlers vs Server Actions decision
- `02-patterns/crud-pattern.md` — Full CRUD data flow implementation
- `02-patterns/optimistic-ui.md` — useOptimistic with Server Actions
- `01-architecture/folder-structure.md` — Where queries and actions live

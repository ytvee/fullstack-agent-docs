---
category: architecture
topic: feature-sliced-design
status: draft
---

## Проблема / Контекст

As Next.js App Router projects grow, the default file-system routing encourages dumping everything near the route that uses it. This leads to implicit coupling: a `ProjectCard` component in `app/(dashboard)/projects/_components/` gets imported by a `RecentProjects` widget on the dashboard page, which imports from the billing feature to check upgrade prompts. Circular imports, spaghetti dependencies, and no clear ownership.

Feature-Sliced Design (FSD) is an architectural methodology that imposes a **strict unidirectional dependency rule**: higher layers can import from lower layers, but never vice versa. This makes the codebase scalable and allows teams to own vertical slices of the product without stepping on each other.

The challenge is mapping FSD's layer model onto Next.js App Router's file-system routing, which does not naturally enforce import direction.

## Решение

### FSD Layers — Mapped to Next.js

FSD defines 7 layers (top = highest abstraction, bottom = lowest):

```
app        →  src/app/              (Next.js routing, layouts, providers)
pages      →  src/app/(groups)/     (individual route page.tsx files)
widgets    →  src/widgets/          (composite UI blocks, route-agnostic)
features   →  src/features/         (user-facing capabilities with actions)
entities   →  src/entities/         (business domain objects + their UI)
shared     →  src/lib/, src/components/ui/, src/types/, src/hooks/
```

**Import rule**: A module at layer N may only import from layers N+1, N+2, … (lower layers). Never upward.

```
app
 └─ can import → pages, widgets, features, entities, shared
pages
 └─ can import → widgets, features, entities, shared
widgets
 └─ can import → features, entities, shared
features
 └─ can import → entities, shared
entities
 └─ can import → shared
shared
 └─ can import → nothing (only external packages)
```

### Layer Definitions in Practice

**`shared`** — Zero business logic. Framework-agnostic utilities, design system primitives, type definitions.
```
src/lib/utils.ts           — cn(), formatCurrency(), formatDate()
src/lib/constants.ts       — PLANS, ROUTES, APP_NAME
src/components/ui/         — shadcn/ui components
src/types/api.ts           — ApiResponse<T>, ActionResult<T>
src/hooks/use-debounce.ts  — generic client hooks
```

**`entities`** — A business domain object: its data shape, database queries, and passive UI representation. No mutations.
```
src/entities/user/
  ├── model.ts         — Drizzle select type, Zod schema, derived helpers
  ├── queries.ts       — getUserById, getUserByEmail (read-only)
  └── ui/
      ├── user-avatar.tsx
      └── user-badge.tsx

src/entities/project/
  ├── model.ts
  ├── queries.ts       — getProjectById, getProjectsByOrgId
  └── ui/
      └── project-status-badge.tsx

src/entities/subscription/
  ├── model.ts         — Plan type, status helpers, isActive(), isPro()
  ├── queries.ts       — getSubscriptionByUserId
  └── ui/
      └── plan-badge.tsx
```

**`features`** — A user-facing capability: a form, a button that triggers an action, a toggle. Composes entities.
```
src/features/auth/
  ├── login/
  │   ├── ui/login-form.tsx
  │   ├── actions.ts       — signInWithCredentials()
  │   └── schemas.ts
  ├── register/
  │   ├── ui/register-form.tsx
  │   ├── actions.ts
  │   └── schemas.ts
  └── oauth/
      └── ui/oauth-buttons.tsx

src/features/project-create/
  ├── ui/create-project-form.tsx
  ├── actions.ts             — createProject()
  └── schemas.ts

src/features/project-delete/
  ├── ui/delete-project-button.tsx
  └── actions.ts             — deleteProject()

src/features/billing/
  ├── upgrade/
  │   ├── ui/upgrade-button.tsx
  │   └── actions.ts         — createCheckoutSession()
  ├── portal/
  │   ├── ui/manage-billing-button.tsx
  │   └── actions.ts         — createPortalSession()
  └── cancel/
      ├── ui/cancel-subscription-dialog.tsx
      └── actions.ts
```

**`widgets`** — Composed UI blocks that assemble multiple features and entities for a specific section of the screen. Route-agnostic.
```
src/widgets/
  ├── project-list/
  │   └── ui/project-list.tsx    — uses entities/project + features/project-delete
  ├── billing-overview/
  │   └── ui/billing-overview.tsx — uses entities/subscription + features/billing/*
  ├── dashboard-header/
  │   └── ui/dashboard-header.tsx
  └── settings-nav/
      └── ui/settings-nav.tsx
```

**`pages`** (route pages) — Thin orchestrators. Fetch data, pass it to widgets.
```typescript
// src/app/(dashboard)/dashboard/page.tsx
import { auth } from '@/server/auth'
import { getProjectsByOrgId } from '@/entities/project/queries'
import { getSubscriptionByUserId } from '@/entities/subscription/queries'
import { ProjectList } from '@/widgets/project-list/ui/project-list'
import { BillingOverview } from '@/widgets/billing-overview/ui/billing-overview'
import { redirect } from 'next/navigation'

export default async function DashboardPage() {
  const session = await auth()
  if (!session?.user) redirect('/login')

  const [projects, subscription] = await Promise.all([
    getProjectsByOrgId(session.user.orgId),
    getSubscriptionByUserId(session.user.id),
  ])

  return (
    <main className="space-y-8 p-6">
      <BillingOverview subscription={subscription} />
      <ProjectList projects={projects} />
    </main>
  )
}
```

### Full Billing Feature Slice — Complete Example

The billing slice spans entities, features, and widgets. Here is the complete vertical cut:

**Entity: `src/entities/subscription/model.ts`**
```typescript
import { subscriptions } from '@/server/db/schema'
import { InferSelectModel } from 'drizzle-orm'
import { z } from 'zod'

export type Subscription = InferSelectModel<typeof subscriptions>

export const PLANS = {
  FREE: 'free',
  PRO: 'pro',
  ENTERPRISE: 'enterprise',
} as const

export type Plan = (typeof PLANS)[keyof typeof PLANS]

export function isActive(subscription: Subscription | null): boolean {
  if (!subscription) return false
  return subscription.status === 'active' || subscription.status === 'trialing'
}

export function isPro(subscription: Subscription | null): boolean {
  return isActive(subscription) && subscription?.plan === PLANS.PRO
}

export function getTrialDaysLeft(subscription: Subscription | null): number {
  if (!subscription?.trialEndsAt) return 0
  const diff = subscription.trialEndsAt.getTime() - Date.now()
  return Math.max(0, Math.ceil(diff / (1000 * 60 * 60 * 24)))
}
```

**Entity: `src/entities/subscription/queries.ts`**
```typescript
import 'server-only'
import { db } from '@/server/db'
import { subscriptions } from '@/server/db/schema'
import { eq } from 'drizzle-orm'
import type { Subscription } from './model'

export async function getSubscriptionByUserId(
  userId: string
): Promise<Subscription | null> {
  const result = await db.query.subscriptions.findFirst({
    where: eq(subscriptions.userId, userId),
  })
  return result ?? null
}
```

**Feature: `src/features/billing/upgrade/actions.ts`**
```typescript
'use server'

import { auth } from '@/server/auth'
import { stripe } from '@/lib/stripe'
import { db } from '@/server/db'
import { subscriptions } from '@/server/db/schema'
import { eq } from 'drizzle-orm'
import { redirect } from 'next/navigation'
import { z } from 'zod'
import type { ActionResult } from '@/types/api'

const upgradeSchema = z.object({
  priceId: z.string().min(1),
  successUrl: z.string().url().optional(),
  cancelUrl: z.string().url().optional(),
})

export async function createCheckoutSession(
  input: z.infer<typeof upgradeSchema>
): Promise<ActionResult<{ url: string }>> {
  const session = await auth()
  if (!session?.user?.id) {
    return { success: false, error: 'Unauthorized' }
  }

  const parsed = upgradeSchema.safeParse(input)
  if (!parsed.success) {
    return { success: false, error: 'Invalid input' }
  }

  const existing = await db.query.subscriptions.findFirst({
    where: eq(subscriptions.userId, session.user.id),
  })

  const checkoutSession = await stripe.checkout.sessions.create({
    customer: existing?.stripeCustomerId ?? undefined,
    customer_email: existing?.stripeCustomerId ? undefined : session.user.email!,
    mode: 'subscription',
    line_items: [{ price: parsed.data.priceId, quantity: 1 }],
    success_url:
      parsed.data.successUrl ?? `${process.env.NEXT_PUBLIC_APP_URL}/settings/billing?success=1`,
    cancel_url:
      parsed.data.cancelUrl ?? `${process.env.NEXT_PUBLIC_APP_URL}/settings/billing`,
    metadata: { userId: session.user.id },
    subscription_data: {
      trial_period_days: existing ? undefined : 14,
    },
  })

  if (!checkoutSession.url) {
    return { success: false, error: 'Failed to create checkout session' }
  }

  return { success: true, data: { url: checkoutSession.url } }
}
```

**Feature: `src/features/billing/upgrade/ui/upgrade-button.tsx`**
```typescript
'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { createCheckoutSession } from '../actions'
import { toast } from 'sonner'

interface UpgradeButtonProps {
  priceId: string
  label?: string
  className?: string
}

export function UpgradeButton({
  priceId,
  label = 'Upgrade to Pro',
  className,
}: UpgradeButtonProps) {
  const [loading, setLoading] = useState(false)

  async function handleUpgrade() {
    setLoading(true)
    const result = await createCheckoutSession({ priceId })
    if (result.success) {
      window.location.href = result.data.url
    } else {
      toast.error(result.error)
      setLoading(false)
    }
  }

  return (
    <Button onClick={handleUpgrade} disabled={loading} className={className}>
      {loading ? 'Redirecting…' : label}
    </Button>
  )
}
```

**Widget: `src/widgets/billing-overview/ui/billing-overview.tsx`**
```typescript
import { isPro, isActive, getTrialDaysLeft } from '@/entities/subscription/model'
import type { Subscription } from '@/entities/subscription/model'
import { PlanBadge } from '@/entities/subscription/ui/plan-badge'
import { UpgradeButton } from '@/features/billing/upgrade/ui/upgrade-button'
import { ManageBillingButton } from '@/features/billing/portal/ui/manage-billing-button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { env } from '@/lib/env'

interface BillingOverviewProps {
  subscription: Subscription | null
}

export function BillingOverview({ subscription }: BillingOverviewProps) {
  const active = isActive(subscription)
  const pro = isPro(subscription)
  const trialDays = getTrialDaysLeft(subscription)

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          Billing
          <PlanBadge subscription={subscription} />
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {!active && (
          <p className="text-sm text-muted-foreground">
            You are on the free plan. Upgrade to unlock all features.
          </p>
        )}
        {trialDays > 0 && (
          <p className="text-sm text-amber-600">
            {trialDays} days left in your trial.
          </p>
        )}
        <div className="flex gap-2">
          {!pro && <UpgradeButton priceId={env.NEXT_PUBLIC_PRO_PRICE_ID} />}
          {active && <ManageBillingButton />}
        </div>
      </CardContent>
    </Card>
  )
}
```

### Enforcing Import Rules with ESLint

Add `eslint-plugin-boundaries` or use path alias conventions to detect violations:

```javascript
// eslint.config.mjs
import boundaries from 'eslint-plugin-boundaries'

export default [
  {
    plugins: { boundaries },
    rules: {
      'boundaries/element-types': [
        'error',
        {
          // entities cannot import from features or widgets
          default: 'disallow',
          rules: [
            { from: 'shared', allow: [] },
            { from: 'entities', allow: ['shared'] },
            { from: 'features', allow: ['entities', 'shared'] },
            { from: 'widgets', allow: ['features', 'entities', 'shared'] },
            { from: 'pages', allow: ['widgets', 'features', 'entities', 'shared'] },
            { from: 'app', allow: ['pages', 'widgets', 'features', 'entities', 'shared'] },
          ],
        },
      ],
    },
  },
]
```

## Антипаттерн

```typescript
// BAD: features/billing importing from features/auth
// features/billing/upgrade/actions.ts
import { getCurrentUser } from '@/features/auth/queries'  // VIOLATION: feature → feature

// BAD: entities importing from features
// entities/project/model.ts
import { deleteProject } from '@/features/project-delete/actions'  // VIOLATION

// BAD: widget importing from another widget
// widgets/dashboard-stats/ui/dashboard-stats.tsx
import { BillingOverview } from '@/widgets/billing-overview/ui/billing-overview'  // VIOLATION

// CORRECT: all three should go through shared or restructure into a higher layer
```

Cross-feature communication should happen at the **widget or page layer**, not by direct import between features.

## Связанные документы

- `01-architecture/folder-structure.md` — Full directory tree reference
- `01-architecture/data-flow.md` — Where data fetching belongs in each layer
- `02-patterns/crud-pattern.md` — CRUD implemented as a feature slice
- `02-patterns/auth-flow.md` — Auth as an entity + feature combo

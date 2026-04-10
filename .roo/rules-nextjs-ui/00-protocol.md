# UI Mode — Operating Protocol

You build accessible interfaces with Tailwind CSS and shadcn/ui.

## Before building any component

Check `src/components/ui/` for existing shadcn components to reuse.
Do not reinvent `Button`, `Input`, `Dialog`, `Card`, `Sheet`, etc.

To add a missing component:
```bash
npx shadcn@latest add [component-name]
```
Never copy-paste shadcn source manually. Never edit files in `src/components/ui/` directly.

Read `.roo/skills/shadcn-component/SKILL.md` before any shadcn-related work.

## Component structure

```typescript
// Named export — never default export
export function FeatureCard({ ... }: FeatureCardProps) { ... }

// Co-located skeleton — same file or same directory
export function FeatureCardSkeleton() {
  return <div className="h-24 w-full animate-pulse rounded-lg bg-muted" />
}
```

Props should be minimal. Data fetching belongs in the Server Component parent.

## Accessibility checklist

Before completing any component:

- [ ] All `<Image>` have meaningful `alt` text (or `alt=""` if decorative)
- [ ] Form inputs have `<label htmlFor>` or `aria-label`
- [ ] Interactive elements have visible focus ring: `focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2`
- [ ] Color is not the only way to convey information (add icon or text alongside color)
- [ ] Heading hierarchy is logical: `h1 → h2 → h3` (no skipped levels)
- [ ] Buttons have descriptive text or `aria-label` (not just "Click here")

## Styling rules

- Tailwind only — no `style={{}}` except CSS variables for dynamic values (e.g., heights calculated in JS)
- No `.css` or `.scss` files
- Dark mode: use `dark:` variant and shadcn semantic tokens (`bg-background`, `text-foreground`, `text-muted-foreground`)
- Never hardcode color values (`bg-[#3b82f6]`) — use Tailwind palette or CSS variables

## Animation rules

```typescript
// Simple transitions — Tailwind
className="transition-colors duration-200"

// Complex animations — Framer Motion, only in 'use client' components
// Respect reduced motion
className="motion-safe:animate-fade-in"
```

## LCP images

Any image above the fold must have `priority`:

```typescript
<Image src="/hero.jpg" alt="Hero" width={1200} height={600} priority />
```

Omitting `priority` on an LCP image is a REQUEST CHANGES issue in review.

## Heavy libraries

Rich-text editors, date pickers, charts, maps — load via `next/dynamic` with `ssr: false`,
inside a Client Component wrapper. Never import them directly in a Server Component.

```typescript
'use client'
import dynamic from 'next/dynamic'

const RichEditor = dynamic(() => import('./RichEditor'), {
  ssr: false,
  loading: () => <Skeleton className="h-64 w-full" />,
})
```

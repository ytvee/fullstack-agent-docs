---
name: shadcn-component
description: Installs and customizes shadcn/ui components in Next.js projects. Handles npx shadcn add commands, component wrapping patterns, cn() utility usage, CSS variable theming, and cva variants. Triggers on requests like "add a button component", "install shadcn", "customize shadcn theme", "create component variant", "add dialog", "use cn utility", "make a card component".
---

## Installing components

Always install via CLI. Never copy-paste component code manually.

```bash
npx shadcn@latest add <component-name>
```

Common components:

```bash
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
npx shadcn@latest add form
npx shadcn@latest add input
npx shadcn@latest add label
npx shadcn@latest add select
npx shadcn@latest add sheet
npx shadcn@latest add table
npx shadcn@latest add toast
npx shadcn@latest add dropdown-menu
npx shadcn@latest add avatar
npx shadcn@latest add badge
npx shadcn@latest add separator
npx shadcn@latest add skeleton
npx shadcn@latest add tabs
npx shadcn@latest add textarea
npx shadcn@latest add tooltip
```

Full list: `npx shadcn@latest add --help`

Initial setup (if not done): `npx shadcn@latest init`

## Where components live

Installed components go to `src/components/ui/`. Do not edit these files directly. Updates via `npx shadcn@latest add` will overwrite manual changes.

Custom logic belongs in wrappers stored in `src/components/` (not inside `ui/`).

## Importing components

Always import from the local path, never from a package named `shadcn/ui`:

```typescript
// Correct
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

// Wrong — this package does not exist
import { Button } from 'shadcn/ui'
```

## cn() utility

Use `cn()` from `@/lib/utils` whenever combining class names. It merges Tailwind classes correctly and handles conflicts:

```typescript
import { cn } from '@/lib/utils'

function MyComponent({ className, isActive }: { className?: string; isActive: boolean }) {
  return (
    <div
      className={cn(
        'rounded-lg border p-4',
        isActive && 'border-blue-500 bg-blue-50',
        className
      )}
    />
  )
}
```

Never use template literals or `clsx` directly if `cn` is available — `cn` already wraps `clsx` and `tailwind-merge`.

## Wrapping components

Extend shadcn components with wrappers instead of editing source files:

```typescript
// src/components/ui/button-link.tsx
import { Button, ButtonProps } from '@/components/ui/button'
import Link from 'next/link'

interface ButtonLinkProps extends ButtonProps {
  href: string
}

export function ButtonLink({ href, children, ...props }: ButtonLinkProps) {
  return (
    <Button asChild {...props}>
      <Link href={href}>{children}</Link>
    </Button>
  )
}
```

Use `asChild` when you need a shadcn component to render as a different element. The `asChild` prop delegates rendering to the child element while keeping the component's styles and behavior.

```typescript
// Button that renders as an anchor tag
<Button asChild>
  <a href="https://example.com">External link</a>
</Button>
```

## CSS variable theming

Shadcn uses CSS variables defined in `src/app/globals.css`. Customize the theme by overriding these variables:

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --accent: 210 40% 96.1%;
  --accent-foreground: 222.2 47.4% 11.2%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;
  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;
  --radius: 0.5rem;
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --primary: 210 40% 98%;
  --primary-foreground: 222.2 47.4% 11.2%;
  /* ... rest of dark variables */
}
```

Values are in HSL format without the `hsl()` wrapper. Tailwind reads them as `hsl(var(--primary))`.

See [docs/customization.md](docs/customization.md) for a full theming guide and how to use the shadcn theme generator.

## Variants with cva

`class-variance-authority` is installed as a shadcn dependency. Use it to create components with multiple visual variants:

```typescript
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const alertVariants = cva(
  'relative w-full rounded-lg border p-4',
  {
    variants: {
      variant: {
        default: 'bg-background text-foreground',
        destructive: 'border-destructive/50 text-destructive',
        success: 'border-green-500/50 text-green-700',
      },
      size: {
        sm: 'p-2 text-sm',
        default: 'p-4',
        lg: 'p-6 text-lg',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)

interface AlertProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof alertVariants> {}

export function Alert({ className, variant, size, ...props }: AlertProps) {
  return (
    <div className={cn(alertVariants({ variant, size }), className)} {...props} />
  )
}
```

## Common mistakes

**Never edit files in `src/components/ui/` directly.** Running `npx shadcn@latest add` again will overwrite the file. Create wrappers in `src/components/` instead.

**Use `asChild` for polymorphic rendering.** When you need a `Button` to render as a `Link` or `a`, pass `asChild` and wrap the target element as a child. Do not create separate button variants that duplicate styles.

**Do not install `shadcn/ui` as a package.** There is no npm package called `shadcn/ui`. Components are added to your source code via the CLI. Imports come from `@/components/ui/`.

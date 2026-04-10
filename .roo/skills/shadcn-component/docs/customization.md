# shadcn/ui customization guide

## Theme generator

Use the official shadcn theme generator to create a custom palette: visit the shadcn/ui documentation site and navigate to the Themes section. Copy the generated CSS variables and paste them into your `src/app/globals.css`, replacing the existing `:root` and `.dark` blocks.

## CSS variable format

All color values use HSL components without the `hsl()` wrapper. Tailwind reads them as `hsl(var(--variable))`.

```css
/* Correct */
--primary: 222.2 47.4% 11.2%;

/* Wrong */
--primary: hsl(222.2, 47.4%, 11.2%);
--primary: #1c2b4a;
```

## Full variable list

```css
:root {
  /* Base */
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;

  /* Card */
  --card: 0 0% 100%;
  --card-foreground: 222.2 84% 4.9%;

  /* Popover */
  --popover: 0 0% 100%;
  --popover-foreground: 222.2 84% 4.9%;

  /* Brand */
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;

  /* Secondary */
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;

  /* Muted */
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;

  /* Accent */
  --accent: 210 40% 96.1%;
  --accent-foreground: 222.2 47.4% 11.2%;

  /* Destructive */
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;

  /* Borders and inputs */
  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;

  /* Radius — affects all rounded-* values in components */
  --radius: 0.5rem;
}
```

## Dark mode

Shadcn uses the `class` strategy with `next-themes`. Install and configure:

```bash
npm install next-themes
```

```typescript
// src/app/providers.tsx
'use client'
import { ThemeProvider } from 'next-themes'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
      {children}
    </ThemeProvider>
  )
}
```

```typescript
// src/app/layout.tsx
import { Providers } from './providers'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
```

`suppressHydrationWarning` on `<html>` is required to prevent React hydration errors when the theme class is applied on the client.

## Theme toggle component

```typescript
// src/components/theme-toggle.tsx
'use client'
import { useTheme } from 'next-themes'
import { Button } from '@/components/ui/button'

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()

  return (
    <Button
      variant="outline"
      size="icon"
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
    >
      {theme === 'dark' ? 'Light' : 'Dark'}
    </Button>
  )
}
```

## Adding custom colors

Extend the palette by adding new CSS variables and mapping them in `tailwind.config.ts`:

```css
/* globals.css */
:root {
  --brand: 262 80% 50%;
  --brand-foreground: 0 0% 100%;
}

.dark {
  --brand: 262 80% 65%;
  --brand-foreground: 0 0% 100%;
}
```

```typescript
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        brand: 'hsl(var(--brand))',
        'brand-foreground': 'hsl(var(--brand-foreground))',
      },
    },
  },
}
```

Use in components: `<div className="bg-brand text-brand-foreground" />`.

## Changing border radius

The `--radius` variable controls the base radius. Components use fractions of it:

```css
:root {
  --radius: 0.75rem;  /* Rounder */
}
```

```css
:root {
  --radius: 0.25rem;  /* Sharper */
}
```

Setting `--radius: 0` gives square components throughout.

## Font customization

Shadcn does not set fonts. Add fonts in `src/app/layout.tsx` using `next/font`:

```typescript
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'], variable: '--font-sans' })

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="font-sans">{children}</body>
    </html>
  )
}
```

Then in `tailwind.config.ts`:

```typescript
fontFamily: {
  sans: ['var(--font-sans)', ...defaultTheme.fontFamily.sans],
}
```

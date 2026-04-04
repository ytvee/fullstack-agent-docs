---
category: accessibility
topic: wcag-checklist
status: draft
---

## Проблема / Контекст

WCAG 2.2 AA is the legal baseline in most jurisdictions (EU, US ADA, UK Equality Act). Beyond legal compliance, accessible apps have better SEO, work better on mobile, and serve a user base that is 15-20% larger (disabled users globally). Next.js App Router and shadcn/ui provide a solid foundation, but automated tools catch only ~30% of accessibility issues — the rest requires developer knowledge.

---

## Решение

### 1. Perceivable

**1.1 Alt text for images:**

```typescript
// next/image requires alt prop — but the VALUE matters

// BAD: unhelpful or missing alt
<Image src="/user-profile.jpg" alt="image" width={40} height={40} />
<Image src="/product.jpg" alt="" width={400} height={300} /> // wrong use of empty alt

// GOOD: descriptive alt for informative images
<Image src="/checkout-flow.png" alt="Three-step checkout: cart, shipping, payment" width={400} height={300} />

// GOOD: empty alt (role="presentation") for decorative images
// The icon next to the button label is decorative — the button label provides the meaning
<Image src="/decorative-swoosh.svg" alt="" width={100} height={20} aria-hidden={true} />

// GOOD: user avatar — describe the function, not the appearance
<Image
  src={user.avatarUrl}
  alt={`${user.name}'s profile picture`}
  width={40}
  height={40}
  className="rounded-full"
/>

// RULE: If an image conveys information that isn't in surrounding text, it needs alt text.
// If the image is purely decorative, use alt="" AND aria-hidden="true".
```

**1.3 Color contrast — minimum 4.5:1 for normal text, 3:1 for large text:**

```typescript
// Tailwind v4 — use colors that meet contrast in both light and dark mode
// shadcn/ui's default palette is designed to meet 4.5:1

// Check your custom colors:
// https://webaim.org/resources/contrastchecker/

// Common failure: gray text on white background
// text-gray-400 on white = 2.85:1 — FAILS AA
// text-gray-600 on white = 5.74:1 — PASSES AA

// Tailwind v4 CSS variable approach:
// globals.css
:root {
  --color-text-muted: oklch(0.5 0 0); /* verify contrast before using */
}

// For non-text elements (icons, borders): minimum 3:1
```

**1.4 Captions for video content:**

```typescript
// Always provide captions for video/audio content
<video controls>
  <source src="/demo.mp4" type="video/mp4" />
  <track
    kind="captions"
    src="/demo-captions-en.vtt"
    srcLang="en"
    label="English"
    default
  />
  Your browser does not support video.
</video>
```

---

### 2. Operable

**2.1 Keyboard navigation — everything clickable must be keyboard reachable:**

```typescript
// ALL interactive elements must be reachable with Tab
// and activatable with Enter/Space

// BAD: onClick on a non-interactive element
<div onClick={handleSelect} className="cursor-pointer">Select option</div>
// A keyboard user cannot Tab to this, and screen readers won't announce it as interactive

// GOOD: use semantic elements or add correct ARIA
<button onClick={handleSelect} className="cursor-pointer">Select option</button>

// If you MUST use a div (e.g., for specific styling reasons):
<div
  role="button"
  tabIndex={0}
  onClick={handleSelect}
  onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") handleSelect(); }}
  className="cursor-pointer"
>
  Select option
</div>
```

**2.4 Focus management for dynamic content:**

```typescript
// After a modal opens, focus must move to the first interactive element inside
// shadcn/ui Dialog handles this automatically via Radix UI

// For custom navigation/drawer:
"use client";
import { useEffect, useRef } from "react";

interface DrawerProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export function Drawer({ isOpen, onClose, children }: DrawerProps) {
  const firstFocusableRef = useRef<HTMLButtonElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement as HTMLElement;
      firstFocusableRef.current?.focus();
    } else {
      // Return focus to the trigger when closing
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div role="dialog" aria-modal="true" aria-label="Navigation menu">
      <button ref={firstFocusableRef} onClick={onClose} aria-label="Close menu">
        ×
      </button>
      {children}
    </div>
  );
}
```

**2.4.1 Skip navigation link:**

```typescript
// app/layout.tsx — first focusable element on every page
// Allows keyboard users to skip the navigation and jump to main content
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {/* Skip link: visible only when focused */}
        <a
          href="#main-content"
          className="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-50 focus:rounded focus:bg-background focus:px-4 focus:py-2 focus:text-foreground focus:ring-2 focus:ring-ring"
        >
          Skip to main content
        </a>
        <Header />
        <main id="main-content" tabIndex={-1}>
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
```

---

### 3. Understandable

**3.1 Language attribute:**

```typescript
// app/layout.tsx — always set lang attribute
// Without this, screen readers use the OS language to read content
<html lang="en">

// For multilingual apps:
// app/[locale]/layout.tsx
export default function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: { locale: string };
}) {
  return <html lang={params.locale}>{/* ... */}</html>;
}
```

**3.2 Form labels — every input must have an associated label:**

```typescript
// BAD: placeholder-only — not a label, disappears on input
<input type="email" placeholder="Enter your email" />

// BAD: label without for/htmlFor association
<label>Email</label>
<input type="email" />

// GOOD: explicit association
<label htmlFor="email">
  Email address
  <span aria-hidden="true" className="text-red-500"> *</span>
  <span className="sr-only">(required)</span>
</label>
<input
  id="email"
  type="email"
  required
  aria-required="true"
  aria-describedby="email-error"
  autoComplete="email"
/>
{errors.email && (
  <p id="email-error" role="alert" className="text-sm text-red-600">
    {errors.email.message}
  </p>
)}

// GOOD with shadcn/ui FormField (auto-handles association):
<FormField
  control={form.control}
  name="email"
  render={({ field }) => (
    <FormItem>
      <FormLabel>Email address</FormLabel>
      <FormControl>
        <Input type="email" autoComplete="email" {...field} />
      </FormControl>
      <FormMessage /> {/* aria-describedby wired automatically */}
    </FormItem>
  )}
/>
```

**3.3 Error identification — errors must be descriptive:**

```typescript
// BAD: generic error
<p className="text-red-600">Invalid input</p>

// GOOD: specific, actionable error messages
// Each error identifies: what is wrong + how to fix it
const errors = {
  email: "Please enter a valid email address (e.g., name@example.com)",
  password: "Password must be at least 8 characters and include a number",
  cardNumber: "Card number must be 16 digits with no spaces",
};
```

---

### 4. Robust

**4.1 Semantic HTML — use the right element for the job:**

```typescript
// Use semantic elements — they're accessible for free
<header>    → <div role="banner"> is equivalent but more verbose
<nav>       → <div role="navigation"> is equivalent
<main>      → <div role="main"> is equivalent
<footer>    → <div role="contentinfo"> is equivalent
<aside>     → <div role="complementary"> is equivalent
<article>   → meaningful for blog posts, product cards
<section>   → grouping with a heading
<h1>-<h6>  → heading hierarchy (never skip levels: h1 → h3)
<button>    → for actions (never <a> without href)
<a href>    → for navigation (never <button> for links)

// BAD heading hierarchy — confuses screen reader users
<h1>Dashboard</h1>
<h3>Recent Orders</h3>  // jumped from h1 to h3 — h2 is missing

// GOOD hierarchy:
<h1>Dashboard</h1>
<h2>Recent Orders</h2>
<h3>Order #1234</h3>
```

---

## Пример кода

### Automated testing with axe-playwright

```typescript
// tests/e2e/accessibility.spec.ts
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("Accessibility — WCAG 2.2 AA", () => {
  test("homepage has no automatically detectable violations", async ({ page }) => {
    await page.goto("/");

    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"])
      .analyze();

    expect(results.violations).toHaveLength(0);
  });

  test("sign-in form is accessible", async ({ page }) => {
    await page.goto("/sign-in");

    const results = await new AxeBuilder({ page })
      .withTags(["wcag2aa"])
      .analyze();

    if (results.violations.length > 0) {
      // Print violation details for debugging
      console.log(
        "Violations:",
        results.violations.map((v) => ({
          id: v.id,
          description: v.description,
          nodes: v.nodes.map((n) => n.html),
        }))
      );
    }

    expect(results.violations).toHaveLength(0);
  });

  test("checkout form keyboard navigation works", async ({ page }) => {
    await page.goto("/checkout");

    // Tab through all form fields
    await page.keyboard.press("Tab"); // skip link
    await page.keyboard.press("Tab"); // first field
    const focused = await page.evaluate(() => document.activeElement?.id);
    expect(focused).toBe("email");
  });
});
```

### shadcn/ui — what's already accessible vs what needs attention

```typescript
// ALREADY HANDLED by shadcn/ui + Radix UI:
// - Dialog/Modal: focus trap, aria-modal, aria-labelledby, Escape key close
// - DropdownMenu: keyboard navigation, aria-expanded, aria-haspopup
// - Select: keyboard navigation, aria-expanded, aria-selected
// - Checkbox: aria-checked, keyboard activation
// - RadioGroup: arrow key navigation, aria-checked
// - Tabs: arrow key navigation, aria-selected, aria-controls
// - Toast: aria-live="polite" notifications
// - Tooltip: follows button aria pattern

// STILL NEEDS YOUR ATTENTION:
// 1. Form labels — FormLabel maps to htmlFor, but you must use FormField correctly
// 2. Error messages — FormMessage uses aria-describedby, but error text must be meaningful
// 3. Loading states — add aria-busy and aria-live for async operations
// 4. Page titles — each route needs a unique <title> for navigation history
// 5. Images — alt text is not provided by shadcn/ui components
// 6. Color contrast — shadcn themes meet AA, but custom colors may not
// 7. Animation — respect prefers-reduced-motion

// Respecting reduced motion:
// globals.css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

// Or in Tailwind:
<div className="transition-opacity motion-reduce:transition-none" />
```

---

## Антипаттерн

```typescript
// BAD: Using color alone to convey status
<span className="text-red-500">Error</span>  // color blind users miss the meaning
// GOOD: add an icon or text that doesn't rely on color
<span className="text-red-500 flex items-center gap-1">
  <AlertCircle className="h-4 w-4" aria-hidden="true" />
  Error: Email is required
</span>

// BAD: Keyboard trap — user can Tab into modal but not Tab out
// shadcn/ui Dialog DOES trap focus correctly
// Custom modals often forget to implement focus trap

// BAD: Icon-only buttons without accessible name
<button onClick={deleteItem}>
  <TrashIcon className="h-4 w-4" />
</button>
// Screen reader announces: "button" — no name

// GOOD:
<button onClick={deleteItem} aria-label="Delete item">
  <TrashIcon className="h-4 w-4" aria-hidden="true" />
</button>

// BAD: Auto-playing video with audio — violates WCAG 1.4.2
<video autoPlay src="/promo.mp4" />
// At minimum: autoPlay only for muted video, provide pause control
<video autoPlay muted loop playsInline aria-label="Product demo (muted autoplay)">
```

---

## Связанные документы

- `knowledge/custom/08-accessibility/aria-patterns.md` — ARIA patterns for complex components
- `knowledge/custom/05-testing/test-strategy.md` — E2E tests include axe-playwright
- `knowledge/custom/07-performance/cwv-nextjs.md` — INP and accessible interaction

---
category: performance
topic: cwv-nextjs
status: draft
---

## Проблема / Контекст

Core Web Vitals are Google's metrics for page experience and directly influence search ranking. Next.js 15 with App Router provides built-in primitives for each metric, but you must use them correctly. The three metrics that matter for ranking in 2025 are:

- **LCP (Largest Contentful Paint)** — time until the main content is visible. Target: < 2.5s
- **CLS (Cumulative Layout Shift)** — visual stability. Target: < 0.1
- **INP (Interaction to Next Paint)** — responsiveness to all interactions. Target: < 200ms (replaced FID in March 2024)

---

## Решение

### LCP — Largest Contentful Paint

The LCP element is almost always a hero image or H1. The browser must discover it in the initial HTML and start fetching it immediately.

**1. Preload the LCP image with `next/image priority`:**

```typescript
// app/(marketing)/page.tsx
import Image from "next/image";

// The priority prop:
// - Adds rel="preload" to <head>
// - Removes lazy loading
// - Adds fetchpriority="high" to the <img>
// Only use priority on the above-the-fold image — never on multiple images
export default function HeroSection() {
  return (
    <section>
      <Image
        src="/hero.jpg"
        alt="Product showcase"
        width={1280}
        height={720}
        priority           // ← critical for LCP
        quality={85}       // 85 is the sweet spot: quality vs. file size
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 80vw, 1280px"
        className="w-full h-auto object-cover"
      />
    </section>
  );
}
```

**2. Optimize fonts with `next/font` — eliminates render-blocking font requests:**

```typescript
// app/layout.tsx
import { Inter, Playfair_Display } from "next/font/google";

// next/font downloads fonts at BUILD TIME and self-hosts them
// This eliminates the third-party DNS lookup + connection to fonts.googleapis.com
const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",   // text remains visible during font load (no FOIT)
  preload: true,
  fallback: ["system-ui", "arial"],
});

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-playfair",
  display: "optional", // for headings: "optional" prevents CLS from font swap
  weight: ["400", "700"],
});

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${inter.variable} ${playfair.variable}`}>
      <body className="font-sans">{children}</body>
    </html>
  );
}
```

**3. Generate blur placeholder for images — prevents CLS and improves perceived LCP:**

```typescript
// src/lib/image.ts
import { getPlaiceholder } from "plaiceholder";
import fs from "fs/promises";

export async function getImagePlaceholder(src: string) {
  const buffer = await fetch(src).then((res) => res.arrayBuffer());
  const { base64 } = await getPlaiceholder(Buffer.from(buffer));
  return base64;
}

// In a Server Component:
const blurDataURL = await getImagePlaceholder("https://cdn.myapp.com/hero.jpg");

<Image
  src="https://cdn.myapp.com/hero.jpg"
  alt="Hero"
  width={1280}
  height={720}
  placeholder="blur"
  blurDataURL={blurDataURL}
  priority
/>
```

---

### CLS — Cumulative Layout Shift

CLS happens when content jumps because dimensions are unknown. The fix is always to **reserve space before the content loads**.

**1. Always provide explicit dimensions for images:**

```typescript
// next/image enforces width/height which reserves space automatically
// With fill prop: parent must have position: relative and explicit height
<div className="relative h-64 w-full">
  <Image src="/photo.jpg" alt="..." fill className="object-cover" />
</div>

// NEVER: images without dimensions — browser has no idea how tall they are
// <img src="/photo.jpg" alt="..." /> ← CLS source
```

**2. Avoid dynamic content injections that push layout:**

```typescript
// BAD — cookie banner appears after hydration, pushing content down
"use client";
import { useState, useEffect } from "react";

export function CookieBanner() {
  const [show, setShow] = useState(false);
  useEffect(() => {
    setShow(!localStorage.getItem("cookie-consent")); // shows after hydration → CLS
  }, []);
  if (!show) return null;
  return <div className="fixed-bottom-banner">...</div>; // use fixed/sticky, not static
}

// GOOD — use position: fixed so it doesn't affect document flow
// className="fixed bottom-0 left-0 right-0 z-50"
```

**3. Reserve ad slots:**

```typescript
// Reserve the exact height of the ad container before it loads
// Prevents 50-250px jumps when the ad fills in
<div className="min-h-[250px] w-full bg-gray-100">
  <AdSlot id="homepage-banner" />
</div>
```

---

### INP — Interaction to Next Paint

INP measures the time from ANY user interaction (click, tap, keyboard) to the next visual frame. Unlike FID which only measured first input, INP measures throughout the page lifetime.

**1. Minimize main thread work with Server Components:**

```typescript
// Server Components have ZERO JavaScript bundle cost — they render on the server
// and send HTML. Move as much logic as possible to Server Components.

// app/products/page.tsx — Server Component (no "use client")
// This entire component generates zero client-side JS
export default async function ProductsPage() {
  const products = await db.query.products.findMany({ limit: 20 });
  return (
    <div>
      {products.map((p) => (
        <ProductCard key={p.id} product={p} />
        // ProductCard is also a Server Component — no bundle cost
      ))}
    </div>
  );
}
```

**2. Defer non-critical JS with `next/dynamic`:**

```typescript
// app/dashboard/page.tsx
import dynamic from "next/dynamic";

// Heavy chart library — only load after page is interactive
const RevenueChart = dynamic(
  () => import("@/components/charts/revenue-chart"),
  {
    loading: () => <div className="h-64 animate-pulse bg-gray-200 rounded" />,
    ssr: false, // Chart libraries often use window/document
  }
);

// Video player — never in initial bundle
const VideoPlayer = dynamic(() => import("@/components/video-player"), {
  ssr: false,
});

export default function DashboardPage() {
  return (
    <div>
      <RevenueChart /> {/* Loads after hydration — doesn't block INP */}
    </div>
  );
}
```

**3. Use Suspense boundaries for below-the-fold data:**

```typescript
// app/products/[id]/page.tsx
import { Suspense } from "react";

export default function ProductPage({ params }: { params: { id: string } }) {
  return (
    <div>
      {/* Critical: render immediately */}
      <ProductHeader productId={params.id} />

      {/* Non-critical: stream in later without blocking */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <ProductReviews productId={params.id} />
      </Suspense>

      <Suspense fallback={<RelatedProductsSkeleton />}>
        <RelatedProducts productId={params.id} />
      </Suspense>
    </div>
  );
}
```

**4. Debounce expensive event handlers:**

```typescript
// src/components/search.tsx
"use client";

import { useState, useTransition, useCallback } from "react";
import { useRouter } from "next/navigation";

export function SearchInput() {
  const [query, setQuery] = useState("");
  const [isPending, startTransition] = useTransition();
  const router = useRouter();

  // useTransition marks the navigation as non-urgent
  // The browser remains responsive to higher-priority interactions
  const handleChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setQuery(value); // Update input immediately

    startTransition(() => {
      // Navigation is deferred — doesn't block INP
      router.push(`/search?q=${encodeURIComponent(value)}`);
    });
  }, [router]);

  return (
    <input
      value={query}
      onChange={handleChange}
      placeholder="Search..."
      aria-busy={isPending}
    />
  );
}
```

---

## Пример кода

### Vercel Analytics + Speed Insights setup

```typescript
// app/layout.tsx
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {children}
        {/* Analytics: page views and custom events */}
        <Analytics />
        {/* Speed Insights: real-user CWV data from your actual visitors */}
        <SpeedInsights />
      </body>
    </html>
  );
}
```

### Custom CWV measurement for non-Vercel deployments

```typescript
// src/lib/web-vitals.ts
import { onCLS, onINP, onLCP, onFCP, onTTFB, type Metric } from "web-vitals";

function sendToAnalytics(metric: Metric) {
  const body = JSON.stringify({
    name: metric.name,
    value: metric.value,
    rating: metric.rating, // "good" | "needs-improvement" | "poor"
    delta: metric.delta,
    id: metric.id,
    pathname: window.location.pathname,
  });

  // Use sendBeacon so the request completes even if the page unloads
  if (navigator.sendBeacon) {
    navigator.sendBeacon("/api/vitals", body);
  } else {
    fetch("/api/vitals", { method: "POST", body, keepalive: true });
  }
}

export function reportWebVitals() {
  onCLS(sendToAnalytics);
  onINP(sendToAnalytics);
  onLCP(sendToAnalytics);
  onFCP(sendToAnalytics);
  onTTFB(sendToAnalytics);
}

// app/layout.tsx
"use client";
import { useEffect } from "react";
import { reportWebVitals } from "@/lib/web-vitals";

export function WebVitalsReporter() {
  useEffect(() => {
    reportWebVitals();
  }, []);
  return null;
}
```

### Lab data: Lighthouse CI in GitHub Actions

```yaml
# .github/workflows/lighthouse.yml
- name: Run Lighthouse CI
  run: npx lhci autorun
  env:
    LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}

# lighthouserc.js
module.exports = {
  ci: {
    collect: { url: ["http://localhost:3000", "http://localhost:3000/products"] },
    assert: {
      assertions: {
        "categories:performance": ["warn", { minScore: 0.9 }],
        "first-contentful-paint": ["error", { maxNumericValue: 2000 }],
        "largest-contentful-paint": ["error", { maxNumericValue: 2500 }],
        "cumulative-layout-shift": ["error", { maxNumericValue: 0.1 }],
        "total-blocking-time": ["warn", { maxNumericValue: 300 }],
      },
    },
  },
};
```

---

## Антипаттерн

```typescript
// BAD LCP: multiple priority images — only one image should have priority
<Image src="/hero.jpg" priority ... />
<Image src="/hero-mobile.jpg" priority ... />
<Image src="/logo.png" priority ... />  // logo is never the LCP element

// BAD CLS: image without dimensions
<img src="/user-avatar.jpg" className="rounded-full" />
// Browser doesn't know the height until the image loads → layout shift

// BAD INP: heavy computation in a click handler on the main thread
onClick={async () => {
  const result = await processLargeDataset(data); // blocks main thread for 500ms
  setResults(result);
}}
// FIX: Use a Web Worker for CPU-intensive operations, or move to a Server Action

// BAD INP: importing an entire date library for one function
import { format } from "date-fns"; // adds ~15KB to client bundle
// FIX: Use Intl.DateTimeFormat (built into browsers, zero bundle cost)
const formatted = new Intl.DateTimeFormat("en-US", { dateStyle: "medium" }).format(date);
```

---

## Связанные документы

- `knowledge/custom/07-performance/bundle-optimization.md` — reducing JS bundle for better INP
- `knowledge/custom/07-performance/db-query-patterns.md` — fast data fetching for better LCP
- `knowledge/custom/08-accessibility/wcag-checklist.md` — accessible images with alt text

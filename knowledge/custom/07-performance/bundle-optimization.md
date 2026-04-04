---
category: performance
topic: bundle-optimization
status: draft
---

## Проблема / Контекст

JavaScript bundle size is the single largest controllable factor in Time to Interactive and INP on mobile. Next.js 15 App Router dramatically reduces the client-side bundle by moving rendering to the server, but every `"use client"` directive, every third-party import, and every barrel file re-export creates bundle pressure. A 500KB compressed JS bundle on a mid-range Android phone at 3G takes ~5 seconds to parse and execute — before your page is interactive.

---

## Решение

### Analyze first, optimize second

```bash
# Install the bundle analyzer
pnpm add -D @next/bundle-analyzer

# Run the analysis
ANALYZE=true pnpm build
# Opens three treemap visualizations: server, client, edge bundles
```

```typescript
// next.config.ts
import type { NextConfig } from "next";
import BundleAnalyzer from "@next/bundle-analyzer";

const withBundleAnalyzer = BundleAnalyzer({
  enabled: process.env.ANALYZE === "true",
});

const nextConfig: NextConfig = {
  // ... your config
};

export default withBundleAnalyzer(nextConfig);
```

**What to look for in the analyzer:**
- Modules > 50KB that appear in the client bundle
- Libraries that should only be on the server (e.g., `postgres`, `bcrypt`, `nodemailer`)
- Duplicate packages at different versions
- `node_modules` appearing multiple times in the bundle (bundler deduplication failure)

---

### Server Components have zero bundle cost

```typescript
// This file has ZERO client-side JavaScript — it's a React Server Component
// The database client, Drizzle, bcrypt — none of it ships to the browser
// app/products/page.tsx (no "use client" directive = Server Component by default)
import { db } from "@/db";
import { products } from "@/db/schema";

export default async function ProductsPage() {
  const items = await db.query.products.findMany({
    limit: 20,
    columns: { id: true, name: true, priceInCents: true, imageUrl: true },
  });

  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>{item.name}</li> // pure HTML, no JS
      ))}
    </ul>
  );
}

// The "use client" boundary is the only place where code enters the bundle
// Keep it as DEEP in the tree as possible
```

### Dynamic imports for heavy libraries

```typescript
// BEFORE: The entire chart library loads with the initial bundle
// import { AreaChart, LineChart, BarChart } from "recharts"; // ~180KB

// AFTER: Load only when the component is actually rendered
import dynamic from "next/dynamic";

// next/dynamic wraps React.lazy with SSR control
const RevenueChart = dynamic(
  () => import("@/components/charts/revenue-chart").then((mod) => mod.RevenueChart),
  {
    loading: () => (
      // Skeleton prevents CLS — matches the chart's dimensions exactly
      <div className="h-64 w-full animate-pulse rounded-lg bg-muted" />
    ),
    ssr: false, // recharts, chart.js, etc. use browser APIs
  }
);

// Heavy markdown editor — never in initial load
const MarkdownEditor = dynamic(() => import("@/components/markdown-editor"), {
  ssr: false,
  loading: () => <div className="h-96 animate-pulse bg-muted rounded" />,
});

// Date picker — use ssr: true if it renders server-side without errors
const DatePicker = dynamic(() => import("@/components/date-picker"), {
  ssr: true,
  loading: () => <input type="date" className="input" />, // native fallback
});
```

### Avoid importing entire libraries

```typescript
// LODASH — worst offender: entire lodash is ~70KB minified

// BAD: imports everything
import _ from "lodash";
const sorted = _.sortBy(items, "name");

// BAD: even named imports pull the whole library if not ESM
import { sortBy } from "lodash";

// GOOD option 1: use lodash-es (ESM, tree-shakeable)
import { sortBy } from "lodash-es"; // only sortBy is bundled

// GOOD option 2: native JS (always zero cost)
const sorted = [...items].sort((a, b) => a.name.localeCompare(b.name));

// DATE-FNS

// BAD: v2 default import
import { format, parseISO, addDays } from "date-fns"; // ~75KB if not tree-shaken

// GOOD option 1: date-fns v3 is properly tree-shakeable
import { format } from "date-fns/format"; // ~3KB
import { parseISO } from "date-fns/parseISO";

// GOOD option 2: Intl API for simple formatting (zero bundle cost)
const formatted = new Intl.DateTimeFormat("en-US", {
  year: "numeric", month: "short", day: "numeric",
}).format(new Date());

// GOOD option 3: Keep date logic in Server Components — zero bundle cost
// app/blog/[slug]/page.tsx (Server Component)
import { format } from "date-fns/format"; // only runs on server, never in browser

// ICONS

// BAD: importing from the root package
import { Search, User, Bell, Settings, X, Check } from "lucide-react";
// All icons referenced from one import → only the used ones are bundled
// Actually fine for lucide-react which is ESM — but check your library

// Watch for: @heroicons/react v1 (not tree-shakeable)
// GOOD: @heroicons/react v2
import { MagnifyingGlassIcon } from "@heroicons/react/24/outline"; // only this icon
```

### Tree shaking requirements

```typescript
// For tree shaking to work the library must:
// 1. Ship ES modules (package.json "module" or "exports" field with "import")
// 2. Have no side effects (package.json "sideEffects": false)
// 3. Use named exports, not default exports of objects

// Check if a library is ESM:
// node_modules/some-lib/package.json
{
  "main": "./dist/index.cjs.js",    // CommonJS fallback
  "module": "./dist/index.esm.js",  // ESM — Next.js uses this
  "exports": {
    ".": {
      "import": "./dist/index.esm.js",
      "require": "./dist/index.cjs.js"
    }
  },
  "sideEffects": false // ← required for tree shaking
}

// If sideEffects is missing or true, bundler must include everything
```

### Barrel file problem

```typescript
// The barrel file anti-pattern — creates massive bundle chunks

// src/components/index.ts (barrel file)
export { Button } from "./button";
export { Card } from "./card";
export { Modal } from "./modal";
export { DatePicker } from "./date-picker"; // imports heavy lib
export { RichTextEditor } from "./rich-text-editor"; // imports ~200KB editor
export { Chart } from "./chart"; // imports recharts

// IMPORTING FROM BARREL:
import { Button } from "@/components";
// Next.js must analyze the entire barrel to find Button
// Even with tree shaking, some bundlers pull in all re-exports

// FIX option 1: Direct imports (always correct)
import { Button } from "@/components/button";
import { Card } from "@/components/card";

// FIX option 2: Configure Next.js modularize imports (for common libraries)
// next.config.ts
const nextConfig: NextConfig = {
  modularizeImports: {
    // Automatically rewrites:
    // import { Button, Card } from "@/components"
    // to individual file imports
    "@/components": {
      transform: "@/components/{{member}}",
      skipDefaultConversion: true,
    },
    // For lodash:
    "lodash": {
      transform: "lodash/{{member}}",
    },
  },
};
```

### Code splitting with route groups

```typescript
// App Router automatically code-splits by route segment
// Each page.tsx is a separate chunk — unrelated pages don't share code

// app/(marketing)/layout.tsx — marketing-specific providers (analytics, chat widget)
// app/(app)/layout.tsx — app-specific providers (auth, notifications)
// app/(admin)/layout.tsx — admin-specific code (heavy tables, charts)

// The admin bundle never loads for regular users
// The marketing bundle (lighter) loads for public pages

// Route group structure for optimal splitting:
// app/
// ├── (marketing)/      ← landing, pricing, blog — minimal JS
// │   ├── layout.tsx
// │   └── page.tsx
// ├── (app)/            ← dashboard, settings — full app JS
// │   ├── layout.tsx
// │   └── dashboard/
// └── (admin)/          ← admin panel — heavy analytics JS, only for admins
//     ├── layout.tsx
//     └── users/
```

### Measure bundle impact before merging

```bash
# Compare bundle sizes between branches
# Install bundlesize or use Next.js built-in stats

# next.config.ts
const nextConfig: NextConfig = {
  experimental: {
    // Generates .next/analyze/client.html with bundle stats
  },
};

# In CI: fail if the client bundle grows by more than 10KB
# package.json
"bundlesize": [
  {
    "path": ".next/static/chunks/pages/*.js",
    "maxSize": "150 kB"
  },
  {
    "path": ".next/static/chunks/app/*.js",
    "maxSize": "100 kB"
  }
]
```

---

## Антипаттерн

```typescript
// BAD: "use client" at the top of a layout file
// app/(app)/layout.tsx
"use client"; // ← ALL children are now client components by default
// The entire subtree loses server rendering benefits

// GOOD: Only mark the interactive leaf component as client
// app/(app)/layout.tsx — Server Component (no directive)
export default function AppLayout({ children }) {
  return (
    <div>
      <ServerSidebar />  {/* Server Component */}
      <ClientThemeToggle />  {/* Only this leaf is "use client" */}
      {children}
    </div>
  );
}

// BAD: Heavy import in a client component
"use client";
import { PDFDocument } from "pdf-lib"; // 200KB — loads on every page
export function DownloadButton() {
  // PDF generation only happens on click
  return <button onClick={() => generatePDF()}>Download</button>;
}

// GOOD: Dynamic import inside the event handler
"use client";
export function DownloadButton() {
  async function handleDownload() {
    const { PDFDocument } = await import("pdf-lib"); // loads only on click
    // ...
  }
  return <button onClick={handleDownload}>Download</button>;
}
```

---

## Связанные документы

- `knowledge/custom/07-performance/cwv-nextjs.md` — CWV and INP impact of bundle size
- `knowledge/custom/03-antipatterns/client-server-boundary.md` — "use client" boundary mistakes

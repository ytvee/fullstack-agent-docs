---
category: devops
topic: vercel-deploy
status: draft
---

## Проблема / Контекст

Vercel — основная платформа для деплоя Next.js 15 приложений. Несмотря на простоту базового деплоя (`git push`), production-ready настройка требует правильной конфигурации: управление переменными окружения, выбор runtime (Edge vs Node.js), настройка ISR и on-demand revalidation, Cron Jobs, защита preview деплоев, мониторинг производительности.

Без правильной настройки: секреты утекают через preview URLs, ISR не работает корректно, кэш не инвалидируется при обновлении данных, нет мониторинга Core Web Vitals.

## Решение

### vercel.json — основная конфигурация

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "framework": "nextjs",
  "buildCommand": "pnpm build",
  "devCommand": "pnpm dev",
  "installCommand": "pnpm install --frozen-lockfile",
  "regions": ["fra1"],
  "functions": {
    "app/api/heavy-computation/route.ts": {
      "maxDuration": 60,
      "memory": 1024
    },
    "app/api/webhooks/stripe/route.ts": {
      "maxDuration": 30
    }
  },
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        },
        {
          "key": "Referrer-Policy",
          "value": "strict-origin-when-cross-origin"
        },
        {
          "key": "Permissions-Policy",
          "value": "camera=(), microphone=(), geolocation=()"
        }
      ]
    },
    {
      "source": "/fonts/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ],
  "redirects": [
    {
      "source": "/home",
      "destination": "/",
      "permanent": true
    }
  ],
  "rewrites": [
    {
      "source": "/api/proxy/:path*",
      "destination": "https://internal-api.yoursite.com/:path*"
    }
  ],
  "crons": [
    {
      "path": "/api/cron/send-digests",
      "schedule": "0 9 * * 1"
    },
    {
      "path": "/api/cron/cleanup-sessions",
      "schedule": "0 2 * * *"
    }
  ]
}
```

### Переменные окружения: production vs preview vs development

Vercel разделяет env vars на три среды. Это критически важно для безопасности.

```bash
# Настройка через Vercel CLI
vercel env add DATABASE_URL production
vercel env add DATABASE_URL preview
vercel env add DATABASE_URL development

# Или через vercel.json (только non-sensitive values)
# Sensitive vars — ТОЛЬКО через Vercel Dashboard или CLI
```

```typescript
// lib/env.ts — типизация и валидация переменных окружения
import { z } from "zod";

const envSchema = z.object({
  // База данных
  DATABASE_URL: z.string().url(),
  DATABASE_URL_UNPOOLED: z.string().url().optional(), // для миграций

  // Auth
  AUTH_SECRET: z.string().min(32),
  AUTH_URL: z.string().url(),

  // Внешние сервисы
  STRIPE_SECRET_KEY: z.string().startsWith("sk_"),
  STRIPE_WEBHOOK_SECRET: z.string().startsWith("whsec_"),

  // Публичные переменные (доступны в браузере)
  NEXT_PUBLIC_SITE_URL: z.string().url(),
  NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY: z.string().startsWith("pk_"),

  // Опциональные
  RESEND_API_KEY: z.string().optional(),
  UPSTASH_REDIS_REST_URL: z.string().url().optional(),
  UPSTASH_REDIS_REST_TOKEN: z.string().optional(),

  // Vercel-специфичные (автоматически устанавливаются Vercel)
  VERCEL_ENV: z.enum(["production", "preview", "development"]).optional(),
  VERCEL_URL: z.string().optional(), // автоматический URL деплоя
  VERCEL_GIT_COMMIT_SHA: z.string().optional(),
});

// Валидация при старте приложения
const _env = envSchema.safeParse(process.env);

if (!_env.success) {
  console.error("❌ Invalid environment variables:", _env.error.format());
  throw new Error("Invalid environment variables");
}

export const env = _env.data;

// Использование: import { env } from "@/lib/env"
// env.DATABASE_URL — типизировано и валидировано
```

```typescript
// Получение правильного URL в зависимости от среды
// lib/get-base-url.ts
export function getBaseUrl(): string {
  // В браузере — всегда используй NEXT_PUBLIC_SITE_URL
  if (typeof window !== "undefined") {
    return process.env.NEXT_PUBLIC_SITE_URL ?? "";
  }

  // Production
  if (process.env.VERCEL_ENV === "production") {
    return process.env.NEXT_PUBLIC_SITE_URL ?? "https://yoursite.com";
  }

  // Preview deployments (Vercel автоматически устанавливает VERCEL_URL)
  if (process.env.VERCEL_URL) {
    return `https://${process.env.VERCEL_URL}`;
  }

  // Local development
  return "http://localhost:3000";
}
```

### Edge vs Node.js Runtime

```typescript
// Edge Runtime — быстрее, но ограничения:
// - Нет Node.js API (fs, child_process, Buffer не поддерживается полностью)
// - Нет нативных npm пакетов (bcrypt, sharp)
// - Drizzle с pg не работает на Edge — только с @neondatabase/serverless или Turso

// app/api/geo/route.ts — Edge подходит для lightweight endpoints
export const runtime = "edge";

export async function GET(request: Request) {
  const country = request.headers.get("x-vercel-ip-country") ?? "RU";
  return Response.json({ country });
}
```

```typescript
// Node.js Runtime — используй для:
// - Drizzle ORM с pg/postgres.js
// - bcrypt, sharp, puppeteer
// - File operations

// app/api/upload/route.ts
export const runtime = "nodejs"; // явно указывай или оставь default

import sharp from "sharp"; // работает только в Node.js runtime
```

```typescript
// middleware.ts — всегда выполняется на Edge
// Не импортируй Drizzle или тяжёлые Node.js пакеты!
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { auth } from "@/lib/auth"; // Auth.js middleware работает на Edge

export default auth((request) => {
  const { pathname } = request.nextUrl;

  // Geo-based routing
  const country = request.headers.get("x-vercel-ip-country");
  if (pathname === "/" && country === "US") {
    return NextResponse.redirect(new URL("/en", request.url));
  }

  return NextResponse.next();
});

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
```

### ISR и On-Demand Revalidation

```typescript
// app/products/[slug]/page.tsx — ISR с revalidate
// Страница перегенерируется максимум раз в 3600 секунд (1 час)
export const revalidate = 3600;

// ИЛИ используй fetch с cache options:
async function getProduct(slug: string) {
  const product = await db.query.products.findFirst({
    where: eq(products.slug, slug),
  });
  return product;
}
// Drizzle не использует fetch, поэтому управляй кэшем через revalidate на уровне страницы
```

```typescript
// app/api/webhooks/cms/route.ts — on-demand revalidation при обновлении контента
import { revalidatePath, revalidateTag } from "next/cache";
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  // Верификация webhook секрета
  const signature = request.headers.get("x-webhook-secret");
  if (signature !== process.env.WEBHOOK_SECRET) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await request.json() as {
    type: "product.updated" | "article.published" | "category.updated";
    slug?: string;
  };

  switch (body.type) {
    case "product.updated":
      revalidatePath(`/products/${body.slug}`);
      revalidatePath("/products");
      revalidateTag("products"); // если используешь unstable_cache с tags
      break;

    case "article.published":
      revalidatePath(`/blog/${body.slug}`);
      revalidatePath("/blog");
      revalidatePath("/sitemap.xml");
      break;

    case "category.updated":
      revalidatePath("/products");
      revalidatePath(`/categories/${body.slug}`);
      break;
  }

  return NextResponse.json({ revalidated: true, timestamp: Date.now() });
}
```

### Vercel Cron Jobs

```typescript
// app/api/cron/send-digests/route.ts
// Запускается каждый понедельник в 9:00 UTC (см. vercel.json)
import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { users } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { sendWeeklyDigest } from "@/lib/email";

export async function GET(request: NextRequest) {
  // Vercel автоматически добавляет Authorization header для Cron Jobs
  const authHeader = request.headers.get("authorization");
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const subscribers = await db.query.users.findMany({
    where: eq(users.weeklyDigestEnabled, true),
    columns: { id: true, email: true, name: true },
  });

  let sent = 0;
  let failed = 0;

  // Batch обработка, чтобы не перегружать email провайдера
  for (const user of subscribers) {
    try {
      await sendWeeklyDigest(user.email, user.name);
      sent++;
    } catch (error) {
      console.error(`Failed to send digest to ${user.email}:`, error);
      failed++;
    }
  }

  console.log(`Digest cron: ${sent} sent, ${failed} failed`);
  return NextResponse.json({ sent, failed });
}
```

### Preview Deployments и Deployment Protection

```typescript
// middleware.ts — защита preview деплоев от случайного индексирования
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Vercel устанавливает x-vercel-deployment-url в preview деплоях
  const isPreview = process.env.VERCEL_ENV === "preview";

  if (isPreview) {
    // Добавляем noindex header для всех страниц в preview
    const response = NextResponse.next();
    response.headers.set("x-robots-tag", "noindex, nofollow");
    return response;
  }

  return NextResponse.next();
}
```

В Vercel Dashboard: Settings → Deployment Protection → включи "Vercel Authentication" для preview URLs или используй Password Protection для demo-деплоев клиентам.

### Speed Insights и Web Analytics

```typescript
// app/layout.tsx
import { SpeedInsights } from "@vercel/speed-insights/next";
import { Analytics } from "@vercel/analytics/react";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru">
      <body>
        {children}
        {/* Web Vitals tracking — отправляет LCP, FID, CLS в Vercel Dashboard */}
        <SpeedInsights />
        {/* Page views и custom events */}
        <Analytics />
      </body>
    </html>
  );
}
```

```typescript
// Кастомные события для Analytics
import { track } from "@vercel/analytics";

// В клиентском компоненте:
function ProductCard({ product }: { product: Product }) {
  return (
    <button
      onClick={() => {
        track("product_viewed", {
          productId: product.id,
          category: product.category,
          price: product.price,
        });
        // ... add to cart logic
      }}
    >
      Добавить в корзину
    </button>
  );
}
```

### Кастомные домены

```bash
# Через Vercel CLI
vercel domains add yoursite.com
vercel domains add www.yoursite.com

# Редирект www → apex через vercel.json
# Или используй Vercel Dashboard: Settings → Domains → Add

# DNS записи для Railway DB доступа:
# yoursite.com → A record → 76.76.21.21 (Vercel anycast IP)
# www.yoursite.com → CNAME → cname.vercel-dns.com
```

## Пример кода

### Полный скрипт деплоя с проверками

```bash
#!/bin/bash
# scripts/deploy.sh — запускается в CI перед деплоем

set -e

echo "🔍 Running pre-deploy checks..."

# Typecheck
pnpm tsc --noEmit

# Lint
pnpm lint

# Unit tests
pnpm test:unit --run

# Build check
pnpm build

echo "✅ All checks passed. Deploying..."
vercel --prod --token=$VERCEL_TOKEN
```

### Частые ошибки деплоя и решения

```typescript
// ОШИБКА: "Error: ENOENT: no such file or directory, open '...'"
// ПРИЧИНА: импорт файла из /public в Server Component
// РЕШЕНИЕ: используй process.cwd() для абсолютных путей
import path from "path";
import fs from "fs/promises";

const filePath = path.join(process.cwd(), "public", "data", "config.json");
const data = await fs.readFile(filePath, "utf-8");

// ОШИБКА: "ReferenceError: window is not defined"
// ПРИЧИНА: использование browser API в Server Component
// РЕШЕНИЕ: перенести в "use client" компонент или использовать dynamic import
import dynamic from "next/dynamic";
const MapComponent = dynamic(() => import("@/components/map"), {
  ssr: false,
});

// ОШИБКА: "Error: connect ECONNREFUSED" при подключении к Railway DB
// ПРИЧИНА: DATABASE_URL не установлен в Vercel environment
// РЕШЕНИЕ: vercel env add DATABASE_URL production
// Проверить: vercel env ls
```

## Антипаттерн

```typescript
// ПЛОХО: хранить секреты в vercel.json
// vercel.json публичен в git репозитории!
{
  "env": {
    "DATABASE_URL": "postgresql://user:password@host/db" // НИКОГДА
  }
}

// ХОРОШО: только через Vercel Dashboard или CLI
// vercel env add DATABASE_URL production

// ПЛОХО: использовать Edge Runtime с Drizzle + pg
export const runtime = "edge";
import { db } from "@/lib/db"; // pg не работает на Edge!

// ХОРОШО: для Edge используй Drizzle с HTTP-клиентом
// import { drizzle } from "drizzle-orm/neon-http";
// или оставляй Node.js runtime для роутов с DB
```

## Связанные документы

- `knowledge/custom/10-devops/railway-infra.md` — подключение Railway DB к Vercel
- `knowledge/custom/10-devops/github-actions-ci.md` — CI/CD с Vercel deploy hooks
- `knowledge/custom/09-seo/sitemap-robots.md` — ISR для sitemap

---
category: seo
topic: sitemap-robots
status: draft
---

## Проблема / Контекст

Sitemap.xml и robots.txt — фундаментальные SEO-файлы. Без sitemap Google медленнее обнаруживает новые страницы. Без правильного robots.txt краулер индексирует служебные страницы (dashboard, auth, api routes), тратя краулинговый бюджет впустую. В Next.js 15 оба файла генерируются программно через TypeScript, что позволяет подключать БД и автоматически включать все опубликованные страницы.

Проблемы при ручном подходе: забытые страницы, устаревшие URLs, необходимость обновления вручную при добавлении контента, неправильные приоритеты.

## Решение

### app/sitemap.ts — статические + динамические URLs

Next.js 15 читает `app/sitemap.ts` и отдаёт его по `/sitemap.xml`. Функция должна возвращать массив `MetadataRoute.Sitemap`.

```typescript
// app/sitemap.ts
import type { MetadataRoute } from "next";
import { db } from "@/lib/db";
import { products, articles, categories } from "@/lib/db/schema";
import { eq, and } from "drizzle-orm";

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://yoursite.com";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  // 1. Статические страницы
  const staticPages: MetadataRoute.Sitemap = [
    {
      url: SITE_URL,
      lastModified: new Date(),
      changeFrequency: "daily",
      priority: 1.0,
    },
    {
      url: `${SITE_URL}/about`,
      lastModified: new Date("2025-01-01"),
      changeFrequency: "monthly",
      priority: 0.7,
    },
    {
      url: `${SITE_URL}/contact`,
      lastModified: new Date("2025-01-01"),
      changeFrequency: "monthly",
      priority: 0.6,
    },
    {
      url: `${SITE_URL}/blog`,
      lastModified: new Date(),
      changeFrequency: "daily",
      priority: 0.9,
    },
    {
      url: `${SITE_URL}/products`,
      lastModified: new Date(),
      changeFrequency: "daily",
      priority: 0.9,
    },
  ];

  // 2. Продукты из БД
  const allProducts = await db.query.products.findMany({
    where: and(eq(products.isPublished, true), eq(products.isDeleted, false)),
    columns: { slug: true, updatedAt: true, priority: true },
  });

  const productPages: MetadataRoute.Sitemap = allProducts.map((product) => ({
    url: `${SITE_URL}/products/${product.slug}`,
    lastModified: product.updatedAt,
    changeFrequency: "weekly" as const,
    priority: product.priority ?? 0.8,
  }));

  // 3. Статьи блога
  const allArticles = await db.query.articles.findMany({
    where: and(
      eq(articles.status, "published"),
      eq(articles.isDeleted, false)
    ),
    columns: { slug: true, updatedAt: true, publishedAt: true },
    orderBy: (articles, { desc }) => [desc(articles.publishedAt)],
  });

  const articlePages: MetadataRoute.Sitemap = allArticles.map((article) => ({
    url: `${SITE_URL}/blog/${article.slug}`,
    lastModified: article.updatedAt,
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  // 4. Категории
  const allCategories = await db.query.categories.findMany({
    where: eq(categories.isActive, true),
    columns: { slug: true, updatedAt: true },
  });

  const categoryPages: MetadataRoute.Sitemap = allCategories.map((cat) => ({
    url: `${SITE_URL}/categories/${cat.slug}`,
    lastModified: cat.updatedAt,
    changeFrequency: "weekly" as const,
    priority: 0.8,
  }));

  return [
    ...staticPages,
    ...productPages,
    ...articlePages,
    ...categoryPages,
  ];
}
```

### app/robots.ts — программный robots.txt

```typescript
// app/robots.ts
import type { MetadataRoute } from "next";

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://yoursite.com";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        // Основные правила для всех ботов
        userAgent: "*",
        allow: ["/", "/products/", "/blog/", "/categories/", "/about", "/contact"],
        disallow: [
          "/dashboard/",      // приватные страницы пользователя
          "/admin/",          // административная панель
          "/api/",            // API routes
          "/auth/",           // страницы входа/регистрации
          "/_next/",          // внутренние ресурсы Next.js
          "/private/",
          "/*?*sort=",        // URL с sort параметром (дубликаты)
          "/*?*page=",        // пагинация (опционально)
          "/*?ref=",          // реферальные параметры
        ],
      },
      {
        // Более жёсткие правила для агрессивных ботов
        userAgent: ["AhrefsBot", "SemrushBot", "MJ12bot"],
        disallow: "/",
      },
      {
        // GPTBot и AI-краулеры — разрешить для видимости в AI поиске
        userAgent: ["GPTBot", "ChatGPT-User", "PerplexityBot", "Google-Extended"],
        allow: "/",
        disallow: ["/dashboard/", "/admin/", "/api/", "/auth/"],
      },
    ],
    sitemap: `${SITE_URL}/sitemap.xml`,
    host: SITE_URL,
  };
}
```

### Multi-sitemap для больших сайтов (Sitemap Index)

При более 50,000 URLs (лимит Google) или при желании разбить sitemap по типам контента:

```typescript
// app/sitemap.ts — возвращает sitemap index
import type { MetadataRoute } from "next";

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://yoursite.com";

// Sitemap index — ссылается на отдельные sitemaps
export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: `${SITE_URL}/sitemaps/static.xml`,
      lastModified: new Date(),
    },
    {
      url: `${SITE_URL}/sitemaps/products.xml`,
      lastModified: new Date(),
    },
    {
      url: `${SITE_URL}/sitemaps/blog.xml`,
      lastModified: new Date(),
    },
  ];
}
```

```typescript
// app/sitemaps/products/route.ts — отдельный sitemap для продуктов
import { db } from "@/lib/db";
import { products } from "@/lib/db/schema";
import { eq, and } from "drizzle-orm";

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://yoursite.com";
const PRODUCTS_PER_SITEMAP = 50_000;

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const page = parseInt(searchParams.get("page") ?? "1");

  const allProducts = await db.query.products.findMany({
    where: and(eq(products.isPublished, true), eq(products.isDeleted, false)),
    columns: { slug: true, updatedAt: true },
    limit: PRODUCTS_PER_SITEMAP,
    offset: (page - 1) * PRODUCTS_PER_SITEMAP,
  });

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allProducts
  .map(
    (product) => `  <url>
    <loc>${SITE_URL}/products/${product.slug}</loc>
    <lastmod>${product.updatedAt.toISOString()}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>`
  )
  .join("\n")}
</urlset>`;

  return new Response(xml, {
    headers: {
      "Content-Type": "application/xml",
      "Cache-Control": "public, max-age=86400, s-maxage=86400", // кэш на 24 часа
    },
  });
}
```

### Noindex для приватных разделов через metadata

Вместо robots.txt для отдельных страниц используй metadata:

```typescript
// app/dashboard/layout.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  robots: {
    index: false,
    follow: false,
    nocache: true,
    googleBot: {
      index: false,
      follow: false,
    },
  },
};
```

```typescript
// app/auth/login/page.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Войти",
  robots: {
    index: false,
    follow: true, // разрешаем следовать ссылкам со страницы входа
  },
};
```

### Автоматическая отправка в Google Search Console

После деплоя новых страниц можно автоматически уведомить Google через Indexing API:

```typescript
// lib/indexing-api.ts
import { google } from "googleapis";

const auth = new google.auth.GoogleAuth({
  credentials: {
    client_email: process.env.GOOGLE_INDEXING_CLIENT_EMAIL,
    private_key: process.env.GOOGLE_INDEXING_PRIVATE_KEY?.replace(/\\n/g, "\n"),
  },
  scopes: ["https://www.googleapis.com/auth/indexing"],
});

const indexing = google.indexing({ version: "v3", auth });

export async function notifyGoogleIndexing(
  url: string,
  type: "URL_UPDATED" | "URL_DELETED" = "URL_UPDATED"
) {
  try {
    await indexing.urlNotifications.publish({
      requestBody: { url, type },
    });
    console.log(`Notified Google about: ${url}`);
  } catch (error) {
    console.error(`Failed to notify Google for ${url}:`, error);
  }
}
```

```typescript
// Использование в Server Action при публикации статьи
// app/actions/articles.ts
"use server";

import { db } from "@/lib/db";
import { articles } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { revalidatePath } from "next/cache";
import { notifyGoogleIndexing } from "@/lib/indexing-api";

export async function publishArticle(articleId: string) {
  const [article] = await db
    .update(articles)
    .set({ status: "published", publishedAt: new Date() })
    .where(eq(articles.id, articleId))
    .returning({ slug: articles.slug });

  if (!article) throw new Error("Article not found");

  const articleUrl = `${process.env.NEXT_PUBLIC_SITE_URL}/blog/${article.slug}`;

  // Уведомляем Google об обновлении
  await notifyGoogleIndexing(articleUrl, "URL_UPDATED");

  // Инвалидируем кэш
  revalidatePath("/blog");
  revalidatePath(`/blog/${article.slug}`);
  revalidatePath("/sitemap.xml");
}
```

### Динамическая перегенерация sitemap через on-demand revalidation

```typescript
// app/api/revalidate-sitemap/route.ts
import { revalidatePath } from "next/cache";
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  const authHeader = request.headers.get("authorization");
  const token = process.env.REVALIDATION_SECRET;

  if (authHeader !== `Bearer ${token}`) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  revalidatePath("/sitemap.xml");
  revalidatePath("/robots.txt");

  return NextResponse.json({ revalidated: true, timestamp: Date.now() });
}
```

### Проверка sitemap через curl

```bash
# Проверить sitemap доступен и валиден
curl -s https://yoursite.com/sitemap.xml | head -20

# Проверить robots.txt
curl -s https://yoursite.com/robots.txt

# Проверить что noindex работает на dashboard
curl -s https://yoursite.com/dashboard | grep -i "robots"
# должно вернуть: <meta name="robots" content="noindex,nofollow">
```

## Пример кода

### Утилита для получения даты последнего изменения секции

```typescript
// lib/sitemap-utils.ts
import { db } from "@/lib/db";
import { products, articles } from "@/lib/db/schema";
import { desc, eq, and } from "drizzle-orm";

// Получить дату последнего обновления для секции
export async function getLastModifiedForSection(
  section: "products" | "articles"
): Promise<Date> {
  if (section === "products") {
    const latest = await db.query.products.findFirst({
      where: and(eq(products.isPublished, true), eq(products.isDeleted, false)),
      columns: { updatedAt: true },
      orderBy: (products, { desc }) => [desc(products.updatedAt)],
    });
    return latest?.updatedAt ?? new Date();
  }

  const latest = await db.query.articles.findFirst({
    where: and(
      eq(articles.status, "published"),
      eq(articles.isDeleted, false)
    ),
    columns: { updatedAt: true },
    orderBy: (articles, { desc }) => [desc(articles.updatedAt)],
  });
  return latest?.updatedAt ?? new Date();
}
```

## Антипаттерн

```typescript
// ПЛОХО: включать все URL без фильтрации isPublished
const allProducts = await db.query.products.findMany();
// Вернёт черновики, удалённые, недоступные товары — Google получит 404

// ПЛОХО: статический sitemap.xml в /public
// Не обновляется автоматически при добавлении контента

// ПЛОХО: слишком высокий priority для всех страниц
// priority: 1.0 для каждого URL — Google игнорирует, если все одинаковые

// ПЛОХО: crawl-delay в robots.txt
// robots: { rules: [{ crawlDelay: 10 }] }
// Google игнорирует crawl-delay, используй GSC для управления скоростью краулинга

// ХОРОШО: дифференцированные приоритеты
// Главная: 1.0, Категории: 0.8-0.9, Продукты: 0.7-0.8, Блог: 0.6-0.7, Статьи: 0.5-0.6
```

## Связанные документы

- `knowledge/custom/09-seo/metadata-api.md` — Metadata API, robots в metadata
- `knowledge/custom/09-seo/structured-data.md` — JSON-LD схемы
- `knowledge/custom/10-devops/vercel-deploy.md` — кэширование и ISR для sitemap
- `knowledge/custom/10-devops/github-actions-ci.md` — автоматическая отправка sitemap в CI/CD

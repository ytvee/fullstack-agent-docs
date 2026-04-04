---
category: seo
topic: metadata-api
status: draft
---

## Проблема / Контекст

Next.js 15 предоставляет встроенный Metadata API для управления SEO-тегами без сторонних библиотек (react-helmet, next-seo). Правильная настройка метаданных критична: заголовки, описания, Open Graph теги и canonical URLs напрямую влияют на индексацию и CTR в поисковой выдаче. Без правильной реализации страницы получают дублирующиеся теги, отсутствующие og:image, неправильные canonical URLs и слабые Twitter Cards.

Два подхода: **статический** export объекта `metadata` для страниц с неизменяемыми данными и **динамический** `generateMetadata` для страниц, зависящих от данных из БД (продукты, статьи, категории).

## Решение

### Статические метаданные в layout.tsx

Базовая конфигурация для всего сайта задаётся в корневом `app/layout.tsx`. Используй `title.template` для автоматического форматирования заголовков дочерних страниц.

```typescript
// app/layout.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  metadataBase: new URL("https://yoursite.com"),
  title: {
    default: "YourSite — Краткое описание",
    template: "%s | YourSite",
  },
  description:
    "Основное описание сайта до 160 символов. Точное, релевантное, с ключевыми словами.",
  keywords: ["next.js", "typescript", "web development"],
  authors: [{ name: "Your Name", url: "https://yoursite.com/about" }],
  creator: "Your Company",
  publisher: "Your Company",
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  openGraph: {
    type: "website",
    locale: "ru_RU",
    url: "https://yoursite.com",
    siteName: "YourSite",
    title: "YourSite — Краткое описание",
    description: "Описание для соцсетей, до 200 символов.",
    images: [
      {
        url: "/og-default.png",
        width: 1200,
        height: 630,
        alt: "YourSite Preview",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    site: "@yourhandle",
    creator: "@yourhandle",
    title: "YourSite — Краткое описание",
    description: "Описание для Twitter.",
    images: ["/og-default.png"],
  },
  verification: {
    google: "ваш-google-verification-token",
    yandex: "ваш-yandex-verification-token",
  },
  alternates: {
    canonical: "https://yoursite.com",
    languages: {
      "ru-RU": "https://yoursite.com",
      "en-US": "https://en.yoursite.com",
    },
  },
};
```

**Важно:** `metadataBase` обязателен для правильного разрешения относительных путей к изображениям OG. Без него Next.js выведет предупреждение в консоли.

### Статические метаданные для обычных страниц

```typescript
// app/about/page.tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "О компании", // станет "О компании | YourSite" через template
  description:
    "Мы занимаемся разработкой с 2018 года. Команда опытных разработчиков.",
  openGraph: {
    title: "О компании",
    description: "Узнайте больше о нашей команде и ценностях.",
    images: [{ url: "/og-about.png", width: 1200, height: 630 }],
  },
  alternates: {
    canonical: "https://yoursite.com/about",
  },
};

export default function AboutPage() {
  return <main>{/* ... */}</main>;
}
```

### generateMetadata для динамических страниц с Drizzle

Для страниц `/products/[slug]` или `/blog/[slug]` метаданные зависят от данных из БД. `generateMetadata` выполняется на сервере, имеет доступ к params и searchParams.

```typescript
// app/products/[slug]/page.tsx
import type { Metadata, ResolvingMetadata } from "next";
import { notFound } from "next/navigation";
import { db } from "@/lib/db";
import { products } from "@/lib/db/schema";
import { eq } from "drizzle-orm";

interface Props {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}

// generateMetadata имеет доступ к parent metadata через ResolvingMetadata
export async function generateMetadata(
  { params }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  const { slug } = await params;

  const product = await db.query.products.findFirst({
    where: eq(products.slug, slug),
    columns: {
      id: true,
      name: true,
      description: true,
      imageUrl: true,
      price: true,
      category: true,
      updatedAt: true,
    },
  });

  if (!product) {
    return {
      title: "Продукт не найден",
      robots: { index: false, follow: false },
    };
  }

  // Наследуем openGraph images из родителя как fallback
  const previousImages = (await parent).openGraph?.images ?? [];

  const ogImages = product.imageUrl
    ? [
        {
          url: product.imageUrl,
          width: 1200,
          height: 630,
          alt: product.name,
        },
        ...previousImages,
      ]
    : previousImages;

  return {
    title: `${product.name} — купить по лучшей цене`,
    description: product.description.slice(0, 160),
    openGraph: {
      title: product.name,
      description: product.description.slice(0, 200),
      type: "website",
      images: ogImages,
      url: `https://yoursite.com/products/${slug}`,
    },
    twitter: {
      card: "summary_large_image",
      title: product.name,
      description: product.description.slice(0, 200),
      images: product.imageUrl ? [product.imageUrl] : [],
    },
    alternates: {
      canonical: `https://yoursite.com/products/${slug}`,
    },
    other: {
      "product:price:amount": product.price.toString(),
      "product:price:currency": "RUB",
    },
  };
}

// generateStaticParams для SSG — pre-render всех продуктов
export async function generateStaticParams() {
  const allProducts = await db.query.products.findMany({
    columns: { slug: true },
    where: eq(products.isPublished, true),
  });

  return allProducts.map((p) => ({ slug: p.slug }));
}

export default async function ProductPage({ params }: Props) {
  const { slug } = await params;
  const product = await db.query.products.findFirst({
    where: eq(products.slug, slug),
  });

  if (!product) notFound();

  return <main>{/* product UI */}</main>;
}
```

### OpenGraph Images с ImageResponse

Генерация OG-изображений "на лету" через `next/og`. Создаётся в `app/opengraph-image.tsx` (статически) или `app/products/[slug]/opengraph-image.tsx` (динамически).

```typescript
// app/products/[slug]/opengraph-image.tsx
import { ImageResponse } from "next/og";
import { db } from "@/lib/db";
import { products } from "@/lib/db/schema";
import { eq } from "drizzle-orm";

export const runtime = "edge";
export const alt = "Product preview";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

interface Props {
  params: Promise<{ slug: string }>;
}

export default async function ProductOGImage({ params }: Props) {
  const { slug } = await params;

  const product = await db.query.products.findFirst({
    where: eq(products.slug, slug),
    columns: { name: true, price: true, category: true },
  });

  // Загружаем шрифт для корректного рендера кириллицы
  const fontData = await fetch(
    new URL("../../../public/fonts/Inter-Bold.ttf", import.meta.url)
  ).then((res) => res.arrayBuffer());

  return new ImageResponse(
    (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          width: "100%",
          height: "100%",
          backgroundColor: "#0f172a",
          padding: "60px",
          fontFamily: "Inter",
        }}
      >
        <div style={{ display: "flex", color: "#94a3b8", fontSize: 24 }}>
          {product?.category ?? "Продукт"}
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 16,
          }}
        >
          <div style={{ color: "#f8fafc", fontSize: 64, fontWeight: 700 }}>
            {product?.name ?? "Продукт не найден"}
          </div>
          {product?.price && (
            <div style={{ color: "#22c55e", fontSize: 40 }}>
              от {product.price.toLocaleString("ru-RU")} ₽
            </div>
          )}
        </div>
        <div style={{ display: "flex", color: "#475569", fontSize: 20 }}>
          yoursite.com
        </div>
      </div>
    ),
    {
      ...size,
      fonts: [{ name: "Inter", data: fontData, style: "normal", weight: 700 }],
    }
  );
}
```

### Robots для закрытых страниц

Страницы авторизации, дашборды и административные панели должны быть закрыты от индексации:

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

// Это применится ко всем дочерним страницам /dashboard/*
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
```

### Метаданные для статей блога с Article schema

```typescript
// app/blog/[slug]/page.tsx
import type { Metadata } from "next";
import { db } from "@/lib/db";
import { articles } from "@/lib/db/schema";
import { eq } from "drizzle-orm";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;

  const article = await db.query.articles.findFirst({
    where: eq(articles.slug, slug),
    with: { author: { columns: { name: true } } },
  });

  if (!article) return { title: "Статья не найдена" };

  return {
    title: article.title,
    description: article.excerpt,
    authors: [{ name: article.author.name }],
    openGraph: {
      type: "article",
      title: article.title,
      description: article.excerpt,
      publishedTime: article.publishedAt?.toISOString(),
      modifiedTime: article.updatedAt.toISOString(),
      authors: [article.author.name],
      tags: article.tags,
      images: [
        {
          url: article.coverImage ?? "/og-blog-default.png",
          width: 1200,
          height: 630,
          alt: article.title,
        },
      ],
    },
    alternates: {
      canonical: `https://yoursite.com/blog/${slug}`,
    },
  };
}
```

### Verification Tags

Теги верификации для Google Search Console, Yandex.Webmaster и других сервисов:

```typescript
// app/layout.tsx (добавить в metadata)
export const metadata: Metadata = {
  // ...
  verification: {
    google: "abc123xyz",      // из Google Search Console → Settings → Ownership
    yandex: "def456uvw",      // из Яндекс.Вебмастер → Инструменты → Подтверждение
    other: {
      "msvalidate.01": "ghi789rst",  // Bing Webmaster Tools
      "p:domain_verify": "jkl012mno", // Pinterest
    },
  },
};
```

## Пример кода

### Полная структура метаданных для e-commerce сайта

```typescript
// lib/metadata.ts — утилита для генерации метаданных
import type { Metadata } from "next";

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://yoursite.com";
const SITE_NAME = "YourStore";

interface GenerateMetadataOptions {
  title: string;
  description: string;
  image?: string;
  canonical?: string;
  noIndex?: boolean;
  type?: "website" | "article";
  publishedTime?: string;
  modifiedTime?: string;
}

export function generateSeoMetadata(options: GenerateMetadataOptions): Metadata {
  const {
    title,
    description,
    image = "/og-default.png",
    canonical,
    noIndex = false,
    type = "website",
    publishedTime,
    modifiedTime,
  } = options;

  const fullTitle = `${title} | ${SITE_NAME}`;
  const canonicalUrl = canonical
    ? `${SITE_URL}${canonical}`
    : undefined;

  return {
    title: fullTitle,
    description,
    robots: noIndex
      ? { index: false, follow: false }
      : { index: true, follow: true },
    openGraph: {
      title: fullTitle,
      description,
      type,
      siteName: SITE_NAME,
      images: [{ url: image, width: 1200, height: 630 }],
      ...(publishedTime && { publishedTime }),
      ...(modifiedTime && { modifiedTime }),
    },
    twitter: {
      card: "summary_large_image",
      title: fullTitle,
      description,
      images: [image],
    },
    ...(canonicalUrl && {
      alternates: { canonical: canonicalUrl },
    }),
  };
}
```

## Антипаттерн

```typescript
// ПЛОХО: метаданные внутри компонента — так не работает
export default function ProductPage() {
  // Нельзя использовать хуки или async/await здесь для метаданных
  return (
    <>
      {/* Устаревший подход, не используй next/head в App Router */}
      <head>
        <title>Продукт</title>
        <meta name="description" content="..." />
      </head>
      <main>{/* ... */}</main>
    </>
  );
}

// ПЛОХО: дублирование DB запроса
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  // Этот запрос дублируется в компоненте страницы!
  const product = await fetch(`/api/products/${slug}`).then(r => r.json());
  return { title: product.name };
}
// ХОРОШО: использовать React cache() для дедупликации запросов
import { cache } from "react";

const getProduct = cache(async (slug: string) => {
  return db.query.products.findFirst({ where: eq(products.slug, slug) });
});

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const product = await getProduct(slug); // дедуплицируется
  return { title: product?.name ?? "Not found" };
}

export default async function ProductPage({ params }: Props) {
  const { slug } = await params;
  const product = await getProduct(slug); // тот же кэш — один DB запрос
  // ...
}
```

## Связанные документы

- `knowledge/custom/09-seo/structured-data.md` — JSON-LD схемы для rich results
- `knowledge/custom/09-seo/sitemap-robots.md` — sitemap.ts и robots.ts
- `knowledge/custom/09-seo/geo-aeo.md` — оптимизация для AI-поисковиков
- `knowledge/custom/10-devops/vercel-deploy.md` — настройка `NEXT_PUBLIC_SITE_URL` в Vercel

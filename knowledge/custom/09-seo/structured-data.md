---
category: seo
topic: structured-data
status: draft
---

## Проблема / Контекст

Структурированные данные (JSON-LD) — способ сообщить поисковым системам о типе и содержимом страницы в машиночитаемом формате. Google использует их для отображения rich results: звёзды рейтингов, цены, хлебные крошки, FAQ-вставки в выдаче. Без JSON-LD сайт теряет потенциальные визуальные улучшения SERP и сниппеты, которые значительно повышают CTR.

Ключевые проблемы при реализации: отсутствие TypeScript типизации, вставка схем в неправильное место (клиентские компоненты), дублирование данных между схемами и метаданными, неверный формат дат и URLs.

## Решение

### Архитектура вставки JSON-LD

В Next.js 15 App Router JSON-LD вставляется через тег `<script type="application/ld+json">` непосредственно в Server Components — `page.tsx` или `layout.tsx`. Это гарантирует, что скрипт доступен при первоначальном HTTP-ответе.

```typescript
// Базовый паттерн вставки схемы
// app/products/[slug]/page.tsx
export default async function ProductPage({ params }: Props) {
  const { slug } = await params;
  const product = await getProduct(slug);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Product",
    name: product.name,
    // ...
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <main>{/* product content */}</main>
    </>
  );
}
```

### TypeScript типы для Schema.org

Создай централизованный файл типов для всех схем:

```typescript
// lib/structured-data/types.ts

export interface SchemaOrgBase {
  "@context": "https://schema.org";
  "@type": string;
}

export interface OrganizationSchema extends SchemaOrgBase {
  "@type": "Organization";
  name: string;
  url: string;
  logo?: string | ImageObjectSchema;
  description?: string;
  sameAs?: string[];
  contactPoint?: ContactPointSchema[];
  address?: PostalAddressSchema;
}

export interface WebSiteSchema extends SchemaOrgBase {
  "@type": "WebSite";
  name: string;
  url: string;
  potentialAction?: SearchActionSchema;
}

export interface SearchActionSchema {
  "@type": "SearchAction";
  target: {
    "@type": "EntryPoint";
    urlTemplate: string;
  };
  "query-input": string;
}

export interface ProductSchema extends SchemaOrgBase {
  "@type": "Product";
  name: string;
  description?: string;
  image?: string | string[];
  sku?: string;
  brand?: { "@type": "Brand"; name: string };
  offers?: OfferSchema | OfferSchema[];
  aggregateRating?: AggregateRatingSchema;
  review?: ReviewSchema[];
}

export interface OfferSchema {
  "@type": "Offer";
  price: number;
  priceCurrency: string;
  availability:
    | "https://schema.org/InStock"
    | "https://schema.org/OutOfStock"
    | "https://schema.org/PreOrder";
  url?: string;
  priceValidUntil?: string;
  seller?: { "@type": "Organization"; name: string };
}

export interface AggregateRatingSchema {
  "@type": "AggregateRating";
  ratingValue: number;
  reviewCount: number;
  bestRating?: number;
  worstRating?: number;
}

export interface ReviewSchema {
  "@type": "Review";
  reviewRating: { "@type": "Rating"; ratingValue: number; bestRating?: number };
  author: { "@type": "Person"; name: string };
  reviewBody?: string;
  datePublished?: string;
}

export interface ArticleSchema extends SchemaOrgBase {
  "@type": "Article" | "BlogPosting" | "NewsArticle";
  headline: string;
  description?: string;
  image?: string | string[];
  author: PersonSchema | OrganizationSchema;
  publisher: OrganizationSchema;
  datePublished: string;
  dateModified?: string;
  mainEntityOfPage?: { "@type": "WebPage"; "@id": string };
  articleBody?: string;
  wordCount?: number;
  keywords?: string;
}

export interface PersonSchema {
  "@type": "Person";
  name: string;
  url?: string;
  image?: string;
}

export interface BreadcrumbListSchema extends SchemaOrgBase {
  "@type": "BreadcrumbList";
  itemListElement: BreadcrumbItemSchema[];
}

export interface BreadcrumbItemSchema {
  "@type": "ListItem";
  position: number;
  name: string;
  item?: string;
}

export interface FAQPageSchema extends SchemaOrgBase {
  "@type": "FAQPage";
  mainEntity: FAQItemSchema[];
}

export interface FAQItemSchema {
  "@type": "Question";
  name: string;
  acceptedAnswer: {
    "@type": "Answer";
    text: string;
  };
}

export interface ImageObjectSchema {
  "@type": "ImageObject";
  url: string;
  width?: number;
  height?: number;
}

export interface ContactPointSchema {
  "@type": "ContactPoint";
  telephone?: string;
  email?: string;
  contactType: string;
  availableLanguage?: string;
}

export interface PostalAddressSchema {
  "@type": "PostalAddress";
  streetAddress?: string;
  addressLocality?: string;
  addressRegion?: string;
  postalCode?: string;
  addressCountry: string;
}

// Union тип для всех схем
export type AnySchema =
  | OrganizationSchema
  | WebSiteSchema
  | ProductSchema
  | ArticleSchema
  | BreadcrumbListSchema
  | FAQPageSchema;
```

### Organization + WebSite в root layout

Эти схемы вставляются один раз в корневой layout, они применяются ко всему сайту:

```typescript
// app/layout.tsx
import type { OrganizationSchema, WebSiteSchema } from "@/lib/structured-data/types";

const organizationSchema: OrganizationSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: "YourCompany",
  url: "https://yoursite.com",
  logo: {
    "@type": "ImageObject",
    url: "https://yoursite.com/logo.png",
    width: 200,
    height: 60,
  },
  description: "Описание компании для поисковых систем.",
  sameAs: [
    "https://t.me/yourhandle",
    "https://vk.com/yourhandle",
    "https://github.com/yourorg",
  ],
  contactPoint: [
    {
      "@type": "ContactPoint",
      email: "hello@yoursite.com",
      contactType: "customer support",
      availableLanguage: "Russian",
    },
  ],
};

const webSiteSchema: WebSiteSchema = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  name: "YourSite",
  url: "https://yoursite.com",
  potentialAction: {
    "@type": "SearchAction",
    target: {
      "@type": "EntryPoint",
      urlTemplate: "https://yoursite.com/search?q={search_term_string}",
    },
    "query-input": "required name=search_term_string",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru">
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(organizationSchema) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(webSiteSchema) }}
        />
        {children}
      </body>
    </html>
  );
}
```

### Product Schema с данными из Drizzle

```typescript
// lib/structured-data/product.ts
import type { ProductSchema } from "./types";

interface ProductFromDB {
  name: string;
  description: string;
  imageUrl: string | null;
  sku: string;
  price: number;
  currency: string;
  inStock: boolean;
  brand: string;
  rating: number | null;
  reviewCount: number;
  slug: string;
}

export function buildProductSchema(product: ProductFromDB): ProductSchema {
  return {
    "@context": "https://schema.org",
    "@type": "Product",
    name: product.name,
    description: product.description,
    image: product.imageUrl ?? undefined,
    sku: product.sku,
    brand: {
      "@type": "Brand",
      name: product.brand,
    },
    offers: {
      "@type": "Offer",
      price: product.price,
      priceCurrency: product.currency,
      availability: product.inStock
        ? "https://schema.org/InStock"
        : "https://schema.org/OutOfStock",
      url: `https://yoursite.com/products/${product.slug}`,
      seller: {
        "@type": "Organization",
        name: "YourStore",
      },
    },
    ...(product.rating !== null && {
      aggregateRating: {
        "@type": "AggregateRating",
        ratingValue: product.rating,
        reviewCount: product.reviewCount,
        bestRating: 5,
        worstRating: 1,
      },
    }),
  };
}
```

```typescript
// app/products/[slug]/page.tsx
import { buildProductSchema } from "@/lib/structured-data/product";
import { buildBreadcrumbSchema } from "@/lib/structured-data/breadcrumb";
import { db } from "@/lib/db";
import { products } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { notFound } from "next/navigation";

export default async function ProductPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;

  const product = await db.query.products.findFirst({
    where: eq(products.slug, slug),
    with: {
      category: true,
      reviews: {
        columns: { rating: true, body: true, createdAt: true },
        with: { user: { columns: { name: true } } },
        limit: 5,
      },
    },
  });

  if (!product) notFound();

  const productSchema = buildProductSchema({
    name: product.name,
    description: product.description,
    imageUrl: product.imageUrl,
    sku: product.sku,
    price: product.price / 100, // конвертация копеек в рубли
    currency: "RUB",
    inStock: product.stock > 0,
    brand: product.brand ?? "YourBrand",
    rating: product.avgRating,
    reviewCount: product.reviews.length,
    slug: product.slug,
  });

  const breadcrumbSchema = buildBreadcrumbSchema([
    { name: "Главная", url: "https://yoursite.com" },
    { name: product.category.name, url: `https://yoursite.com/categories/${product.category.slug}` },
    { name: product.name }, // последний элемент без URL
  ]);

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(productSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }}
      />
      <main>{/* product content */}</main>
    </>
  );
}
```

### BreadcrumbList Schema

```typescript
// lib/structured-data/breadcrumb.ts
import type { BreadcrumbListSchema } from "./types";

interface BreadcrumbItem {
  name: string;
  url?: string;
}

export function buildBreadcrumbSchema(items: BreadcrumbItem[]): BreadcrumbListSchema {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      ...(item.url && { item: item.url }),
    })),
  };
}
```

### Article Schema для блога

```typescript
// lib/structured-data/article.ts
import type { ArticleSchema } from "./types";

interface ArticleFromDB {
  title: string;
  excerpt: string;
  coverImage: string | null;
  authorName: string;
  authorUrl: string;
  publishedAt: Date;
  updatedAt: Date;
  slug: string;
  content: string;
  tags: string[];
}

export function buildArticleSchema(article: ArticleFromDB): ArticleSchema {
  return {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    headline: article.title,
    description: article.excerpt,
    image: article.coverImage ?? "https://yoursite.com/og-blog-default.png",
    author: {
      "@type": "Person",
      name: article.authorName,
      url: article.authorUrl,
    },
    publisher: {
      "@context": "https://schema.org",
      "@type": "Organization",
      name: "YourSite",
      url: "https://yoursite.com",
      logo: {
        "@type": "ImageObject",
        url: "https://yoursite.com/logo.png",
      },
    },
    datePublished: article.publishedAt.toISOString(),
    dateModified: article.updatedAt.toISOString(),
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `https://yoursite.com/blog/${article.slug}`,
    },
    wordCount: article.content.split(/\s+/).length,
    keywords: article.tags.join(", "),
  };
}
```

### FAQPage Schema

```typescript
// lib/structured-data/faq.ts
import type { FAQPageSchema } from "./types";

export interface FAQItem {
  question: string;
  answer: string;
}

export function buildFAQSchema(items: FAQItem[]): FAQPageSchema {
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: items.map((item) => ({
      "@type": "Question",
      name: item.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: item.answer,
      },
    })),
  };
}
```

```typescript
// app/faq/page.tsx — или добавить FAQ на продуктовую страницу
import { buildFAQSchema } from "@/lib/structured-data/faq";

const faqItems = [
  {
    question: "Как оформить заказ?",
    answer: "Выберите товар, добавьте в корзину и оформите через форму заказа. Доставка 1-3 дня.",
  },
  {
    question: "Можно ли вернуть товар?",
    answer: "Да, возврат в течение 14 дней в соответствии с законом о защите прав потребителей.",
  },
];

export default function FAQPage() {
  const schema = buildFAQSchema(faqItems);

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
      />
      <main>
        <h1>Часто задаваемые вопросы</h1>
        {faqItems.map((item) => (
          <details key={item.question}>
            <summary>{item.question}</summary>
            <p>{item.answer}</p>
          </details>
        ))}
      </main>
    </>
  );
}
```

### Несколько схем на одной странице

На странице продукта можно объединить Product + BreadcrumbList + FAQPage:

```typescript
// Хелпер для рендера нескольких схем
// components/json-ld.tsx
import type { AnySchema } from "@/lib/structured-data/types";

interface JsonLdProps {
  schemas: AnySchema[];
}

export function JsonLd({ schemas }: JsonLdProps) {
  return (
    <>
      {schemas.map((schema, index) => (
        <script
          key={`${schema["@type"]}-${index}`}
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
        />
      ))}
    </>
  );
}
```

```typescript
// Использование в странице
import { JsonLd } from "@/components/json-ld";

export default async function ProductPage({ params }: Props) {
  // ... fetch product, reviews, faq

  const schemas = [
    buildProductSchema(product),
    buildBreadcrumbSchema(breadcrumbs),
    ...(product.faqs.length > 0 ? [buildFAQSchema(product.faqs)] : []),
  ];

  return (
    <>
      <JsonLd schemas={schemas} />
      <main>{/* ... */}</main>
    </>
  );
}
```

### Тестирование структурированных данных

После деплоя проверь схемы следующими инструментами:

1. **Google Rich Results Test**: https://search.google.com/test/rich-results — проверяет, имеет ли страница право на rich results
2. **Schema.org Validator**: https://validator.schema.org — валидирует JSON-LD по спецификации
3. **Google Search Console** → Enhancements → отслеживает ошибки в структурированных данных в продакшне

Для локального тестирования можно использовать ngrok или Vercel preview URLs напрямую в Rich Results Test.

## Пример кода

### Утилита для санитизации HTML в описаниях

Google требует текст без HTML тегов в полях `description`, `reviewBody` и т.д.:

```typescript
// lib/structured-data/utils.ts

export function stripHtml(html: string): string {
  return html
    .replace(/<[^>]*>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

export function truncate(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength - 3) + "...";
}

// Форматирование цены для schema.org (без символа валюты)
export function formatPrice(priceInCents: number): number {
  return Math.round(priceInCents) / 100;
}

// ISO дата без миллисекунд (более широкая совместимость)
export function toSchemaDate(date: Date): string {
  return date.toISOString().split(".")[0] + "Z";
}
```

## Антипаттерн

```typescript
// ПЛОХО: JSON-LD в клиентском компоненте
"use client";
export function ProductSchemaClient({ product }: { product: Product }) {
  // Клиентский компонент — скрипт не будет в начальном HTML,
  // поисковик может его не обработать
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify({ name: product.name }) }}
    />
  );
}

// ПЛОХО: данные не совпадают с видимым контентом
// Если schema говорит price: 100, а на странице написано 200 — Google может исключить
// страницу из rich results за несоответствие

// ПЛОХО: HTML теги в полях описания
const badSchema = {
  description: "<p>Описание <strong>продукта</strong></p>", // НЕВЕРНО
};

// ХОРОШО:
const goodSchema = {
  description: stripHtml("<p>Описание <strong>продукта</strong></p>"),
  // -> "Описание продукта"
};
```

## Связанные документы

- `knowledge/custom/09-seo/metadata-api.md` — метаданные Open Graph и Twitter Cards
- `knowledge/custom/09-seo/sitemap-robots.md` — sitemap и robots.txt
- `knowledge/custom/09-seo/geo-aeo.md` — GEO/AEO оптимизация для AI-поисковиков

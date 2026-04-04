---
category: seo
topic: geo-aeo
status: draft
---

## Проблема / Контекст

GEO (Generative Engine Optimization) и AEO (Answer Engine Optimization) — оптимизация контента для AI-powered поисковиков: Perplexity AI, ChatGPT Search, Google AI Overviews, Microsoft Copilot и аналогичных систем. В отличие от традиционного SEO, ориентированного на ссылки и ключевые слова, AI-поисковики синтезируют ответы из источников — и ваш контент должен быть structured, factual и citation-friendly.

К 2025-2026 году значительная часть информационных запросов обрабатывается AI-инструментами, которые не показывают список сайтов, а дают прямой ответ. Попасть в источники, на которые ссылается AI — новый SEO-приоритет. При этом традиционное SEO не исчезает: для транзакционных запросов Google по-прежнему показывает классическую выдачу.

## Решение

### Принципы GEO/AEO

**1. Прямые ответы на вопросы** — контент должен начинаться с прямого, фактического ответа, без вводных слов. AI-системы извлекают "answer snippets" — первые 1-3 предложения после заголовка.

**2. Чёткая структура** — заголовки H1-H3, определения, списки, таблицы. AI-краулеры лучше обрабатывают структурированный контент.

**3. E-E-A-T сигналы** (Experience, Expertise, Authoritativeness, Trustworthiness) — авторство, даты обновления, источники, биографии авторов.

**4. FAQ и Question-Answer блоки** — прямые форматы вопрос-ответ наиболее часто цитируются AI-системами.

**5. Фактические данные** — числа, даты, конкретные факты. "Увеличивает конверсию на 23%" лучше чем "значительно улучшает".

**6. `llms.txt`** — новый стандарт (аналог `robots.txt`) для обозначения контента, доступного для LLM-обработки.

### llms.txt — файл для AI-краулеров

`llms.txt` — инициатива (не стандарт W3C, но широко принятая конвенция) для обозначения, какой контент может использоваться LLM-системами и как он структурирован.

```typescript
// app/llms.txt/route.ts
import { NextResponse } from "next/server";
import { db } from "@/lib/db";
import { articles, products } from "@/lib/db/schema";
import { eq, and, desc } from "drizzle-orm";

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://yoursite.com";

export async function GET() {
  // Получаем последние опубликованные материалы
  const recentArticles = await db.query.articles.findMany({
    where: and(eq(articles.status, "published"), eq(articles.isDeleted, false)),
    columns: { title: true, slug: true, excerpt: true, updatedAt: true },
    orderBy: (articles, { desc }) => [desc(articles.publishedAt)],
    limit: 50,
  });

  const topProducts = await db.query.products.findMany({
    where: and(eq(products.isPublished, true), eq(products.isDeleted, false)),
    columns: { name: true, slug: true, description: true },
    orderBy: (products, { desc }) => [desc(products.viewCount)],
    limit: 20,
  });

  const content = `# YourSite — llms.txt

> YourSite — платформа для [краткое описание бизнеса].
> Основана в 2020 году. Россия, Москва.
> Контакт: hello@yoursite.com

## О сайте

YourSite предоставляет [описание продукта/услуги].
Аудитория: [описание целевой аудитории].

## Ключевые разделы

- [Главная](${SITE_URL}/) — обзор продуктов и услуг
- [Блог](${SITE_URL}/blog) — экспертные статьи по теме
- [О компании](${SITE_URL}/about) — информация о команде и миссии
- [Контакты](${SITE_URL}/contact)

## Последние статьи

${recentArticles
  .map(
    (a) =>
      `- [${a.title}](${SITE_URL}/blog/${a.slug}) — ${a.excerpt?.slice(0, 100) ?? ""}`
  )
  .join("\n")}

## Популярные продукты

${topProducts
  .map(
    (p) =>
      `- [${p.name}](${SITE_URL}/products/${p.slug}) — ${p.description?.slice(0, 80) ?? ""}`
  )
  .join("\n")}

## Разрешения для AI

Этот сайт разрешает LLM-системам:
- Цитировать публичный контент с указанием источника
- Индексировать страницы /blog, /products, /about
- Использовать контент для обучения AI-ответов

Запрещено:
- Scraping /dashboard, /admin, /api
- Массовое скачивание контента без атрибуции

## Технические данные

- Платформа: Next.js 15 App Router
- Язык контента: русский
- Обновление: ежедневно
- Sitemap: ${SITE_URL}/sitemap.xml
- Последнее обновление: ${new Date().toISOString().split("T")[0]}
`;

  return new NextResponse(content, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=86400",
    },
  });
}
```

### Компонент для структурирования ответов (Answer Blocks)

AI-системы извлекают "answer snippets" — чёткие определения и ответы в начале секций:

```typescript
// components/answer-block.tsx
// Компонент для контента, оптимизированного под AI-цитирование

interface AnswerBlockProps {
  question: string;
  answer: string;
  facts?: Array<{ label: string; value: string }>;
  updatedAt?: Date;
}

export function AnswerBlock({
  question,
  answer,
  facts,
  updatedAt,
}: AnswerBlockProps) {
  return (
    // Используем itemScope/itemType для дополнительного семантического контекста
    <section
      className="rounded-lg border border-border bg-muted/30 p-6"
      itemScope
      itemType="https://schema.org/Question"
    >
      <h3 className="text-lg font-semibold mb-3" itemProp="name">
        {question}
      </h3>
      <div
        itemScope
        itemType="https://schema.org/Answer"
        itemProp="acceptedAnswer"
      >
        <p className="text-foreground leading-relaxed" itemProp="text">
          {answer}
        </p>
        {facts && facts.length > 0 && (
          <dl className="mt-4 grid grid-cols-2 gap-2">
            {facts.map((fact) => (
              <div key={fact.label} className="flex flex-col">
                <dt className="text-sm text-muted-foreground">{fact.label}</dt>
                <dd className="font-medium">{fact.value}</dd>
              </div>
            ))}
          </dl>
        )}
      </div>
      {updatedAt && (
        <time
          dateTime={updatedAt.toISOString()}
          className="mt-3 block text-xs text-muted-foreground"
        >
          Обновлено: {updatedAt.toLocaleDateString("ru-RU")}
        </time>
      )}
    </section>
  );
}
```

### Паттерны структуры контента для AI-видимости

```typescript
// components/article-layout.tsx — шаблон статьи с AEO-оптимизацией

interface ArticleLayoutProps {
  title: string;
  description: string; // Прямой ответ на вопрос, вынесенный в заголовок
  author: { name: string; title: string; avatarUrl: string };
  publishedAt: Date;
  updatedAt: Date;
  readingTimeMinutes: number;
  children: React.ReactNode;
}

export function ArticleLayout({
  title,
  description,
  author,
  publishedAt,
  updatedAt,
  readingTimeMinutes,
  children,
}: ArticleLayoutProps) {
  return (
    <article
      className="max-w-3xl mx-auto"
      itemScope
      itemType="https://schema.org/Article"
    >
      {/* Заголовок — должен быть вопросом или четким утверждением */}
      <h1 className="text-4xl font-bold mb-4" itemProp="headline">
        {title}
      </h1>

      {/* КЛЮЧЕВОЙ ЭЛЕМЕНТ: прямой ответ в первом абзаце — именно его цитируют AI */}
      <p
        className="text-xl text-muted-foreground mb-6 font-medium leading-relaxed"
        itemProp="description"
      >
        {description}
      </p>

      {/* E-E-A-T: авторство видно краулеру */}
      <div
        className="flex items-center gap-3 mb-8 pb-6 border-b"
        itemProp="author"
        itemScope
        itemType="https://schema.org/Person"
      >
        <img
          src={author.avatarUrl}
          alt={author.name}
          className="w-10 h-10 rounded-full"
          itemProp="image"
        />
        <div>
          <p className="font-medium" itemProp="name">
            {author.name}
          </p>
          <p className="text-sm text-muted-foreground" itemProp="jobTitle">
            {author.title}
          </p>
        </div>
        <div className="ml-auto text-sm text-muted-foreground">
          <time
            dateTime={publishedAt.toISOString()}
            itemProp="datePublished"
          >
            {publishedAt.toLocaleDateString("ru-RU")}
          </time>
          {" · "}
          <time dateTime={updatedAt.toISOString()} itemProp="dateModified">
            Обновлено {updatedAt.toLocaleDateString("ru-RU")}
          </time>
          {" · "}
          <span>{readingTimeMinutes} мин чтения</span>
        </div>
      </div>

      {/* Тело статьи */}
      <div
        className="prose prose-neutral dark:prose-invert max-w-none"
        itemProp="articleBody"
      >
        {children}
      </div>
    </article>
  );
}
```

### FAQ компонент с JSON-LD для AI-видимости

FAQ секции — наиболее часто цитируемый формат AI-системами. Комбинируй видимый контент с JSON-LD:

```typescript
// components/faq-section.tsx
import { buildFAQSchema } from "@/lib/structured-data/faq";

interface FAQSectionProps {
  items: Array<{ question: string; answer: string }>;
  title?: string;
}

export function FAQSection({ items, title = "Часто задаваемые вопросы" }: FAQSectionProps) {
  const schema = buildFAQSchema(items);

  return (
    <section
      className="mt-12"
      itemScope
      itemType="https://schema.org/FAQPage"
    >
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
      />
      <h2 className="text-2xl font-bold mb-6">{title}</h2>
      <div className="space-y-4">
        {items.map((item, index) => (
          <details
            key={index}
            className="group border rounded-lg"
            itemScope
            itemType="https://schema.org/Question"
            itemProp="mainEntity"
          >
            <summary
              className="flex items-center justify-between p-4 cursor-pointer font-medium"
              itemProp="name"
            >
              {item.question}
            </summary>
            <div
              className="px-4 pb-4 text-muted-foreground"
              itemScope
              itemType="https://schema.org/Answer"
              itemProp="acceptedAnswer"
            >
              <p itemProp="text">{item.answer}</p>
            </div>
          </details>
        ))}
      </div>
    </section>
  );
}
```

### Structured Definitions — для терминологических запросов

Когда пользователи спрашивают "что такое X", AI ищет чёткое определение:

```typescript
// components/definition-block.tsx

interface DefinitionBlockProps {
  term: string;
  definition: string;
  context?: string;
}

export function DefinitionBlock({ term, definition, context }: DefinitionBlockProps) {
  return (
    <div
      className="my-6 border-l-4 border-primary pl-6"
      itemScope
      itemType="https://schema.org/DefinedTerm"
    >
      <dt
        className="text-lg font-bold mb-2"
        itemProp="name"
      >
        {term}
      </dt>
      <dd
        className="text-muted-foreground leading-relaxed"
        itemProp="description"
      >
        {definition}
      </dd>
      {context && (
        <p className="mt-2 text-sm text-muted-foreground/70">
          {context}
        </p>
      )}
    </div>
  );
}
```

### Приоритеты схем для GEO/AEO

Не все JSON-LD схемы одинаково влияют на видимость в AI. Порядок приоритетов:

```typescript
// lib/geo-priorities.ts

/**
 * Приоритет схем для AI-видимости (от высокого к низкому):
 *
 * 1. FAQPage — прямые Q&A, наиболее цитируемый формат
 * 2. HowTo — пошаговые инструкции
 * 3. Article / BlogPosting — с четким author и datePublished
 * 4. Product с AggregateRating — факты + социальное доказательство
 * 5. Organization — доверие к источнику
 * 6. BreadcrumbList — контекст навигации
 */

export const GEO_SCHEMA_PRIORITY = {
  FAQPage: 1,
  HowTo: 2,
  Article: 3,
  BlogPosting: 3,
  Product: 4,
  Organization: 5,
  BreadcrumbList: 6,
} as const;

// HowTo Schema для инструкций
interface HowToSchema {
  "@context": "https://schema.org";
  "@type": "HowTo";
  name: string;
  description: string;
  step: HowToStep[];
  totalTime?: string; // ISO 8601 duration: "PT30M" = 30 минут
}

interface HowToStep {
  "@type": "HowToStep";
  name: string;
  text: string;
  url?: string;
  image?: string;
}

export function buildHowToSchema(
  title: string,
  description: string,
  steps: Array<{ name: string; text: string }>,
  totalMinutes?: number
): HowToSchema {
  return {
    "@context": "https://schema.org",
    "@type": "HowTo",
    name: title,
    description,
    step: steps.map((step) => ({
      "@type": "HowToStep",
      name: step.name,
      text: step.text,
    })),
    ...(totalMinutes && { totalTime: `PT${totalMinutes}M` }),
  };
}
```

### Robots.txt с разрешениями для AI-краулеров

```typescript
// app/robots.ts — дополнение с AI-краулерами
import type { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/dashboard/", "/admin/", "/api/", "/auth/"],
      },
      // Явно разрешаем основным AI-краулерам
      {
        userAgent: "GPTBot",        // OpenAI ChatGPT Search
        allow: "/",
        disallow: ["/dashboard/", "/admin/", "/api/"],
      },
      {
        userAgent: "PerplexityBot", // Perplexity AI
        allow: "/",
        disallow: ["/dashboard/", "/admin/", "/api/"],
      },
      {
        userAgent: "Google-Extended", // Google AI Overviews / Gemini
        allow: "/",
        disallow: ["/dashboard/", "/admin/", "/api/"],
      },
      {
        userAgent: "Applebot-Extended", // Apple Intelligence
        allow: "/",
        disallow: ["/dashboard/", "/admin/", "/api/"],
      },
      {
        userAgent: "ClaudeBot", // Anthropic Claude
        allow: "/",
        disallow: ["/dashboard/", "/admin/", "/api/"],
      },
      // Блокируем менее качественные агрегаторы
      {
        userAgent: ["AhrefsBot", "SemrushBot", "DotBot"],
        disallow: "/",
      },
    ],
    sitemap: `${process.env.NEXT_PUBLIC_SITE_URL}/sitemap.xml`,
  };
}
```

## Пример кода

### Полная страница статьи с GEO/AEO оптимизацией

```typescript
// app/blog/[slug]/page.tsx
import { db } from "@/lib/db";
import { articles } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { notFound } from "next/navigation";
import { ArticleLayout } from "@/components/article-layout";
import { FAQSection } from "@/components/faq-section";
import { AnswerBlock } from "@/components/answer-block";
import { buildArticleSchema } from "@/lib/structured-data/article";
import { cache } from "react";

const getArticle = cache(async (slug: string) => {
  return db.query.articles.findFirst({
    where: eq(articles.slug, slug),
    with: {
      author: true,
      faqs: { orderBy: (f, { asc }) => [asc(f.order)] },
    },
  });
});

export default async function ArticlePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const article = await getArticle(slug);
  if (!article) notFound();

  const schema = buildArticleSchema({
    title: article.title,
    excerpt: article.excerpt,
    coverImage: article.coverImage,
    authorName: article.author.name,
    authorUrl: `https://yoursite.com/authors/${article.author.slug}`,
    publishedAt: article.publishedAt!,
    updatedAt: article.updatedAt,
    slug: article.slug,
    content: article.content,
    tags: article.tags,
  });

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
      />
      <ArticleLayout
        title={article.title}
        description={article.excerpt} // Первый абзац — прямой ответ
        author={article.author}
        publishedAt={article.publishedAt!}
        updatedAt={article.updatedAt}
        readingTimeMinutes={article.readingTimeMinutes}
      >
        {/* Основной контент */}
        <div dangerouslySetInnerHTML={{ __html: article.contentHtml }} />

        {/* FAQ для AI-цитирования */}
        {article.faqs.length > 0 && (
          <FAQSection items={article.faqs} />
        )}
      </ArticleLayout>
    </>
  );
}
```

## Антипаттерн

```typescript
// ПЛОХО: контент начинается с вводных фраз без ответа
// "В данной статье мы рассмотрим важный вопрос о..." — AI пропускает это
// ХОРОШО: "Next.js 15 использует App Router по умолчанию.
//          Для создания страницы создайте файл page.tsx в папке app/."

// ПЛОХО: блокировать AI-краулеры без необходимости
// robots.txt: User-agent: GPTBot\nDisallow: /
// Это лишает сайт видимости в ChatGPT Search и похожих

// ПЛОХО: контент без авторства и дат
// AI-системы снижают доверие к контенту без E-E-A-T сигналов

// ПЛОХО: llms.txt с неточной информацией
// Файл должен отражать реальное содержимое сайта
```

## Связанные документы

- `knowledge/custom/09-seo/metadata-api.md` — метаданные и OpenGraph
- `knowledge/custom/09-seo/structured-data.md` — JSON-LD схемы (FAQPage, Article)
- `knowledge/custom/09-seo/sitemap-robots.md` — robots.txt с AI-краулерами

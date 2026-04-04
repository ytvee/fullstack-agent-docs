---
category: antipatterns
topic: secrets-exposure
status: draft
---

## Проблема / Контекст

Утечка секретов в Next.js — критическая уязвимость. Два основных вектора:

1. **`NEXT_PUBLIC_` prefix** — любая переменная с этим префиксом попадает в JS бандл, доступна в браузере. Разработчики случайно добавляют его к секретным ключам.

2. **Импорт серверного кода в Client Components** — если Client Component импортирует модуль, который импортирует `process.env.SECRET_KEY`, Next.js может включить это значение в бандл через tree-shaking артефакты.

3. **Случайное включение в бандл** — серверные модули (Drizzle, NodeJS crypto, stripe server SDK) не должны попадать в клиентский бандл, но попадают через неправильную архитектуру импортов.

## Решение

**`server-only` пакет** — жёсткий guard на импорт серверных модулей в клиентский код (ошибка сборки). **Правило именования**: никогда не добавляй `NEXT_PUBLIC_` к ключам которые не должны быть публичными. **Аудит бандла** — регулярно проверяй `next build --debug` или bundle analyzer.

**Установка:**
```bash
npm install server-only client-only
```

## Пример кода

### 1. NEXT_PUBLIC_ — что попадает в браузер

```bash
# .env.local

# ✅ БЕЗОПАСНО — серверные переменные (без NEXT_PUBLIC_)
DATABASE_URL=postgresql://user:password@localhost:5432/db
STRIPE_SECRET_KEY=sk_live_...
OPENAI_API_KEY=sk-...
RESEND_API_KEY=re_...
AUTH_SECRET=super-secret-random-string
UPLOADTHING_SECRET=sk_live_...
INTERNAL_API_SECRET=internal-only-secret

# ✅ БЕЗОПАСНО — клиентские переменные (с NEXT_PUBLIC_)
NEXT_PUBLIC_APP_URL=https://myapp.com
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...  # publishable key — НЕ secret
NEXT_PUBLIC_SENTRY_DSN=https://xxx@sentry.io/123  # DSN — публичный по дизайну
NEXT_PUBLIC_UPLOADTHING_APP_ID=app-id  # app ID — не секрет

# ❌ ОПАСНО — секрет с NEXT_PUBLIC_ → утекает в браузер!
NEXT_PUBLIC_STRIPE_SECRET_KEY=sk_live_...   # КАТАСТРОФА
NEXT_PUBLIC_DATABASE_URL=postgresql://...   # КАТАСТРОФА
NEXT_PUBLIC_OPENAI_API_KEY=sk-...           # КАТАСТРОФА
NEXT_PUBLIC_AUTH_SECRET=...                 # КАТАСТРОФА
```

### 2. server-only — жёсткий guard от импорта на клиенте

```typescript
// src/lib/db.ts
import "server-only"; // ← Если этот файл импортировать в Client Component → ошибка сборки

import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "@/db/schema";

const client = postgres(process.env.DATABASE_URL!);
export const db = drizzle(client, { schema });

// src/lib/stripe.ts
import "server-only"; // ← Защита от случайного импорта в клиент

import Stripe from "stripe";
export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: "2024-11-20.acacia",
});

// src/lib/resend.ts
import "server-only";

import { Resend } from "resend";
export const resend = new Resend(process.env.RESEND_API_KEY!);

// src/lib/auth.ts
import "server-only";
// Auth.js конфиг — содержит AUTH_SECRET, не должен попасть в бандл
```

### 3. Что происходит при нарушении

```typescript
// src/components/bad-component.tsx
"use client";

// ❌ Эта строка вызовет ошибку сборки благодаря server-only:
// Error: You're importing a component that imports server-only.
// It only works in a Server Component but one of its parents is marked with "use client"
import { db } from "@/lib/db";

export function BadClientComponent() {
  // Без server-only: db.ts попадёт в бандл
  // process.env.DATABASE_URL окажется в исходниках на клиенте
  return <div>...</div>;
}
```

### 4. Типизированная конфигурация env с валидацией

```typescript
// src/env.ts — единое место для всех переменных окружения

import { z } from "zod";

// Схема ТОЛЬКО для серверных переменных
const serverEnvSchema = z.object({
  // БД
  DATABASE_URL: z.string().url(),

  // Auth
  AUTH_SECRET: z.string().min(32, "AUTH_SECRET must be at least 32 characters"),
  GITHUB_CLIENT_ID: z.string(),
  GITHUB_CLIENT_SECRET: z.string(),

  // Stripe
  STRIPE_SECRET_KEY: z.string().startsWith("sk_"),
  STRIPE_WEBHOOK_SECRET: z.string().startsWith("whsec_"),

  // Email
  RESEND_API_KEY: z.string().startsWith("re_"),

  // Upload
  UPLOADTHING_SECRET: z.string(),
  UPLOADTHING_APP_ID: z.string(),

  // Node
  NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
});

// Схема для ПУБЛИЧНЫХ переменных
const clientEnvSchema = z.object({
  NEXT_PUBLIC_APP_URL: z.string().url(),
  NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY: z.string().startsWith("pk_"),
  NEXT_PUBLIC_SENTRY_DSN: z.string().url().optional(),
});

// Парсим и валидируем при старте
const _serverEnv = serverEnvSchema.safeParse(process.env);
const _clientEnv = clientEnvSchema.safeParse({
  NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL,
  NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY: process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY,
  NEXT_PUBLIC_SENTRY_DSN: process.env.NEXT_PUBLIC_SENTRY_DSN,
});

if (!_serverEnv.success) {
  console.error("❌ Invalid server environment variables:", _serverEnv.error.format());
  throw new Error("Invalid server environment variables");
}

if (!_clientEnv.success) {
  console.error("❌ Invalid client environment variables:", _clientEnv.error.format());
  throw new Error("Invalid client environment variables");
}

// Серверный объект — только для серверного кода
import "server-only";
export const serverEnv = _serverEnv.data;

// Клиентский объект — безопасен для импорта везде
export const clientEnv = _clientEnv.data;
```

### 5. Правильные паттерны использования API ключей

```typescript
// src/actions/send-email.ts — ПРАВИЛЬНО: серверный ключ только в Server Action
"use server";

import { resend } from "@/lib/resend"; // server-only guard защитит
import { auth } from "@/lib/auth";

export async function sendWelcomeEmail(userId: string) {
  const session = await auth();
  if (!session?.user?.id) return;

  await resend.emails.send({
    from: "noreply@myapp.com",
    to: session.user.email!,
    subject: "Welcome to MyApp",
    html: "<p>Welcome!</p>",
  });
}

// src/components/stripe-payment.tsx — ПРАВИЛЬНО: publishable key на клиенте
"use client";

import { loadStripe } from "@stripe/stripe-js";
import { clientEnv } from "@/env";

// Publishable key — специально создан для использования на клиенте
const stripePromise = loadStripe(clientEnv.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY);

// src/actions/payment.ts — ПРАВИЛЬНО: secret key только на сервере
"use server";

import { stripe } from "@/lib/stripe"; // server-only
export async function createPaymentIntent(amount: number) {
  const paymentIntent = await stripe.paymentIntents.create({
    amount,
    currency: "usd",
  });
  // Клиенту отправляем только clientSecret — это безопасно
  return { clientSecret: paymentIntent.client_secret };
}
```

### 6. Аудит клиентского бандла

```bash
# Метод 1: @next/bundle-analyzer
npm install @next/bundle-analyzer

# next.config.ts
import bundleAnalyzer from "@next/bundle-analyzer";
const withBundleAnalyzer = bundleAnalyzer({
  enabled: process.env.ANALYZE === "true",
});
export default withBundleAnalyzer({});

# Запуск:
ANALYZE=true npm run build
# Откроется браузер с визуализацией бандла

# Метод 2: Проверка через grep после сборки
npm run build
grep -r "sk_live" .next/static/     # Stripe secret key в статике?
grep -r "postgresql://" .next/static/  # DATABASE_URL в статике?
grep -r "RESEND" .next/static/       # API ключи в статике?

# Метод 3: next/dist/compiled инспекция
# После сборки проверяем .next/static/chunks/
# Ищем паттерны секретов через:
strings .next/static/chunks/*.js | grep -E "sk_live|re_[A-Za-z]|postgresql://"
```

### 7. client-only для Browser-only кода

```typescript
// src/lib/analytics.ts — работает только в браузере
import "client-only"; // Ошибка если импортировать в Server Component

export function trackEvent(event: string, properties?: Record<string, unknown>) {
  if (typeof window === "undefined") return;
  // @ts-expect-error — analytics не типизирован
  window.analytics?.track(event, properties);
}

export function initAnalytics() {
  if (typeof window === "undefined") return;
  // Posthog, Mixpanel и т.п.
}
```

### 8. Безопасный паттерн для передачи конфига клиенту

```typescript
// Иногда клиенту нужны некоторые конфигурационные данные с сервера
// НЕ секреты, а настройки

// src/app/layout.tsx — Server Component
import { getPublicConfig } from "@/lib/config";

export default async function RootLayout({ children }) {
  // Только публичные данные — никаких секретов
  const publicConfig = await getPublicConfig();

  return (
    <html>
      <body>
        {/* Передаём как props, не через window.__NEXT_DATA__ напрямую */}
        <ConfigProvider config={publicConfig}>
          {children}
        </ConfigProvider>
      </body>
    </html>
  );
}

// src/lib/config.ts
import "server-only";

export async function getPublicConfig() {
  return {
    appName: "MyApp",
    version: process.env.npm_package_version,
    features: {
      payments: Boolean(process.env.STRIPE_SECRET_KEY), // наличие фичи — не сам ключ!
      ai: Boolean(process.env.OPENAI_API_KEY),
    },
    // НЕ ВКЛЮЧАТЬ: DATABASE_URL, SECRET_KEY, и т.п.
  };
}
```

## Антипаттерн

```typescript
// ❌ ПЛОХО #1: Случайный NEXT_PUBLIC_ для "удобства"
// .env
NEXT_PUBLIC_SUPABASE_SERVICE_ROLE_KEY=eyJ...  // Полный доступ к БД!

// ❌ ПЛОХО #2: Создание API proxy без проверки
// src/app/api/openai/route.ts
export async function POST(req: Request) {
  const { prompt } = await req.json();
  // Нет аутентификации → любой может использовать твой OpenAI ключ!
  const response = await openai.chat.completions.create({
    model: "gpt-4",
    messages: [{ role: "user", content: prompt }],
  });
  return Response.json(response);
}

// ❌ ПЛОХО #3: Логирование секретов
console.log("Config:", process.env); // Все env переменные в логах!
console.log("DB URL:", process.env.DATABASE_URL); // В Vercel логах это видно!

// ❌ ПЛОХО #4: Секреты в исходном коде (а не в .env)
export const stripe = new Stripe("sk_live_abc123HARDCODED", {...}); // В git навсегда

// ❌ ПЛОХО #5: Передача секретов через URL
fetch(`/api/data?apiKey=${process.env.SECRET_KEY}`); // В браузер history, логах сервера
```

## Связанные документы

- `knowledge/custom/03-antipatterns/use-client-abuse.md` — импорт серверного кода в клиент
- `knowledge/custom/06-security/` — OWASP Sensitive Data Exposure
- `knowledge/custom/04-linting/eslint-rules-explained.md` — no-restricted-imports для защиты

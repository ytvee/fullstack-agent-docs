# 30 - Security

> **Область применения:** Все файлы проекта
>
> **Взаимодействие:** Дополняет `00-context.md`. Базовые правила (env, Git) описаны там. Здесь — архитектура безопасности, паттерны и конфигурации.

## 1. Модель угроз Next.js 15

Перед реализацией любой фичи с данными — явно ответь на три вопроса:

1. Кто может вызвать этот код? (Server Action / Route Handler — публичный HTTP-эндпоинт)
2. Может ли ответ утечь на клиент? (Server Component → Client Component граница)
3. Проверяется ли авторизация рядом с данными, а не только в middleware?

Middleware — не граница безопасности. Используй его только для редиректов и UX-оптимизаций. Реальная проверка авторизации должна быть в Data Access Layer.

> **CVE-2025-29927:** В марте 2025 раскрыта критическая уязвимость (CVSS 9.1) в Next.js 11.1.4–15.2.2. Атакующий мог передать заголовок `x-middleware-subrequest` и полностью обойти middleware, включая все проверки аутентификации. Исправлено в Next.js **15.2.3+**. Убедись что версия актуальна.

---

## 2. Data Access Layer (DAL)

Официальная рекомендация Next.js для новых проектов: вся логика доступа к данным — в отдельном слое `src/lib/dal.ts` или `src/features/*/queries.ts`.

Каждый DAL-файл обязан начинаться с:

```typescript
import 'server-only'
```

Это вызовет ошибку сборки, если DAL-модуль будет импортирован в Client Component.

### Структура DAL-функции

```typescript
// src/lib/dal.ts
import 'server-only'
import { cache } from 'react'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import { db } from '@/lib/db'

// cache() — одна проверка сессии за весь render-pass, без дублирования запросов к БД
export const verifySession = cache(async () => {
  const cookieStore = await cookies()
  const token = cookieStore.get('session')?.value
  if (!token) redirect('/login')

  const session = await validateToken(token)
  if (!session) redirect('/login')

  return session
})

// Никогда не возвращай сырой ORM-объект — только DTO с нужными полями
export async function getUserProfile(targetUserId: string) {
  const session = await verifySession()

  // Проверка авторизации рядом с данными (authorization, не только authentication)
  if (session.userId !== targetUserId && session.role !== 'admin') {
    return null
  }

  return db.user.findUnique({
    where: { id: targetUserId },
    select: { id: true, name: true, email: true }, // только нужные поля
  })
}
```

### Правила DAL

* `import 'server-only'` — обязателен в каждом файле DAL.
* Верификация сессии — через `cache()` из React. Одна функция `verifySession` вызывается везде.
* Авторизация проверяется внутри DAL-функции, не в компоненте.
* Возвращай DTO — только поля которые нужны UI. Никогда не возвращай сырые Prisma-объекты с полями вроде `passwordHash`, `internalNotes`.
* Прямые вызовы DAL из Server Components — не делай `fetch('http://localhost/api/...')`.

---

## 3. Безопасность Server Actions

Server Action — публичный HTTP POST-эндпоинт. Проверь каждый по этому шаблону:

```typescript
// features/posts/actions.ts
'use server'

import { z } from 'zod'
import { revalidatePath } from 'next/cache'
import { verifySession } from '@/lib/dal'
import { db } from '@/lib/db'

const UpdatePostSchema = z.object({
  postId: z.string().cuid(),
  title: z.string().min(1).max(200),
  content: z.string().min(1),
})

export async function updatePost(formData: FormData) {
  // 1. Аутентификация — кто вызывает?
  const session = await verifySession()

  // 2. Валидация входных данных через Zod
  const parsed = UpdatePostSchema.safeParse({
    postId: formData.get('postId'),
    title: formData.get('title'),
    content: formData.get('content'),
  })
  if (!parsed.success) return { error: parsed.error.flatten() }

  // 3. Авторизация — имеет ли этот пользователь право на это действие?
  // Проверка владения ресурсом предотвращает IDOR-атаки
  const post = await db.post.findUnique({ where: { id: parsed.data.postId } })
  if (!post) return { error: 'Not found' }
  if (post.authorId !== session.userId) return { error: 'Forbidden' }

  // 4. Мутация
  await db.post.update({
    where: { id: parsed.data.postId },
    data: { title: parsed.data.title, content: parsed.data.content },
  })

  revalidatePath('/posts')
}
```

### Что запрещено в Server Actions

* Проверка прав только на уровне страницы — Action вызывается напрямую, независимо от UI.
* Возврат полных объектов из БД — только нужные поля.
* Throw непойманных ошибок наружу — логируй серверно, возвращай `{ error: string }`.
* Доверять любым данным из `formData` без валидации Zod.

---

## 4. Переменные окружения

```
# Доступны только на сервере (безопасно)
DATABASE_URL=
AUTH_SECRET=
STRIPE_SECRET_KEY=

# Видны клиенту в JS-бандле (только публичные данные)
NEXT_PUBLIC_APP_URL=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
```

Правила:

* Секреты (ключи API, пароли БД, токены) — никогда с префиксом `NEXT_PUBLIC_`.
* `process.env.SECRET` читать только в DAL, Server Actions и Route Handlers — не в компонентах.
* В ответах, логах, комментариях и git-диффах — никогда не показывай значения из `.env`.
* `.env.local` в `.gitignore`. Коммитить можно только `.env.example` с заменёнными значениями.

---

## 5. Cookies и сессии

```typescript
// lib/session.ts
import 'server-only'
import { cookies } from 'next/headers'

export async function setSessionCookie(token: string) {
  const cookieStore = await cookies()
  cookieStore.set('session', token, {
    httpOnly: true,   // недоступен через document.cookie (защита от XSS)
    secure: true,     // только по HTTPS
    sameSite: 'lax',  // защита от CSRF; 'strict' — если нет внешних переходов
    path: '/',
    maxAge: 60 * 60 * 24, // 24 часа
  })
}
```

Запрещено:

* Хранить session token в `localStorage` или `sessionStorage` — читается любым JS на странице.
* Использовать `sameSite: 'none'` без чёткого обоснования.
* Сессии без `maxAge` — они не истекают при закрытии браузера только на уровне сервера.

---

## 6. HTTP Security Headers

Добавляй через `next.config.ts`. Для CSP с nonce — через middleware.

### Статические заголовки (next.config.ts)

```typescript
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          { key: 'X-Content-Type-Options', value: 'nosniff' },
          { key: 'X-Frame-Options', value: 'DENY' },
          { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
          { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
          {
            key: 'Strict-Transport-Security',
            value: 'max-age=31536000; includeSubDomains',
          },
        ],
      },
    ]
  },
}

export default nextConfig
```

### CSP с nonce (middleware.ts)

Используй когда нужны inline-скрипты (аналитика, GTM). Nonce генерируется per-request:

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server'

export function middleware(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const isDev = process.env.NODE_ENV === 'development'

  const csp = [
    "default-src 'self'",
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${isDev ? " 'unsafe-eval'" : ''}`,
    `style-src 'self' 'nonce-${nonce}'`,
    "img-src 'self' blob: data:",
    "font-src 'self'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
    "upgrade-insecure-requests",
  ].join('; ')

  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)
  requestHeaders.set('Content-Security-Policy', csp)

  const response = NextResponse.next({ request: { headers: requestHeaders } })
  response.headers.set('Content-Security-Policy', csp)

  return response
}

export const config = {
  matcher: [
    {
      source: '/((?!_next/static|_next/image|favicon.ico).*)',
      missing: [
        { type: 'header', key: 'next-router-prefetch' },
        { type: 'header', key: 'purpose', value: 'prefetch' },
      ],
    },
  ],
}
```

Прочитать nonce в Server Component:

```typescript
import { headers } from 'next/headers'

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const nonce = (await headers()).get('x-nonce') ?? ''
  // передавай nonce в <Script nonce={nonce} />
}
```


| Заголовок          | Значение                           | Защита от                                                               |
| --------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| `X-Content-Type-Options`    | `nosniff`                                  | MIME-sniffing атак                                                          |
| `X-Frame-Options`           | `DENY`                                     | Clickjacking                                                                    |
| `Referrer-Policy`           | `strict-origin-when-cross-origin`          | Утечки URL в заголовке Referer                                  |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains`      | Downgrade-атак (HTTPS-only)                                                 |
| `Permissions-Policy`        | `camera=(), microphone=(), geolocation=()` | Несанкционированного доступа к API браузера |
| `Content-Security-Policy`   | nonce + strict-dynamic                     | XSS                                                                             |

---

## 7. Middleware: только оптимизации, не безопасность

Middleware подходит для:

* Редиректов неаутентифицированных пользователей (UX, не безопасность).
* Установки заголовков безопасности.
* Rewrite и локализации.

Middleware не подходит для:

* Единственной проверки авторизации — после CVE-2025-29927 это недопустимый паттерн.
* Прямых обращений к БД (Prisma и подобные) в Edge Runtime.
* Бизнес-логики и тяжёлых вычислений.

Если middleware делает редирект — DAL всё равно проверяет права при доступе к данным.

---

## 8. Route Handlers

```typescript
// app/api/posts/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { verifySession } from '@/lib/dal'
import { z } from 'zod'

const QuerySchema = z.object({
  page: z.coerce.number().int().positive().default(1),
})

export async function GET(request: NextRequest) {
  // Аутентификация даже в GET если данные не публичные
  const session = await verifySession()

  const { searchParams } = request.nextUrl
  const parsed = QuerySchema.safeParse({ page: searchParams.get('page') })
  if (!parsed.success) {
    return NextResponse.json({ error: 'Invalid params' }, { status: 400 })
  }

  // ... логика
}
```

Правила:

* Route Handler — публичный эндпоинт. Проверяй auth даже если вызывается только из твоего фронтенда.
* Параметры из `searchParams` и `params` — всегда валидируй через Zod.
* Не логируй `request.body` целиком — может содержать пароли и токены.
* Возвращай одинаковые ошибки для несуществующих и недоступных ресурсов (`404`, не `403`) когда нужно скрыть факт существования.

---

## 9. Чек-лист безопасности

Перед коммитом любой фичи с данными проверь:

**Server Actions:**

* Проверка аутентификации (`verifySession()`) — первой строкой.
* Проверка авторизации на конкретный ресурс (не только "залогинен ли пользователь").
* Все входные данные валидированы через Zod до использования.

**Data Access Layer:**

* Файл начинается с `import 'server-only'`.
* Возвращается DTO, а не сырой ORM-объект.
* `verifySession` обёрнут в `cache()`.

**Переменные окружения:**

* Секреты без префикса `NEXT_PUBLIC_`.
* `.env.local` в `.gitignore`.

**Cookies:**

* `httpOnly: true`, `secure: true`, `sameSite: 'lax'` или `'strict'`.
* Токены не в `localStorage`.

**Middleware:**

* Не является единственной точкой проверки доступа.
* Нет обращений к БД в Edge Runtime.

**Версия Next.js:**

* Не ниже 15.2.3 (патч CVE-2025-29927).

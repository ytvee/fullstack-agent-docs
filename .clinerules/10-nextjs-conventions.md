# 10 - Next.js Conventions (App Router)

> **Область применения:** Все файлы и компоненты в проекте Next.js
>
> **Версия Next.js:** 15+ (с React 19)
>
> **Взаимодействие:** Дополняет `00-context.md`. При конфликте этот файл имеет приоритет в деталях Next.js.

## 1. Роутинг и структура `app/`

Структура проекта и разделение `features/` описаны в `00-context.md`. Здесь — только специфика роутинга.

Специальные файловые сегменты:


| Файл        | Назначение                                                     |
| --------------- | ------------------------------------------------------------------------ |
| `layout.tsx`    | Персистентный враппер сегмента               |
| `page.tsx`      | Публичный роут                                              |
| `loading.tsx`   | Suspense fallback на уровне сегмента                     |
| `error.tsx`     | Error boundary (обязательно`'use client'`)                    |
| `not-found.tsx` | 404 для сегмента                                              |
| `route.ts`      | Route Handler (REST / вебхуки)                                    |
| `template.tsx`  | Как layout, но пересоздаётся при навигации |

Соглашения:

* Route groups: `(kebab-case)` — не влияют на URL
* Динамические сегменты: `[slug]`, `[...catchAll]`, `[[...optional]]`
* Приватные папки (не становятся роутами): `_components/`, `_lib/`

### `params` — это Promise в Next.js 15

Все динамические параметры необходимо awaiting в Next.js 15:

```typescript
// app/blog/[slug]/page.tsx
type Props = {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ q?: string }>
}

export default async function BlogPost({ params, searchParams }: Props) {
  const { slug } = await params
  const { q } = await searchParams
  // ...
}

// В Client Components используй React.use()
import { use } from 'react'

export default function ClientPage(props: Props) {
  const { slug } = use(props.params)
  // ...
}
```

## 2. Server vs Client Components — нюансы

Основные правила в `00-context.md`. Здесь — только специфика Next.js.

### Запрещено в Next.js 15

`ssr: false` нельзя использовать с `next/dynamic` внутри Server Components:

```typescript
// Запрещено: ssr: false в Server Component
const Chart = dynamic(() => import('./Chart'), { ssr: false }) // ошибка сборки

// Правильно: обернуть в Client Component-враппер
// components/ChartWrapper.tsx
'use client'
import dynamic from 'next/dynamic'

const Chart = dynamic(() => import('./Chart'), {
  ssr: false,
  loading: () => <Skeleton />,
})

export { Chart }
```

### Композиция Server + Client

```typescript
// Server Component передаёт данные через props или children
export default async function Page() {
  const user = await getUser()
  return (
    <ClientShell>          // Client Component
      <UserCard user={user} />   // Server Component как children
    </ClientShell>
  )
}
```

## 3. Навигация

### `<Link>` (предпочтительно для внутренних переходов)

```typescript
import Link from 'next/link'

// Статический роут
<Link href="/dashboard">Dashboard</Link>

// Внешняя ссылка
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  External
</a>
```

### `useRouter` (только в Client Components)

```typescript
'use client'
import { useRouter } from 'next/navigation'

const router = useRouter()
router.push('/dashboard')    // навигация
router.replace('/login')     // без записи в history
router.refresh()             // обновляет Server Component данные
```

### `next/form` (новое в Next.js 15)

```typescript
import Form from 'next/form'

// Расширяет <form>: client-side navigation, prefetch action URL
<Form action="/search">
  <input name="q" />
  <button type="submit">Search</button>
</Form>
```

## 4. Data Fetching

### Прямой доступ к данным в Server Components

```typescript
// app/products/page.tsx
import { db } from '@/lib/db'

export default async function ProductsPage() {
  const products = await db.product.findMany()
  return <ProductList products={products} />
}
```

### `generateStaticParams` для статических динамических роутов

```typescript
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await db.post.findMany({ select: { slug: true } })
  return posts.map((post) => ({ slug: post.slug }))
}
```

### Стриминг с Suspense

```typescript
// app/dashboard/page.tsx
import { Suspense } from 'react'
import { UserCard, UserCardSkeleton } from '@/features/user/components/UserCard'
import { OrderList, OrderListSkeleton } from '@/features/orders/components/OrderList'

export default function Dashboard() {
  return (
    <>
      <Suspense fallback={<UserCardSkeleton />}>
        <UserCard />
      </Suspense>
      <Suspense fallback={<OrderListSkeleton />}>
        <OrderList />
      </Suspense>
    </>
  )
}
```

### Server Actions и клиентская обработка

Шаблон Actions описан в `00-context.md`. Здесь — только `useActionState`:

```typescript
// features/newsletter/actions.ts
'use server'
import { z } from 'zod'
import { revalidatePath } from 'next/cache'

const Schema = z.object({ email: z.string().email() })

export async function subscribeEmail(
  prevState: { error?: string; success?: boolean } | null,
  formData: FormData,
) {
  const parsed = Schema.safeParse({ email: formData.get('email') })
  if (!parsed.success) return { error: 'Некорректный email' }

  await db.subscriber.create({ data: parsed.data })
  revalidatePath('/newsletter')
  return { success: true }
}
```

```typescript
// features/newsletter/components/SubscribeForm.tsx
'use client'
import { useActionState } from 'react'
import { subscribeEmail } from '../actions'

export function SubscribeForm() {
  const [state, action, isPending] = useActionState(subscribeEmail, null)

  return (
    <form action={action}>
      <input name="email" type="email" disabled={isPending} />
      {state?.error && <p>{state.error}</p>}
      <button type="submit" disabled={isPending}>
        {isPending ? 'Отправка...' : 'Подписаться'}
      </button>
    </form>
  )
}
```

## 5. Производительность

### `next/image`

```typescript
import Image from 'next/image'

// Всегда указывай width + height или fill + sizes
<Image src="/hero.jpg" alt="Hero" width={1200} height={600} />

// LCP-изображение — priority обязателен
<Image src="/hero.jpg" alt="Hero" width={1200} height={600} priority />

// Внешние источники — настрой в next.config.ts
<Image src="https://cdn.example.com/photo.jpg" alt="Photo" fill sizes="100vw" />
```

### `next/font`

```typescript
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',   // обязателен
})
```

### Динамический импорт тяжёлых Client Components

```typescript
// Только в Client Component — враппере
'use client'
import dynamic from 'next/dynamic'

const HeavyChart = dynamic(() => import('./HeavyChart'), {
  loading: () => <Skeleton />,
  // ssr: false — только внутри Client Component
})
```

## 6. Partial Prerendering (PPR)

PPR — экспериментальная функция Next.js 15. Не рекомендована для production.

Включение в `next.config.ts`:

```typescript
const nextConfig: NextConfig = {
  experimental: {
    ppr: 'incremental',  // не 'true' — только incremental в stable 15.x
  },
}
```

Включение на конкретном роуте:

```typescript
// app/dashboard/page.tsx
import { Suspense } from 'react'
import { StaticContent } from '@/features/dashboard/components/StaticContent'
import { DynamicFeed } from '@/features/dashboard/components/DynamicFeed'

export const experimental_ppr = true  // opt-in для этого сегмента

export default function Dashboard() {
  return (
    <>
      <StaticContent />
      <Suspense fallback={<Skeleton />}>
        <DynamicFeed />   // стримится динамически
      </Suspense>
    </>
  )
}
```

`experimental_ppr = true` распространяется на все дочерние layout и page. Не нужно добавлять в каждый файл.

## 7. View Transitions

Экспериментальная функция. Включается в `next.config.ts`:

```typescript
const nextConfig: NextConfig = {
  experimental: {
    viewTransition: true,
  },
}
```

`<ViewTransition>` импортируется из React напрямую — никаких сторонних пакетов не нужно:

```typescript
import { ViewTransition } from 'react'
import Image from 'next/image'
import Link from 'next/link'

function PhotoGrid({ photos }: { photos: Photo[] }) {
  return (
    <div>
      {photos.map((photo) => (
        <Link key={photo.id} href={`/photo/${photo.id}`}>
          <ViewTransition name={`photo-${photo.id}`}>
            <Image src={photo.src} alt={photo.title} />
          </ViewTransition>
        </Link>
      ))}
    </div>
  )
}
```

## 8. Middleware

По умолчанию — Edge Runtime. Node.js runtime стал stable в Next.js 15.5:

```typescript
// middleware.ts
import { NextRequest, NextResponse } from 'next/server'

export function middleware(request: NextRequest) {
  // логика
  return NextResponse.next()
}

export const config = {
  matcher: ['/dashboard/:path*', '/admin/:path*'],
  runtime: 'nodejs',  // stable с Next.js 15.5; без этой строки — Edge Runtime
}
```

Правила для Middleware:

* Никакой бизнес-логики и тяжёлых вычислений
* Никаких прямых обращений к БД (через Prisma и подобное) в Edge Runtime
* Используй только для проверки auth-токена, редиректов, rewrite

## 9. Граничные состояния

### `error.tsx` — обязательно Client Component

```typescript
'use client'
import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // логируй серверно, не показывай стектрейс пользователю
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Что-то пошло не так</h2>
      <button onClick={reset}>Попробовать снова</button>
    </div>
  )
}
```

### `not-found.tsx`

```typescript
// В Server Component вызывай notFound() из next/navigation
import { notFound } from 'next/navigation'

export default async function ProductPage({ params }: Props) {
  const { id } = await params
  const product = await getProduct(id)
  if (!product) notFound()
  // ...
}
```

## 10. Конфигурация `next.config.ts`

```typescript
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      { protocol: 'https', hostname: 'cdn.example.com' },
    ],
  },
  experimental: {
    ppr: 'incremental',       // PPR — только incremental в stable 15.x
    viewTransition: true,     // View Transitions API (experimental)
    // dynamicIO: true        // только в next@canary, не в stable
  },
  eslint: { ignoreDuringBuilds: false },
  typescript: { ignoreBuildErrors: false },
  output: 'standalone',       // для Docker
}

export default nextConfig
```

## 11. Чек-лист перед коммитом

* Нет лишних `'use client'`
* `params` и `searchParams` — awaited (они Promise в Next.js 15)
* `ssr: false` в `next/dynamic` — только внутри Client Component
* Все изображения через `next/image` с обязательными размерами
* Server Actions: валидация Zod + `revalidatePath` / `revalidateTag`
* Роуты с асинхронными данными имеют `loading.tsx` или `<Suspense>`
* `generateStaticParams` реализован для статических динамических роутов
* `tsc --noEmit` и `next lint` проходят без ошибок

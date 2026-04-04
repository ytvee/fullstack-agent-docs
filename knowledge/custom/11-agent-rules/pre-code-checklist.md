---
category: agent-rules
topic: pre-code-checklist
status: draft
---

## Проблема / Контекст

AI-агент, пишущий код без предварительного планирования, делает одни и те же ошибки: забывает проверить авторизацию, создаёт лишние DB запросы, смешивает Server и Client Components, не обрабатывает error states. Чеклист — структурированный процесс, который нужно пройти ДО написания первой строки кода. Это не бюрократия, а профилактика: дешевле подумать 2 минуты, чем переписывать готовый код.

## Решение

### Чеклист для выполнения перед написанием кода

---

## ✅ ЧЕКЛИСТ: Выполнить ДО написания кода

---

- [ ] ESLint запущен без ошибок: npm run lint:strict
- [ ] Нет eslint-disable без комментария с причиной
- [ ] Prettier применён: npm run format

### 1. Авторизация и доступ

**Вопросы для проверки:**
- Требует ли эта функциональность аутентификацию?
- Какие роли имеют доступ к данным/действию?
- Нужна ли проверка владения ресурсом (user can only edit their own posts)?

**Действия:**

```typescript
// Если да — определить где именно добавить проверку:

// В Server Component:
import { auth } from "@/lib/auth";
import { redirect } from "next/navigation";

const session = await auth();
if (!session?.user) redirect("/auth/login");
if (session.user.role !== "admin") redirect("/dashboard");

// В Server Action — всегда проверяй в самом начале:
export async function deleteProduct(productId: string) {
  const session = await auth();
  if (!session?.user) throw new Error("Unauthorized");

  // Проверить владение ресурсом:
  const product = await db.query.products.findFirst({
    where: and(eq(products.id, productId), eq(products.userId, session.user.id)),
  });
  if (!product) throw new Error("Not found or forbidden");
  // ...
}

// В Route Handler:
export async function DELETE(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const session = await auth();
  if (!session?.user) return Response.json({ error: "Unauthorized" }, { status: 401 });
  // ...
}
```

**Вывод до написания кода:** "Эта функция требует: [ ] аутентификации, [ ] роли admin, [ ] проверки владения"

---

### 2. Схема БД и отношения

**Вопросы для проверки:**
- Какие таблицы затрагивает эта функция?
- Какие отношения (relations) нужно включить через `with`?
- Нужны ли новые поля или таблицы? Если да — создай миграцию ПЕРВОЙ.
- Какие индексы нужны для запросов фильтрации?

**Действия:**

```typescript
// Проверить схему Drizzle ПЕРЕД написанием запросов:
// lib/db/schema/

// Если нужно новое поле — сначала обновить schema:
// lib/db/schema/products.ts
export const products = pgTable("products", {
  id: uuid("id").primaryKey().defaultRandom(),
  // ... существующие поля
  viewCount: integer("view_count").notNull().default(0), // НОВОЕ ПОЛЕ
}, (table) => ({
  slugIdx: index("products_slug_idx").on(table.slug),     // НОВЫЙ ИНДЕКС
}));

// Затем запустить миграцию:
// pnpm db:generate && pnpm db:migrate
```

**Вывод до написания кода:** "Нужны таблицы: [X], новые поля: [Y], миграция: [нужна/не нужна]"

---

### 3. Zod схемы валидации — определить ПЕРВЫМИ

Zod схема — это контракт. Определи его до реализации, чтобы TypeScript типы вытекали из схемы.

```typescript
// СНАЧАЛА — определить схему:
import { z } from "zod";

export const createProductSchema = z.object({
  name: z.string().min(1, "Name required").max(200),
  description: z.string().min(10).max(5000),
  price: z.number().int().positive().max(10_000_000), // в копейках
  categoryId: z.string().uuid(),
  imageUrls: z.array(z.string().url()).min(1).max(10),
  tags: z.array(z.string()).max(20).optional().default([]),
  isPublished: z.boolean().optional().default(false),
});

// Тип ВЫТЕКАЕТ из схемы — не дублируй
export type CreateProductInput = z.infer<typeof createProductSchema>;

// ПОТОМ — реализация с этой схемой
```

**Вывод до написания кода:** "Zod схема определена: [имя]. Покрывает все входные данные: [да/нет]"

---

### 4. Server Components vs Client Components

Задай себе вопросы по дереву решений:

```
Нужны ли интерактивность, хуки, браузерные API?
├── НЕТ → Server Component (по умолчанию)
│   ├── Прямой доступ к БД через Drizzle
│   ├── Без лишнего JavaScript в бандле
│   └── Async/await без useEffect
└── ДА → Client Component ("use client")
    ├── Минимально возможный — только то что нужно
    ├── Обёртывает только интерактивную часть
    └── Данные получает через props от Server Component
```

```typescript
// ПЛАНИРОВАНИЕ: нарисуй дерево компонентов до написания

// ProductPage (Server) — получает данные из БД
//   ├── ProductGallery (Client) — carousel, zoom
//   ├── ProductInfo (Server) — статичная информация
//   └── AddToCartButton (Client) — click handler, optimistic update

// Это означает: данные передаём в Client как props,
// а не делаем клиентский fetch
```

**Вывод до написания кода:** "Компоненты: [список SC/CC с обоснованием]"

---

### 5. Кэш-инвалидация и revalidation

**Вопросы для проверки:**
- Что должно обновиться после этого действия?
- Какие пути/теги нужно инвалидировать?
- Нужен ли `revalidatePath` или `revalidateTag`?
- Есть ли ISR (статические страницы), которые нужно перегенерировать?

```typescript
// Заранее определить все пути для инвалидации:
export async function createProduct(data: CreateProductInput) {
  // ... создание продукта

  // ИНВАЛИДАЦИЯ — определена заранее:
  revalidatePath("/products");                    // список продуктов
  revalidatePath("/admin/products");              // админская страница
  revalidatePath(`/categories/${data.categoryId}`); // страница категории
  revalidatePath("/sitemap.xml");                 // sitemap обновляется
  // revalidateTag("products") — если используешь unstable_cache с тегами
}
```

**Вывод до написания кода:** "Инвалидировать: [список путей]"

---

### 6. Существующие паттерны в кодовой базе

**Перед написанием нового кода:**

```bash
# Ищем похожие реализации:
# - Аналогичные Server Actions
# - Похожие формы (RHF + Zod + Server Action)
# - Аналогичные страницы с data fetching

# Цель: не изобретать велосипед, следовать устоявшимся паттернам
# Примеры для поиска:
grep -r "revalidatePath" app/actions/   # как другие actions инвалидируют
grep -r "zodResolver" components/       # как другие формы устроены
```

**Вывод до написания кода:** "Аналогичный паттерн в файле: [путь]. Следую ему / отклонение потому что: [причина]"

---

### 7. TypeScript типы — определить до реализации

```typescript
// Определяем типы ДО реализации функций:

// Тип для ответа Server Action:
type ActionResult<T = void> =
  | { success: true; data: T }
  | { success: false; error: string; fieldErrors?: Record<string, string[]> };

// Тип для пропсов компонента:
interface ProductCardProps {
  product: {
    id: string;
    name: string;
    price: number;
    imageUrl: string | null;
    category: { name: string; slug: string };
  };
  showAddToCart?: boolean;
}

// Тип для данных из БД (вытекает из Drizzle):
type ProductWithCategory = typeof products.$inferSelect & {
  category: typeof categories.$inferSelect;
};
```

**Вывод до написания кода:** "Ключевые типы определены: [список]. Нет `any` типов в плане"

---

### 8. Error States

**Для каждой функции определить все возможные ошибки:**

```typescript
// Матрица error states для Server Action:

// 1. Аутентификация: пользователь не авторизован
// 2. Авторизация: нет прав доступа
// 3. Валидация: некорректные входные данные
// 4. Not Found: ресурс не существует
// 5. Конфликт: дублирующийся slug/email
// 6. Rate Limit: слишком много запросов
// 7. External Service: платёжный шлюз недоступен
// 8. Database: ошибка подключения к БД

// Для каждого — определить:
// - Что показать пользователю?
// - Логировать ли в Sentry/console?
// - Какой HTTP status код?
```

**Вывод до написания кода:** "Error states: [список]. Каждый обработан в реализации"

---

### 9. Loading States

```typescript
// Определить loading states ДО реализации UI:

// Для страниц: нужен ли loading.tsx?
// app/products/loading.tsx — скелетон для всей страницы

// Для форм: disabled состояние кнопок при submit
// const [isPending, startTransition] = useTransition();
// ИЛИ используй useFormStatus() в submit button

// Для мутаций: оптимистичное обновление или spinner?
// Оптимистичное — когда вероятность успеха высока
// Spinner — когда нужна обратная связь (загрузка файла, платёж)

// Для данных: Suspense boundary или skeleton?
// <Suspense fallback={<ProductCardSkeleton />}>
//   <ProductCard id={id} />
// </Suspense>
```

**Вывод до написания кода:** "Loading states: [список компонентов со стратегией]"

---

### 10. Безопасность: кто имеет доступ к данным?

```typescript
// Для КАЖДОГО поля, возвращаемого пользователю:
// "Должен ли пользователь X видеть поле Y?"

// Пример: GET /api/users/[id]
// - id: ДА (публичное)
// - name: ДА (публичное)
// - email: ТОЛЬКО свой профиль или admin
// - passwordHash: НИКОГДА
// - stripeCustomerId: НИКОГДА в API
// - isAdmin: ТОЛЬКО для admin endpoint

// Drizzle: явно выбирай только нужные поля:
const user = await db.query.users.findFirst({
  where: eq(users.id, userId),
  columns: {
    id: true,
    name: true,
    avatarUrl: true,
    // НЕ включаем: passwordHash, email (если публичный профиль), stripeCustomerId
  },
});

// SQL Injection: используй только параметризованные запросы (Drizzle делает это автоматически)
// XSS: не используй dangerouslySetInnerHTML без sanitize
// CSRF: Server Actions защищены встроенно, Route Handlers — нет (используй Origin check)
```

**Вывод до написания кода:** "Данные безопасны: проверена минимальность экспозиции, input validation, auth checks"

---

## Шаблон итогового плана

Перед написанием кода заполни этот план (можно в комментарии или в голове):

```
ПЛАН РЕАЛИЗАЦИИ: [название функции/страницы]

1. АВТОРИЗАЦИЯ:
   - Требует auth: ДА/НЕТ
   - Роли: [список]
   - Проверка владения: ДА/НЕТ

2. БД:
   - Таблицы: [список]
   - Новые поля/таблицы: [список или "нет"]
   - Нужна миграция: ДА/НЕТ

3. ZOD СХЕМЫ:
   - Схемы определены: [список]
   - Типы выведены из схем: ДА

4. КОМПОНЕНТЫ:
   - SC: [список]
   - CC: [список с обоснованием]

5. КЭШ:
   - revalidatePath: [список]
   - revalidateTag: [список или "нет"]

6. ПАТТЕРН:
   - Следую [имя файла] или создаю новый потому что [причина]

7. ТИПЫ:
   - [список ключевых типов]

8. ERRORS:
   - [список с обработкой]

9. LOADING:
   - [стратегия]

10. БЕЗОПАСНОСТЬ:
    - Поля API: минимальны ✓
    - Auth checks: есть ✓
    - Input validation: Zod ✓
```

## Связанные документы

- `knowledge/custom/11-agent-rules/decision-trees.md` — деревья решений для архитектурных выборов
- `knowledge/custom/11-agent-rules/file-templates.md` — готовые шаблоны кода
- `knowledge/custom/11-agent-rules/review-criteria.md` — критерии проверки после написания
- `knowledge/custom/11-agent-rules/naming-conventions.md` — правила именования

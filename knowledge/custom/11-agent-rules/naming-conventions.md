---
category: agent-rules
topic: naming-conventions
status: draft
---

## Проблема / Контекст

Несогласованное именование в большом проекте — источник когнитивной нагрузки и ошибок. Когда файл называется `UserProfile.tsx`, а рядом `user-settings.tsx` — непонятно где искать. Когда Server Action называется `handleSubmit` вместо `updateProfile` — непонятно что она делает. Соглашения ниже применяются ко всей кодовой базе и должны соблюдаться без исключений.

## Решение

### 1. Файлы и директории: kebab-case

Все файлы и папки в kebab-case, кроме специальных файлов Next.js.

```
app/
├── (marketing)/            # route groups в kebab-case
│   ├── about/
│   │   └── page.tsx        # специальный файл Next.js — оставляем как есть
│   └── pricing/
│       └── page.tsx
├── dashboard/
│   ├── page.tsx
│   ├── layout.tsx          # специальный файл Next.js
│   ├── loading.tsx         # специальный файл Next.js
│   ├── error.tsx           # специальный файл Next.js
│   └── not-found.tsx       # специальный файл Next.js
├── products/
│   └── [slug]/
│       ├── page.tsx
│       └── opengraph-image.tsx  # специальный файл Next.js
└── api/
    └── webhooks/
        └── stripe/
            └── route.ts    # специальный файл Next.js

components/
├── ui/                     # shadcn/ui компоненты
│   ├── button.tsx          # kebab-case
│   ├── input.tsx
│   └── dialog.tsx
├── forms/
│   ├── contact-form.tsx    # kebab-case: компонент формы
│   ├── product-form.tsx
│   └── sign-in-form.tsx
├── layouts/
│   ├── main-header.tsx
│   ├── sidebar-nav.tsx
│   └── footer.tsx
└── product-card.tsx        # не ProductCard.tsx!

lib/
├── db/
│   ├── index.ts
│   ├── schema/
│   │   ├── index.ts
│   │   ├── users.ts        # kebab-case
│   │   └── products.ts
│   └── migrations/
├── auth.ts
├── env.ts
└── utils.ts
```

**Специальные файлы Next.js (исключения из kebab-case):**
- `page.tsx`, `layout.tsx`, `error.tsx`, `loading.tsx`, `not-found.tsx`
- `route.ts`, `middleware.ts`
- `opengraph-image.tsx`, `twitter-image.tsx`
- `sitemap.ts`, `robots.ts`
- `favicon.ico`, `apple-icon.png`

---

### 2. Компоненты React: PascalCase для экспортов

```typescript
// components/product-card.tsx — файл kebab-case
// но экспорт PascalCase:

interface ProductCardProps {
  product: ProductWithCategory;
  className?: string;
}

// ХОРОШО: именованный экспорт PascalCase
export function ProductCard({ product, className }: ProductCardProps) {
  return (
    <div className={cn("...", className)}>
      {/* ... */}
    </div>
  );
}

// Для Next.js page/layout — default export с PascalCase именем функции:
// app/products/page.tsx
export default function ProductsPage() { ... }
export default function ProductLayout({ children }: ...) { ... }

// ПЛОХО:
export function productCard() { ... }    // camelCase для компонента
export default function page() { ... }  // lowercase для page
```

---

### 3. Функции: camelCase

```typescript
// Обычные функции — camelCase:
export function formatPrice(priceInCents: number): string {
  return (priceInCents / 100).toLocaleString("ru-RU", {
    style: "currency",
    currency: "RUB",
  });
}

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

// Хуки — camelCase с префиксом "use":
export function useProductFilters() { ... }
export function useDebounce<T>(value: T, delay: number): T { ... }
export function useLocalStorage<T>(key: string, initialValue: T): [T, (v: T) => void] { ... }

// Асинхронные утилиты — camelCase:
export async function sendEmail(to: string, template: EmailTemplate): Promise<void> { ... }
export async function uploadFile(file: File): Promise<string> { ... }
```

---

### 4. Server Actions: глагол + существительное

Формат: `[verb][Noun]` — что делаем + с чем.

```typescript
// app/actions/products.ts
"use server";

// ХОРОШО: глагол + существительное
export async function createProduct(data: CreateProductInput) { ... }
export async function updateProduct(id: string, data: UpdateProductInput) { ... }
export async function deleteProduct(id: string) { ... }
export async function publishProduct(id: string) { ... }
export async function archiveProduct(id: string) { ... }

// app/actions/users.ts
export async function updateProfile(data: UpdateProfileInput) { ... }
export async function changePassword(data: ChangePasswordInput) { ... }
export async function uploadAvatar(formData: FormData) { ... }
export async function deleteAccount(confirmation: string) { ... }

// app/actions/orders.ts
export async function createOrder(items: CartItem[]) { ... }
export async function cancelOrder(orderId: string) { ... }
export async function refundOrder(orderId: string, amount: number) { ... }

// ПЛОХО:
export async function handleProduct() { ... }     // что делает?
export async function productUpdate() { ... }     // существительное+глагол
export async function submitProductForm() { ... } // "form" — это UI, не бизнес-логика
```

---

### 5. Константы: SCREAMING_SNAKE_CASE

```typescript
// lib/constants.ts

// Числовые константы
export const MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024; // 5MB
export const MAX_PRODUCTS_PER_PAGE = 24;
export const SESSION_EXPIRY_SECONDS = 60 * 60 * 24 * 30; // 30 days
export const OTP_EXPIRY_MINUTES = 10;

// Строковые константы
export const DEFAULT_LOCALE = "ru";
export const SUPPORTED_LOCALES = ["ru", "en"] as const;
export const CURRENCY_CODE = "RUB";

// Enum-подобные константы
export const ORDER_STATUSES = {
  PENDING: "pending",
  PAID: "paid",
  SHIPPED: "shipped",
  DELIVERED: "delivered",
  CANCELLED: "cancelled",
} as const;

export type OrderStatus = (typeof ORDER_STATUSES)[keyof typeof ORDER_STATUSES];

// ПЛОХО:
export const maxFileSize = 5 * 1024 * 1024;  // camelCase для константы
export const MaxFileSizeMB = 5;               // PascalCase для константы
```

---

### 6. БД: snake_case для колонок, camelCase в Drizzle schema

```typescript
// lib/db/schema/products.ts
import { pgTable, uuid, varchar, integer, boolean, timestamp, text, index } from "drizzle-orm/pg-core";

export const products = pgTable(
  "products",            // snake_case: название таблицы
  {
    id: uuid("id").primaryKey().defaultRandom(),
    name: varchar("name", { length: 200 }).notNull(),
    slug: varchar("slug", { length: 200 }).notNull().unique(),
    description: text("description"),

    // snake_case в БД ("price_in_cents"), camelCase в Drizzle (priceInCents)
    priceInCents: integer("price_in_cents").notNull(),
    stockCount: integer("stock_count").notNull().default(0),
    isPublished: boolean("is_published").notNull().default(false),
    isDeleted: boolean("is_deleted").notNull().default(false),

    // Внешние ключи: snake_case с суффиксом _id
    categoryId: uuid("category_id").references(() => categories.id),
    createdById: uuid("created_by_id").references(() => users.id),

    // Timestamps: всегда createdAt / updatedAt
    createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
    updatedAt: timestamp("updated_at", { withTimezone: true }).notNull().defaultNow(),
  },
  (table) => ({
    // Индексы: [table]_[column]_idx
    slugIdx: index("products_slug_idx").on(table.slug),
    categoryIdx: index("products_category_id_idx").on(table.categoryId),
    publishedIdx: index("products_is_published_idx").on(table.isPublished),
  })
);

// Типы выводим из схемы Drizzle:
export type Product = typeof products.$inferSelect;
export type NewProduct = typeof products.$inferInsert;
```

---

### 7. Zod схемы: camelCase с суффиксом Schema

```typescript
// lib/validations/product.ts
import { z } from "zod";

// Суффикс Schema — обязательно:
export const createProductSchema = z.object({
  name: z.string().min(1).max(200),
  priceInCents: z.number().int().positive(),
  categoryId: z.string().uuid(),
});

export const updateProductSchema = createProductSchema.partial().extend({
  id: z.string().uuid(),
});

export const productFiltersSchema = z.object({
  categorySlug: z.string().optional(),
  minPrice: z.number().optional(),
  maxPrice: z.number().optional(),
  sortBy: z.enum(["price_asc", "price_desc", "newest", "popular"]).optional(),
  page: z.number().int().min(1).optional().default(1),
});

// Типы от Schema:
export type CreateProductInput = z.infer<typeof createProductSchema>;
export type UpdateProductInput = z.infer<typeof updateProductSchema>;
export type ProductFilters = z.infer<typeof productFiltersSchema>;

// ПЛОХО:
export const ProductSchema = z.object({ ... });  // PascalCase для Zod схемы
export const createProduct = z.object({ ... });  // без суффикса Schema
```

---

### 8. Route Handlers: всегда route.ts, никогда api.ts

```
app/api/
├── auth/
│   └── [...nextauth]/
│       └── route.ts        ✅
├── products/
│   ├── route.ts            ✅ (GET /api/products, POST /api/products)
│   └── [id]/
│       └── route.ts        ✅ (GET, PATCH, DELETE /api/products/:id)
├── webhooks/
│   └── stripe/
│       └── route.ts        ✅
└── health/
    └── route.ts            ✅

# ПЛОХО:
app/api/products/api.ts     ❌
app/api/products/index.ts   ❌
app/api/getProducts.ts      ❌
```

---

### 9. TypeScript Types и Interfaces: PascalCase с описательными именами

```typescript
// types/index.ts или domain-specific:

// Interfaces для объектов — I-prefix НЕ используем (не Java):
interface User {
  id: string;
  email: string;
  role: UserRole;
}

// Type aliases для unions и primitives:
type UserRole = "admin" | "user" | "moderator";
type ProductStatus = "draft" | "published" | "archived";
type Nullable<T> = T | null;
type Optional<T> = T | undefined;

// Generic types — одна буква или описательное имя:
type ApiResponse<TData> = {
  data: TData;
  error: null;
} | {
  data: null;
  error: string;
};

// Props types — суффикс Props:
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "destructive";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
}

// Page props — суффикс PageProps или Props:
interface ProductPageProps {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}
```

---

### 10. Zustand Store: camelCase для actions, PascalCase для Store type

```typescript
// stores/cart-store.ts — файл kebab-case

interface CartItem {
  productId: string;
  quantity: number;
  priceInCents: number;
}

interface CartStore {
  // State — существительные
  items: CartItem[];
  isOpen: boolean;

  // Actions — глаголы camelCase
  addItem: (item: CartItem) => void;
  removeItem: (productId: string) => void;
  updateQuantity: (productId: string, quantity: number) => void;
  clearCart: () => void;
  openCart: () => void;
  closeCart: () => void;
}

export const useCartStore = create<CartStore>()(
  persist(
    (set, get) => ({
      items: [],
      isOpen: false,

      addItem: (item) => set((state) => ({
        items: [...state.items, item],
      })),
      // ...
    }),
    { name: "cart-storage" }
  )
);
```

---

### Сводная таблица

| Что                              | Формат                    | Пример                          |
|----------------------------------|---------------------------|---------------------------------|
| Файлы компонентов                | kebab-case.tsx            | `product-card.tsx`              |
| Файлы утилит                     | kebab-case.ts             | `format-price.ts`               |
| Специальные файлы Next.js        | lowercase.tsx/ts          | `page.tsx`, `route.ts`          |
| Компоненты React (экспорт)       | PascalCase                | `ProductCard`                   |
| Хуки                             | camelCase с `use`         | `useProductFilters`             |
| Server Actions                   | camelCase: глагол+объект  | `createProduct`, `updateProfile`|
| Обычные функции                  | camelCase                 | `formatPrice`, `slugify`        |
| Константы                        | SCREAMING_SNAKE_CASE      | `MAX_FILE_SIZE_BYTES`           |
| Zod схемы                        | camelCase + Schema        | `createProductSchema`           |
| TypeScript типы/interfaces       | PascalCase                | `ProductWithCategory`           |
| DB колонки (SQL)                 | snake_case                | `price_in_cents`                |
| DB поля в Drizzle                | camelCase                 | `priceInCents`                  |
| DB таблицы                       | snake_case plural         | `products`, `order_items`       |
| Zustand store slice actions      | camelCase глагол          | `addItem`, `clearCart`          |
| CSS классы (Tailwind)            | kebab-case (авто)         | `text-primary`, `flex-col`      |
| Environment variables            | SCREAMING_SNAKE_CASE      | `DATABASE_URL`, `AUTH_SECRET`   |

## Антипаттерн

```typescript
// ПЛОХО: смешение стилей в одном файле
// user-profile.tsx:
export function UserProfile() { ... }      // OK
export const userprofile = () => { ... }   // lowercase
export const USER_COMPONENT = () => { ... } // SCREAMING для компонента

// ПЛОХО: хранить Zod схему вместе с компонентом
// components/product-form.tsx:
const schema = z.object({ ... }); // лучше в lib/validations/product.ts

// ПЛОХО: называть Server Action по UI-действию
export async function handleFormSubmit() { ... } // что именно делает?
// ХОРОШО:
export async function createProduct() { ... }    // бизнес-действие

// ПЛОХО: использовать default exports для компонентов в lib/components
// Именованные экспорты — более явные, лучше поддерживаются IDE
export default function ProductCard() { ... }
// ХОРОШО:
export function ProductCard() { ... }
// Исключение: Next.js page/layout ТРЕБУЕТ default export
```

## Связанные документы

- `knowledge/custom/11-agent-rules/file-templates.md` — шаблоны с правильным именованием
- `knowledge/custom/11-agent-rules/pre-code-checklist.md` — чеклист включает проверку именования
- `knowledge/custom/11-agent-rules/review-criteria.md` — проверка именования в code review

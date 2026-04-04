---
category: antipatterns
topic: hydration-mismatch
status: draft
---

## Проблема / Контекст

Hydration mismatch — ошибка `Error: Hydration failed because the initial UI does not match what was rendered on the server`. Возникает когда HTML от SSR не совпадает с тем, что React рендерит на клиенте при гидрации. Next.js 15 бросает в dev режиме явную ошибку, в проде — молча перерендеривает (но это дорого и ломает UX).

Самые частые причины:
1. **Дата/время** — сервер и клиент в разных часовых поясах
2. **Math.random() / uuid()** — разные значения на сервере и клиенте
3. **Browser-only APIs** — `window`, `localStorage`, `navigator` не существуют на сервере
4. **Условный рендеринг по client state** — флаги которые undefined на сервере
5. **Форматирование чисел/дат** — locale может отличаться
6. **Расширения браузера** — вставляют свои DOM элементы

## Решение

Ключевое правило: **сервер и клиент должны рендерить одинаковый HTML при первом рендере**. Всё браузер-специфичное откладывается через `useEffect`. Для неизбежных расхождений — `suppressHydrationWarning`. Компоненты с browser-only логикой выносятся через `dynamic()` с `ssr: false`.

## Пример кода

### 1. Дата и время — самая частая причина

```typescript
// ПЛОХО: дата рендерится по-разному на сервере (UTC) и клиенте (локальный TZ)
"use client";
export function LastUpdated({ date }: { date: Date }) {
  return <span>Updated: {date.toLocaleString()}</span>;
  // Сервер: "Updated: 4/5/2026, 12:00:00 PM" (UTC)
  // Клиент: "Updated: 4/5/2026, 3:00:00 PM" (UTC+3)
  // → MISMATCH
}

// ПРАВИЛЬНО #1: useEffect для client-only форматирования
"use client";
import { useState, useEffect } from "react";

export function LastUpdated({ date }: { date: Date }) {
  const [formatted, setFormatted] = useState<string | null>(null);

  useEffect(() => {
    // Запускается только на клиенте, после гидрации
    setFormatted(date.toLocaleString());
  }, [date]);

  // Во время SSR и первой гидрации — показываем нейтральный формат
  if (!formatted) {
    return <span>Updated: {date.toISOString().slice(0, 10)}</span>;
  }

  return <span>Updated: {formatted}</span>;
}

// ПРАВИЛЬНО #2: formatDistanceToNow безопасен только на клиенте
"use client";
import { useState, useEffect } from "react";
import { formatDistanceToNow } from "date-fns";

export function RelativeTime({ date }: { date: Date }) {
  const [relative, setRelative] = useState<string>("");

  useEffect(() => {
    setRelative(formatDistanceToNow(date, { addSuffix: true }));

    // Обновляем каждую минуту
    const interval = setInterval(() => {
      setRelative(formatDistanceToNow(date, { addSuffix: true }));
    }, 60_000);

    return () => clearInterval(interval);
  }, [date]);

  // SSR: ISO строка без timezone
  return (
    <time
      dateTime={date.toISOString()}
      title={date.toISOString()}
    >
      {relative || date.toISOString().slice(0, 10)}
    </time>
  );
}

// ПРАВИЛЬНО #3: suppressHydrationWarning для date (когда расхождение приемлемо)
// Используй ТОЛЬКО для листьев дерева, не для контейнеров
export function ServerClock() {
  return (
    <time
      suppressHydrationWarning // ← явно говорим React игнорировать mismatch здесь
      dateTime={new Date().toISOString()}
    >
      {new Date().toLocaleString()} {/* Намеренно разное на сервере/клиенте */}
    </time>
  );
}
```

### 2. Math.random() и UUID

```typescript
// ПЛОХО: каждый рендер генерирует новый ID
"use client";
export function RandomKey({ items }: { items: string[] }) {
  return (
    <ul>
      {items.map((item) => (
        // Новый UUID каждый раз → mismatch
        <li key={Math.random()}>{item}</li>
      ))}
    </ul>
  );
}

// ПЛОХО: ID для label/input пары
"use client";
export function FormField({ label }: { label: string }) {
  const id = Math.random().toString(36); // Разный на сервере и клиенте
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} />
    </div>
  );
}

// ПРАВИЛЬНО: детерминированные ID через useId()
"use client";
import { useId } from "react";

export function FormField({ label }: { label: string }) {
  const id = useId(); // React гарантирует одинаковый ID на сервере и клиенте
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} />
    </div>
  );
}

// ПРАВИЛЬНО: stable keys из данных
export function ItemList({ items }: { items: Array<{ id: string; name: string }> }) {
  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>{item.name}</li> // Детерминированный key из данных
      ))}
    </ul>
  );
}
```

### 3. Browser-only APIs

```typescript
// ПЛОХО: window/localStorage на сервере = ReferenceError
"use client";
export function ThemeProvider({ children }: { children: React.ReactNode }) {
  // window не существует при SSR
  const theme = localStorage.getItem("theme") ?? "light"; // ← ReferenceError on server
  return <div data-theme={theme}>{children}</div>;
}

// ПЛОХО: navigator без проверки
"use client";
export function OnlineStatus() {
  const isOnline = navigator.onLine; // ← undefined on server
  return <span>{isOnline ? "Online" : "Offline"}</span>;
}

// ПРАВИЛЬНО: проверка typeof window
"use client";
import { useState, useEffect } from "react";

export function OnlineStatus() {
  const [isOnline, setIsOnline] = useState(true); // дефолт совпадает с сервером

  useEffect(() => {
    setIsOnline(navigator.onLine);

    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, []);

  return <span>{isOnline ? "Online" : "Offline"}</span>;
}

// ПРАВИЛЬНО: кастомный хук isMounted
"use client";
import { useState, useEffect } from "react";

function useIsMounted(): boolean {
  const [isMounted, setIsMounted] = useState(false);
  useEffect(() => setIsMounted(true), []);
  return isMounted;
}

// Использование для любой browser-only логики
export function BrowserOnlyComponent() {
  const isMounted = useIsMounted();

  if (!isMounted) {
    return <div className="h-10 w-32 animate-pulse bg-muted" />; // skeleton
  }

  return <div>Screen: {window.innerWidth}px</div>;
}
```

### 4. dynamic() с ssr: false

```typescript
// Компоненты которые НЕЛЬЗЯ рендерить на сервере

// src/components/charts/revenue-chart.tsx
"use client";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts"; // Recharts использует window при импорте

interface RevenueChartProps {
  data: Array<{ month: string; revenue: number }>;
}

export function RevenueChart({ data }: RevenueChartProps) {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <AreaChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="month" />
        <YAxis />
        <Tooltip />
        <Area type="monotone" dataKey="revenue" stroke="#8884d8" fill="#8884d8" />
      </AreaChart>
    </ResponsiveContainer>
  );
}

// src/app/dashboard/page.tsx — используем через dynamic
import dynamic from "next/dynamic";
import { Skeleton } from "@/components/ui/skeleton";

// dynamic с ssr:false — компонент никогда не рендерится на сервере
const RevenueChart = dynamic(
  () => import("@/components/charts/revenue-chart").then((m) => m.RevenueChart),
  {
    ssr: false,
    loading: () => <Skeleton className="h-[300px] w-full" />, // placeholder во время загрузки
  }
);

export default async function DashboardPage() {
  const revenueData = await getRevenueData(); // серверный запрос

  return (
    <div>
      <h2>Revenue</h2>
      {/* Рендерится только на клиенте — нет риска hydration mismatch */}
      <RevenueChart data={revenueData} />
    </div>
  );
}

// Другие кандидаты для ssr:false:
// - rich text editors (Quill, TipTap с некоторыми расширениями)
// - карты (Leaflet, Google Maps)
// - WebRTC компоненты
// - компоненты использующие crypto.getRandomValues
const RichTextEditor = dynamic(
  () => import("@/components/editor/rich-text-editor"),
  { ssr: false, loading: () => <div className="h-64 animate-pulse bg-muted rounded" /> }
);
```

### 5. Conditional rendering — скрытый источник mismatch

```typescript
// ПЛОХО: рендер зависит от client-only данных
"use client";
export function UserMenu() {
  // При SSR: session = undefined → рендерим "Login"
  // После гидрации: session = {...} → рендерим "Username"
  // → MISMATCH
  const session = useSession();
  return session.data ? (
    <span>{session.data.user.name}</span>
  ) : (
    <a href="/login">Login</a>
  );
}

// ПРАВИЛЬНО: сервер передаёт начальное состояние через props
// src/components/user-menu-wrapper.tsx — Server Component
import { auth } from "@/lib/auth";
import { UserMenu } from "./user-menu";

export async function UserMenuWrapper() {
  const session = await auth();
  // Передаём в Client Component — сервер и клиент начинают с одного значения
  return <UserMenu initialUser={session?.user ?? null} />;
}

// src/components/user-menu.tsx — Client Component
"use client";
import { useSession } from "next-auth/react";

export function UserMenu({ initialUser }: { initialUser: User | null }) {
  const { data: session } = useSession();
  // initialUser из сервера совпадает с первым рендером на клиенте
  const user = session?.user ?? initialUser;

  if (!user) return <a href="/login">Login</a>;
  return <span>{user.name}</span>;
}
```

### 6. suppressHydrationWarning — когда это приемлемо

```typescript
// suppressHydrationWarning ДОПУСТИМ только для:
// 1. Временных меток которые намеренно разные
// 2. Конкретных атрибутов на листовых элементах

// ДОПУСТИМО: серверное время в footer
export function Footer() {
  return (
    <footer>
      <time suppressHydrationWarning>
        {new Date().getFullYear()} MyApp
      </time>
    </footer>
  );
}

// НЕДОПУСТИМО: suppressHydrationWarning на контейнере
export function BadExample() {
  return (
    // Маскирует реальные проблемы в дочерних элементах!
    <div suppressHydrationWarning>
      <ComplexComponent /> {/* скрытые ошибки внутри */}
    </div>
  );
}

// НЕДОПУСТИМО: как заглушка для плохого кода
export function WrongFix() {
  return (
    <span suppressHydrationWarning>
      {Math.random()} {/* "исправлено" suppressHydrationWarning, но проблема не решена */}
    </span>
  );
}
```

## Антипаттерн

```typescript
// Антипаттерн #1: suppressHydrationWarning везде как "быстрое исправление"
// Маскирует реальные проблемы и ухудшает производительность

// Антипаттерн #2: Проверка window в render функции без useEffect
"use client";
export function WindowWidth() {
  // При SSR: window = undefined → 0
  // При первом клиентском рендере: window.innerWidth = 1440
  // → MISMATCH даже с проверкой!
  const width = typeof window !== "undefined" ? window.innerWidth : 0;
  return <span>{width}</span>;
}
// Правильно: useEffect + useState как показано выше

// Антипаттерн #3: разные className на сервере и клиенте
"use client";
export function PlatformBadge() {
  // navigator.platform разный или недоступен на сервере
  const isIOS = typeof navigator !== "undefined" && /iPhone|iPad/.test(navigator.platform);
  return <div className={isIOS ? "ios-badge" : "other-badge"}>Platform</div>;
  // className разный → mismatch
}
```

## Связанные документы

- `knowledge/custom/03-antipatterns/use-client-abuse.md` — когда выносить "use client"
- `knowledge/custom/07-performance/` — dynamic imports и производительность
- `knowledge/custom/03-antipatterns/data-waterfall.md` — SSR vs CSR данные

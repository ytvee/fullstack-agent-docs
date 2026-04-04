---
category: antipatterns
topic: use-client-abuse
status: draft
---

## Проблема / Контекст

`"use client"` — одна из самых часто неправильно применяемых директив Next.js 15. Разработчики, переходящие с Pages Router или React SPA, привыкли что весь код — клиентский. В App Router всё наоборот: **Server Components — дефолт**. Добавление `"use client"` к компоненту выносит его (и всё его дерево) из серверного рендеринга в клиентский бандл.

Последствия злоупотребления `"use client"`:
- Больший JS бандл → медленнее FCP и TTI
- Потеря серверного доступа к БД, переменным окружения, файловой системе
- Невозможность использовать async/await на верхнем уровне компонента
- Теряется streaming и Suspense для server-rendered данных
- Секреты случайно попадают в клиентский бандл

## Решение

Правило: добавляй `"use client"` только когда компоненту **реально нужны** браузерные API: `useState`, `useEffect`, обработчики событий (`onClick`, `onChange`), браузерные API (`window`, `localStorage`), сторонние клиентские библиотеки (charts, rich text editors).

**Стратегия:** Держи `"use client"` как можно ближе к листьям дерева компонентов. Передавай данные из Server Components в Client Components через props.

## Пример кода

### 1. Базовый антипаттерн — use client на весь модуль

```typescript
// ПЛОХО: весь компонент стал клиентским ради одной кнопки
"use client";

import { db } from "@/db"; // ← ОШИБКА: db недоступна на клиенте!
import { useState } from "react";

// Этот компонент мог бы быть Server Component
export default async function ProjectsPage() {
  // С "use client" async на верхнем уровне не работает как ожидается
  const projects = await db.query.projects.findMany(); // ← падает в runtime

  const [search, setSearch] = useState("");

  return (
    <div>
      <input value={search} onChange={(e) => setSearch(e.target.value)} />
      {projects.map((p) => <div key={p.id}>{p.name}</div>)}
    </div>
  );
}
```

```typescript
// ПРАВИЛЬНО: разделяем на Server + Client компоненты

// src/app/(app)/projects/page.tsx — Server Component (нет директивы)
import { db } from "@/db";
import { auth } from "@/lib/auth";
import { ProjectSearch } from "./project-search"; // Client Component

export default async function ProjectsPage() {
  const session = await auth();

  // Запрос к БД прямо в Server Component — быстро, без API roundtrip
  const projects = await db.query.projects.findMany({
    where: eq(projects.userId, session!.user.id),
    orderBy: (p, { desc }) => desc(p.createdAt),
  });

  // Передаём данные как props в Client Component
  return (
    <div>
      <h1>Projects</h1>
      {/* ProjectSearch — клиентский, но получает данные с сервера */}
      <ProjectSearch initialProjects={projects} />
    </div>
  );
}

// src/app/(app)/projects/project-search.tsx — Client Component ТОЛЬКО там где нужно
"use client";

import { useState } from "react";
import type { Project } from "@/db/schema/projects";

interface ProjectSearchProps {
  initialProjects: Project[];
}

export function ProjectSearch({ initialProjects }: ProjectSearchProps) {
  const [search, setSearch] = useState("");

  const filtered = initialProjects.filter((p) =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search projects..."
        className="border rounded px-3 py-2"
      />
      <ul>
        {filtered.map((p) => (
          <li key={p.id}>{p.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 2. Composition pattern — Server Children в Client Component

```typescript
// Проблема: ClientLayout нужен клиентский state (sidebar), но внутри него RSC

// ПЛОХО: весь layout стал клиентским
"use client";
export default function Layout({ children }: { children: React.ReactNode }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  // children — это Server Components, но теперь они в клиентском контексте
  // На деле они теряют возможность быть серверными
  return (
    <div>
      <Sidebar open={sidebarOpen} onToggle={() => setSidebarOpen(!sidebarOpen)} />
      <main>{children}</main>
    </div>
  );
}

// ПРАВИЛЬНО: Composition pattern — children передаются снаружи как prop
// Server Component в качестве обёртки
// src/app/(app)/layout.tsx — Server Component
import { SidebarLayout } from "@/components/layouts/sidebar-layout";

export default function AppLayout({ children }: { children: React.ReactNode }) {
  // Сервер рендерит layout, передаёт children клиентскому компоненту
  return <SidebarLayout>{children}</SidebarLayout>;
}

// src/components/layouts/sidebar-layout.tsx — Client Component
"use client";

import { useState } from "react";
import { Sidebar } from "./sidebar";

export function SidebarLayout({ children }: { children: React.ReactNode }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex h-screen">
      <Sidebar
        open={sidebarOpen}
        onToggle={() => setSidebarOpen((prev) => !prev)}
      />
      {/* children — это Server Components! Они остаются серверными
          потому что были созданы на сервере и переданы как prop */}
      <main className="flex-1 overflow-auto">{children}</main>
    </div>
  );
}
```

### 3. Interactive Islands — минимальные клиентские острова

```typescript
// Страница преимущественно статическая, только кнопка "лайк" интерактивна

// src/app/blog/[slug]/page.tsx — Server Component
import { db } from "@/db";
import { LikeButton } from "@/components/like-button"; // только эта кнопка — client

export default async function BlogPost({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const post = await db.query.posts.findFirst({
    where: eq(posts.slug, slug),
    with: { likes: true },
  });

  if (!post) notFound();

  return (
    <article>
      <h1>{post.title}</h1>
      {/* Весь контент — Server Component */}
      <div dangerouslySetInnerHTML={{ __html: post.htmlContent }} />

      {/* Только интерактивная часть — Client Component */}
      {/* "остров" интерактивности среди серверного контента */}
      <LikeButton
        postId={post.id}
        initialLikes={post.likes.length}
      />
    </article>
  );
}

// src/components/like-button.tsx — маленький клиентский остров
"use client";

import { useState, useTransition } from "react";
import { toggleLike } from "@/actions/likes";
import { Heart } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

export function LikeButton({
  postId,
  initialLikes,
}: {
  postId: string;
  initialLikes: number;
}) {
  const [liked, setLiked] = useState(false);
  const [likes, setLikes] = useState(initialLikes);
  const [isPending, startTransition] = useTransition();

  function handleLike() {
    setLiked((prev) => !prev);
    setLikes((prev) => (liked ? prev - 1 : prev + 1));
    startTransition(() => toggleLike(postId));
  }

  return (
    <Button
      variant="ghost"
      size="sm"
      onClick={handleLike}
      disabled={isPending}
      className="gap-2"
    >
      <Heart
        className={cn("h-4 w-4", liked && "fill-red-500 text-red-500")}
      />
      {likes}
    </Button>
  );
}
```

### 4. Как правильно передавать Server Component данные

```typescript
// Паттерн: Server Component собирает данные → передаёт в Client

// src/app/(app)/dashboard/page.tsx
import { UserGreeting } from "@/components/user-greeting"; // Client
import { db } from "@/db";
import { auth } from "@/lib/auth";

export default async function Dashboard() {
  // Параллельная загрузка — только на сервере
  const [session, stats] = await Promise.all([
    auth(),
    db.query.projectStats.findFirst({ where: eq(projectStats.userId, userId) }),
  ]);

  return (
    <div>
      {/* Server Component — чистый HTML, 0 JS */}
      <section>
        <h2>Recent Activity</h2>
        {/* Server Component, загружает данные сам */}
        <RecentActivity userId={session!.user.id} />
      </section>

      {/* Client Component — получает данные как props, не fetches сам */}
      <UserGreeting
        name={session!.user.name ?? "User"}
        projectCount={stats?.projectCount ?? 0}
      />
    </div>
  );
}

// src/components/recent-activity.tsx — Server Component
// Нет "use client" — может делать async запросы
async function RecentActivity({ userId }: { userId: string }) {
  const activities = await db.query.activityLog.findMany({
    where: eq(activityLog.userId, userId),
    limit: 10,
    orderBy: (a, { desc }) => desc(a.createdAt),
  });

  return (
    <ul>
      {activities.map((a) => (
        <li key={a.id}>{a.description}</li>
      ))}
    </ul>
  );
}
```

### 5. Когда use client ОБЯЗАТЕЛЕН

```typescript
// Легитимные причины для "use client":

// 1. useState / useReducer
"use client";
export function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}

// 2. useEffect — side effects, subscriptions
"use client";
export function AnalyticsTracker({ pageId }: { pageId: string }) {
  useEffect(() => {
    analytics.track("page_view", { pageId });
  }, [pageId]);
  return null; // невидимый компонент
}

// 3. Browser APIs — window, localStorage, navigator
"use client";
export function ThemeToggle() {
  const [theme, setTheme] = useState<"light" | "dark">(() => {
    if (typeof window === "undefined") return "light";
    return (localStorage.getItem("theme") as "light" | "dark") ?? "light";
  });
  // ...
}

// 4. Event handlers — onClick, onChange, onSubmit
"use client";
export function SearchInput({ onSearch }: { onSearch: (q: string) => void }) {
  return <input onChange={(e) => onSearch(e.target.value)} />;
}

// 5. Клиентские библиотеки — charts, editors, maps
"use client";
import { Chart } from "recharts"; // клиентская библиотека
export function StatsChart({ data }: { data: ChartData[] }) {
  return <Chart data={data} />;
}
```

## Антипаттерн

```typescript
// ТОП ошибок:

// 1. "use client" в lib/utils — распространяется на весь бандл
"use client"; // ← зачем? utils не используют браузерные API
export function cn(...classes: string[]) { ... }
export function formatDate(date: Date) { ... }
// Последствие: все импортёры utils тоже становятся клиентскими

// 2. "use client" в providers с async контекстом
"use client";
export async function DataProvider() { // async + "use client" = не работает правильно
  const data = await fetchData(); // не будет ждать на клиенте как ожидается
  return <Context.Provider value={data}>{children}</Context.Provider>;
}

// 3. Импорт серверного кода в клиентский компонент
"use client";
import { db } from "@/db"; // db использует pg-native — не работает в браузере!
import { env } from "@/env"; // может утечь STRIPE_SECRET_KEY в бандл

// 4. use client на весь feature folder через barrel export
// src/features/dashboard/index.ts
"use client"; // ← нет смысла в barrel файле
export * from "./stats";       // stats могли быть серверными
export * from "./chart";       // chart нужен клиентский
export * from "./data-table";  // data-table мог быть серверным
// Теперь ВСЁ — клиентское
```

## Связанные документы

- `knowledge/custom/03-antipatterns/data-waterfall.md` — RSC параллельные запросы
- `knowledge/custom/03-antipatterns/secrets-exposure.md` — утечка env через клиентский бандл
- `knowledge/custom/03-antipatterns/hydration-mismatch.md` — проблемы гидрации Client Components

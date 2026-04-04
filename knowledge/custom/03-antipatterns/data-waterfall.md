---
category: antipatterns
topic: data-waterfall
status: draft
---

## Проблема / Контекст

Data waterfall (водопад запросов) — когда запросы к данным выполняются последовательно, каждый ожидая завершения предыдущего. В Next.js 15 с RSC это особенно болезненно: каждый `await` в Server Component добавляет latency к TTFB (Time to First Byte). Запрос пользователя → запрос 1 (100ms) → запрос 2 (80ms) → запрос 3 (60ms) → ответ: 240ms вместо возможных 100ms.

Типичные сценарии:
- Последовательный `await` для независимых данных
- Parent component ждёт данные которые нужны только child
- useEffect цепочки в Client Components
- N+1 запросов в циклах

## Решение

**Promise.all** для независимых параллельных запросов. **React `cache()`** для дедупликации одинаковых запросов в разных компонентах. **`preload()`** для ранней инициации запросов до рендеринга. **Suspense** с параллельными стримами для независимых частей UI.

## Пример кода

### 1. Базовый антипаттерн — последовательные await

```typescript
// ПЛОХО: каждый запрос ждёт предыдущий
// Общее время: 100 + 80 + 60 = 240ms
export default async function DashboardPage() {
  const user = await getUser();           // 100ms
  const projects = await getProjects();   // 80ms — начинается ПОСЛЕ getUser
  const stats = await getStats();         // 60ms — начинается ПОСЛЕ getProjects
  // ИТОГО: 240ms

  return <Dashboard user={user} projects={projects} stats={stats} />;
}

// ХОРОШО: параллельно через Promise.all
// Общее время: max(100, 80, 60) = 100ms
export default async function DashboardPage() {
  const [user, projects, stats] = await Promise.all([
    getUser(),    // 100ms ─┐
    getProjects(), // 80ms ─┤ параллельно
    getStats(),    // 60ms ─┘
    // ИТОГО: 100ms — выигрыш 140ms
  ]);

  return <Dashboard user={user} projects={projects} stats={stats} />;
}
```

### 2. Реальный пример с Drizzle

```typescript
// src/app/(app)/dashboard/page.tsx

// ПЛОХО: sequential waterfal
export default async function DashboardBad() {
  const session = await auth(); // 50ms
  if (!session?.user?.id) redirect("/login");

  const user = await db.query.users.findFirst({
    where: eq(users.id, session.user.id),
  }); // 40ms — ждёт auth

  const projectCount = await db.$count(
    projects,
    eq(projects.userId, session.user.id)
  ); // 30ms — ждёт user query

  const recentActivity = await db.query.activityLog.findMany({
    where: eq(activityLog.userId, session.user.id),
    limit: 5,
    orderBy: (a, { desc }) => desc(a.createdAt),
  }); // 35ms — ждёт projectCount

  // Итого: 50 + 40 + 30 + 35 = 155ms

  return <Dashboard user={user} projectCount={projectCount} activity={recentActivity} />;
}

// ХОРОШО: auth сначала (нужен userId), потом всё параллельно
export default async function DashboardGood() {
  const session = await auth(); // 50ms — единственный обязательный sequential
  if (!session?.user?.id) redirect("/login");

  const userId = session.user.id;

  // Все независимые запросы параллельно
  const [user, projectCount, recentActivity] = await Promise.all([
    db.query.users.findFirst({
      where: eq(users.id, userId),
      columns: { name: true, image: true, role: true },
    }),
    db.$count(projects, eq(projects.userId, userId)),
    db.query.activityLog.findMany({
      where: eq(activityLog.userId, userId),
      limit: 5,
      orderBy: (a, { desc }) => desc(a.createdAt),
    }),
  ]);
  // Итого: 50 + max(40, 30, 35) = 50 + 40 = 90ms — выигрыш 65ms

  return <Dashboard user={user} projectCount={projectCount} activity={recentActivity} />;
}
```

### 3. N+1 запросов в циклах

```typescript
// ПЛОХО: N+1 — 1 запрос для списка + N запросов для деталей
export async function ProjectList() {
  const projects = await db.query.projects.findMany({ limit: 20 });

  // N запросов для авторов — катастрофа при большом списке!
  const projectsWithAuthors = await Promise.all(
    projects.map(async (project) => {
      const author = await db.query.users.findFirst({
        where: eq(users.id, project.userId), // 1 запрос × 20 проектов = 20 запросов
      });
      return { ...project, author };
    })
  );

  return <ul>{projectsWithAuthors.map(p => <li key={p.id}>{p.name} by {p.author?.name}</li>)}</ul>;
}

// ХОРОШО: JOIN через Drizzle relations — 1 запрос
export async function ProjectList() {
  const projects = await db.query.projects.findMany({
    limit: 20,
    with: {
      author: {
        columns: { name: true, image: true },
      },
    },
  });
  // 1 запрос — получили проекты + авторов

  return (
    <ul>
      {projects.map((p) => (
        <li key={p.id}>
          {p.name} by {p.author?.name}
        </li>
      ))}
    </ul>
  );
}

// ХОРОШО: если JOIN невозможен — batch IN запрос
export async function ProjectList() {
  const projects = await db.query.projects.findMany({ limit: 20 });

  const authorIds = [...new Set(projects.map((p) => p.userId))];
  const authors = await db.query.users.findMany({
    where: inArray(users.id, authorIds), // 1 запрос для всех авторов
    columns: { id: true, name: true, image: true },
  });

  const authorMap = new Map(authors.map((a) => [a.id, a]));
  const projectsWithAuthors = projects.map((p) => ({
    ...p,
    author: authorMap.get(p.userId),
  }));

  return <ul>{projectsWithAuthors.map(p => <li key={p.id}>{p.name}</li>)}</ul>;
}
```

### 4. React cache() для дедупликации

```typescript
// Проблема: один и тот же запрос в нескольких компонентах в одном render

// src/lib/data/users.ts
import { cache } from "react";
import { db } from "@/db";
import { users } from "@/db/schema/users";
import { eq } from "drizzle-orm";
import { auth } from "@/lib/auth";

// cache() мемоизирует результат в рамках одного React рендер дерева (per request)
// Второй вызов с теми же аргументами → возвращает кэшированный результат без DB запроса
export const getCurrentUser = cache(async () => {
  const session = await auth();
  if (!session?.user?.id) return null;

  return db.query.users.findFirst({
    where: eq(users.id, session.user.id),
  });
});

export const getUserById = cache(async (userId: string) => {
  return db.query.users.findFirst({
    where: eq(users.id, userId),
  });
});

// Теперь несколько компонентов могут вызывать getCurrentUser()
// — БД запрос выполнится только ОДИН раз за render

// src/app/(app)/layout.tsx
export default async function AppLayout({ children }) {
  const user = await getCurrentUser(); // Запрос 1
  // ...
}

// src/components/user-avatar.tsx
export async function UserAvatar() {
  const user = await getCurrentUser(); // cache() → нет нового запроса!
  return <img src={user?.image} />;
}

// src/components/user-nav.tsx
export async function UserNav() {
  const user = await getCurrentUser(); // cache() → нет нового запроса!
  return <span>{user?.name}</span>;
}
```

### 5. preload() pattern для ранней загрузки

```typescript
// preload() — инициирует запрос немедленно, не ожидая его результата
// Используй когда точно знаешь что данные понадобятся, но рендер ещё не начался

// src/lib/data/projects.ts
import { cache } from "react";
import { db } from "@/db";
import { auth } from "@/lib/auth";
import { eq } from "drizzle-orm";

export const getProjects = cache(async (userId: string) => {
  return db.query.projects.findMany({
    where: eq(projects.userId, userId),
    with: { tags: true },
    orderBy: (p, { desc }) => desc(p.updatedAt),
  });
});

// preload — инициирует fetch без await, результат кэшируется в cache()
export function preloadProjects(userId: string): void {
  void getProjects(userId); // Запускаем без await — fire and forget
}

// src/app/(app)/projects/page.tsx
import { preloadProjects, getProjects } from "@/lib/data/projects";
import { auth } from "@/lib/auth";
import { ProjectGrid } from "./project-grid";

export default async function ProjectsPage() {
  const session = await auth(); // 50ms
  if (!session?.user?.id) redirect("/login");

  // Стартуем загрузку проектов НЕМЕДЛЕННО, не дожидаясь других операций
  preloadProjects(session.user.id); // fire and forget — запрос уже летит

  // Теперь можем делать другие операции пока проекты загружаются
  const [userPrefs, orgData] = await Promise.all([
    getUserPreferences(session.user.id),  // идут параллельно с preload
    getOrgData(session.user.id),           // идут параллельно с preload
  ]);

  // К этому моменту getProjects скорее всего уже завершился
  // cache() вернёт готовый результат без нового запроса
  const projects = await getProjects(session.user.id);

  return (
    <ProjectGrid
      projects={projects}
      userPrefs={userPrefs}
      orgData={orgData}
    />
  );
}
```

### 6. Suspense для параллельного стриминга

```typescript
// Независимые блоки UI загружаются параллельно и стримятся по мере готовности

// src/app/(app)/dashboard/page.tsx
import { Suspense } from "react";
import { Skeleton } from "@/components/ui/skeleton";

// Server Components — каждый загружает свои данные независимо
async function UserStats({ userId }: { userId: string }) {
  const stats = await getUserStats(userId); // 80ms
  return <StatsCard stats={stats} />;
}

async function RecentProjects({ userId }: { userId: string }) {
  const projects = await getRecentProjects(userId); // 120ms
  return <ProjectList projects={projects} />;
}

async function ActivityFeed({ userId }: { userId: string }) {
  const activities = await getActivities(userId); // 60ms
  return <Feed activities={activities} />;
}

export default async function Dashboard() {
  const session = await auth();
  if (!session?.user?.id) redirect("/login");

  // Все три компонента начинают загрузку ОДНОВРЕМЕННО
  // Каждый стримится как только готов — не ждёт остальных
  return (
    <div className="grid grid-cols-3 gap-4">
      {/* UserStats (80ms) стримится первым */}
      <Suspense fallback={<Skeleton className="h-40" />}>
        <UserStats userId={session.user.id} />
      </Suspense>

      {/* ActivityFeed (60ms) стримится вторым */}
      <Suspense fallback={<Skeleton className="h-80" />}>
        <ActivityFeed userId={session.user.id} />
      </Suspense>

      {/* RecentProjects (120ms) стримится последним */}
      <Suspense fallback={<Skeleton className="h-80" />}>
        <RecentProjects userId={session.user.id} />
      </Suspense>
    </div>
  );
  // Пользователь видит данные по мере их загрузки, не ждёт все 120ms
}
```

### 7. Когда последовательный await ПРАВИЛЬНЫЙ выбор

```typescript
// Последовательный await нормален когда запросы ЗАВИСЯТ друг от друга:

export default async function ProjectDetailPage({
  params,
}: {
  params: Promise<{ projectId: string }>;
}) {
  const { projectId } = await params;

  // ПРАВИЛЬНО: сначала проверяем существование и права
  const session = await auth();
  if (!session?.user?.id) redirect("/login");

  // ПРАВИЛЬНО: projectId нужен для следующих запросов
  const project = await db.query.projects.findFirst({
    where: and(
      eq(projects.id, projectId),
      eq(projects.userId, session.user.id) // проверка владельца
    ),
  });

  if (!project) notFound();

  // ПРАВИЛЬНО: project.teamId нужен для следующих независимых запросов
  const [teamMembers, projectTasks, projectFiles] = await Promise.all([
    getTeamMembers(project.teamId), // зависит от project.teamId
    getProjectTasks(project.id),    // зависит от project.id
    getProjectFiles(project.id),    // зависит от project.id
  ]);

  return (
    <ProjectDetail
      project={project}
      team={teamMembers}
      tasks={projectTasks}
      files={projectFiles}
    />
  );
}
```

## Антипаттерн

```typescript
// Антипаттерн #1: Promise.all с зависимыми запросами
// Если запросы зависят друг от друга — Promise.all не поможет
const [user, userProjects] = await Promise.all([
  getUser(userId),
  getProjectsByUser(userId), // OK — userId уже известен, независим
]);

// НО:
const [user, userTeamProjects] = await Promise.all([
  getUser(userId),
  getProjectsByTeam(user.teamId), // ← ОШИБКА: user.teamId недоступен до завершения getUser
]);

// Антипаттерн #2: useEffect waterfal в Client Components
"use client";
export function UserDashboard({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(r => r.json())
      .then(user => {
        setUser(user);
        // ПЛОХО: второй fetch начинается только после первого!
        return fetch(`/api/users/${user.id}/projects`);
      })
      .then(r => r.json())
      .then(setProjects);
  }, [userId]);
  // Решение: данные должны приходить из Server Component как props
}

// Антипаттерн #3: Suspense как намеренный waterfall
// Иногда разработчики неправильно вкладывают Suspense:
<Suspense fallback={<Skeleton />}>
  <UserStats userId={userId} />
  {/* RecentProjects внутри UserStats — начнёт загружаться ПОСЛЕ UserStats! */}
</Suspense>

// Правильно: параллельные Suspense на одном уровне (как в примере 6)
```

## Связанные документы

- `knowledge/custom/07-performance/` — кэширование запросов, ISR
- `knowledge/custom/03-antipatterns/use-client-abuse.md` — RSC vs Client Components для данных
- `knowledge/custom/01-architecture/` — стратегии загрузки данных

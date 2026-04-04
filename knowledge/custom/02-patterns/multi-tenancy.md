---
category: patterns
topic: multi-tenancy
status: draft
---

## Проблема / Контекст

Multi-tenancy — это когда одно приложение обслуживает множество изолированных организаций (тенантов). Критическая задача: данные тенанта А никогда не должны быть доступны тенанту Б. Утечка данных между тенантами — катастрофический баг.

Два основных подхода маршрутизации:
1. **Subdomain:** `acme.app.com`, `globex.app.com` — лучший UX для B2B SaaS
2. **Path-based:** `app.com/acme/dashboard`, `app.com/globex/dashboard` — проще в деплое

Независимо от подхода: изоляция данных в БД через `orgId` на каждой таблице — обязательна.

## Решение

**Архитектура:** Middleware резолвит тенанта из subdomain/path и помещает `orgId` в request headers. Server Components и Server Actions читают `orgId` из headers (не из URL — его можно подделать). Все Drizzle запросы включают `where eq(table.orgId, orgId)`.

## Пример кода

### 1. Drizzle схема с tenant isolation

```typescript
// src/db/schema/organizations.ts
import { pgTable, text, timestamp, uuid, boolean } from "drizzle-orm/pg-core";

export const organizations = pgTable("organizations", {
  id: uuid("id").primaryKey().defaultRandom(),
  name: text("name").notNull(),
  slug: text("slug").notNull().unique(), // используется в URL/subdomain
  domain: text("domain").unique(), // кастомный домен (опционально)
  plan: text("plan").notNull().default("free"),
  isActive: boolean("is_active").notNull().default(true),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

// src/db/schema/org-members.ts
import { pgTable, uuid, pgEnum, timestamp, primaryKey } from "drizzle-orm/pg-core";
import { users } from "./users";
import { organizations } from "./organizations";

export const orgRoleEnum = pgEnum("org_role", ["owner", "admin", "member", "viewer"]);

export const orgMembers = pgTable(
  "org_members",
  {
    userId: uuid("user_id")
      .notNull()
      .references(() => users.id, { onDelete: "cascade" }),
    orgId: uuid("org_id")
      .notNull()
      .references(() => organizations.id, { onDelete: "cascade" }),
    role: orgRoleEnum("role").notNull().default("member"),
    createdAt: timestamp("created_at").defaultNow().notNull(),
  },
  (t) => ({
    pk: primaryKey({ columns: [t.userId, t.orgId] }),
  })
);

// src/db/schema/projects.ts — пример tenant-изолированной таблицы
import { pgTable, text, timestamp, uuid } from "drizzle-orm/pg-core";
import { organizations } from "./organizations";
import { users } from "./users";

export const projects = pgTable("projects", {
  id: uuid("id").primaryKey().defaultRandom(),
  // orgId ОБЯЗАТЕЛЕН на каждой таблице с tenant-данными
  orgId: uuid("org_id")
    .notNull()
    .references(() => organizations.id, { onDelete: "cascade" }),
  createdBy: uuid("created_by").references(() => users.id, { onDelete: "set null" }),
  name: text("name").notNull(),
  description: text("description"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});
```

### 2. Middleware: subdomain routing

```typescript
// src/middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { auth } from "@/lib/auth";

const APP_DOMAIN = process.env.NEXT_PUBLIC_APP_DOMAIN ?? "app.com";

export default auth(async (req: NextRequest) => {
  const hostname = req.headers.get("host") ?? "";
  const { pathname } = req.nextUrl;

  // Определяем slug из subdomain
  // acme.app.com → acme
  // app.com → null (лендинг)
  let orgSlug: string | null = null;

  if (hostname.endsWith(`.${APP_DOMAIN}`)) {
    orgSlug = hostname.replace(`.${APP_DOMAIN}`, "");
  } else if (hostname !== APP_DOMAIN && hostname !== `www.${APP_DOMAIN}`) {
    // Кастомный домен — резолвим через БД в Edge-совместимом запросе
    // Для этого нужен отдельный Edge API или кэш
    orgSlug = await resolveCustomDomain(hostname);
  }

  // Нет slug — лендинг или www
  if (!orgSlug || orgSlug === "www") {
    return NextResponse.next();
  }

  // Инжектируем orgSlug в headers — Server Components прочитают отсюда
  // НЕ из URL params — их можно подделать
  const requestHeaders = new Headers(req.headers);
  requestHeaders.set("x-org-slug", orgSlug);
  requestHeaders.set("x-pathname", pathname);

  return NextResponse.next({ request: { headers: requestHeaders } });
});

// Edge-совместимый резолвинг кастомного домена
// Используем Vercel KV или аналог для кэша
async function resolveCustomDomain(domain: string): Promise<string | null> {
  try {
    // Обращаемся к внутреннему API endpoint (не Drizzle — нужен Edge)
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_APP_URL}/api/internal/resolve-domain?domain=${domain}`,
      {
        next: { revalidate: 300 }, // кэш 5 минут
        headers: { "x-internal-secret": process.env.INTERNAL_API_SECRET! },
      }
    );
    if (!res.ok) return null;
    const data = (await res.json()) as { slug: string | null };
    return data.slug;
  } catch {
    return null;
  }
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
```

### 3. Middleware: path-based routing

```typescript
// src/middleware.ts — альтернатива для path-based
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { auth } from "@/lib/auth";

export default auth(async (req: NextRequest) => {
  const { pathname } = req.nextUrl;

  // /[orgSlug]/... → извлекаем slug
  const orgSlugMatch = pathname.match(/^\/([a-z0-9-]+)\/(.*)/);
  if (!orgSlugMatch) return NextResponse.next();

  const orgSlug = orgSlugMatch[1];

  // Исключаем системные пути
  const SYSTEM_PATHS = ["api", "_next", "auth", "login", "signup"];
  if (SYSTEM_PATHS.includes(orgSlug)) return NextResponse.next();

  const requestHeaders = new Headers(req.headers);
  requestHeaders.set("x-org-slug", orgSlug);

  return NextResponse.next({ request: { headers: requestHeaders } });
});
```

### 4. Tenant context helper

```typescript
// src/lib/tenant.ts
import { headers } from "next/headers";
import { cache } from "react";
import { db } from "@/db";
import { organizations, orgMembers } from "@/db/schema";
import { eq, and } from "drizzle-orm";
import { auth } from "@/lib/auth";

// cache() — один запрос per RSC render tree, не per request
export const getTenantContext = cache(async () => {
  const headersList = await headers();
  const orgSlug = headersList.get("x-org-slug");

  if (!orgSlug) return null;

  const org = await db.query.organizations.findFirst({
    where: eq(organizations.slug, orgSlug),
    columns: { id: true, name: true, slug: true, plan: true, isActive: true },
  });

  if (!org || !org.isActive) return null;

  return org;
});

// Получить контекст тенанта + проверить членство пользователя
export const getTenantMembership = cache(async () => {
  const [tenant, session] = await Promise.all([
    getTenantContext(),
    auth(),
  ]);

  if (!tenant || !session?.user?.id) return null;

  const membership = await db.query.orgMembers.findFirst({
    where: and(
      eq(orgMembers.orgId, tenant.id),
      eq(orgMembers.userId, session.user.id)
    ),
    columns: { role: true },
  });

  if (!membership) return null;

  return {
    org: tenant,
    user: session.user,
    role: membership.role,
  };
});

// Типизированный guard — бросает если нет доступа
export async function requireTenantAccess() {
  const ctx = await getTenantMembership();
  if (!ctx) {
    throw new Error("Access denied to this organization");
  }
  return ctx;
}
```

### 5. App Router структура для path-based

```
src/app/
├── (landing)/              # Лендинг — без тенанта
│   ├── page.tsx
│   └── pricing/page.tsx
├── [orgSlug]/              # Tenant-scoped маршруты
│   ├── layout.tsx          # Загружает тенанта, провайдит контекст
│   ├── dashboard/
│   │   └── page.tsx
│   ├── projects/
│   │   ├── page.tsx
│   │   └── [projectId]/
│   │       └── page.tsx
│   └── settings/
│       └── page.tsx
└── api/
    └── webhooks/           # Без tenant scope
```

```typescript
// src/app/[orgSlug]/layout.tsx
import { requireTenantAccess } from "@/lib/tenant";
import { redirect } from "next/navigation";
import { OrgProvider } from "@/components/providers/org-provider";

export default async function OrgLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ orgSlug: string }>;
}) {
  const { orgSlug } = await params;

  let ctx;
  try {
    ctx = await requireTenantAccess();
  } catch {
    redirect(`/login?next=/${orgSlug}/dashboard`);
  }

  // Проверяем что slug совпадает (защита от подмены)
  if (ctx.org.slug !== orgSlug) {
    redirect("/403");
  }

  return (
    <OrgProvider org={ctx.org} membership={{ role: ctx.role }}>
      {children}
    </OrgProvider>
  );
}
```

### 6. Server Actions с tenant isolation

```typescript
// src/actions/projects.ts
"use server";

import { requireTenantAccess } from "@/lib/tenant";
import { db } from "@/db";
import { projects } from "@/db/schema/projects";
import { eq, and } from "drizzle-orm";
import { revalidatePath } from "next/cache";
import { z } from "zod";

const createProjectSchema = z.object({
  name: z.string().min(1).max(100),
  description: z.string().max(500).optional(),
});

export async function createProject(
  formData: FormData
): Promise<{ success: boolean; error?: string; projectId?: string }> {
  let ctx;
  try {
    ctx = await requireTenantAccess();
  } catch {
    return { success: false, error: "Unauthorized" };
  }

  // Проверяем роль внутри тенанта
  if (ctx.role === "viewer") {
    return { success: false, error: "Viewers cannot create projects" };
  }

  const parsed = createProjectSchema.safeParse({
    name: formData.get("name"),
    description: formData.get("description"),
  });

  if (!parsed.success) {
    return { success: false, error: parsed.error.errors[0]?.message };
  }

  const [project] = await db
    .insert(projects)
    .values({
      // orgId берём из проверенного контекста, не из FormData!
      orgId: ctx.org.id,
      createdBy: ctx.user.id,
      ...parsed.data,
    })
    .returning({ id: projects.id });

  revalidatePath(`/${ctx.org.slug}/projects`);
  return { success: true, projectId: project?.id };
}

// Обновление с двойной проверкой: orgId + userId
export async function updateProject(
  projectId: string,
  data: { name?: string; description?: string }
): Promise<{ success: boolean; error?: string }> {
  let ctx;
  try {
    ctx = await requireTenantAccess();
  } catch {
    return { success: false, error: "Unauthorized" };
  }

  // КРИТИЧНО: всегда фильтруем и по projectId, и по orgId
  // Иначе member из org A может обновить проект org B зная ID
  const updated = await db
    .update(projects)
    .set({ ...data, updatedAt: new Date() })
    .where(
      and(
        eq(projects.id, projectId),
        eq(projects.orgId, ctx.org.id) // ← tenant isolation guard
      )
    )
    .returning({ id: projects.id });

  if (updated.length === 0) {
    return { success: false, error: "Project not found" };
  }

  revalidatePath(`/${ctx.org.slug}/projects`);
  return { success: true };
}
```

### 7. Row-level security паттерн через Drizzle helper

```typescript
// src/lib/tenant-query.ts
// Обёртки для Drizzle запросов с автоматической tenant фильтрацией

import { getTenantContext } from "./tenant";
import { db } from "@/db";
import { projects } from "@/db/schema/projects";
import { eq, and, type SQL } from "drizzle-orm";

// Фабрика tenant-aware репозитория
export async function createTenantProjectRepo() {
  const tenant = await getTenantContext();
  if (!tenant) throw new Error("No tenant context");

  return {
    findMany: (extraWhere?: SQL) =>
      db.query.projects.findMany({
        where: extraWhere
          ? and(eq(projects.orgId, tenant.id), extraWhere)
          : eq(projects.orgId, tenant.id),
      }),

    findById: (id: string) =>
      db.query.projects.findFirst({
        where: and(eq(projects.id, id), eq(projects.orgId, tenant.id)),
      }),

    delete: (id: string) =>
      db
        .delete(projects)
        .where(and(eq(projects.id, id), eq(projects.orgId, tenant.id))),
  };
}

// Использование в Server Component:
// const repo = await createTenantProjectRepo();
// const userProjects = await repo.findMany();
// const project = await repo.findById(projectId); // null если не принадлежит тенанту
```

### 8. Zustand store с org контекстом

```typescript
// src/stores/org-store.ts
import { create } from "zustand";
import type { Organization } from "@/db/schema/organizations";

interface OrgStore {
  org: Pick<Organization, "id" | "name" | "slug" | "plan"> | null;
  role: string | null;
  setOrg: (org: OrgStore["org"], role: string) => void;
}

export const useOrgStore = create<OrgStore>((set) => ({
  org: null,
  role: null,
  setOrg: (org, role) => set({ org, role }),
}));

// src/components/providers/org-provider.tsx
"use client";

import { useEffect } from "react";
import { useOrgStore } from "@/stores/org-store";
import type { Organization } from "@/db/schema/organizations";

export function OrgProvider({
  org,
  membership,
  children,
}: {
  org: Pick<Organization, "id" | "name" | "slug" | "plan">;
  membership: { role: string };
  children: React.ReactNode;
}) {
  const setOrg = useOrgStore((s) => s.setOrg);

  useEffect(() => {
    setOrg(org, membership.role);
  }, [org, membership.role, setOrg]);

  return <>{children}</>;
}
```

## Антипаттерн

```typescript
// ПЛОХО: orgId берётся из URL params, не из проверенного контекста
export async function getProjects(orgSlug: string) {
  "use server";
  // Злоумышленник передаёт чужой slug и получает чужие данные
  const org = await db.query.organizations.findFirst({
    where: eq(organizations.slug, orgSlug),
  });
  // Нет проверки членства!
  return db.query.projects.findMany({ where: eq(projects.orgId, org!.id) });
}

// ПЛОХО: Запрос без tenant фильтра
export async function getAllProjects() {
  "use server";
  const session = await auth();
  // Возвращает ВСЕ проекты из всех организаций!
  return db.query.projects.findMany();
}

// ПЛОХО: orgId из FormData
export async function createProjectBad(formData: FormData) {
  "use server";
  const orgId = formData.get("orgId"); // Клиент может передать любой orgId
  await db.insert(projects).values({ orgId: orgId as string, ... });
}

// ПЛОХО: Хранить tenant state только на клиенте
function useTenant() {
  // localStorage можно изменить в DevTools
  return { orgId: localStorage.getItem("orgId") };
}
```

**Правила:**
1. `orgId` всегда берётся из проверенного серверного контекста, никогда из URL/FormData
2. Каждый Drizzle запрос к tenant-данным ОБЯЗАН включать `eq(table.orgId, orgId)`
3. При обновлении/удалении — фильтруй и по `id`, и по `orgId` — иначе IDOR уязвимость
4. Проверяй членство пользователя в организации, а не только существование организации
5. Используй `react.cache()` для tenant resolution — дорогой запрос, нужен один per render

## Связанные документы

- `knowledge/custom/02-patterns/rbac.md` — роли внутри организации
- `knowledge/custom/06-security/` — IDOR и broken object level authorization
- `knowledge/custom/01-architecture/` — общая архитектура multi-tenant приложения

---
category: patterns
topic: rbac
status: draft
---

## Проблема / Контекст

Role-Based Access Control (RBAC) в Next.js 15 требует проверки прав на нескольких уровнях: middleware (маршруты), Server Actions (бизнес-логика), Server Components (данные), Client Components (UI). Проверка только на одном уровне — уязвимость. Типичные роли: `admin` (полный доступ), `member` (стандартный доступ), `viewer` (только чтение).

Распространённые ошибки:
- Проверка роли только в UI — скрыть кнопку недостаточно, Server Action остаётся доступным
- Хранение роли только в JWT без синхронизации с БД
- Отсутствие проверки при cross-resource операциях (пользователь А удаляет данные пользователя Б)

## Решение

**Многоуровневая защита:** Middleware блокирует недоступные маршруты по роли из JWT. Server Actions проверяют роль из свежей сессии (не из stale кэша). Хелпер функции `requireRole` / `can` centralizуют логику. UI рендерит компоненты условно, но это только UX-слой, не безопасность.

## Пример кода

### 1. Drizzle схема с ролями

```typescript
// src/db/schema/users.ts
import { pgTable, text, timestamp, uuid, pgEnum } from "drizzle-orm/pg-core";

export const userRoleEnum = pgEnum("user_role", ["admin", "member", "viewer"]);

export const users = pgTable("users", {
  id: uuid("id").primaryKey().defaultRandom(),
  email: text("email").notNull().unique(),
  name: text("name"),
  image: text("image"),
  role: userRoleEnum("role").notNull().default("viewer"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

export type User = typeof users.$inferSelect;
export type UserRole = (typeof userRoleEnum.enumValues)[number];
```

### 2. Auth.js v5 с ролью в сессии

```typescript
// src/lib/auth.ts
import NextAuth from "next-auth";
import GitHub from "next-auth/providers/github";
import { DrizzleAdapter } from "@auth/drizzle-adapter";
import { db } from "@/db";
import { users } from "@/db/schema/users";
import { eq } from "drizzle-orm";
import type { UserRole } from "@/db/schema/users";

declare module "next-auth" {
  interface Session {
    user: {
      id: string;
      email: string;
      name?: string | null;
      image?: string | null;
      role: UserRole;
    };
  }
}

declare module "@auth/core/jwt" {
  interface JWT {
    role: UserRole;
  }
}

export const { auth, handlers, signIn, signOut } = NextAuth({
  adapter: DrizzleAdapter(db),
  session: { strategy: "jwt" },
  providers: [GitHub],
  callbacks: {
    // Загружаем роль из БД при создании JWT
    async jwt({ token, user }) {
      if (user?.id) {
        // При первом логине — берём роль из объекта user (из адаптера)
        const dbUser = await db.query.users.findFirst({
          where: eq(users.id, user.id),
          columns: { role: true },
        });
        token.role = dbUser?.role ?? "viewer";
        token.sub = user.id;
      }
      return token;
    },
    // Пробрасываем роль в сессию
    async session({ session, token }) {
      if (token.sub) {
        session.user.id = token.sub;
        session.user.role = token.role;
      }
      return session;
    },
  },
});
```

### 3. Permission helpers — централизованная логика

```typescript
// src/lib/permissions.ts
import type { UserRole } from "@/db/schema/users";

// Иерархия ролей: чем выше индекс, тем больше прав
const ROLE_HIERARCHY: Record<UserRole, number> = {
  viewer: 0,
  member: 1,
  admin: 2,
};

// Проверка: имеет ли роль минимально необходимые права
export function hasMinRole(userRole: UserRole, minRole: UserRole): boolean {
  return ROLE_HIERARCHY[userRole] >= ROLE_HIERARCHY[minRole];
}

// Матрица разрешений для конкретных действий
export const PERMISSIONS = {
  // Управление пользователями
  "users:read": (role: UserRole) => hasMinRole(role, "viewer"),
  "users:invite": (role: UserRole) => hasMinRole(role, "member"),
  "users:delete": (role: UserRole) => role === "admin",
  "users:changeRole": (role: UserRole) => role === "admin",

  // Контент
  "content:read": (role: UserRole) => hasMinRole(role, "viewer"),
  "content:create": (role: UserRole) => hasMinRole(role, "member"),
  "content:update": (role: UserRole) => hasMinRole(role, "member"),
  "content:delete": (role: UserRole) => hasMinRole(role, "admin"),
  "content:publish": (role: UserRole) => hasMinRole(role, "admin"),

  // Настройки
  "settings:read": (role: UserRole) => hasMinRole(role, "member"),
  "settings:update": (role: UserRole) => role === "admin",

  // Биллинг
  "billing:read": (role: UserRole) => hasMinRole(role, "member"),
  "billing:manage": (role: UserRole) => role === "admin",
} as const;

export type Permission = keyof typeof PERMISSIONS;

export function can(role: UserRole, permission: Permission): boolean {
  return PERMISSIONS[permission](role);
}
```

### 4. Server-side auth guard — для Server Actions

```typescript
// src/lib/auth-guard.ts
import { auth } from "@/lib/auth";
import { can } from "@/lib/permissions";
import type { Permission } from "@/lib/permissions";
import type { UserRole } from "@/db/schema/users";

export class AuthError extends Error {
  constructor(
    message: string,
    public readonly code: "UNAUTHENTICATED" | "UNAUTHORIZED"
  ) {
    super(message);
    this.name = "AuthError";
  }
}

// Получить сессию или бросить ошибку
export async function requireAuth() {
  const session = await auth();
  if (!session?.user?.id) {
    throw new AuthError("Authentication required", "UNAUTHENTICATED");
  }
  return session;
}

// Требовать конкретную роль
export async function requireRole(minRole: UserRole) {
  const session = await requireAuth();
  const { hasMinRole } = await import("@/lib/permissions");
  if (!hasMinRole(session.user.role, minRole)) {
    throw new AuthError(
      `Role '${minRole}' required, got '${session.user.role}'`,
      "UNAUTHORIZED"
    );
  }
  return session;
}

// Требовать конкретное разрешение
export async function requirePermission(permission: Permission) {
  const session = await requireAuth();
  if (!can(session.user.role, permission)) {
    throw new AuthError(
      `Permission '${permission}' denied for role '${session.user.role}'`,
      "UNAUTHORIZED"
    );
  }
  return session;
}
```

### 5. Server Actions с проверкой прав

```typescript
// src/actions/users.ts
"use server";

import { requirePermission } from "@/lib/auth-guard";
import { db } from "@/db";
import { users } from "@/db/schema/users";
import { eq } from "drizzle-orm";
import { revalidatePath } from "next/cache";
import type { UserRole } from "@/db/schema/users";
import { z } from "zod";

const changeRoleSchema = z.object({
  targetUserId: z.string().uuid(),
  newRole: z.enum(["admin", "member", "viewer"]),
});

export async function changeUserRole(
  formData: FormData
): Promise<{ success: boolean; error?: string }> {
  // Проверка: только admin может менять роли
  let session;
  try {
    session = await requirePermission("users:changeRole");
  } catch (error) {
    return { success: false, error: "Insufficient permissions" };
  }

  const parsed = changeRoleSchema.safeParse({
    targetUserId: formData.get("targetUserId"),
    newRole: formData.get("newRole"),
  });

  if (!parsed.success) {
    return { success: false, error: "Invalid input" };
  }

  const { targetUserId, newRole } = parsed.data;

  // Admin не может понизить сам себя
  if (targetUserId === session.user.id && newRole !== "admin") {
    return { success: false, error: "Cannot change your own admin role" };
  }

  await db
    .update(users)
    .set({ role: newRole as UserRole, updatedAt: new Date() })
    .where(eq(users.id, targetUserId));

  revalidatePath("/admin/users");
  return { success: true };
}

export async function deleteUser(
  userId: string
): Promise<{ success: boolean; error?: string }> {
  try {
    const session = await requirePermission("users:delete");

    // Нельзя удалить самого себя
    if (userId === session.user.id) {
      return { success: false, error: "Cannot delete yourself" };
    }

    await db.delete(users).where(eq(users.id, userId));
    revalidatePath("/admin/users");
    return { success: true };
  } catch (error) {
    if (error instanceof Error) {
      return { success: false, error: error.message };
    }
    return { success: false, error: "Unknown error" };
  }
}
```

### 6. Middleware для защиты маршрутов по роли

```typescript
// src/middleware.ts
import { auth } from "@/lib/auth";
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { hasMinRole } from "@/lib/permissions";
import type { UserRole } from "@/db/schema/users";

// Конфиг маршрутов: минимальная роль для доступа
const ROUTE_ROLES: Array<{ pattern: RegExp; minRole: UserRole }> = [
  { pattern: /^\/admin/, minRole: "admin" },
  { pattern: /^\/app\/settings/, minRole: "member" },
  { pattern: /^\/app/, minRole: "viewer" },
];

export default auth((req) => {
  const { pathname } = req.nextUrl;
  const session = req.auth;

  // Находим первое подходящее правило
  const rule = ROUTE_ROLES.find(({ pattern }) => pattern.test(pathname));
  if (!rule) return NextResponse.next(); // публичный маршрут

  // Не авторизован — редирект на логин
  if (!session?.user) {
    const loginUrl = new URL("/login", req.url);
    loginUrl.searchParams.set("callbackUrl", pathname);
    return NextResponse.redirect(loginUrl);
  }

  // Недостаточно прав — 403 страница
  if (!hasMinRole(session.user.role, rule.minRole)) {
    return NextResponse.redirect(new URL("/403", req.url));
  }

  return NextResponse.next();
});

export const config = {
  matcher: [
    // Защищаем всё кроме статики и API без auth
    "/((?!api/auth|_next/static|_next/image|favicon.ico|login|register|403).*)",
  ],
};
```

### 7. Клиентский хук + условный рендеринг

```typescript
// src/hooks/use-permissions.ts
"use client";

import { useSession } from "next-auth/react";
import { can, hasMinRole } from "@/lib/permissions";
import type { Permission } from "@/lib/permissions";
import type { UserRole } from "@/db/schema/users";

export function usePermissions() {
  const { data: session } = useSession();
  const role = session?.user?.role ?? "viewer";

  return {
    role,
    can: (permission: Permission) => can(role, permission),
    hasMinRole: (minRole: UserRole) => hasMinRole(role, minRole),
    isAdmin: role === "admin",
    isMember: role === "member" || role === "admin",
  };
}

// src/components/rbac/can.tsx
"use client";

import { usePermissions } from "@/hooks/use-permissions";
import type { Permission } from "@/lib/permissions";

interface CanProps {
  permission: Permission;
  children: React.ReactNode;
  fallback?: React.ReactNode;
}

// Компонент для условного рендеринга по правам
export function Can({ permission, children, fallback = null }: CanProps) {
  const { can } = usePermissions();
  return can(permission) ? <>{children}</> : <>{fallback}</>;
}
```

### 8. Использование в UI

```typescript
// src/app/(app)/admin/users/page.tsx
import { requirePermission } from "@/lib/auth-guard";
import { db } from "@/db";
import { users } from "@/db/schema/users";
import { redirect } from "next/navigation";
import { UserTable } from "./user-table";

export default async function AdminUsersPage() {
  // Server Component тоже проверяет права
  try {
    await requirePermission("users:read");
  } catch {
    redirect("/403");
  }

  const allUsers = await db.query.users.findMany({
    orderBy: (u, { asc }) => asc(u.createdAt),
  });

  return <UserTable users={allUsers} />;
}

// src/app/(app)/admin/users/user-table.tsx
"use client";

import { Can } from "@/components/rbac/can";
import { changeUserRole, deleteUser } from "@/actions/users";
import { Button } from "@/components/ui/button";
import type { User } from "@/db/schema/users";

export function UserTable({ users }: { users: User[] }) {
  return (
    <table>
      <tbody>
        {users.map((user) => (
          <tr key={user.id}>
            <td>{user.email}</td>
            <td>{user.role}</td>
            <td>
              {/* Кнопки видны только если есть права — но Server Action тоже защищён */}
              <Can permission="users:changeRole">
                <form action={changeUserRole}>
                  <input type="hidden" name="targetUserId" value={user.id} />
                  <select name="newRole" defaultValue={user.role}>
                    <option value="viewer">Viewer</option>
                    <option value="member">Member</option>
                    <option value="admin">Admin</option>
                  </select>
                  <Button type="submit" size="sm">
                    Изменить
                  </Button>
                </form>
              </Can>
              <Can permission="users:delete">
                <form action={deleteUser.bind(null, user.id)}>
                  <Button type="submit" variant="destructive" size="sm">
                    Удалить
                  </Button>
                </form>
              </Can>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

### 9. Server Action для смены роли с multi-role сценарием

```typescript
// src/actions/content.ts — пример multi-role проверки
"use server";

import { auth } from "@/lib/auth";
import { can } from "@/lib/permissions";
import { db } from "@/db";

export async function publishContent(contentId: string) {
  const session = await auth();
  if (!session?.user) return { error: "Unauthorized" };

  // Разные действия в зависимости от роли
  if (!can(session.user.role, "content:publish")) {
    // member может предложить к публикации, но не опубликовать
    if (can(session.user.role, "content:update")) {
      await db.update(content).set({ status: "pending_review" }).where(eq(content.id, contentId));
      return { success: true, status: "pending_review" };
    }
    return { error: "Insufficient permissions" };
  }

  await db.update(content).set({ status: "published", publishedAt: new Date() }).where(eq(content.id, contentId));
  return { success: true, status: "published" };
}
```

## Антипаттерн

```typescript
// ПЛОХО: Проверка роли только в UI
function AdminPanel() {
  const { data: session } = useSession();
  // Скрыть UI недостаточно — Server Action всё равно доступен
  if (session?.user?.role !== "admin") return null;
  return <button onClick={() => deleteUser(userId)}>Delete</button>;
}

// ПЛОХО: Использование роли из клиентского запроса
export async function dangerousAction(formData: FormData) {
  "use server";
  const role = formData.get("role"); // ← Клиент может передать любую роль!
  if (role === "admin") {
    await deleteAllUsers();
  }
}

// ПЛОХО: Хранение роли только в localStorage
// src/hooks/use-role.ts
export function useRole() {
  // localStorage легко модифицировать в DevTools
  return localStorage.getItem("userRole") ?? "viewer";
}

// ПЛОХО: if/else вместо матрицы разрешений
async function checkAccess(action: string, role: string) {
  if (action === "delete" && role === "admin") return true;
  if (action === "create" && (role === "admin" || role === "member")) return true;
  // ... разрастается в неуправляемый if-else лес
}
```

**Правила:**
1. Проверяй права на всех уровнях: middleware + Server Action + Server Component
2. Роль читай из JWT/сессии, никогда из тела запроса
3. Используй матрицу разрешений вместо if/else по ролям
4. Для сложных сценариев: проверяй ownership (userId совпадает) дополнительно к роли
5. При обновлении роли в БД — инвалидируй JWT (принудительный re-sign-in или short JWT TTL)

## Связанные документы

- `knowledge/custom/02-patterns/multi-tenancy.md` — RBAC в контексте организаций
- `knowledge/custom/02-patterns/payments.md` — проверка тарифного плана как часть авторизации
- `knowledge/custom/06-security/` — OWASP Broken Access Control

---
category: patterns
topic: error-handling
status: draft
---

## Проблема / Контекст

Обработка ошибок в Next.js 15 требует нескольких уровней: React Error Boundaries для клиентских ошибок, `error.tsx` файлы для сегментов маршрутов, глобальный `global-error.tsx`, типизированные результаты в Server Actions, и никогда не утекать серверные детали клиенту. Sentry нужен для observability — иначе ошибки в проде исчезают бесследно.

Типичные ошибки:
- Stack trace или SQL ошибки отправляются клиенту
- Server Action бросает необработанное исключение → 500 без контекста
- Отсутствие `error.tsx` → весь layout ломается из-за одного компонента
- Не-типизированные ошибки (`unknown` приводится к `any`)

## Решение

**Многоуровневая стратегия:**
1. `error.tsx` — ловит ошибки в сегменте маршрута, показывает UI с кнопкой retry
2. `global-error.tsx` — ловит ошибки в root layout
3. `not-found.tsx` — 404 страница через `notFound()`
4. Result pattern в Server Actions — типизированный `{ success, data, error }` вместо throw
5. Sentry — отправляет все ошибки в трекер
6. Custom error классы — структурированные ошибки с кодами
7. Toast уведомления — пользователь видит ошибку, не Stack trace

## Пример кода

### 1. Custom error классы

```typescript
// src/lib/errors.ts

// Базовый класс для всех приложенных ошибок
export class AppError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly statusCode: number = 500,
    public readonly isOperational: boolean = true // operational = ожидаемая ошибка
  ) {
    super(message);
    this.name = "AppError";
    // Важно для TypeScript: фиксируем prototype chain
    Object.setPrototypeOf(this, new.target.prototype);
  }
}

export class NotFoundError extends AppError {
  constructor(resource: string, id?: string) {
    super(
      id ? `${resource} with id '${id}' not found` : `${resource} not found`,
      "NOT_FOUND",
      404
    );
    this.name = "NotFoundError";
  }
}

export class UnauthorizedError extends AppError {
  constructor(message = "Authentication required") {
    super(message, "UNAUTHORIZED", 401);
    this.name = "UnauthorizedError";
  }
}

export class ForbiddenError extends AppError {
  constructor(message = "Insufficient permissions") {
    super(message, "FORBIDDEN", 403);
    this.name = "ForbiddenError";
  }
}

export class ValidationError extends AppError {
  constructor(
    message: string,
    public readonly fields?: Record<string, string[]>
  ) {
    super(message, "VALIDATION_ERROR", 422);
    this.name = "ValidationError";
  }
}

export class RateLimitError extends AppError {
  constructor(message = "Too many requests") {
    super(message, "RATE_LIMIT", 429);
    this.name = "RateLimitError";
  }
}

// Хелпер: безопасное сообщение для клиента
export function getClientSafeMessage(error: unknown): string {
  if (error instanceof AppError && error.isOperational) {
    return error.message;
  }
  // Никогда не отправляем детали неожиданных ошибок клиенту
  return "An unexpected error occurred. Please try again.";
}
```

### 2. Result pattern для Server Actions

```typescript
// src/lib/result.ts
// Типизированный Result — явная обработка успеха/ошибки без try/catch в каждом вызове

export type Result<T, E = string> =
  | { success: true; data: T }
  | { success: false; error: E; code?: string };

export function ok<T>(data: T): Result<T> {
  return { success: true, data };
}

export function err<T = never>(error: string, code?: string): Result<T> {
  return { success: false, error, code };
}

// Хелпер для выполнения async операций с автоматическим catch
export async function safeAction<T>(
  fn: () => Promise<T>
): Promise<Result<T>> {
  try {
    const data = await fn();
    return ok(data);
  } catch (error) {
    // Логируем серверную ошибку (Sentry, console)
    if (process.env.NODE_ENV !== "test") {
      console.error("[Server Action Error]:", error);
    }

    // Клиенту отдаём только безопасное сообщение
    const { getClientSafeMessage } = await import("./errors");
    const { AppError } = await import("./errors");

    return {
      success: false,
      error: getClientSafeMessage(error),
      code: error instanceof AppError ? error.code : "UNKNOWN",
    };
  }
}
```

### 3. Server Actions с Result pattern

```typescript
// src/actions/projects.ts
"use server";

import { auth } from "@/lib/auth";
import { db } from "@/db";
import { projects } from "@/db/schema/projects";
import { eq } from "drizzle-orm";
import { revalidatePath } from "next/cache";
import { z } from "zod";
import { ok, err, safeAction, type Result } from "@/lib/result";
import { UnauthorizedError, NotFoundError, ValidationError } from "@/lib/errors";
import * as Sentry from "@sentry/nextjs";

const createProjectSchema = z.object({
  name: z.string().min(1, "Name is required").max(100, "Name too long"),
  description: z.string().max(500).optional(),
});

// Полный Result — нет throws, всё явно
export async function createProject(
  formData: FormData
): Promise<Result<{ id: string; name: string }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return err("Authentication required", "UNAUTHORIZED");
  }

  const parsed = createProjectSchema.safeParse({
    name: formData.get("name"),
    description: formData.get("description"),
  });

  if (!parsed.success) {
    return err(parsed.error.errors[0]?.message ?? "Invalid input", "VALIDATION");
  }

  return safeAction(async () => {
    const [project] = await db
      .insert(projects)
      .values({ ...parsed.data, userId: session.user.id })
      .returning({ id: projects.id, name: projects.name });

    if (!project) throw new Error("Failed to create project");

    revalidatePath("/projects");
    return project;
  });
}

export async function deleteProject(
  projectId: string
): Promise<Result<void>> {
  const session = await auth();
  if (!session?.user?.id) {
    return err("Authentication required", "UNAUTHORIZED");
  }

  // Проверяем владельца
  const project = await db.query.projects.findFirst({
    where: eq(projects.id, projectId),
    columns: { userId: true },
  });

  if (!project) {
    return err("Project not found", "NOT_FOUND");
  }

  if (project.userId !== session.user.id) {
    // Логируем возможную IDOR попытку
    Sentry.captureMessage("Potential IDOR attempt", {
      level: "warning",
      extra: { userId: session.user.id, projectId },
    });
    return err("Access denied", "FORBIDDEN");
  }

  return safeAction(async () => {
    await db.delete(projects).where(eq(projects.id, projectId));
    revalidatePath("/projects");
  });
}
```

### 4. error.tsx — сегментные boundaries

```typescript
// src/app/(app)/error.tsx
"use client"; // Error boundaries ДОЛЖНЫ быть Client Components

import { useEffect } from "react";
import * as Sentry from "@sentry/nextjs";
import { Button } from "@/components/ui/button";
import { AlertCircle } from "lucide-react";

interface ErrorPageProps {
  error: Error & { digest?: string }; // digest — хэш ошибки от Next.js
  reset: () => void; // Попытка повторного рендера сегмента
}

export default function ErrorPage({ error, reset }: ErrorPageProps) {
  useEffect(() => {
    // Отправляем в Sentry при каждом рендере error boundary
    Sentry.captureException(error, {
      extra: { digest: error.digest },
    });
  }, [error]);

  return (
    <div className="flex min-h-[400px] flex-col items-center justify-center gap-4 p-8">
      <AlertCircle className="h-12 w-12 text-destructive" />
      <div className="text-center">
        <h2 className="text-xl font-semibold">Something went wrong</h2>
        <p className="mt-1 text-sm text-muted-foreground">
          {/* digest безопасно показывать — это хэш, не детали */}
          {error.digest ? `Error ID: ${error.digest}` : "An unexpected error occurred"}
        </p>
      </div>
      <div className="flex gap-3">
        <Button onClick={reset} variant="default">
          Try again
        </Button>
        <Button onClick={() => window.location.href = "/"} variant="outline">
          Go home
        </Button>
      </div>
    </div>
  );
}
```

### 5. global-error.tsx — ловит ошибки в root layout

```typescript
// src/app/global-error.tsx
"use client";

import { useEffect } from "react";
import * as Sentry from "@sentry/nextjs";

interface GlobalErrorProps {
  error: Error & { digest?: string };
  reset: () => void;
}

// global-error.tsx заменяет весь html — нужно самому добавить <html><body>
export default function GlobalError({ error, reset }: GlobalErrorProps) {
  useEffect(() => {
    Sentry.captureException(error);
  }, [error]);

  return (
    <html lang="en">
      <body>
        <div
          style={{
            display: "flex",
            minHeight: "100vh",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            gap: "16px",
            fontFamily: "sans-serif",
          }}
        >
          <h1 style={{ fontSize: "1.5rem", fontWeight: "bold" }}>
            Application Error
          </h1>
          <p style={{ color: "#666" }}>
            A critical error occurred. Our team has been notified.
          </p>
          {error.digest && (
            <code style={{ fontSize: "0.75rem", color: "#999" }}>
              {error.digest}
            </code>
          )}
          <button
            onClick={reset}
            style={{
              padding: "8px 16px",
              backgroundColor: "#000",
              color: "#fff",
              border: "none",
              borderRadius: "6px",
              cursor: "pointer",
            }}
          >
            Try again
          </button>
        </div>
      </body>
    </html>
  );
}
```

### 6. not-found.tsx

```typescript
// src/app/not-found.tsx
import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function NotFoundPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-4">
      <div className="text-center">
        <h1 className="text-6xl font-bold text-muted-foreground">404</h1>
        <h2 className="mt-2 text-2xl font-semibold">Page not found</h2>
        <p className="mt-1 text-muted-foreground">
          The page you're looking for doesn't exist or has been moved.
        </p>
      </div>
      <Button asChild>
        <Link href="/">Go home</Link>
      </Button>
    </div>
  );
}

// Использование notFound() в Server Components:
// src/app/(app)/projects/[id]/page.tsx
import { notFound } from "next/navigation";
import { db } from "@/db";

export default async function ProjectPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const project = await db.query.projects.findFirst({
    where: eq(projects.id, id),
  });

  if (!project) notFound(); // Редиректит на not-found.tsx

  return <div>{project.name}</div>;
}
```

### 7. Route Handler error responses

```typescript
// src/app/api/projects/route.ts
import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";
import { AppError, getClientSafeMessage } from "@/lib/errors";
import * as Sentry from "@sentry/nextjs";
import { z } from "zod";

// Хелпер для API ошибок — никогда не утекаем детали
function apiError(
  message: string,
  status: number,
  code?: string
): NextResponse {
  return NextResponse.json(
    { error: message, code: code ?? "UNKNOWN" },
    { status }
  );
}

// Декоратор для Route Handlers — автоматическая обработка ошибок
function withErrorHandler<T extends (...args: Parameters<T>) => Promise<NextResponse>>(
  handler: T
): T {
  return (async (...args: Parameters<T>) => {
    try {
      return await handler(...args);
    } catch (error) {
      // Логируем в Sentry
      if (!(error instanceof AppError) || !error.isOperational) {
        Sentry.captureException(error);
        console.error("[API Error]:", error);
      }

      if (error instanceof AppError) {
        return apiError(error.message, error.statusCode, error.code);
      }

      // Неожиданная ошибка — общее сообщение
      return apiError("Internal server error", 500, "INTERNAL");
    }
  }) as T;
}

export const GET = withErrorHandler(async (req: Request) => {
  const session = await auth();
  if (!session?.user?.id) {
    return apiError("Unauthorized", 401, "UNAUTHORIZED");
  }

  const projects = await db.query.projects.findMany({
    where: eq(projects.userId, session.user.id),
  });

  return NextResponse.json({ projects });
});
```

### 8. Sentry setup для Next.js

```typescript
// src/instrumentation.ts — Next.js 15 instrumentation hook
export async function register() {
  if (process.env.NEXT_RUNTIME === "nodejs") {
    await import("../sentry.server.config");
  }
  if (process.env.NEXT_RUNTIME === "edge") {
    await import("../sentry.edge.config");
  }
}

// sentry.client.config.ts
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: process.env.NODE_ENV === "production" ? 0.1 : 1.0,
  replaysOnErrorSampleRate: 1.0, // 100% сессий с ошибкой
  replaysSessionSampleRate: 0.05, // 5% обычных сессий
  integrations: [
    Sentry.replayIntegration({
      maskAllText: true, // GDPR: маскируем текст
      blockAllMedia: true,
    }),
  ],
});

// sentry.server.config.ts
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: process.env.NODE_ENV === "production" ? 0.05 : 1.0,
});
```

### 9. Toast уведомления для клиентских ошибок

```typescript
// src/hooks/use-action.ts
"use client";

import { useTransition } from "react";
import { toast } from "sonner";
import type { Result } from "@/lib/result";

// Хук для вызова Server Actions с автоматическими toast
export function useAction<TInput, TData>(
  action: (input: TInput) => Promise<Result<TData>>,
  options?: {
    onSuccess?: (data: TData) => void;
    successMessage?: string;
    onError?: (error: string) => void;
  }
) {
  const [isPending, startTransition] = useTransition();

  const execute = (input: TInput) => {
    startTransition(async () => {
      const result = await action(input);

      if (result.success) {
        if (options?.successMessage) {
          toast.success(options.successMessage);
        }
        options?.onSuccess?.(result.data);
      } else {
        // Показываем ошибку пользователю — это уже safe message
        toast.error(result.error);
        options?.onError?.(result.error);
      }
    });
  };

  return { execute, isPending };
}

// Использование:
// const { execute: deleteProject, isPending } = useAction(
//   (id: string) => deleteProjectAction(id),
//   {
//     successMessage: "Project deleted",
//     onSuccess: () => router.push("/projects"),
//   }
// );
```

## Антипаттерн

```typescript
// ПЛОХО: Утечка деталей ошибки клиенту
export async function badAction(formData: FormData) {
  "use server";
  try {
    await db.insert(projects).values({ ... });
  } catch (error) {
    // SQL ошибка отправляется клиенту — раскрывает структуру БД!
    return { error: error.message }; // "duplicate key value violates unique constraint..."
  }
}

// ПЛОХО: throw в Server Action без обработки
export async function throwingAction() {
  "use server";
  // Необработанное исключение → клиент получает 500 без полезной информации
  throw new Error("Database connection failed: postgres://user:password@host:5432/db");
}

// ПЛОХО: Игнорировать ошибки
export async function silentFail(id: string) {
  "use server";
  try {
    await riskyOperation(id);
  } catch (e) {
    // Ошибка проглочена — пользователь думает что всё OK, данные не сохранены
    console.log("error", e);
  }
  return { success: true }; // ← лжём!
}

// ПЛОХО: Нет error.tsx → одна сломанная страница ломает весь layout
// src/app/(app)/          ← нет error.tsx здесь
//   dashboard/page.tsx    ← если бросит ошибку, сломается весь (app) layout
```

**Правила:**
1. Server Action НИКОГДА не бросает — возвращает Result с error string
2. Серверные детали (SQL, stack trace, внутренние пути) никогда не покидают сервер
3. Добавляй `error.tsx` к каждому значимому route group
4. Все неожиданные ошибки логируй в Sentry ПЕРЕД возвратом safe message клиенту
5. `error.digest` безопасно показывать пользователю — это хэш, не детали

## Связанные документы

- `knowledge/custom/03-antipatterns/secrets-exposure.md` — утечка серверных данных
- `knowledge/custom/06-security/` — security logging
- `knowledge/custom/10-devops/` — Sentry в CI/CD

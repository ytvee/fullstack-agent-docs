---
category: devops
topic: railway-infra
status: draft
---

## Проблема / Контекст

Railway — платформа для деплоя инфраструктуры (PostgreSQL, Redis, сервисы) с простым интерфейсом и разумными ценами. Используется как backend-инфраструктура для Next.js приложения на Vercel: БД, кэш, очереди. Основные задачи: правильное подключение к Vercel через переменные окружения, настройка connection pooling через PgBouncer (критично для serverless/edge), резервное копирование, мониторинг.

Без connection pooling serverless-функции Vercel при пиковой нагрузке исчерпывают лимит connections PostgreSQL (обычно 100 для Railway), что приводит к ошибкам "too many clients".

## Решение

### Создание PostgreSQL на Railway

```bash
# Через Railway CLI
npm install -g @railway/cli
railway login

# Создать новый проект
railway init

# Добавить PostgreSQL
railway add --plugin postgresql

# Посмотреть переменные окружения
railway variables

# Открыть shell подключения к БД
railway connect postgresql
```

Railway автоматически создаёт следующие переменные:

```
DATABASE_URL=postgresql://postgres:password@containers-xyz.railway.app:5432/railway
PGDATABASE=railway
PGHOST=containers-xyz.railway.app
PGPASSWORD=password
PGPORT=5432
PGUSER=postgres
```

### Структура подключения в Drizzle

```typescript
// lib/db/index.ts
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "./schema";
import { env } from "@/lib/env";

// Pooled connection для обычных запросов
// max: количество connections в пуле
// idle_timeout: закрыть idle connections через N секунд
// connect_timeout: таймаут подключения
const pooledClient = postgres(env.DATABASE_URL, {
  max: 10,               // максимум connections в пуле
  idle_timeout: 30,      // закрыть неактивные через 30 сек
  connect_timeout: 10,   // таймаут подключения 10 сек
  prepare: false,        // отключить prepared statements для PgBouncer transaction mode
});

export const db = drizzle(pooledClient, {
  schema,
  logger: process.env.NODE_ENV === "development",
});

// Отдельный клиент для миграций (не через PgBouncer)
// Используй DATABASE_URL_UNPOOLED из Railway переменных
export const migrationClient = postgres(env.DATABASE_URL_UNPOOLED ?? env.DATABASE_URL, {
  max: 1,
});
```

### PgBouncer для connection pooling

Railway не предоставляет PgBouncer встроенно, но можно развернуть его как отдельный сервис. Альтернатива — использовать Supabase (встроенный PgBouncer) или Neon (встроенный HTTP-клиент). Для Railway рекомендуется Docker image pgbouncer:

```toml
# railway.toml для PgBouncer сервиса
[build]
dockerfilePath = "infrastructure/pgbouncer/Dockerfile"

[deploy]
startCommand = "pgbouncer /etc/pgbouncer/pgbouncer.ini"
restartPolicyType = "always"
```

```ini
# infrastructure/pgbouncer/pgbouncer.ini
[databases]
railway = host=containers-xyz.railway.app port=5432 dbname=railway

[pgbouncer]
listen_addr = *
listen_port = 6432
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction          ; transaction mode для serverless
max_client_conn = 1000           ; максимум клиентских подключений
default_pool_size = 20           ; connections к PostgreSQL
min_pool_size = 5
reserve_pool_size = 5
reserve_pool_timeout = 5.0
server_idle_timeout = 600
log_connections = 0
log_disconnections = 0
```

Для serverless Vercel с Drizzle используй connection string PgBouncer в `DATABASE_URL` и прямой PostgreSQL URL в `DATABASE_URL_UNPOOLED`.

### Redis для rate limiting и кэширования

```bash
# Добавить Redis в Railway проект
railway add --plugin redis

# Переменные Railway:
# REDIS_URL=redis://default:password@containers-xyz.railway.app:6379
```

```typescript
// lib/redis.ts — подключение Redis через Upstash SDK или ioredis
import { Redis } from "@upstash/redis";
// ИЛИ для Railway Redis используй ioredis:
import IORedis from "ioredis";

// Вариант 1: Upstash Redis (рекомендуется для Edge compatibility)
export const redis = new Redis({
  url: process.env.UPSTASH_REDIS_REST_URL!,
  token: process.env.UPSTASH_REDIS_REST_TOKEN!,
});

// Вариант 2: ioredis для Railway Redis (только Node.js runtime)
export const ioRedis = new IORedis(process.env.REDIS_URL!, {
  maxRetriesPerRequest: 3,
  enableReadyCheck: true,
  lazyConnect: false,
});

// Rate limiting с Railway Redis
import { Ratelimit } from "@upstash/ratelimit";

export const rateLimiter = new Ratelimit({
  redis,
  limiter: Ratelimit.slidingWindow(10, "10 s"), // 10 запросов за 10 секунд
  analytics: true,
  prefix: "ratelimit",
});
```

```typescript
// lib/rate-limit.ts — хелпер для использования в Route Handlers
import { rateLimiter } from "@/lib/redis";
import { headers } from "next/headers";

export async function checkRateLimit(identifier?: string): Promise<{
  success: boolean;
  remaining: number;
  reset: Date;
}> {
  const headersList = await headers();
  const ip =
    headersList.get("x-forwarded-for")?.split(",")[0]?.trim() ??
    headersList.get("x-real-ip") ??
    "anonymous";

  const id = identifier ?? ip;
  const { success, remaining, reset } = await rateLimiter.limit(id);

  return { success, remaining, reset: new Date(reset) };
}
```

### Переменные окружения в Railway

Railway поддерживает несколько способов управления переменными:

```bash
# CLI
railway variables set DATABASE_URL="postgresql://..."
railway variables set REDIS_URL="redis://..."

# Или через Railway Dashboard: Service → Variables

# Важно: Railway автоматически инжектирует переменные в runtime,
# не нужно их передавать явно в docker run
```

```typescript
// Использование Railway Shared Variables между сервисами
// В Railway Dashboard: Project → Shared Variables
// Переменная POSTGRES_PASSWORD может быть shared и доступна всем сервисам проекта
```

### Private Networking между сервисами

Railway предоставляет приватную сеть внутри проекта. Используй `.railway.internal` домены вместо публичных для внутрисервисного общения:

```bash
# Публичный URL (для внешнего доступа):
DATABASE_URL=postgresql://postgres:pass@containers-xyz.railway.app:5432/railway

# Private network URL (между сервисами в Railway):
DATABASE_PRIVATE_URL=postgresql://postgres:pass@postgres.railway.internal:5432/railway

# Преимущества private networking:
# - Быстрее (нет выхода в интернет)
# - Бесплатно (не тратит трафик)
# - Безопаснее (недоступно извне)
```

```typescript
// lib/db/index.ts — использование private URL в Railway
const databaseUrl =
  process.env.NODE_ENV === "production" && process.env.DATABASE_PRIVATE_URL
    ? process.env.DATABASE_PRIVATE_URL  // private networking внутри Railway
    : process.env.DATABASE_URL!;         // публичный URL (для локальной разработки)

const client = postgres(databaseUrl, { /* ... */ });
```

### Backups и Point-in-Time Recovery

Railway предоставляет автоматические бэкапы для PostgreSQL:

```bash
# Просмотреть доступные бэкапы
railway backups

# Создать ручной snapshot перед крупными изменениями
railway backup create --service postgresql

# Восстановить из бэкапа (через Dashboard или CLI)
# Railway Dashboard: PostgreSQL Service → Backups → Restore
```

```typescript
// scripts/backup-verify.ts — скрипт проверки целостности бэкапа
import postgres from "postgres";

async function verifyBackup(connectionString: string) {
  const client = postgres(connectionString, { max: 1 });

  try {
    // Проверяем, что основные таблицы существуют и доступны
    const tables = await client`
      SELECT tablename FROM pg_tables
      WHERE schemaname = 'public'
      ORDER BY tablename
    `;

    console.log("Tables found:", tables.map((t) => t.tablename));

    // Проверяем количество записей в ключевых таблицах
    const [userCount] = await client`SELECT COUNT(*) as count FROM users`;
    console.log("User count:", userCount.count);

    console.log("✅ Backup verification passed");
  } catch (error) {
    console.error("❌ Backup verification failed:", error);
    process.exit(1);
  } finally {
    await client.end();
  }
}

verifyBackup(process.env.BACKUP_DATABASE_URL!);
```

### Railway CLI для локальной разработки

```bash
# Установка
npm install -g @railway/cli

# Авторизация
railway login

# Привязка к проекту
railway link

# Запуск dev сервера с Railway переменными
railway run pnpm dev

# Или создай .env.railway для локальной работы с Railway DB:
railway variables --service postgresql > .env.railway
# Добавь .env.railway в .gitignore!
```

```bash
# .env.local — для локальной разработки (Docker или Railway tunnel)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/myapp_dev
REDIS_URL=redis://localhost:6379

# .env.railway — для разработки с Railway DB напрямую (не коммитить!)
DATABASE_URL=postgresql://postgres:realpass@containers-xyz.railway.app:5432/railway
```

### Подключение Railway к Vercel

Это ключевой шаг: добавить Railway DATABASE_URL как переменную окружения в Vercel.

```bash
# 1. Получить DATABASE_URL из Railway
railway variables --service postgresql

# 2. Добавить в Vercel
vercel env add DATABASE_URL production
# paste: postgresql://postgres:password@containers-xyz.railway.app:5432/railway

vercel env add DATABASE_URL preview
# paste: тот же URL или staging БД

# 3. Для PgBouncer (если настроен):
vercel env add DATABASE_URL production
# paste: postgresql://postgres:password@pgbouncer.railway.internal:6432/railway

vercel env add DATABASE_URL_UNPOOLED production
# paste: прямой URL к PostgreSQL (для миграций)
```

```typescript
// drizzle.config.ts — конфигурация для миграций
import type { Config } from "drizzle-kit";
import { env } from "@/lib/env";

export default {
  schema: "./lib/db/schema/index.ts",
  out: "./lib/db/migrations",
  dialect: "postgresql",
  dbCredentials: {
    // Используем UNPOOLED для миграций (PgBouncer не поддерживает DDL)
    url: process.env.DATABASE_URL_UNPOOLED ?? process.env.DATABASE_URL!,
  },
  verbose: true,
  strict: true,
} satisfies Config;
```

### Cost Optimization Tips

```bash
# 1. Выбор правильного плана Railway
# Hobby Plan: $5/месяц — хватит для старта
# Pro Plan: $20/месяц — для продакшна с командой

# 2. Sleep неактивных сервисов
# Railway Dashboard: Service Settings → Pause Service when inactive
# Подходит для staging/preview окружений

# 3. Resource limits
# Railway Dashboard: Service → Settings → Resource Limits
# CPU: 0.5 vCPU для небольших сервисов
# Memory: 256MB для Redis, 512MB для PostgreSQL (небольшие БД)

# 4. Мониторинг использования
railway metrics

# 5. Оптимизация PostgreSQL для Railway
# shared_buffers = 128MB (default 25% RAM)
# effective_cache_size = 256MB
# max_connections = 100 (уменьши если используешь PgBouncer)
```

```sql
-- Проверка активных connections в PostgreSQL
SELECT count(*), state, client_addr
FROM pg_stat_activity
WHERE datname = 'railway'
GROUP BY state, client_addr
ORDER BY count DESC;

-- Найти медленные запросы (включи pg_stat_statements)
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

## Пример кода

### Health check endpoint для Railway + Vercel

```typescript
// app/api/health/route.ts
import { NextResponse } from "next/server";
import { db } from "@/lib/db";
import { sql } from "drizzle-orm";

export async function GET() {
  const checks: Record<string, "ok" | "error"> = {};

  // Проверка PostgreSQL
  try {
    await db.execute(sql`SELECT 1`);
    checks.database = "ok";
  } catch {
    checks.database = "error";
  }

  // Проверка Redis (если используется)
  try {
    // await redis.ping();
    checks.redis = "ok";
  } catch {
    checks.redis = "error";
  }

  const allHealthy = Object.values(checks).every((v) => v === "ok");
  const status = allHealthy ? 200 : 503;

  return NextResponse.json(
    {
      status: allHealthy ? "healthy" : "degraded",
      checks,
      timestamp: new Date().toISOString(),
      version: process.env.VERCEL_GIT_COMMIT_SHA?.slice(0, 7) ?? "local",
    },
    { status }
  );
}
```

## Антипаттерн

```typescript
// ПЛОХО: хардкодить connection string
const client = postgres("postgresql://postgres:secret@host/db");

// ПЛОХО: использовать публичный URL для внутренних сервисов Railway
// Использует интернет-трафик и медленнее
const url = process.env.DATABASE_URL; // containers-xyz.railway.app
// ХОРОШО:
const url = process.env.DATABASE_PRIVATE_URL; // postgres.railway.internal

// ПЛОХО: запускать миграции через pooled connection (PgBouncer)
// PgBouncer в transaction mode не поддерживает DDL транзакции
// ХОРОШО: всегда миграции через DATABASE_URL_UNPOOLED

// ПЛОХО: не ограничивать max connections в postgres.js
const client = postgres(url); // создаст 10 connections по умолчанию × N serverless instances
// ХОРОШО:
const client = postgres(url, { max: 3, prepare: false }); // явный лимит
```

## Связанные документы

- `knowledge/custom/10-devops/vercel-deploy.md` — подключение Railway к Vercel через env vars
- `knowledge/custom/10-devops/github-actions-ci.md` — автоматические миграции в CI/CD
- `knowledge/custom/06-security/` — управление секретами

# fullstack-agent-docs

RAG knowledge base для AI-агента, который пишет fullstack-приложения на Next.js любой сложности.

## Назначение

Агент получает задачу (например, *"сделай SaaS с auth, платежами и дашбордом"*), проектирует архитектуру и пишет весь код по best practices — используя эту базу знаний как источник актуальной документации и проверенных паттернов.

---

## Зафиксированный стек

| Слой | Инструмент |
|---|---|
| Framework | Next.js 15+ App Router, React 19, TypeScript strict |
| Styling | Tailwind CSS v4 + shadcn/ui |
| Database | **Drizzle ORM** (основной) / Prisma 7 (альтернатива) |
| Auth | **Auth.js v5** (основной) / Better Auth (альтернатива) |
| State | Zustand (только UI state) |
| Validation | Zod + React Hook Form |
| Payments | Stripe |
| Email | Resend |
| Upload | UploadThing |
| Testing | Vitest + Playwright + MSW |
| Deploy | Vercel (Next.js) / Railway (БД, сервисы) |
| Monitoring | Sentry + Vercel Analytics |
| AI | Vercel AI SDK |

> **Важно:** TanStack Query не используется. State management — Zustand + Server Actions + нативный fetch.

---

## Структура репозитория

```
knowledge-base/
│
├── knowledge/
│   ├── official/          ← Layer A: официальная документация (авто-скачивается)
│   │   ├── framework/     # Next.js, React, TypeScript
│   │   ├── stack/         # Drizzle, Auth.js, Tailwind, shadcn, Stripe, etc.
│   │   ├── testing/       # Vitest, Playwright, MSW
│   │   └── devops/        # Vercel, Sentry
│   │
│   └── custom/            ← Layer B: кураторские документы (пишутся вручную)
│       ├── 01-architecture/  # Структура проекта, роутинг, data flow
│       ├── 02-patterns/      # Auth, CRUD, оплаты, загрузка файлов, i18n
│       ├── 03-antipatterns/  # Что нельзя делать и почему
│       ├── 04-linting/       # ESLint, commitlint
│       ├── 05-testing/       # Стратегия тестирования, coverage
│       ├── 06-security/      # OWASP, Server Actions, Auth security
│       ├── 07-performance/   # CWV, bundle, DB queries
│       ├── 08-accessibility/ # WCAG, ARIA
│       ├── 09-seo/           # Metadata API, structured data, sitemap, GEO/AEO
│       ├── 10-devops/        # Vercel deploy, Railway, GitHub Actions
│       └── 11-agent-rules/   # Правила для агента: чеклисты, шаблоны, деревья решений
│
├── scripts/
│   ├── fetch_docs.py      ← Скрипт загрузки Layer A
│   ├── sources.yaml       ← Реестр официальных источников
│   └── requirements.txt
│
├── .hashes.json           ← Автоматически: отслеживает изменения контента
└── README.md
```

---

## Layer A: Официальная документация

Автоматически скачивается из `llms-full.txt` (или `llms.txt`) официальных сайтов.

### Быстрый старт

```bash
cd scripts
pip install -r requirements.txt

# Скачать всё
python fetch_docs.py

# Скачать только один источник
python fetch_docs.py --source nextjs

# Скачать целую категорию
python fetch_docs.py --category framework

# Принудительно пересобрать (игнорировать хэши)
python fetch_docs.py --force

# Посмотреть что изменилось, не скачивая
python fetch_docs.py --dry-run

# Список всех источников
python fetch_docs.py --list
```

### Как работает скрипт

1. Читает `sources.yaml` — реестр всех источников
2. Для каждого источника скачивает контент по `url`
3. Если тип `llms-index` — обходит все страницы из индекса
4. Добавляет YAML frontmatter с метаданными (источник, хэш, дата)
5. Сохраняет в `knowledge/official/{category}/{key}.md`
6. Записывает SHA-256 хэши в `.hashes.json`
7. При повторном запуске пересобирает **только изменившееся**

### Как добавить новый источник

1. Открой `scripts/sources.yaml`
2. Добавь запись по образцу:

```yaml
my-library:
  name: "My Library"
  url: "https://my-library.dev/llms-full.txt"
  category: stack          # framework | stack | testing | devops
  output: knowledge/official/stack/my-library.md
  type: llms-full          # llms-full | llms-index
  priority: medium         # high | medium | low
  tags: [tag1, tag2]
```

3. Запусти `python fetch_docs.py --source my-library`

---

## Layer B: Кураторские документы

Написаны вручную на основе экспертных знаний о стеке. Содержат:
- Проверенные паттерны реализации
- Примеры кода (TypeScript strict, App Router only)
- Антипаттерны и их исправления
- Правила для агента

### Структура файла Layer B

```markdown
---
category: patterns
topic: auth-flow
status: draft | review | stable
---

## Проблема / Контекст
Что и зачем.

## Решение
Как правильно.

## Пример кода
\`\`\`typescript
// реальный TypeScript код
\`\`\`

## Антипаттерн
Как делать не надо (если применимо).

## Связанные документы
- [другой документ](../path/to/doc.md)
```

### Статусы документов

| Статус | Значение |
|---|---|
| `draft` | Черновик, требует проверки |
| `review` | На ревью |
| `stable` | Проверено, можно использовать |

---

## Правила для агента

Ключевые ограничения, которые агент **всегда** соблюдает:

- **App Router only** — никакого Pages Router в примерах
- **TypeScript strict** — `any` запрещён, все типы явные
- **Drizzle ORM** — основной ORM; Prisma только если явно указано
- **Auth.js v5** — основной auth; Better Auth только если явно указано
- **Zustand** — только для UI state; данные сервера через Server Actions
- **Vercel** — деплой Next.js приложений
- **Railway** — вся инфраструктура: PostgreSQL, Redis, сервисы
- **Zod** — валидация везде: клиент + сервер
- Перед мутацией данных — всегда проверка авторизации
- Server Actions — всегда с Zod-валидацией на сервере

---

## Обновление документации

```bash
# Обновить всё (только изменившееся)
python scripts/fetch_docs.py

# Проверить что устарело (без скачивания)
python scripts/fetch_docs.py --dry-run

# Принудительно обновить критические источники
python scripts/fetch_docs.py --category framework --force
```

Рекомендуется запускать `fetch_docs.py` еженедельно или перед началом работы над новым проектом.

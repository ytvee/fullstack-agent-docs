# AGENTS + Skills

Техническое описание содержимого репозитория.

## 1. Что есть в репозитории

Текущие скиллы структурно созданы для агентов Codex. Если использовать для других моделей/сервисов, их необходимо реструктурировать и адаптировать `AGENTS.md`.

## 2. Структура

```text
.
├── AGENTS.md
├── README.md
├── .gitignore
├── .codex
└── .agents/
    ├── project/
    │   ├── anti-patterns.md
    │   ├── architecture-map.md
    │   ├── figma-profile.md
    │   ├── stack-profile.md
    │   ├── styling-profile.md
    │   └── verification-profile.md
    └── skills/
        ├── frontend-review-and-fix/
        ├── frontend-security-inspector/
        ├── frontend-typescript-rules/
        ├── frontend-zod-schema/
        ├── nextjs-app-router/
        ├── project-context-adapter/
        ├── react-component-workflow/
        ├── technical-seo-app/
        └── webapp-task-protocol/
```

Логика структуры:

- `AGENTS.md` задает правила работы для конкретного репозитория
- `.agents/skills/` хранит универсальные workflow-навыки
- `.agents/project/` хранит профиль конкретного проекта

## 3. Стек, на который рассчитаны skills

Сами skills ориентированы на React и Next.js проекты.

Текущий профиль, зашитый в `AGENTS.md` и `.agents/project/*`, описывает такой
целевой стек:

- Next.js `16.2.1`
- App Router
- React `19`
- TypeScript со `strict: true`
- ESLint flat config
- Prettier
- Zod
- CSS Modules
- global token CSS
- MDX через `gray-matter` и `next-mdx-remote`
- без отдельного test runner

Профиль проекта редактируется непосредственно после интеграции скиллов в проект и перед их использованием.

## 4. Skills

Каждый skill лежит в своей папке и начинается с `SKILL.md`. Внутри некоторых
skills есть `references/` с дополнительными правилами.

### 4.1 Основные skills


| Skill                       | Стек / зона                  | Режим                      | Назначение                                                                                                                                                                                                                           |
| --------------------------- | ------------------------------------ | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webapp-task-protocol`      | React и Next.js                     | базовый                  | Классифицирует задачу, определяет проект как`frontend-only` или `fullstack`, выбирает цепочку skills и навязывает порядок `inspect -> plan -> implement -> verify`. |
| `nextjs-app-router`         | Next.js App Router                   | базовый                  | Для`page.tsx`, `layout.tsx`, metadata, dynamic segments, route-level states, server/client boundaries и Figma-driven страниц внутри Next.js.                                                                                  |
| `react-component-workflow`  | React компоненты           | базовый                  | Для декомпозиции компонентов,`props`, `state`, `hooks`, rendering logic и компонентного UI, если задача не про роутинг.                                                          |
| `frontend-typescript-rules` | TypeScript в React/Next.js          | cross-cutting                   | Для strict typing,`import type`, safe refactor, exported API typing и запрета на `any` / `@ts-ignore`.                                                                                                                            |
| `frontend-zod-schema`       | Zod на границах ввода | cross-cutting                   | Для search params, forms, config parsing и payload validation.                                                                                                                                                                             |
| `frontend-review-and-fix`   | Проверка изменений  | финальный проход | Для review после реализации, поиска регрессий, smell'ов и запуска verification steps.                                                                                                               |

### 4.2 Manual-only skills


| Skill                         | Стек / зона               | Режим                  | Назначение                                                                                                                                           |
| ----------------------------- | --------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `technical-seo-app`           | React и Next.js SEO              | только вручную | Для аудита metadata, canonical, robots, sitemap, Open Graph, structured data и crawlability.                                                         |
| `frontend-security-inspector` | React и Next.js security         | только вручную | Для security-аудита public entry points, client/server boundaries, secrets exposure и unsafe data handling.                                          |
| `project-context-adapter`     | Обновление overlay docs | только вручную | Для пересборки`.agents/project/*` под фактический проект без переписывания универсальных skills. |

### 4.3 Что делает каждый skill

#### `webapp-task-protocol`

Папка: `.agents/skills/webapp-task-protocol/`

Содержимое:

- `SKILL.md`
- `references/classification-rules.md`
- `references/task-routing.md`

Роль:

- не пишет код сам по себе
- выбирает дальнейший workflow
- решает, какой domain skill нужен дальше
- подключает cross-cutting skills по ситуации

#### `nextjs-app-router`

Папка: `.agents/skills/nextjs-app-router/`

Содержимое:

- `SKILL.md`
- `references/route-patterns.md`
- `references/server-client-boundaries.md`
- `references/metadata-patterns.md`
- `references/anti-patterns.md`
- `references/figma-implementation.md`

Роль:

- держит route files тонкими
- выносит логику из special files в helpers и feature modules
- навязывает server-first подход, если нет причины для client code
- использует Figma только через built-in capabilities и local project profile

#### `react-component-workflow`

Папка: `.agents/skills/react-component-workflow/`

Содержимое:

- `SKILL.md`
- `references/component-patterns.md`
- `references/hooks-rules.md`
- `references/anti-patterns.md`
- `references/figma-implementation.md`

Роль:

- контролирует декомпозицию компонентов
- следит за потоком данных через `props`
- ограничивает бессмысленные `useEffect`
- отделяет orchestration от presentational logic

#### `frontend-typescript-rules`

Папка: `.agents/skills/frontend-typescript-rules/`

Содержимое:

- `SKILL.md`
- `references/ts-rules.md`
- `references/typing-patterns.md`
- `references/anti-patterns.md`

Роль:

- удерживает strict TypeScript
- не дает размывать типы
- фиксирует правила для экспортируемых API и refactor-safe typing

#### `frontend-zod-schema`

Папка: `.agents/skills/frontend-zod-schema/`

Содержимое:

- `SKILL.md`
- `references/schema-patterns.md`
- `references/boundary-validation.md`

Роль:

- валидирует внешние и пользовательские данные на входе
- держит schema и inferred type рядом
- навязывает нормализацию на boundary, а не глубоко в коде

#### `frontend-review-and-fix`

Папка: `.agents/skills/frontend-review-and-fix/`

Содержимое:

- `SKILL.md`
- `references/review-checklist.md`
- `references/verification-steps.md`

Роль:

- финальный review pass
- поиск регрессий после основной реализации
- запуск релевантных checks из project profile

#### `technical-seo-app`

Папка: `.agents/skills/technical-seo-app/`

Содержимое:

- `SKILL.md`
- `references/metadata-rules.md`
- `references/crawling-indexing.md`
- `references/structured-data.md`

Роль:

- точечный SEO-аудит
- не должен запускаться автоматически
- fixes применяются только по явному запросу

#### `frontend-security-inspector`

Папка: `.agents/skills/frontend-security-inspector/`

Содержимое:

- `SKILL.md`
- `references/security-checklist-next.md`
- `references/security-checklist-react.md`
- `references/reporting-template.md`
- `assets/audit-report-template.md`

Роль:

- ручной security review
- построение findings report
- без неявного запуска в обычном feature workflow

#### `project-context-adapter`

Папка: `.agents/skills/project-context-adapter/`

Содержимое:

- `SKILL.md`
- `references/sync-procedure.md`
- `references/extraction-checklist.md`

Роль:

- пересобирает `.agents/project/*`
- читает конфиги и структуру фактического проекта
- не должен вшивать repo-specific правду в универсальные skills

## 5. `AGENTS.md`

`AGENTS.md` в этом репозитории уже заполнен и задает текущий профиль работы.

Сейчас в нем зафиксировано:

- порядок чтения контекста: `AGENTS.md -> .agents/project/* -> source files`
- дефолтная классификация проекта: `frontend-only`
- карта skills
- stack snapshot
- validation commands
- dev workflow

Текущий `AGENTS.md` описывает content-driven Next.js приложение, а не содержимое
этого репозитория как кодовой базы. Это repo-level entrypoint, который надо
переопределять под фактический проект после переноса.

## 6. Файлы в `.agents/project/`

`.agents/project/` содержит не общие инструкции, а профиль конкретного проекта.

В текущем репозитории там лежат такие файлы:


| Файл                  | Что описывает                                                                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `stack-profile.md`        | Целевой стек, тип проекта, tooling, MDX/data слой и способ проверки.                                                                         |
| `architecture-map.md`     | Структуру приложения:`src/app`, shared UI, feature queries, `src/lib`, data flow и правила размещения логики.                             |
| `styling-profile.md`      | CSS Modules как основной styling system, global tokens и ограничения на смену стека стилей.                                                 |
| `verification-profile.md` | Порядок запусков`tsc`, `eslint`, `prettier`, `next build` и оговорку про отсутствие test runner.                                                |
| `anti-patterns.md`        | Локальные запреты: Tailwind в CSS Modules областях, логика в route files, ненужный client conversion,`any`, hardcoded Figma values и т.д. |
| `figma-profile.md`        | Как использовать built-in Figma capabilities и как переносить дизайн в существующую token/layout систему.                     |

Важно: эти файлы сейчас уже заполнены под один конкретный профиль Next.js
проекта. В другом репозитории их нужно переписать под реальные факты.

## 7. Как адаптировать репозиторий под другой проект

### 7.1 Что копировать

В другой репозиторий переносятся:

- `AGENTS.md`
- вся папка `.agents/skills/`
- вся папка `.agents/project/`

### 7.2 Что менять обязательно

После переноса нужно обновить:

- `AGENTS.md`
- `.agents/project/stack-profile.md`
- `.agents/project/architecture-map.md`
- `.agents/project/styling-profile.md`
- `.agents/project/verification-profile.md`
- `.agents/project/anti-patterns.md`
- `.agents/project/figma-profile.md`

### 7.3 Что обычно не трогать

Папку `.agents/skills/` не нужно переписывать под каждый новый проект, если:

- не меняется сам workflow
- не меняется логика выбора задач
- не нужны новые универсальные правила

Skills должны оставаться общими. Проектная правда должна жить в
`.agents/project/*`.

### 7.4 Как обновлять project overlay

Есть два варианта:

1. Обновить `.agents/project/*` вручную.
2. Использовать `project-context-adapter`.

Если использовать агент, рабочий запрос может быть таким:

```text
адаптируй навыки под текущий проект
```

или:

```text
обнови .agents/project под этот репозиторий
```

Ожидаемый результат:

- агент читает `package.json`, `tsconfig.json`, ESLint, Prettier, route tree,
  styling system и структуру компонентов
- обновляет только `.agents/project/*`
- не переписывает core skills без отдельной причины

### 7.5 Что проверить после адаптации

После переноса стоит проверить:

- что `.gitignore` не исключает `AGENTS.md` и `.agents/`
- что manual-only skills действительно не вызываются неявно
- что `AGENTS.md` совпадает с фактическим стеком
- что `.agents/project/*` описывает реальную структуру проекта, а не шаблон

## 8. Оставшиеся файлы

### `README.md`

Этот файл описывает состав репозитория и порядок его адаптации.

### `.gitignore`

Сейчас в `.gitignore` исключены:

- `.DS_Store`
- `.cache`
- `.idea`
- `.codex`
- `.vscode`
- `logs`
- `*.log`
- `.npm`

### `.codex`

Сейчас это пустой файл. Он присутствует в корне репозитория, но также добавлен
в `.gitignore`.

### `.git/`

Обычный Git-метакаталог репозитория.

## 9. Usage

Ниже практический порядок использования всего репозитория после переноса в
рабочий проект.

### 9.1 Базовый порядок

1. Агент читает `AGENTS.md`.
2. Агент читает релевантные файлы из `.agents/project/`.
3. Агент выбирает skill.
4. Агент читает код и конфиги.
5. Агент делает изменения.
6. Агент заканчивает работу verification pass.

### 9.2 Обычная feature-задача

Ожидаемая цепочка:

1. `webapp-task-protocol`
2. `nextjs-app-router` или `react-component-workflow`
3. `frontend-typescript-rules`
4. `frontend-zod-schema`, если на границе есть внешний ввод
5. `frontend-review-and-fix`

### 9.3 Задача по Next.js роутингу

Используется, если меняются:

- `page.tsx`
- `layout.tsx`
- metadata
- dynamic routes
- server/client boundaries

Ожидаемый skill:

1. `nextjs-app-router`

### 9.4 Задача по React-компонентам

Используется, если меняются:

- композиция компонентов
- `props`
- `state`
- hooks
- rendering logic

Ожидаемый skill:

1. `react-component-workflow`

### 9.5 Задача по типам

Используется, если затронуты:

- exported types
- helpers
- component props
- safe refactor

Ожидаемый skill:

1. `frontend-typescript-rules`

### 9.6 Задача по boundary validation

Используется, если затронуты:

- forms
- search params
- config parsing
- payload validation

Ожидаемый skill:

1. `frontend-zod-schema`

### 9.7 Финальная проверка

После реализации используется:

1. `frontend-review-and-fix`

### 9.8 Ручные сценарии

SEO:

1. `technical-seo-app`

Security:

1. `frontend-security-inspector`

Обновление project overlay:

1. `project-context-adapter`

### 9.9 Работа с Figma

Если задача начинается с Figma URL или node reference:

1. сначала использовать built-in Figma capabilities
2. потом читать `.agents/project/figma-profile.md`
3. потом адаптировать дизайн к текущему проекту

Figma не должна обходить текущую styling system и project profile.

## 10. Короткая сводка

Если коротко, то в этом репозитории есть:

- один repo-level entrypoint: `AGENTS.md`
- девять skills в `.agents/skills/`
- шесть project overlay docs в `.agents/project/`
- README с описанием структуры и usage

Сам репозиторий кода приложения не содержит. Он хранит только агентную
конфигурацию, которую нужно переносить и адаптировать под конкретный проект.

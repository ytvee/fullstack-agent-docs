# AGENTS + Skills README

Это пользовательская инструкция для системы локальных навыков Codex.

Документ описывает:

- как устроена система `AGENTS.md` + `.agents/`
- за что отвечает каждый skill
- как перенести эту систему в любой React или Next.js проект
- как адаптировать ее под новый репозиторий

## 1. Из чего состоит система

Система делится на 3 слоя:

1. `AGENTS.md`
   Это entrypoint для конкретного репозитория.
   Он задает:
    - общий workflow
    - тип проекта
    - quality gates
    - карту skills
    - общие правила по стилю и разработке

2. `.agents/skills/`
   Это библиотека переиспользуемых skills.
   Они должны быть универсальными и не содержать привязки к конкретному проекту.

3. `.agents/project/`
   Это project overlay.
   Здесь лежит фактическая информация о текущем репозитории:
    - какой стек используется
    - как устроены маршруты и структура кода
    - как устроены стили
    - какие есть локальные анти-паттерны
    - какие проверки запускать
    - как адаптировать реализацию из Figma к текущему проекту

Коротко:

- `AGENTS.md` отвечает на вопрос: «как работать в этом репо»
- `.agents/skills/` отвечает на вопрос: «как выполнять конкретный тип задачи»
- `.agents/project/` отвечает на вопрос: «что именно является правдой в этом проекте»

## 2. Как работает система в рантайме

Ожидаемый порядок работы агента:

1. Сначала прочитать `AGENTS.md`
2. Затем выбрать нужный skill из `.agents/skills/`
3. Затем дочитать нужные overlay-документы из `.agents/project/`
4. Затем читать код и вносить изменения

Это важно:

- core-skills не должны хранить проектные детали
- проектные детали должны жить в `.agents/project/`
- при переносе системы в другой репозиторий core-skills не переписываются под новый проект
- под новый проект обновляется только `AGENTS.md` и `.agents/project/*`

## 3. Какие skills входят в систему

### `webapp-task-protocol`

Главный skill-маршрутизатор.

Его задача:

- понять тип задачи: `feature`, `refactor`, `bugfix`, `review`, `audit`
- понять стек: React или Next.js
- понять тип проекта: `frontend-only` или `fullstack`
- выбрать правильную цепочку skills
- навязать порядок `inspect -> plan -> implement -> verify`

Это не skill для написания кода.
Это skill для выбора следующего workflow.

### `nextjs-app-router`

Domain-skill для Next.js App Router.

Его зона:

- `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`
- dynamic segments
- metadata
- server/client boundaries
- route-level states
- реализация UI по Figma внутри Next.js проекта

Он не должен хранить проектные соглашения одного конкретного репо.
Все repo-specific правила он берет из `.agents/project/*`.

### `react-component-workflow`

Domain-skill для React-компонентов.

Его зона:

- decomposition
- props/state flow
- hooks discipline
- rendering logic
- presentational vs orchestration split
- реализация компонентов по Figma, если задача не про роутинг

### `frontend-typescript-rules`

Cross-cutting skill для TypeScript.

Его зона:

- strict TS
- `import type`
- запрет на `any`
- safe refactors
- exported API typing
- type narrowing

### `frontend-zod-schema`

Cross-cutting skill для валидации границ.

Его зона:

- search params
- forms
- config parsing
- payload validation
- schema-driven typing

### `frontend-review-and-fix`

Финальный review skill.

Его задача:

- проверить изменения после реализации
- найти регрессии и smell’ы
- прогнать verification workflow
- сделать точечные follow-up исправления

### `technical-seo-app`

Ручной skill для технического SEO.

Важно:

- он не должен вызываться автоматически
- он должен запускаться только по явному запросу пользователя

Его зона:

- titles / descriptions
- canonical
- robots / sitemap
- crawlability / indexability
- Open Graph
- structured data

### `frontend-security-inspector`

Ручной skill для security-аудита.

Важно:

- он не должен вызываться автоматически
- он должен запускаться только по явному запросу пользователя

Его зона:

- public entry points
- secrets exposure
- client/server boundary mistakes
- unsafe data handling
- auth/session related risks

### `project-context-adapter`

Ручной maintenance-skill.

Он нужен для команды вроде:

- «адаптируй навыки под текущий проект»
- «обнови overlay docs после рефактора»
- «пересобери project profile»

Этот skill:

- анализирует фактический проект
- обновляет только `.agents/project/*.md`
- не переписывает core-skills

## 4. Какие skills запускаются автоматически, а какие вручную

### Автоматические / implicit

- `webapp-task-protocol`
- `nextjs-app-router`
- `react-component-workflow`
- `frontend-typescript-rules`
- `frontend-zod-schema`
- `frontend-review-and-fix`

### Только вручную / manual only

- `technical-seo-app`
- `frontend-security-inspector`
- `project-context-adapter`

Практический смысл:

- feature work не должен внезапно превращаться в SEO-аудит
- обычная реализация не должна внезапно запускать security-inspection
- адаптация навыков под проект должна происходить осознанно, а не “сама собой”

## 5. Как ставить эту систему в любой проект

Ниже базовый способ установки в новый React/Next проект.

### Шаг 1. Скопировать файлы

Перенесите в новый репозиторий:

- `AGENTS.md`
- всю папку `.agents/skills/`
- шаблонную папку `.agents/project/`

Если вы выносите систему в отдельный repo-шаблон, структура может выглядеть так:

```text
AGENTS.md
.agents/
  skills/
  project/
```

### Шаг 2. Проверить `.gitignore`

Убедитесь, что новый репозиторий не игнорирует:

- `AGENTS.md`
- `.agents/`

Если эти пути игнорируются, агентная система не попадет в Git и не будет
нормально распространяться по проектам.

### Шаг 3. Настроить `AGENTS.md` под новый репозиторий

В `AGENTS.md` нужно обновить:

- stack snapshot
- project classification по умолчанию
- quality gates
- skill map при необходимости
- dev workflow

Важно:

- `AGENTS.md` должен оставаться коротким
- не превращайте его в энциклопедию
- детали проекта выносите в `.agents/project/*`

### Шаг 4. Заполнить `.agents/project/*`

Минимально нужно обновить:

- `stack-profile.md`
- `architecture-map.md`
- `styling-profile.md`
- `verification-profile.md`
- `anti-patterns.md`
- `figma-profile.md`

Есть два варианта:

1. Заполнить вручную
2. Использовать `project-context-adapter`

Рекомендуемый вариант:

- сначала положить шаблонные файлы
- потом вручную запустить `project-context-adapter`

### Шаг 5. Запустить адаптацию под проект

После переноса в новый репозиторий дайте агенту явную команду:

`адаптируй навыки под текущий проект`

или

`обнови .agents/project под этот репозиторий`

Ожидаемое поведение:

- агент читает `package.json`, `tsconfig.json`, ESLint, Prettier, route tree, styling
- обновляет `.agents/project/*`
- не трогает core-skills

### Шаг 6. Проверить ручные skills

Убедитесь, что в `agents/openai.yaml` для следующих skills стоит manual-only режим:

- `technical-seo-app`
- `frontend-security-inspector`
- `project-context-adapter`

То есть:

```yaml
policy:
    allow_implicit_invocation: false
```

## 6. Как использовать систему в новом проекте

### Сценарий: “добавь страницу” / “сделай фичу”

Ожидаемая цепочка:

1. `webapp-task-protocol`
2. `nextjs-app-router` или `react-component-workflow`
3. `frontend-typescript-rules`
4. `frontend-zod-schema`, если есть boundary input
5. `frontend-review-and-fix`

### Сценарий: “проверь SEO”

Ожидаемая цепочка:

1. `technical-seo-app`

### Сценарий: “проверь безопасность”

Ожидаемая цепочка:

1. `frontend-security-inspector`

### Сценарий: “адаптируй навыки под проект”

Ожидаемая цепочка:

1. `project-context-adapter`

## 7. Как работать с Figma

В этой системе нет локального Figma-skill.

Figma работает так:

1. Пользователь дает Figma URL
2. `webapp-task-protocol` или domain-skill понимает, что задача дизайн-driven
3. Агент сначала использует встроенные Figma capabilities
4. Потом читает `.agents/project/figma-profile.md`
5. Потом реализует интерфейс под текущую дизайн-систему и breakpoints

Важно:

- не хардкодить дизайн поверх существующей системы токенов
- сначала переиспользовать текущие компоненты и переменные
- если нужен новый reusable token или паттерн, добавлять его осознанно

## 8. Что не должно входить в core-skills

В универсальные skills не нужно зашивать:

- имя проекта
- локальные пути одного конкретного репозитория
- content-authoring workflow
- frontmatter конкретного блога
- CMS-specific правила
- feature directory contract одного проекта

Все это должно лежать:

- либо в `.agents/project/*`
- либо в runtime-коде проекта
- либо в user-facing docs проекта

## 9. Что делать с контентом и frontmatter

Если в проекте есть блог, документация или MDX-контент, не обязательно делать
для этого отдельный skill.

Рекомендуемая схема:

- runtime schema живет в коде
- author-facing инструкция живет в обычной markdown-документации

Например:

- `src/lib/mdx.ts`
- `src/app/content/README.md`

Это удобнее, чем держать authoring workflow внутри универсальной engineering
skill-библиотеки.

## 10. Рекомендованный порядок переноса в отдельный репозиторий

Если вы хотите вынести эту систему в отдельный repo-шаблон:

1. Перенесите `AGENTS.md`
2. Перенесите `.agents/skills/`
3. Добавьте шаблонные `.agents/project/*`
4. Добавьте этот `AGENTS_README.MD`
5. В новом потребляющем проекте:
    - скопируйте систему
    - снимите игнор с `AGENTS.md` и `.agents/`, если он есть
    - запустите `project-context-adapter`
    - проверьте `AGENTS.md`

## 11. Короткая памятка

- `AGENTS.md` — общие правила репозитория
- `.agents/skills/` — универсальные workflow-навыки
- `.agents/project/` — факты и паттерны текущего проекта
- `project-context-adapter` — обновляет overlay docs под новый проект
- SEO и security — только вручную
- Figma — через built-in capabilities, не через локальный skill
- content contracts — вне skill-системы, в коде и обычной документации

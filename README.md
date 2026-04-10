# fullstack-agent-docs

Конфигурационный репозиторий для работы в VS Code со связкой:

- `roo-code` (режимы, правила, skills)
- `Codex` (`Codex – OpenAI’s coding agent`)

Репозиторий не содержит приложения Next.js. Это набор инструкций, протоколов и шаблонов, которые направляют поведение агента при разработке.

## Как работает система

1. `roo-code` читает `.roomodes` и регистрирует пользовательские режимы (`Architect`, `Code`, `Security`, `Review`, `QA`, `UI`, `Debug`).
2. Базовые правила из `.roo/rules/*.md` задают постоянный контекст (архитектура, конвенции, качество, безопасность, skills).
3. Для каждого режима используется свой протокол из `.roo/rules-nextjs-*/00-protocol.md`.
4. При задачах по определённой теме агент подтягивает `SKILL.md` из `.roo/skills/*` и, при необходимости, документы из `docs/` и шаблоны из `templates/`.
5. `Codex` использует эти же файлы как рабочий контекст проекта.

## Структура проекта

```text
.
├── .gitignore
├── .rooignore
├── .roomodes
├── .vscode/
│   └── settings.json
├── README.md
├── codex.md
└── .roo/
    ├── rules/
    │   ├── 00-context.md
    │   ├── 10-nextjs-conventions.md
    │   ├── 20-quality-gates.md
    │   ├── 30-security.md
    │   └── 40-skills.md
    ├── rules-nextjs-architect/00-protocol.md
    ├── rules-nextjs-code/00-protocol.md
    ├── rules-nextjs-debug/00-protocol.md
    ├── rules-nextjs-qa/00-protocol.md
    ├── rules-nextjs-review/00-protocol.md
    ├── rules-nextjs-security/00-protocol.md
    ├── rules-nextjs-ui/00-protocol.md
    └── skills/
        ├── mdx-blog/
        │   ├── SKILL.md
        │   ├── docs/
        │   │   ├── frontmatter.md
        │   │   └── plugins.md
        │   └── templates/
        │       └── post.mdx
        ├── nextjs-app-router/
        │   └── SKILL.md
        ├── shadcn-component/
        │   ├── SKILL.md
        │   └── docs/
        │       └── customization.md
        └── zod-schema/
            ├── SKILL.md
            └── docs/
                └── patterns.md
```

## Описание файлов

### Корневые файлы

- `.gitignore` — файлы и директории, которые не должны попадать в Git (`.codex`, логи, IDE-кэш).
- `.rooignore` — что исключать из контекста Roo/Cline-агента (например, `.git/`, `node_modules/`, `build`).
- `.roomodes` — главный файл режимов: роли, ограничения и группы доступных инструментов.
- `codex.md` — сжатый high-level контекст для Codex (стек, архитектурные правила, порядок создания файлов).
- `README.md` — документация по репозиторию (этот файл).
- `.vscode/settings.json` — настройки VS Code для темы + параметры `roo-cline` (разрешённые команды, summarization, лимит табов в контексте).

### Глобальные правила (`.roo/rules`)

- `00-context.md` — базовая persona агента и общая архитектура Next.js 15+.
- `10-nextjs-conventions.md` — конвенции App Router, `params/searchParams`, `Suspense`, `next/image`, middleware.
- `20-quality-gates.md` — quality gates (`tsc`, `eslint`, `prettier`, `build`) и требования к TS/линтингу.
- `30-security.md` — security-модель: DAL, Server Actions, cookies, заголовки, CVE-2025-29927.
- `40-skills.md` — правила, когда и какой skill подключать.

### Протоколы режимов (`.roo/rules-nextjs-*`)

- `rules-nextjs-architect/00-protocol.md` — планирование фич без кода.
- `rules-nextjs-code/00-protocol.md` — реализация кода с фиксированным порядком файлов.
- `rules-nextjs-security/00-protocol.md` — аудит и шаблоны безопасности.
- `rules-nextjs-review/00-protocol.md` — правила code review и критерии BLOCK/REQUEST CHANGES.
- `rules-nextjs-qa/00-protocol.md` — тестирование и запуск quality gates.
- `rules-nextjs-ui/00-protocol.md` — UI/A11y/Tailwind/shadcn требования.
- `rules-nextjs-debug/00-protocol.md` — методика диагностики и минимальных исправлений.

### Skills (`.roo/skills`)

- `nextjs-app-router/SKILL.md` — паттерны структуры фич, `page.tsx` shell, Server Actions, DAL, `generateStaticParams`.
- `mdx-blog/SKILL.md` — построение MDX-блога (`content/posts`, frontmatter, рендеринг, роуты).
- `mdx-blog/docs/frontmatter.md` — схема обязательных/дополнительных полей frontmatter.
- `mdx-blog/docs/plugins.md` — настройка `@next/mdx`, `remark/rehype` и `mdx-components.tsx`.
- `mdx-blog/templates/post.mdx` — шаблон поста.
- `shadcn-component/SKILL.md` — установка и использование shadcn/ui через CLI, обёртки, `cn()`, `cva`.
- `shadcn-component/docs/customization.md` — настройка темы, `next-themes`, тёмная тема, кастомные токены.
- `zod-schema/SKILL.md` — правила валидации и типизации через Zod (`safeParse`, `coerce`, формы, query).
- `zod-schema/docs/patterns.md` — продвинутые Zod-паттерны (env, union, refine, трансформации).

## Режимы из `.roomodes`

- `nextjs-architect` — проектирование и декомпозиция задач.
- `nextjs-code` — написание production-кода.
- `nextjs-security` — security-аудит и DAL.
- `nextjs-review` — ревью без внесения правок.
- `nextjs-qa` — тесты и quality gates.
- `nextjs-ui` — UI и доступность.
- `nextjs-debug` — отладка и поиск root cause.

## Быстрый старт

1. Откройте папку в VS Code, где установлены `roo-code` и расширение `Codex`.
2. Выберите нужный режим из `.roomodes`.
3. Формулируйте задачу: правила из `.roo/rules/*` применятся как базовый контекст.
4. Если задача попадает под домен skill, агент должен прочитать соответствующий `SKILL.md` и следовать его протоколу.

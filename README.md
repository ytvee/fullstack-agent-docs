# fullstack-agent-docs

Документационный репозиторий с базой знаний для RAG/AI-агента, который помогает проектировать и писать fullstack-приложения вокруг экосистемы Next.js.

Это не приложение и не шаблон проекта, а набор Markdown-документов. Сейчас в репозитории зафиксированы `4983` official-файла и `40` custom-файлов.

## Что находится в репозитории

- `knowledge/official` — снимки официальной документации, разложенные по темам и источникам.
- `knowledge/custom` — вручную написанные гайды, паттерны, антипаттерны и правила для агента.
- `scripts/sources.yaml` — реестр части upstream-источников.
- `todo` — внутренняя рабочая заметка по доработке базы знаний.

## Фактическая структура проекта

```text
.
├── .vscode/
├── knowledge/
│   ├── custom/
│   └── official/
│       ├── devops/
│       │   └── vercel/
│       ├── framework/
│       │   ├── nextjs/
│       │   ├── react/
│       │   ├── react-hook-form/
│       │   ├── shadcn/
│       │   └── tailwindcss/
│       ├── stack/
│       │   ├── drizzle/
│       │   ├── prisma/
│       │   ├── resend/
│       │   ├── typescript/
│       │   └── zustand/
│       └── testing/
│           └── vitest/
└── scripts/
    └── sources.yaml
```

## Official layer

`knowledge/official` хранит официальные материалы, в основном на английском языке. Внутри каждой директории источника обычно есть:

- исходный крупный файл вида `<source>.md`;
- много более мелких Markdown-фрагментов, разбитых по страницам или разделам;
- frontmatter с метаданными вроде `title`, `description`, `url`, `version`.

Текущий набор checked-in источников:

| Категория | Источник | Файлов |
|---|---|---:|
| `devops` | `vercel` | 680 |
| `framework` | `nextjs` | 425 |
| `framework` | `react` | 179 |
| `framework` | `react-hook-form` | 34 |
| `framework` | `shadcn` | 171 |
| `framework` | `tailwindcss` | 26 |
| `stack` | `drizzle` | 1688 |
| `stack` | `prisma` | 706 |
| `stack` | `resend` | 395 |
| `stack` | `typescript` | 454 |
| `stack` | `zustand` | 45 |
| `testing` | `vitest` | 180 |

Важно: official-слой отражает upstream-документацию как есть. Поэтому внутри него встречаются и Pages Router, и App Router, и альтернативные подходы, даже если custom-слой рекомендует более узкий набор практик.

## Custom layer

`knowledge/custom` — это кураторский слой с рекомендациями для агента и команды. Сейчас в нём 40 документов по 11 разделам:

- `01-architecture` — 5 файлов
- `02-patterns` — 9 файлов
- `03-antipatterns` — 4 файла
- `04-linting` — 2 файла
- `05-testing` — 2 файла
- `06-security` — 3 файла
- `07-performance` — 3 файла
- `08-accessibility` — 2 файла
- `09-seo` — 4 файла
- `10-devops` — 3 файла
- `11-agent-rules` — 3 файла

Обычно custom-документы содержат:

- YAML frontmatter с `category`, `topic`, `status`;
- объяснения на русском языке;
- примеры на TypeScript/Next.js;
- практические правила, чеклисты и антипримеры.

Именно в этом слое зафиксированы проектные предпочтения, например:

- Next.js App Router как основной подход;
- TypeScript strict;
- Drizzle как основной ORM;
- Auth.js v5, Zod, Server Actions, Zustand для UI state;
- Vercel/Railway как рекомендуемая инфраструктура.

Эти правила описаны в документах, но не являются "кодом проекта", потому что сам репозиторий состоит только из базы знаний.

## Как этим пользоваться

- Для retrieval/RAG обычно полезнее брать split-файлы из `knowledge/official/<category>/<source>/`, а не только крупный `<source>.md`.
- Для проектных решений и внутренних соглашений в первую очередь смотреть `knowledge/custom`.
- Если нужен authoritative source, сначала находить ответ в `knowledge/official`, а затем сверять с custom-ограничениями агента.

## Что важно не перепутать

В репозитории сейчас нет того, что описывалось в старой версии `README`:

- нет `fetch_docs.py`;
- нет `requirements.txt`;
- нет `.hashes.json`;
- нет `package.json`, Python-пакета или другой автоматики для сборки/обновления базы знаний.

`scripts/sources.yaml` существует, но это только YAML-реестр источников. Он не полностью совпадает с текущим checked-in содержимым `knowledge/official`: например, в нём есть `authjs` и `zod`, а в дереве official-документов сейчас присутствуют другие директории, такие как `react`, `typescript`, `shadcn`, `tailwindcss` и `zustand`.

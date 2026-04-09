# 20 - Quality Gates

> **Область применения:** Все файлы проекта
>
> **Взаимодействие:** Дополняет `00-context.md`. Базовые запреты (`any`, именование) описаны там. Здесь — инструменты, конфигурации и автоматизация.

## 1. TypeScript

### Конфигурация `tsconfig.json`

`strict: true` включает группу флагов, но не все полезные проверки. Добавляй явно:

```jsonc
{
  "compilerOptions": {
    // Базовый пакет проверок
    "strict": true,

    // Сверх strict: не включены автоматически
    "noUncheckedIndexedAccess": true,     // arr[0] имеет тип T | undefined
    "exactOptionalPropertyTypes": true,   // foo?: T !== foo?: T | undefined
    "noUncheckedSideEffectImports": true, // импорты без биндинга должны существовать
    "noImplicitReturns": true,            // все ветки функции должны возвращать значение
    "noFallthroughCasesInSwitch": true,   // switch-case без break/return — ошибка

    // Чистота кода
    "noUnusedLocals": true,
    "noUnusedParameters": true,

    // Модули
    "verbatimModuleSyntax": true  // import type обязателен для type-only импортов
  }
}
```

Не отключай и не понижай эти флаги. Если компилятор ругается — исправь код, не конфиг.

### Обязательные практики

Тип-импорты — только через `import type`:

```typescript
// Запрещено
import { User } from './types'

// Правильно
import type { User } from './types'

// Или смешанный импорт
import { fetchUser, type User } from './api'
```

`satisfies` для объектов с известной формой:

```typescript
// Запрещено: теряем точный тип
const config: Config = { theme: 'dark', lang: 'ru' }

// Правильно: валидация + сохранение литерального типа
const config = { theme: 'dark', lang: 'ru' } satisfies Config
```

Явные возвращаемые типы для экспортируемых функций:

```typescript
// Запрещено
export async function getUser(id: string) {
  return db.user.findUnique({ where: { id } })
}

// Правильно
export async function getUser(id: string): Promise<User | null> {
  return db.user.findUnique({ where: { id } })
}
```

Дискриминированные union вместо boolean-флагов:

```typescript
// Запрещено
type Result = { data?: User; error?: string; loading: boolean }

// Правильно
type Result =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: User }
  | { status: 'error'; error: string }
```

---

## 2. ESLint

### Конфигурация

В Next.js 15 используется ESLint 9 с flat config (`eslint.config.mjs`). Формат `.eslintrc.*` — устаревший.

```javascript
// eslint.config.mjs
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
import prettier from 'eslint-config-prettier/flat'

export default defineConfig([
  ...nextVitals,
  prettier,
  globalIgnores(['.next/**', 'out/**', 'build/**', 'next-env.d.ts']),
  {
    rules: {
      // Запреты из 00-context.md, продублированные как ошибки линтера
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-non-null-assertion': 'error',
      '@typescript-eslint/consistent-type-imports': [
        'error',
        { prefer: 'type-imports', fixStyle: 'inline-type-imports' },
      ],

      // Именование boolean-переменных
      '@typescript-eslint/naming-convention': [
        'error',
        {
          selector: 'variable',
          types: ['boolean'],
          format: ['PascalCase'],
          prefix: ['is', 'has', 'can', 'should', 'was', 'will'],
        },
      ],

      // Импорты
      'no-restricted-imports': [
        'error',
        {
          patterns: [
            {
              // Запрет относительных импортов за пределы фичи
              group: ['../../*'],
              message: 'Используй алиас @/* вместо относительных импортов выше уровня фичи',
            },
          ],
        },
      ],
    },
  },
])
```

### Запуск

```bash
# Проверка
npx eslint .

# Автоисправление
npx eslint . --fix
```

В Next.js 15 команда `next lint` ещё работает, но начиная с Next.js 16 — удалена. Используй ESLint напрямую.

---

## 3. Prettier

Единственный форматтер в проекте. Не используй ESLint для форматирования.

```jsonc
// .prettierrc
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 4,
  "trailingComma": "all",
  "printWidth": 100,
  "plugins": ["prettier-plugin-tailwindcss"]
}
```

`prettier-plugin-tailwindcss` сортирует классы Tailwind автоматически — не переставляй их вручную.

```jsonc
// .prettierignore
.next
out
build
public
```

---

## 4. Pre-commit хуки

Линтинг и форматирование на каждый коммит через `husky` + `lint-staged`.

```jsonc
// package.json
{
  "scripts": {
    "prepare": "husky"
  }
}
```

```javascript
// .lintstagedrc.mjs
export default {
  '*.{ts,tsx}': ['eslint --fix', 'prettier --write'],
  '*.{json,md,css}': ['prettier --write'],
}
```

```bash
# .husky/pre-commit
npx lint-staged
```

Инициализация:

```bash
npm install --save-dev husky lint-staged
npx husky init
```

---

## 5. Проверки перед коммитом (ручные)

Перед каждым коммитом агент обязан выполнить последовательно:

```bash
# 1. Проверка типов без компиляции
npx tsc --noEmit

# 2. Линтинг
npx eslint .

# 3. Форматирование (проверка без записи)
npx prettier --check .

# 4. Сборка (обнаруживает ошибки Next.js, недоступные в tsc)
npx next build
```

Если хотя бы один шаг падает — коммит не выполняется. Исправляй ошибки, не обходи их (`// @ts-ignore`, `// eslint-disable`).

---

## 6. Организация импортов

Порядок импортов в каждом файле:

```typescript
// 1. Внешние пакеты
import { Suspense } from 'react'
import type { NextPage } from 'next'
import Link from 'next/link'

// 2. Внутренние — через алиас @/*
import { db } from '@/lib/db'
import type { Product } from '@/features/products/types'
import { ProductCard } from '@/features/products/components/ProductCard'

// 3. Относительные — только внутри одной фичи
import { formatPrice } from '../utils'
```

Между группами — пустая строка. Prettier с плагином `prettier-plugin-organize-imports` автоматизирует сортировку внутри групп.

---

## 7. Запреты на уровне кода

**Магические числа и строки** — всегда выносить в именованные константы:

```typescript
// Запрещено
if (user.role === 2) { ... }
await sleep(3000)

// Правильно
const ADMIN_ROLE_ID = 2
const REDIRECT_DELAY_MS = 3000

if (user.role === ADMIN_ROLE_ID) { ... }
await sleep(REDIRECT_DELAY_MS)
```

**`console.log`** в продуктовом коде — запрещён. Используй серверное логирование:

```typescript
// Запрещено в компонентах и actions
console.log('user:', user)

// Разрешено только в error-границах и dev-утилитах
if (process.env.NODE_ENV === 'development') {
  console.debug('debug info')
}
```

**Вложенность** — не более 3 уровней. При превышении — выноси в функцию или используй early return:

```typescript
// Запрещено
function process(data: Data | null) {
  if (data) {
    if (data.items) {
      if (data.items.length > 0) {
        // логика на 4-м уровне
      }
    }
  }
}

// Правильно
function process(data: Data | null) {
  if (!data) return
  if (!data.items) return
  if (data.items.length === 0) return
  // логика на 1-м уровне
}
```

---

## 8. Итоговый чек-лист качества

Перед тем как считать задачу выполненной, агент проверяет:

* `tsc --noEmit` — без ошибок
* `eslint .` — без ошибок и предупреждений
* `prettier --check .` — без diff
* `next build` — успешная сборка
* Нет `any`, `@ts-ignore`, `eslint-disable` без объяснения
* Нет `console.log` вне dev-веток
* Нет магических чисел и строк
* Все экспортируемые функции имеют явный возвращаемый тип
* Все type-only импорты используют `import type`

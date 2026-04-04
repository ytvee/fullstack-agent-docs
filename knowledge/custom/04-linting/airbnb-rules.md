---
category: linting
topic: airbnb-rules-rationale
stack: [eslint, airbnb, typescript]
last_updated: 2026-04
---

## Проблема / Контекст

Агент должен знать не только КАК настроить Airbnb,
но и ПОЧЕМУ каждое правило существует и когда его можно
переопределить без потери смысла.

## Решение

Три группы правил: берём без изменений, переопределяем, не берём.

## Правила которые берём без изменений

no-console
  Причина: в Next.js используем структурированный logger (pino / winston),
  console.log теряется в продакшне и не имеет уровней.
  Исключение: console.error в error.tsx допустим.

no-unused-vars
  Причина: TypeScript уже ловит это, но Airbnb добавляет
  проверку для переменных в деструктуризации.

prefer-const
  Причина: мутабельность должна быть явной через let.
  Неизменяемые данные — всегда const.

eqeqeq
  Причина: === вместо ==, исключает неочевидные приведения типов.

no-shadow
  Причина: переменная во внутренней области не должна
  скрывать переменную из внешней.

jsx-a11y/*
  Причина: доступность из коробки, без дополнительных усилий.

react-hooks/rules-of-hooks
  Причина: хуки только на верхнем уровне, только в компонентах.

react-hooks/exhaustive-deps
  Причина: предотвращает баги с устаревшими замыканиями в useEffect.

## Правила которые переопределяем под Next.js

react/react-in-jsx-scope: off
  Причина: JSX transform в Next.js не требует импорта React.

import/prefer-default-export: off
  Причина: named exports предпочтительны — лучше tree shaking,
  явные имена, проще рефакторинг.

react/require-default-props: off
  Причина: TypeScript с strict mode покрывает это полностью.
  Дублирование propTypes избыточно.

react/jsx-props-no-spreading: off
  Причина: shadcn/ui построен на spread пропсов.
  Запрет сломает весь UI слой.

require-await: off
  Причина: Server Actions должны быть async по контракту Next.js,
  даже если внутри нет await.

## Правила которые НЕ берём

❌ react/display-name
  Причина: конфликт с React.forwardRef в shadcn/ui компонентах.

❌ import/extensions
  Причина: TypeScript и Next.js резолвят пути без расширений.

❌ no-restricted-exports
  Причина: Next.js требует default export для page.tsx, layout.tsx,
  error.tsx и других специальных файлов.

## Пример кода

Добавить в package.json скрипты:
```json
{
  "scripts": {
    "lint": "next lint",
    "lint:fix": "next lint --fix",
    "lint:strict": "eslint . --max-warnings 0"
  }
}
```

lint:strict используется в CI — падает при любом предупреждении.

## Антипаттерны

❌ Глобальный eslint-disable — всегда отключать точечно с комментарием
❌ Отключать jsx-a11y правила — нарушает доступность
❌ Игнорировать exhaustive-deps — источник багов с useEffect

## Связанные документы

- 04-linting/airbnb-flat-config.md
- 04-linting/eslint-rules-explained.md
- 11-agent-rules/decision-trees.md

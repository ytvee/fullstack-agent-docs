---
category: linting
topic: airbnb-flat-config
stack: [nextjs, typescript, eslint]
last_updated: 2026-04
---

## Проблема / Контекст

Airbnb Style Guide — стандарт де-факто для JS/React проектов.
Но eslint-config-airbnb написан под устаревший формат (.eslintrc).
Next.js 15 использует flat config (eslint.config.mjs).
Нужен адаптер для совместимости.

## Решение

Использовать @eslint/compat для обёртки Airbnb конфига.
Prettier всегда последним — отключает конфликтующие правила форматирования.

## Установка

npm install -D \
  eslint \
  @eslint/compat \
  @eslint/eslintrc \
  eslint-config-airbnb \
  eslint-config-airbnb-typescript \
  eslint-plugin-react \
  eslint-plugin-react-hooks \
  eslint-plugin-jsx-a11y \
  eslint-plugin-import \
  @typescript-eslint/eslint-plugin \
  @typescript-eslint/parser \
  eslint-config-next \
  eslint-config-prettier \
  prettier

## Пример кода

Готовый eslint.config.mjs для Next.js 15 + TypeScript + Airbnb:
```js
import { fixupConfigRules } from "@eslint/compat";
import { FlatCompat } from "@eslint/eslintrc";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

export default [
  // Airbnb через адаптер — порядок строго такой
  ...fixupConfigRules(
    compat.extends(
      "airbnb",
      "airbnb-typescript",
      "airbnb/hooks",
      "next/core-web-vitals",
      "prettier"        // ВСЕГДА последним
    )
  ),

  {
    rules: {
      // Next.js 15 — JSX transform не требует импорта React
      "react/react-in-jsx-scope": "off",

      // Named exports предпочтительны в Next.js
      "import/prefer-default-export": "off",

      // TypeScript покрывает это лучше
      "react/require-default-props": "off",

      // shadcn/ui построен на prop spreading
      "react/jsx-props-no-spreading": "off",

      // Server Actions могут быть async без await
      "require-await": "off",

      // next/image уже ловит next/core-web-vitals
      "@next/next/no-img-element": "error",

      // Явный возвращаемый тип для публичных функций
      "@typescript-eslint/explicit-function-return-type": [
        "warn",
        {
          allowExpressions: true,
          allowTypedFunctionExpressions: true,
        },
      ],
    },
  },

  {
    // Отдельные правила для Server Actions
    files: ["**/actions/**/*.ts", "**/actions.ts"],
    rules: {
      // Server Actions экспортируются как named async functions
      "import/prefer-default-export": "off",
    },
  },

  {
    // Послабления для конфигурационных файлов
    files: ["*.config.ts", "*.config.mjs", "*.config.js"],
    rules: {
      "import/no-extraneous-dependencies": "off",
    },
  },

  {
    // Игнорировать автогенерированное
    ignores: [
      ".next/",
      "node_modules/",
      "drizzle/",         // миграции Drizzle
      "src/components/ui/", // shadcn/ui компоненты
    ],
  },
];
```

## Антипаттерны

❌ Prettier НЕ последним в extends — вызывает конфликты форматирования
❌ Использовать .eslintrc вместо eslint.config.mjs — устаревший формат
❌ Отключать @typescript-eslint/no-explicit-any глобально — теряется смысл strict mode
❌ Добавлять eslint-disable комментарии без объяснения причины

## Связанные документы

- 04-linting/eslint-rules-explained.md
- 04-linting/airbnb-rules.md
- 04-linting/prettier-config.md
- 11-agent-rules/pre-code-checklist.md

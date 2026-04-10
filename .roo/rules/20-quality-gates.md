# 20 - Quality Gates

> **Scope:** All project files
>
> **Relationship:** Extends `00-context.md`. Core prohibitions (`any`, naming) are defined there. This file covers tooling, configurations, and automation.

## 1. TypeScript

### `tsconfig.json` configuration

`strict: true` enables a group of checks but not all useful ones. Add these explicitly:

```jsonc
{
  "compilerOptions": {
    // Base check bundle
    "strict": true,

    // Beyond strict: not included automatically
    "noUncheckedIndexedAccess": true,     // arr[0] has type T | undefined
    "exactOptionalPropertyTypes": true,   // foo?: T !== foo?: T | undefined
    "noUncheckedSideEffectImports": true, // side-effect imports must exist
    "noImplicitReturns": true,            // all function branches must return
    "noFallthroughCasesInSwitch": true,   // switch-case without break/return is an error

    // Code cleanliness
    "noUnusedLocals": true,
    "noUnusedParameters": true,

    // Modules
    "verbatimModuleSyntax": true  // import type required for type-only imports
  }
}
```

Do not disable or downgrade these flags. If the compiler complains — fix the code, not the config.

### Required practices

Type imports — use `import type` only:

```typescript
// Wrong
import { User } from './types'

// Correct
import type { User } from './types'

// Or mixed import
import { fetchUser, type User } from './api'
```

`satisfies` for objects with a known shape:

```typescript
// Wrong: loses the precise type
const config: Config = { theme: 'dark', lang: 'en' }

// Correct: validates + preserves the literal type
const config = { theme: 'dark', lang: 'en' } satisfies Config
```

Explicit return types for exported functions:

```typescript
// Wrong
export async function getUser(id: string) {
  return db.user.findUnique({ where: { id } })
}

// Correct
export async function getUser(id: string): Promise<User | null> {
  return db.user.findUnique({ where: { id } })
}
```

Discriminated unions instead of boolean flags:

```typescript
// Wrong
type Result = { data?: User; error?: string; loading: boolean }

// Correct
type Result =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: User }
  | { status: 'error'; error: string }
```

---

## 2. ESLint

### Configuration

Next.js 15 uses ESLint 9 with flat config (`eslint.config.mjs`). The `.eslintrc.*` format is deprecated.

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
      // Prohibitions from 00-context.md, enforced as linter errors
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-non-null-assertion': 'error',
      '@typescript-eslint/consistent-type-imports': [
        'error',
        { prefer: 'type-imports', fixStyle: 'inline-type-imports' },
      ],

      // Boolean variable naming
      '@typescript-eslint/naming-convention': [
        'error',
        {
          selector: 'variable',
          types: ['boolean'],
          format: ['PascalCase'],
          prefix: ['is', 'has', 'can', 'should', 'was', 'will'],
        },
      ],

      // Imports
      'no-restricted-imports': [
        'error',
        {
          patterns: [
            {
              // Forbid relative imports that escape feature boundaries
              group: ['../../*'],
              message: 'Use the @/* alias instead of relative imports above the feature level',
            },
          ],
        },
      ],
    },
  },
])
```

### Running ESLint

```bash
# Check
npx eslint .

# Auto-fix
npx eslint . --fix
```

In Next.js 15 the `next lint` command still works, but it will be removed in Next.js 16. Use ESLint directly.

---

## 3. Prettier

The only formatter in the project. Do not use ESLint for formatting.

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

`prettier-plugin-tailwindcss` sorts Tailwind classes automatically — do not reorder them manually.

```jsonc
// .prettierignore
.next
out
build
public
```

---

## 4. Pre-commit hooks

Linting and formatting on every commit via `husky` + `lint-staged`.

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

Initialize:

```bash
npm install --save-dev husky lint-staged
npx husky init
```

---

## 5. Pre-commit checks (manual)

Before every commit the agent must run sequentially:

```bash
# 1. Type check without compilation
npx tsc --noEmit

# 2. Linting
npx eslint .

# 3. Formatting check (read-only)
npx prettier --check .

# 4. Build (catches Next.js errors not visible to tsc)
npx next build
```

If any step fails — the commit does not proceed. Fix the errors; do not bypass them (`// @ts-ignore`, `// eslint-disable`).

---

## 6. Import organization

Import order in every file:

```typescript
// 1. External packages
import { Suspense } from 'react'
import type { NextPage } from 'next'
import Link from 'next/link'

// 2. Internal — via @/* alias
import { db } from '@/lib/db'
import type { Product } from '@/features/products/types'
import { ProductCard } from '@/features/products/components/ProductCard'

// 3. Relative — only within the same feature
import { formatPrice } from '../utils'
```

Blank line between groups. Prettier with `prettier-plugin-organize-imports` automates sorting within groups.

---

## 7. Code-level prohibitions

**Magic numbers and strings** — always extract to named constants:

```typescript
// Wrong
if (user.role === 2) { ... }
await sleep(3000)

// Correct
const ADMIN_ROLE_ID = 2
const REDIRECT_DELAY_MS = 3000

if (user.role === ADMIN_ROLE_ID) { ... }
await sleep(REDIRECT_DELAY_MS)
```

**`console.log`** in production code — forbidden. Use server-side logging:

```typescript
// Wrong in components and actions
console.log('user:', user)

// Allowed only in error boundaries and dev utilities
if (process.env.NODE_ENV === 'development') {
  console.debug('debug info')
}
```

**Nesting** — no more than 3 levels. If exceeded — extract to a function or use early returns:

```typescript
// Wrong
function process(data: Data | null) {
  if (data) {
    if (data.items) {
      if (data.items.length > 0) {
        // logic at level 4
      }
    }
  }
}

// Correct
function process(data: Data | null) {
  if (!data) return
  if (!data.items) return
  if (data.items.length === 0) return
  // logic at level 1
}
```

---

## 8. Final quality checklist

Before considering a task done, the agent checks:

- `tsc --noEmit` — no errors
- `eslint .` — no errors or warnings
- `prettier --check .` — no diff
- `next build` — successful build
- No `any`, `@ts-ignore`, `eslint-disable` without explanation
- No `console.log` outside dev branches
- No magic numbers or strings
- All exported functions have explicit return types
- All type-only imports use `import type`

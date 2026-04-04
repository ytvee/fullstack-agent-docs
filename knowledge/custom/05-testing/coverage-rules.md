---
category: testing
topic: coverage-rules
status: draft
---

## Проблема / Контекст

Without enforced coverage thresholds, the CI pipeline provides no guarantee that new code ships with tests. 100% coverage is both unachievable and undesirable — it incentivizes writing trivial tests for generated or config code. The goal is *meaningful* coverage at the layers where bugs are expensive: business logic, Server Actions, Route Handlers.

Vitest's built-in v8 provider gives accurate source-mapped coverage for TypeScript without requiring Babel or Istanbul transforms.

---

## Решение

### Coverage targets by layer

| Layer | Target | Rationale |
|---|---|---|
| `lib/utils`, `lib/formatters`, `lib/validators` | **90%+** | Pure functions, cheap to test, expensive to debug in prod |
| `schemas/` (Zod) | **90%+** | Every schema branch has a real edge case |
| `actions/` (Server Actions) | **80%+** | Auth + validation + DB writes — the core of the app |
| `app/api/` (Route Handlers) | **80%+** | Webhook handlers, REST endpoints |
| `components/` (UI) | **60%+** | Test logic, skip pure markup |
| `app/` (pages/layouts) | **not enforced** | Tested via E2E instead |

### What to always skip

- `**/*.config.*` — vitest, playwright, tailwind, next configs
- `**/*.d.ts` — type declarations
- `**/types/**` and `**/interfaces/**`
- `drizzle/**` — generated SQL migrations
- `.next/**` — build output
- `tests/**` — test helpers themselves
- `**/__mocks__/**`
- `**/generated/**` — any codegen output
- `instrumentation.ts`, `middleware.ts` — Next.js runtime wiring, test via E2E

---

## Пример кода

### vitest.config.ts — full coverage configuration

```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";
import path from "path";

export default defineConfig({
  test: {
    globals: true,
    environment: "node",
    setupFiles: ["./tests/setup/vitest.setup.ts"],
    coverage: {
      // v8 uses Node's built-in coverage — no babel transform needed
      provider: "v8",

      // What to include — explicit is safer than relying on exclude alone
      include: [
        "src/lib/**/*.ts",
        "src/schemas/**/*.ts",
        "src/actions/**/*.ts",
        "src/app/api/**/*.ts",
        "src/components/**/*.tsx",
        "src/hooks/**/*.ts",
      ],

      // What to skip
      exclude: [
        "**/*.config.*",
        "**/*.d.ts",
        "**/types/**",
        "**/interfaces/**",
        "drizzle/**",
        ".next/**",
        "tests/**",
        "**/__mocks__/**",
        "**/generated/**",
        "src/app/**/page.tsx",      // pages tested via E2E
        "src/app/**/layout.tsx",    // layouts tested via E2E
        "src/app/**/loading.tsx",
        "src/app/**/error.tsx",
        "src/app/**/not-found.tsx",
        "src/middleware.ts",
        "src/instrumentation.ts",
      ],

      // Reporters
      reporter: ["text", "json", "html", "lcov"],
      reportsDirectory: "./coverage",

      // Thresholds — CI fails if these are not met
      // Per-file thresholds catch newly added files with zero tests
      thresholds: {
        // Global thresholds
        lines: 75,
        functions: 75,
        branches: 70,
        statements: 75,

        // Per-file thresholds — stricter for critical paths
        perFile: true,

        // Override per directory
        "src/lib/**": {
          lines: 90,
          functions: 90,
          branches: 85,
        },
        "src/schemas/**": {
          lines: 90,
          functions: 90,
          branches: 90,
        },
        "src/actions/**": {
          lines: 80,
          functions: 80,
          branches: 75,
        },
        "src/app/api/**": {
          lines: 80,
          functions: 80,
          branches: 75,
        },
      },

      // Fail the build if coverage drops
      // This is the key: CI returns non-zero exit code
      all: true, // include uncovered files in report (don't hide them)
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
```

### package.json scripts

```json
{
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "test:coverage:ui": "vitest run --coverage --reporter=html && open coverage/index.html",
    "test:unit": "vitest run --testPathPattern='.unit.test'",
    "test:integration": "vitest run --testPathPattern='.integration.test'",
    "test:e2e": "playwright test",
    "test:e2e:ui": "playwright test --ui",
    "test:ci": "vitest run --coverage --reporter=junit --outputFile=test-results/vitest.xml"
  }
}
```

### GitHub Actions CI coverage gate

```yaml
# .github/workflows/test.yml
name: Test & Coverage

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  unit-integration:
    name: Unit & Integration Tests
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v4
        with:
          version: 9

      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: "pnpm"

      - run: pnpm install --frozen-lockfile

      - name: Run Drizzle migrations on test DB
        run: pnpm drizzle-kit migrate
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/testdb

      - name: Run tests with coverage
        run: pnpm test:ci
        env:
          TEST_DATABASE_URL: postgresql://test:test@localhost:5432/testdb
          NEXTAUTH_SECRET: ci-test-secret-32-chars-minimum
          NODE_ENV: test

      # Fail the job if coverage thresholds are not met
      # (vitest --coverage already does this via thresholds config,
      # but we also upload the report for PR comments)
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage/lcov.info
          fail_ci_if_error: true
          token: ${{ secrets.CODECOV_TOKEN }}

      - name: Comment coverage on PR
        if: github.event_name == 'pull_request'
        uses: davelosert/vitest-coverage-report-action@v2
        with:
          json-summary-path: ./coverage/coverage-summary.json
          json-final-path: ./coverage/coverage-final.json

  e2e:
    name: E2E Tests (Playwright)
    runs-on: ubuntu-latest
    needs: unit-integration  # only run E2E if unit/integration pass

    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: "pnpm"
      - run: pnpm install --frozen-lockfile
      - run: pnpm playwright install --with-deps chromium
      - run: pnpm test:e2e
        env:
          TEST_DATABASE_URL: ${{ secrets.E2E_DATABASE_URL }}
          NEXTAUTH_SECRET: ${{ secrets.NEXTAUTH_SECRET }}
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 7
```

### Checking coverage for a specific file

```bash
# Check coverage for a single module during development
pnpm vitest run --coverage --coverage.include="src/actions/product.ts"

# Open the HTML report to find uncovered branches visually
pnpm test:coverage:ui
```

### Coverage summary JSON — what it looks like

```json
// coverage/coverage-summary.json (auto-generated, do not edit)
{
  "total": {
    "lines": { "total": 842, "covered": 698, "skipped": 0, "pct": 82.9 },
    "functions": { "total": 124, "covered": 103, "skipped": 0, "pct": 83.06 },
    "statements": { "total": 901, "covered": 745, "skipped": 0, "pct": 82.69 },
    "branches": { "total": 213, "covered": 162, "skipped": 0, "pct": 76.05 }
  }
}
```

### Practical: writing tests to hit branch coverage

```typescript
// src/lib/price.ts
export function formatPrice(cents: number, currency: string = "USD"): string {
  if (cents < 0) throw new Error("Price cannot be negative");
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency,
  }).format(cents / 100);
}

// src/lib/price.unit.test.ts
import { describe, it, expect } from "vitest";
import { formatPrice } from "./price";

describe("formatPrice", () => {
  // Branch 1: normal path
  it("formats USD cents correctly", () => {
    expect(formatPrice(4999)).toBe("$49.99");
  });

  // Branch 2: different currency
  it("formats EUR cents correctly", () => {
    expect(formatPrice(1000, "EUR")).toBe("€10.00");
  });

  // Branch 3: zero
  it("formats zero price", () => {
    expect(formatPrice(0)).toBe("$0.00");
  });

  // Branch 4: the throw path — without this, branch coverage for the guard is 50%
  it("throws for negative price", () => {
    expect(() => formatPrice(-1)).toThrow("Price cannot be negative");
  });
});
```

---

## Антипаттерн

```typescript
// BAD: Writing empty tests to game coverage
it("calculates price", () => {
  formatPrice(100); // no assertion — still increments line coverage
  expect(true).toBe(true);
});

// BAD: Setting all thresholds to 0 "temporarily"
// vitest.config.ts
thresholds: {
  lines: 0,   // "we'll fix this later" — it never gets fixed
}

// BAD: Excluding too much to make the numbers look good
exclude: [
  "src/actions/**",  // The most important code excluded from coverage!
  "src/lib/**",
]

// GOOD: Fail fast in CI — the build error message tells you exactly what's uncovered
// vitest exits with code 1 and prints:
// ERROR: Coverage for lines (61.5%) does not meet global threshold (75%)
// This forces the PR author to either write tests or explicitly justify an exclusion.
```

---

## Связанные документы

- `knowledge/custom/05-testing/test-strategy.md` — overall three-layer strategy
- `knowledge/custom/10-devops/ci-cd.md` — full CI/CD pipeline setup

---
category: devops
topic: github-actions-ci
status: draft
---

## Проблема / Контекст

GitHub Actions автоматизирует проверку качества кода при каждом PR и CD при мердже в main. Для Next.js 15 проекта нужны три pipeline: 1) быстрые проверки на PR (lint, typecheck, tests, build), 2) E2E тесты на реальном preview деплое, 3) автоматическое обновление зависимостей через Dependabot. Без CI команда полагается на ручные проверки, что приводит к регрессиям в продакшне.

Ключевые задачи: кэширование `node_modules` и `.next/cache` для быстрых запусков, изоляция тестовой БД, управление секретами, интеграция с Vercel preview деплоями.

## Решение

### Workflow 1: PR Checks (lint + typecheck + tests + build)

```yaml
# .github/workflows/pr-checks.yml
name: PR Checks

on:
  pull_request:
    branches: [main, develop]
    types: [opened, synchronize, reopened]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true  # Отменяем старые запуски при новых коммитах

env:
  NODE_VERSION: "20"
  PNPM_VERSION: "9"

jobs:
  lint-and-typecheck:
    name: Lint & TypeCheck
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: ${{ env.PNPM_VERSION }}

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: "pnpm"  # кэшируем на основе pnpm-lock.yaml

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run ESLint
        run: pnpm lint

      - name: Run TypeScript check
        run: pnpm tsc --noEmit

  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: ${{ env.PNPM_VERSION }}

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: "pnpm"

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run Vitest
        run: pnpm test:unit --run --reporter=verbose
        env:
          # Unit тесты не требуют реальной БД — используем моки
          DATABASE_URL: "postgresql://test:test@localhost:5432/test"
          AUTH_SECRET: "test-secret-for-ci-at-least-32-characters-long"

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        if: always()
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          file: ./coverage/lcov.info

  build:
    name: Build
    runs-on: ubuntu-latest
    timeout-minutes: 20
    needs: [lint-and-typecheck]  # Не запускаем build если lint упал

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: ${{ env.PNPM_VERSION }}

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: "pnpm"

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      # Кэшируем .next/cache для ускорения последующих сборок
      - name: Cache Next.js build
        uses: actions/cache@v4
        with:
          path: |
            .next/cache
          key: ${{ runner.os }}-nextjs-${{ hashFiles('**/pnpm-lock.yaml') }}-${{ hashFiles('**/*.ts', '**/*.tsx') }}
          restore-keys: |
            ${{ runner.os }}-nextjs-${{ hashFiles('**/pnpm-lock.yaml') }}-
            ${{ runner.os }}-nextjs-

      - name: Build Next.js
        run: pnpm build
        env:
          # Минимальные переменные для успешного build
          NEXT_PUBLIC_SITE_URL: "https://yoursite.com"
          DATABASE_URL: ${{ secrets.DATABASE_URL_CI }}
          AUTH_SECRET: ${{ secrets.AUTH_SECRET_CI }}
          NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY: ${{ secrets.STRIPE_PUBLISHABLE_KEY_TEST }}

      - name: Check bundle size
        uses: preactjs/compressed-size-action@v2
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          build-script: "build"
          pattern: ".next/static/**/*.{js,css}"
          minimum-change-threshold: 1000  # Сообщать только об изменениях > 1KB
```

### Workflow 2: E2E Tests на Preview Deployment

```yaml
# .github/workflows/e2e-tests.yml
name: E2E Tests

on:
  # Запускаем после успешного деплоя preview
  deployment_status:

jobs:
  e2e:
    name: Playwright E2E
    # Только для успешных preview деплоев от Vercel
    if: |
      github.event.deployment_status.state == 'success' &&
      github.event.deployment_status.environment == 'Preview'
    runs-on: ubuntu-latest
    timeout-minutes: 30

    services:
      # Тестовая PostgreSQL БД
      postgres:
        image: postgres:16-alpine
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
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: "9"

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "pnpm"

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      # Кэшируем Playwright browsers
      - name: Cache Playwright browsers
        uses: actions/cache@v4
        id: playwright-cache
        with:
          path: ~/.cache/ms-playwright
          key: ${{ runner.os }}-playwright-${{ hashFiles('**/pnpm-lock.yaml') }}

      - name: Install Playwright browsers
        if: steps.playwright-cache.outputs.cache-hit != 'true'
        run: pnpm exec playwright install --with-deps chromium

      - name: Install browser deps (if cached)
        if: steps.playwright-cache.outputs.cache-hit == 'true'
        run: pnpm exec playwright install-deps chromium

      - name: Run DB migrations on test DB
        run: pnpm db:migrate
        env:
          DATABASE_URL: "postgresql://test:test@localhost:5432/testdb"

      - name: Seed test data
        run: pnpm db:seed:test
        env:
          DATABASE_URL: "postgresql://test:test@localhost:5432/testdb"

      - name: Run Playwright tests
        run: pnpm test:e2e
        env:
          # URL preview деплоя от Vercel
          PLAYWRIGHT_BASE_URL: ${{ github.event.deployment_status.target_url }}
          DATABASE_URL: "postgresql://test:test@localhost:5432/testdb"
          AUTH_SECRET: ${{ secrets.AUTH_SECRET_CI }}
          # Тестовые данные
          TEST_USER_EMAIL: "test@example.com"
          TEST_USER_PASSWORD: "Test1234!"

      - name: Upload Playwright report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report-${{ github.run_id }}
          path: playwright-report/
          retention-days: 7

      - name: Comment PR with test results
        uses: actions/github-script@v7
        if: always() && github.event_name == 'pull_request'
        with:
          script: |
            const { data: comments } = await github.rest.issues.listComments({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
            });
            const botComment = comments.find(c => c.body.includes('<!-- e2e-results -->'));
            const status = '${{ job.status }}' === 'success' ? '✅' : '❌';
            const body = `<!-- e2e-results -->
            ## ${status} E2E Test Results
            **Status:** ${{ job.status }}
            **Preview URL:** ${{ github.event.deployment_status.target_url }}
            **Report:** [View artifact](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }})`;

            if (botComment) {
              await github.rest.issues.updateComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                comment_id: botComment.id,
                body,
              });
            } else {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                body,
              });
            }
```

### Workflow 3: Production Deploy с миграциями

```yaml
# .github/workflows/deploy-production.yml
name: Deploy Production

on:
  push:
    branches: [main]

jobs:
  run-migrations:
    name: Run DB Migrations
    runs-on: ubuntu-latest
    timeout-minutes: 10
    environment: production

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: "9"

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "pnpm"

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run Drizzle migrations
        run: pnpm db:migrate
        env:
          # Используем UNPOOLED connection для миграций
          DATABASE_URL: ${{ secrets.DATABASE_URL_UNPOOLED }}

  deploy-vercel:
    name: Deploy to Vercel
    runs-on: ubuntu-latest
    timeout-minutes: 20
    needs: [run-migrations]  # Деплоим только после успешных миграций

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: "--prod"

      - name: Notify team on success
        if: success()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "✅ Production deploy successful: ${{ github.sha }}",
              "channel": "#deployments"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}

      - name: Notify team on failure
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "❌ Production deploy failed! Check: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}",
              "channel": "#deployments"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
```

### Dependabot для автоматических обновлений

```yaml
# .github/dependabot.yml
version: 2
updates:
  # npm зависимости
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "09:00"
      timezone: "Europe/Moscow"
    open-pull-requests-limit: 5
    groups:
      # Группируем minor/patch обновления
      next-ecosystem:
        patterns:
          - "next"
          - "react"
          - "react-dom"
          - "@types/react*"
        update-types:
          - "minor"
          - "patch"
      drizzle:
        patterns:
          - "drizzle-*"
        update-types:
          - "minor"
          - "patch"
      testing:
        patterns:
          - "vitest"
          - "@vitest/*"
          - "playwright"
          - "@playwright/*"
        update-types:
          - "minor"
          - "patch"
    ignore:
      # Пропускаем major версии — обновляем вручную
      - dependency-name: "*"
        update-types: ["version-update:semver-major"]
    labels:
      - "dependencies"
      - "automated"

  # GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
    labels:
      - "dependencies"
      - "github-actions"
```

### Secrets Management

Список всех необходимых GitHub Secrets:

```bash
# Через GitHub CLI
gh secret set DATABASE_URL_CI --body "postgresql://test:test@..."
gh secret set DATABASE_URL_UNPOOLED --body "postgresql://postgres:..."
gh secret set AUTH_SECRET_CI --body "min-32-chars-secret-for-ci"
gh secret set VERCEL_TOKEN --body "..."
gh secret set VERCEL_ORG_ID --body "team_..."
gh secret set VERCEL_PROJECT_ID --body "prj_..."
gh secret set STRIPE_PUBLISHABLE_KEY_TEST --body "pk_test_..."
gh secret set CODECOV_TOKEN --body "..."
gh secret set SLACK_WEBHOOK_URL --body "https://hooks.slack.com/..."

# Просмотреть список secrets (без значений)
gh secret list
```

```typescript
// В GitHub Actions secrets НИКОГДА не попадают в логи
// Даже если попытаться напечатать:
// run: echo "${{ secrets.DATABASE_URL }}"
// Вывод: echo "***"

// Для environment-specific secrets используй GitHub Environments:
// Settings → Environments → production → Environment secrets
// Это позволяет защитить production secrets с required reviewers
```

### Матричное тестирование

```yaml
# .github/workflows/matrix-tests.yml
name: Matrix Tests

on:
  pull_request:
    branches: [main]

jobs:
  test-matrix:
    name: Test (Node ${{ matrix.node-version }})
    runs-on: ubuntu-latest
    timeout-minutes: 15

    strategy:
      matrix:
        node-version: ["18", "20", "22"]
      fail-fast: false  # Продолжать другие jobs даже если один упал

    steps:
      - uses: actions/checkout@v4

      - name: Setup pnpm
        uses: pnpm/action-setup@v4
        with:
          version: "9"

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: "pnpm"

      - run: pnpm install --frozen-lockfile
      - run: pnpm test:unit --run
```

### Интеграция с Vercel Deploy Hooks

```yaml
# .github/workflows/deploy-preview.yml
name: Deploy Preview

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  deploy-preview:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Vercel preview deploy
        run: |
          curl -X POST "${{ secrets.VERCEL_DEPLOY_HOOK_PREVIEW }}"

      # Vercel автоматически создаст preview и обновит deployment_status,
      # что запустит e2e-tests.yml workflow
```

## Пример кода

### Reusable workflow для проверок

```yaml
# .github/workflows/reusable-checks.yml
name: Reusable Checks

on:
  workflow_call:
    inputs:
      node-version:
        required: false
        type: string
        default: "20"
      run-build:
        required: false
        type: boolean
        default: true
    secrets:
      DATABASE_URL_CI:
        required: true
      AUTH_SECRET_CI:
        required: true

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: "9"
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: "pnpm"
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm tsc --noEmit
      - run: pnpm test:unit --run
      - if: inputs.run-build
        run: pnpm build
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL_CI }}
          AUTH_SECRET: ${{ secrets.AUTH_SECRET_CI }}
```

## Антипаттерн

```yaml
# ПЛОХО: хранить секреты в коде workflow
- name: Connect to DB
  run: pnpm db:migrate
  env:
    DATABASE_URL: "postgresql://postgres:hardcodedpassword@host/db"  # НИКОГДА

# ПЛОХО: не кэшировать зависимости
- run: pnpm install  # без cache: "pnpm" — медленно на каждом запуске

# ПЛОХО: запускать E2E на localhost вместо реального preview
- run: pnpm build && pnpm start &
  # Лучше использовать реальный Vercel preview URL

# ПЛОХО: не использовать concurrency groups
# Без cancel-in-progress каждый push создаёт новый workflow run,
# старые продолжают работать впустую

# ХОРОШО: всегда устанавливать timeout-minutes
# Без него зависший тест может занимать resources 6 часов
```

## Связанные документы

- `knowledge/custom/10-devops/vercel-deploy.md` — Vercel deploy hooks и preview деплои
- `knowledge/custom/10-devops/railway-infra.md` — тестовая БД в CI
- `knowledge/custom/05-testing/` — настройка Vitest и Playwright

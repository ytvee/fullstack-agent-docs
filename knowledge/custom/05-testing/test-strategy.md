---
category: testing
topic: test-strategy
status: draft
---

## Проблема / Контекст

Next.js 15 App Router introduces Server Components, Server Actions, and Route Handlers — constructs that don't exist in traditional React SPAs. Standard testing guidance (e.g., react-testing-library DOM tests) covers only part of the surface area. Without a deliberate strategy you end up either overtesting UI pixels, or undertesting the business logic that actually runs on the server and touches the database.

The project stack (Vitest, Playwright, MSW, Drizzle, Auth.js v5) covers three distinct testing layers, each with a different cost/confidence trade-off.

---

## Решение

### Three-Layer Testing Pyramid

```
        /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
       /   E2E (Playwright)  \    ← few, slow, high confidence
      /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
     /  Integration (Vitest+MSW) \  ← moderate, medium speed
    /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
   /    Unit (Vitest, pure logic)   \  ← many, fast, narrow scope
  /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
```

---

### Layer 1 — Unit Tests (Vitest)

**What to test:**
- Pure utility functions (`lib/utils.ts`, `lib/formatters.ts`)
- Zod schema validation (all `schemas/*.ts` files)
- Business logic helpers that have no I/O
- Date/price calculations

**What NOT to test:**
- React components with no logic (just markup)
- Next.js framework internals
- Third-party library behavior
- Auto-generated Drizzle schema types

**File naming:** `*.unit.test.ts` or `__tests__/unit/`

---

### Layer 2 — Integration Tests (Vitest + MSW)

**What to test:**
- Server Actions: auth guard, Zod validation, DB writes, return values
- Route Handlers: request parsing, response shape, status codes
- Drizzle queries against a real test database
- Email sending (MSW intercepts Resend HTTP calls)
- Stripe webhook handlers (MSW intercepts Stripe verification)

**What NOT to test:**
- Next.js request/response wiring itself
- React rendering of Server Components (too expensive, low ROI)
- Playwright-level flows (auth + checkout in one go)

**File naming:** `*.integration.test.ts` or `__tests__/integration/`

---

### Layer 3 — E2E Tests (Playwright)

**What to test (critical paths only):**
1. Auth flow: sign-up, email verification, sign-in, sign-out
2. OAuth flow: Google sign-in (Playwright mocks OAuth provider)
3. Checkout: add to cart → Stripe checkout → webhook → order created
4. Core CRUD that generates revenue or user data
5. Role-based access: ensure `/admin` is inaccessible to regular users

**What NOT to test in E2E:**
- Every form validation message (unit test the schema)
- Every API response shape (integration test the handler)
- Visual design / pixel diffing (separate tool)

**File naming:** `tests/e2e/*.spec.ts`

---

## Пример кода

### vitest.config.ts

```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";
import path from "path";

export default defineConfig({
  test: {
    globals: true,
    environment: "node",
    setupFiles: ["./tests/setup/vitest.setup.ts"],
    include: [
      "**/*.unit.test.ts",
      "**/*.integration.test.ts",
    ],
    exclude: [
      "node_modules",
      "tests/e2e/**",
      ".next/**",
    ],
    coverage: {
      provider: "v8",
      reporter: ["text", "json", "html", "lcov"],
      reportsDirectory: "./coverage",
      exclude: [
        "*.config.*",
        "**/*.d.ts",
        "**/types/**",
        "drizzle/**",          // generated migrations
        ".next/**",
        "tests/**",
        "**/__mocks__/**",
      ],
    },
    // Separate pools so unit tests don't share DB state with integration
    poolOptions: {
      forks: {
        singleFork: true,      // integration tests run serially to avoid DB race conditions
      },
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "@/db": path.resolve(__dirname, "./src/db"),
      "@/lib": path.resolve(__dirname, "./src/lib"),
      "@/schemas": path.resolve(__dirname, "./src/schemas"),
      "@/actions": path.resolve(__dirname, "./src/actions"),
    },
  },
});
```

### tests/setup/vitest.setup.ts

```typescript
// tests/setup/vitest.setup.ts
import { beforeAll, afterAll, afterEach } from "vitest";
import { server } from "../mocks/server";

// MSW: start mock service worker for integration tests
beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

### tests/setup/db.setup.ts — Test database with Drizzle

```typescript
// tests/setup/db.setup.ts
import { drizzle } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import { migrate } from "drizzle-orm/postgres-js/migrator";
import * as schema from "@/db/schema";

// Use a separate test database — never the development DB
const TEST_DATABASE_URL = process.env.TEST_DATABASE_URL;
if (!TEST_DATABASE_URL) {
  throw new Error("TEST_DATABASE_URL must be set for integration tests");
}

const connection = postgres(TEST_DATABASE_URL, { max: 1 });
export const testDb = drizzle(connection, { schema });

export async function runMigrations() {
  await migrate(testDb, { migrationsFolder: "./drizzle" });
}

export async function cleanDatabase() {
  // Delete in reverse dependency order to respect FK constraints
  await testDb.delete(schema.orderItems);
  await testDb.delete(schema.orders);
  await testDb.delete(schema.sessions);
  await testDb.delete(schema.accounts);
  await testDb.delete(schema.users);
}

export async function closeConnection() {
  await connection.end();
}
```

### Unit test example — Zod schema

```typescript
// src/schemas/product.unit.test.ts
import { describe, it, expect } from "vitest";
import { createProductSchema } from "./product";

describe("createProductSchema", () => {
  it("accepts valid product data", () => {
    const result = createProductSchema.safeParse({
      name: "Widget Pro",
      priceInCents: 4999,
      slug: "widget-pro",
      stock: 10,
    });
    expect(result.success).toBe(true);
  });

  it("rejects negative price", () => {
    const result = createProductSchema.safeParse({
      name: "Widget",
      priceInCents: -1,
      slug: "widget",
      stock: 5,
    });
    expect(result.success).toBe(false);
    expect(result.error?.issues[0].path).toContain("priceInCents");
  });

  it("rejects slug with spaces", () => {
    const result = createProductSchema.safeParse({
      name: "Widget",
      priceInCents: 100,
      slug: "my widget",
      stock: 1,
    });
    expect(result.success).toBe(false);
    expect(result.error?.issues[0].path).toContain("slug");
  });
});
```

### Integration test example — Server Action

```typescript
// src/actions/product.integration.test.ts
import { describe, it, expect, beforeAll, afterAll, afterEach } from "vitest";
import { createProduct } from "./product";
import { testDb, runMigrations, cleanDatabase, closeConnection } from "../../tests/setup/db.setup";
import { users } from "@/db/schema";

// Override the module's db import to use testDb
vi.mock("@/db", () => ({ db: testDb }));

// Mock Auth.js session
vi.mock("@/auth", () => ({
  auth: vi.fn(),
}));

import { auth } from "@/auth";

const mockAdminSession = {
  user: { id: "user-1", email: "admin@test.com", role: "admin" },
  expires: new Date(Date.now() + 1000 * 60 * 60).toISOString(),
};

beforeAll(async () => {
  await runMigrations();
  // Seed a user for FK constraints
  await testDb.insert(users).values({
    id: "user-1",
    email: "admin@test.com",
    role: "admin",
  });
});

afterEach(async () => {
  // Clean only the table under test, keep seed user
  await testDb.delete(schema.products);
});

afterAll(async () => {
  await cleanDatabase();
  await closeConnection();
});

describe("createProduct server action", () => {
  it("returns error when unauthenticated", async () => {
    vi.mocked(auth).mockResolvedValueOnce(null);

    const result = await createProduct({
      name: "Test",
      priceInCents: 100,
      slug: "test",
      stock: 1,
    });

    expect(result.success).toBe(false);
    expect(result.error).toBe("Unauthorized");
  });

  it("creates product when admin is authenticated", async () => {
    vi.mocked(auth).mockResolvedValueOnce(mockAdminSession);

    const result = await createProduct({
      name: "New Widget",
      priceInCents: 2999,
      slug: "new-widget",
      stock: 5,
    });

    expect(result.success).toBe(true);
    expect(result.data?.slug).toBe("new-widget");

    // Verify it actually persisted to the test DB
    const rows = await testDb.query.products.findMany();
    expect(rows).toHaveLength(1);
    expect(rows[0].slug).toBe("new-widget");
  });

  it("returns validation error for duplicate slug", async () => {
    vi.mocked(auth).mockResolvedValue(mockAdminSession);

    await createProduct({ name: "A", priceInCents: 100, slug: "dup", stock: 1 });
    const result = await createProduct({ name: "B", priceInCents: 200, slug: "dup", stock: 2 });

    expect(result.success).toBe(false);
    expect(result.error).toMatch(/slug/i);
  });
});
```

### playwright.config.ts

```typescript
// playwright.config.ts
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests/e2e",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ["html", { outputFolder: "playwright-report" }],
    ["junit", { outputFile: "test-results/junit.xml" }],
  ],
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL ?? "http://localhost:3000",
    trace: "on-first-retry",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
  projects: [
    // Desktop Chrome — primary
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
    // Mobile viewport — critical for responsive checkout
    {
      name: "mobile-chrome",
      use: { ...devices["Pixel 7"] },
      testMatch: ["**/checkout.spec.ts", "**/auth.spec.ts"],
    },
    // Safari — for payment sheet quirks
    {
      name: "webkit",
      use: { ...devices["Desktop Safari"] },
      testMatch: ["**/checkout.spec.ts"],
    },
  ],
  // Start the Next.js dev server automatically in CI
  webServer: {
    command: "pnpm build && pnpm start",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
    env: {
      DATABASE_URL: process.env.TEST_DATABASE_URL!,
      NEXTAUTH_SECRET: "test-secret-32-chars-minimum-here",
      NEXTAUTH_URL: "http://localhost:3000",
    },
  },
});
```

### E2E test example — auth flow

```typescript
// tests/e2e/auth.spec.ts
import { test, expect } from "@playwright/test";
import { createTestUser, deleteTestUser } from "../helpers/db";

test.describe("Authentication flow", () => {
  const testEmail = `e2e-${Date.now()}@test.com`;
  const testPassword = "SecurePassword123!";

  test.afterAll(async () => {
    await deleteTestUser(testEmail);
  });

  test("user can sign up and sign in", async ({ page }) => {
    // Sign up
    await page.goto("/sign-up");
    await page.getByLabel("Email").fill(testEmail);
    await page.getByLabel("Password").fill(testPassword);
    await page.getByRole("button", { name: "Create account" }).click();

    // Should redirect to dashboard or email verification page
    await expect(page).toHaveURL(/\/(dashboard|verify-email)/);

    // Sign out
    await page.getByRole("button", { name: "Sign out" }).click();
    await expect(page).toHaveURL("/");

    // Sign back in
    await page.goto("/sign-in");
    await page.getByLabel("Email").fill(testEmail);
    await page.getByLabel("Password").fill(testPassword);
    await page.getByRole("button", { name: "Sign in" }).click();
    await expect(page).toHaveURL("/dashboard");
  });

  test("protected route redirects unauthenticated users", async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page).toHaveURL(/\/sign-in/);
    // Should preserve intended destination
    await expect(page.url()).toContain("callbackUrl");
  });
});
```

### MSW server setup

```typescript
// tests/mocks/server.ts
import { setupServer } from "msw/node";
import { resendHandlers } from "./handlers/resend";
import { stripeHandlers } from "./handlers/stripe";
import { uploadthingHandlers } from "./handlers/uploadthing";

export const server = setupServer(
  ...resendHandlers,
  ...stripeHandlers,
  ...uploadthingHandlers
);

// tests/mocks/handlers/resend.ts
import { http, HttpResponse } from "msw";

export const resendHandlers = [
  http.post("https://api.resend.com/emails", () => {
    return HttpResponse.json({ id: "mock-email-id-123" });
  }),
];
```

---

## Антипаттерн

```typescript
// BAD: Testing every shadcn/ui component render — wastes time, tests library not your code
it("renders the button", () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText("Click me")).toBeInTheDocument();
});

// BAD: Mocking the entire DB and testing no real SQL
vi.mock("@/db", () => ({
  db: { insert: vi.fn().mockResolvedValue([{ id: "1" }]) },
}));
// This test proves nothing — it just runs your mock back at you.

// BAD: One massive E2E test that tests 15 things
test("everything works", async ({ page }) => {
  // 200 lines testing sign up + product create + checkout + admin + settings
  // When it breaks you have no idea which part failed
});

// GOOD: Focused integration test with real test DB
it("createProduct writes to DB with correct FK", async () => {
  vi.mocked(auth).mockResolvedValueOnce(mockAdminSession);
  const result = await createProduct({ ... });
  const rows = await testDb.query.products.findMany();
  expect(rows[0].createdById).toBe("user-1");
});
```

---

## Связанные документы

- `knowledge/custom/05-testing/coverage-rules.md` — thresholds and CI coverage gate
- `knowledge/custom/06-security/server-action-validation.md` — what to validate in Server Actions
- `knowledge/custom/02-patterns/server-actions.md` — Server Action patterns being tested
- `knowledge/custom/02-patterns/route-handlers.md` — Route Handler patterns being tested

# SQLite (/docs/orm/core-concepts/supported-databases/sqlite)



Prisma ORM supports SQLite and SQLite-compatible databases. This includes local SQLite files, Turso's distributed libSQL, and Cloudflare's serverless D1.

Setup [#setup]

Configure the SQLite provider in your Prisma schema:

```prisma title="schema.prisma"
datasource db {
  provider = "sqlite"
}
```

Set the connection URL in `prisma.config.ts`:

```typescript title="prisma.config.ts"
import { defineConfig } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  datasource: {
    url: "file:./dev.db", // or libsql:// for Turso
  },
});
```

Using driver adapters [#using-driver-adapters]

Instead of Prisma's built-in driver, you can use JavaScript database drivers via [driver adapters](/orm/core-concepts/supported-databases/database-drivers#driver-adapters):

**Local SQLite with `better-sqlite3`:**

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm install @prisma/adapter-better-sqlite3
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add @prisma/adapter-better-sqlite3
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add @prisma/adapter-better-sqlite3
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add @prisma/adapter-better-sqlite3
    ```
  </CodeBlockTab>
</CodeBlockTabs>

```ts
import { PrismaBetterSqlite3 } from "@prisma/adapter-better-sqlite3";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaBetterSqlite3({ url: "file:./prisma/dev.db" });
const prisma = new PrismaClient({ adapter });
```

**Turso with `@prisma/adapter-libsql`:**

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm install @prisma/adapter-libsql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add @prisma/adapter-libsql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add @prisma/adapter-libsql
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add @prisma/adapter-libsql
    ```
  </CodeBlockTab>
</CodeBlockTabs>

```ts
import { PrismaLibSQL } from "@prisma/adapter-libsql";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaLibSQL({
  url: process.env.TURSO_DATABASE_URL,
  authToken: process.env.TURSO_AUTH_TOKEN,
});
const prisma = new PrismaClient({ adapter });
```

**Cloudflare D1 with `@prisma/adapter-d1`:**

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm install @prisma/adapter-d1
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add @prisma/adapter-d1
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add @prisma/adapter-d1
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add @prisma/adapter-d1
    ```
  </CodeBlockTab>
</CodeBlockTabs>

```ts
import { PrismaD1 } from "@prisma/adapter-d1";
import { PrismaClient } from "./generated/prisma";

const adapter = new PrismaD1(env.DB); // D1 binding in Workers
const prisma = new PrismaClient({ adapter });
```

Supported variants [#supported-variants]

Local SQLite [#local-sqlite]

Standard SQLite database files (`.db`). Connection URL format: `file:./path/to/database.db`

* Use `prisma migrate dev` for schema changes
* Store database file anywhere in your filesystem
* Best for development and small applications

Turso (libSQL) [#turso-libsql]

Edge-hosted, distributed SQLite-compatible database.

* Connection URL format: `libsql://[hostname]`
* Requires authentication token
* Supports embedded replicas for faster local reads
* Use local SQLite file + Turso CLI for migrations (see [Turso docs](https://docs.turso.tech/))

**Key differences:**

* Remote access over HTTP
* Replication and automated backups
* Schema changes via `prisma migrate diff` + Turso CLI

Cloudflare D1 [#cloudflare-d1]

Serverless SQLite database for Cloudflare Workers.

* Automatic read-replication across regions
* Schema changes via Wrangler CLI + `prisma migrate diff`
* Local (`.wrangler/state`) and remote versions available

**Key differences:**

* No transaction support currently
* Migrations via Wrangler: `wrangler d1 migrations apply`
* Deploy with Cloudflare Workers

Type mappings [#type-mappings]

| Prisma ORM | SQLite    |
| ---------- | --------- |
| `String`   | `TEXT`    |
| `Boolean`  | `BOOLEAN` |
| `Int`      | `INTEGER` |
| `BigInt`   | `INTEGER` |
| `Float`    | `REAL`    |
| `Decimal`  | `DECIMAL` |
| `DateTime` | `NUMERIC` |
| `Json`     | `JSONB`   |
| `Bytes`    | `BLOB`    |
| `Enum`     | `TEXT`    |

<CalloutContainer type="info">
  <CalloutDescription>
    SQLite stores booleans as `0` (false) or `1` (true). Learn more about [SQLite type affinity](https://www.sqlite.org/datatype3.html#boolean).
  </CalloutDescription>
</CalloutContainer>

Common considerations [#common-considerations]

**Timestamp format with driver adapters:**

Configure how `DateTime` values are stored:

```ts
const adapter = new PrismaBetterSqlite3(
  { url: "file:./dev.db" },
  { timestampFormat: "unixepoch-ms" } // For backward compatibility
);
```

* **ISO 8601 (default)**: Best for new projects
* **`unixepoch-ms`**: Required for migrating from Prisma's native driver

**Enum validation:**

SQLite doesn't enforce enum values at the database level. Invalid values will cause Prisma Client queries to fail at runtime.

**Integer overflow:**

Prisma ORM validates that numbers fit within integer boundaries. If a value exceeds limits, you'll get a P2023 error.

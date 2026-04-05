### `dbCredentials`
<rem025/>

Database connection credentials in a form of `url`, 
`user:password@host:port/db` params or exceptions drivers(<Drivers/>) specific connection options.

|               |                      |
| :------------ | :-----------------   |
| type          | union of drivers connection options |
| default       | --                    |
| commands      | `migrate` `push` `pull`   |

<rem025/>

<CodeTabs items={["PostgreSQL", "MySQL", "SQLite", "Turso", "Cloudflare D1", "AWS Data API", "PGLite"]}>
<Section>
```ts
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    url: "postgres://user:password@host:port/db",
  }
});
```
```ts
import { defineConfig } from 'drizzle-kit'

// via connection params
export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    host: "host",
    port: 5432,
    user: "user",
    password: "password",
    database: "dbname",
    ssl: true, // can be boolean | "require" | "allow" | "prefer" | "verify-full" | options from node:tls
  }
});
```
</Section>
<Section>
```ts
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "mysql",
  dbCredentials: {
    url: "mysql://user:password@host:port/db",
  }
});
```
```ts
import { defineConfig } from 'drizzle-kit'

// via connection params
export default defineConfig({
  dialect: "mysql",
  dbCredentials: {
    host: "host",
    port: 5432,
    user: "user",
    password: "password",
    database: "dbname",
    ssl: "...", // can be: string | SslOptions (ssl options from mysql2 package)
  }
});
```
</Section>
```ts
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "sqlite",
  dbCredentials: {
    url: ":memory:", // inmemory database
    // or
    url: "sqlite.db", 
    // or
    url: "file:sqlite.db" // file: prefix is required by libsql
  }
});
```
```ts
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "turso",
  dbCredentials: {
    url: "libsql://acme.turso.io" // remote Turso database url
    authToken: "...",

    // or if you need local db

    url: ":memory:", // inmemory database
    // or
    url: "file:sqlite.db", // file: prefix is required by libsql
  }
});
```
```ts
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "sqlite",
  driver: "d1-http",
  dbCredentials: {
    accountId: "",
    databaseId: "",
    token: "",
  }
});
```
```ts
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "postgresql",
  driver: "aws-data-api",
  dbCredentials: {
    database: "database",
    resourceArn: "resourceArn",
    secretArn: "secretArn",
  },
});
```
```ts
import { defineConfig } from 'drizzle-kit'

export default defineConfig({
  dialect: "postgresql",
  driver: "pglite",
  dbCredentials: {
    url: "./database/", // database folder path
  }
});
```
</CodeTabs>


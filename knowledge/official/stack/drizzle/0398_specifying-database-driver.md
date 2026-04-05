### Specifying database driver
<Callout type="warning">
**Expo SQLite** and **OP SQLite** are on-device(per-user) databases, there's no way to `pull` database schema from there.<br/>
For embedded databases Drizzle provides **embedded migrations** - check out our [get started](/docs/get-started/expo-new) guide.
</Callout>
Drizzle Kit does not come with a pre-bundled database driver, 
it will automatically pick available database driver from your current project based on the `dialect` - [see discussion](https://github.com/drizzle-team/drizzle-orm/discussions/2203).

Mostly all drivers of the same dialect share the same set of connection params, 
as for exceptions like `aws-data-api`, `pglight` and `d1-http` - you will have to explicitely specify `driver` param.

<CodeTabs items={["AWS Data API", "PGLite", "Cloudflare D1 HTTP"]}>
```ts {6}
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  driver: "aws-data-api",
  dbCredentials: {
    database: "database",
    resourceArn: "resourceArn",
    secretArn: "secretArn",
  },
};
```
```ts {6}
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  driver: "pglite",
  dbCredentials: {
    // inmemory
    url: ":memory:"
    
    // or database folder
    url: "./database/"
  },
};
```
```ts {6}
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "sqlite",
  driver: "d1-http",
  dbCredentials: {
    accountId: "accountId",
    databaseId: "databaseId",
    token: "token",
  },
};
```
</CodeTabs>


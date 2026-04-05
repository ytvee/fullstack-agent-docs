# Database connection with Drizzle
Drizzle ORM runs SQL queries on your database via **database drivers**.
<CodeTabs items={["index.ts", "schema.ts"]}>

<CodeTab>
```ts
import { drizzle } from "drizzle-orm/node-postgres"
import { users } from "./schema"

const db = drizzle(process.env.DATABASE_URL);
const usersCount = await db.$count(users);
```
```  
                        ┌──────────────────────┐
                        │   db.$count(users)   │ <--- drizzle query
                        └──────────────────────┘     
                            │               ʌ
select count(*) from users -│               │
                            │               │- [{ count: 0 }]
                            v               │
                         ┌─────────────────────┐
                         │    node-postgres    │ <--- database driver
                         └─────────────────────┘
                            │               ʌ
01101000 01100101 01111001 -│               │
                            │               │- 01110011 01110101 01110000
                            v               │
                         ┌────────────────────┐
                         │      Database      │ 
                         └────────────────────┘
```
</CodeTab>

```ts
import { pgTable, integer, text } from "drizzle-orm";

export const users = pgTable("users", {
  id: integer("id").generateAlwaysAsIdentity(),
  name: text("name"),
})
```
</CodeTabs>

Under the hood Drizzle will create a **node-postgres** driver instance which you can access via `db.$client` if necessary
<Section>
```ts
import { drizzle } from "drizzle-orm/node-postgres"

const db = drizzle(process.env.DATABASE_URL);
const pool = db.$client;
```
```ts
// above is equivalent to
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });
```
</Section>

Drizzle is by design natively compatible with every **edge** or **serverless** runtime, whenever you'd need access to a serverless database - we've got you covered

<CodeTabs items={["Neon HTTP", "Neon with websockets", "Vercel Postgres", "PlanetScale HTTP", "Cloudflare d1"]}>
```ts
import { drizzle } from "drizzle-orm/neon-http";

const db = drizzle(process.env.DATABASE_URL);
```
```ts
import { drizzle } from "drizzle-orm/neon-serverless";

const db = drizzle(process.env.DATABASE_URL);
```
```ts
import { drizzle } from "drizzle-orm/vercel-postgres";

const db = drizzle();
```
```ts
import { drizzle } from "drizzle-orm/planetscale";

const db = drizzle(process.env.DATABASE_URL);
```
```ts
import { drizzle } from "drizzle-orm/d1";

const db = drizzle({ connection: env.DB });
```
</CodeTabs>

And yes, we do support runtime specific drivers like [Bun SQLite](/docs/connect-bun-sqlite) or [Expo SQLite](/docs/connect-expo-sqlite):
<Section>
```ts
import { drizzle } from "drizzle-orm/bun-sqlite"

const db = drizzle(); // <--- will create an in-memory db
const db = drizzle("./sqlite.db");
```
```ts
import { drizzle } from "drizzle-orm/expo-sqlite";
import { openDatabaseSync } from "expo-sqlite";

const expo = openDatabaseSync("db.db");
const db = drizzle(expo);
```
</Section>


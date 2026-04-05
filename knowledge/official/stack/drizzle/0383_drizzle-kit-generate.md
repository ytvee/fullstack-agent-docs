# `drizzle-kit generate` 

<Prerequisites>
- Get started with Drizzle and `drizzle-kit` - [read here](/docs/get-started)
- Drizzle schema fundamentals - [read here](/docs/sql-schema-declaration)
- Database connection basics - [read here](/docs/connect-overview)
- Drizzle migrations fundamentals - [read here](/docs/migrations)
- Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file)
</Prerequisites>


<br/>

`drizzle-kit generate` lets you generate SQL migrations based on your Drizzle schema upon declaration or on subsequent schema changes.
<Callout collapsed="How it works under the hood?">
Drizzle Kit `generate` command triggers a sequence of events:
1. It will read through your Drizzle schema file(s) and compose a json snapshot of your schema
2. It will read through your previous migrations folders and compare current json snapshot to the most recent one
3. Based on json differences it will generate SQL migrations
4. Save `migration.sql` and `snapshot.json` in migration folder under current timestamp

<Section>
```typescript filename="src/schema.ts"
import * as p from "./drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(), 
};
```
```                                  
┌────────────────────────┐                  
│ $ drizzle-kit generate │                  
└─┬──────────────────────┘                  
  │                                           
  └ 1. read previous migration folders
    2. find diff between current and previous schema
    3. prompt developer for renames if necessary
  ┌ 4. generate SQL migration and persist to file
  │    ┌─┴───────────────────────────────────────┐  
  │      📂 drizzle       
  │      └ 📂 20242409125510_premium_mister_fear
  │        ├ 📜 migration.sql
  │        └ 📜 snapshot.json
  v
```
```sql
-- drizzle/20242409125510_premium_mister_fear/migration.sql

CREATE TABLE "users" (
 "id" SERIAL PRIMARY KEY,
 "name" TEXT,
 "email" TEXT UNIQUE
);
```
</Section>
</Callout>

It's designed to cover [code first](/docs/migrations) approach of managing Drizzle migrations. 
You can apply generated migrations using [`drizzle-kit migrate`](/docs/drizzle-kit-migrate), using drizzle-orm's `migrate()`, 
using external migration tools like [bytebase](https://www.bytebase.com/) or running migrations yourself directly on the database. 

`drizzle-kit generate` command requires you to provide both `dialect` and `schema` path options, 
you can set them either via [drizzle.config.ts](/docs/drizzle-config-file) config file or via CLI options
<CodeTabs items={["With config file", "As CLI options"]}>
<Section>
```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
});
```
```shell
npx drizzle-kit generate
```
</Section>

```shell
npx drizzle-kit generate --dialect=postgresql --schema=./src/schema.ts
```
</CodeTabs>


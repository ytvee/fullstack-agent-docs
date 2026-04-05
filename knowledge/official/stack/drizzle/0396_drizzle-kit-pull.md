# `drizzle-kit pull`

<Prerequisites>
- Get started with Drizzle and `drizzle-kit` - [read here](/docs/get-started)
- Drizzle schema fundamentals - [read here](/docs/sql-schema-declaration) 
- Database connection basics - [read here](/docs/connect-overview) 
- Drizzle migrations fundamentals - [read here](/docs/migrations) 
- Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file) docs
</Prerequisites>

`drizzle-kit pull` lets you literally pull(introspect) your existing database schema and generate `schema.ts` drizzle schema file, 
it is designed to cover [database first](/docs/migrations) approach of Drizzle migrations.

<Callout collapsed="How it works under the hood?">
When you run Drizzle Kit `pull` command it will:
1. Pull database schema(DDL) from your existing database
2. Generate `schema.ts` drizzle schema file and save it to `out` folder

<Section>
```
                                  ┌────────────────────────┐      ┌─────────────────────────┐ 
                                  │                        │ <---  CREATE TABLE "users" (
┌──────────────────────────┐      │                        │        "id" SERIAL PRIMARY KEY,
│ ~ drizzle-kit pull       │      │                        │        "name" TEXT,
└─┬────────────────────────┘      │        DATABASE        │        "email" TEXT UNIQUE
  │                               │                        │       );
  └ Pull datatabase schema -----> │                        │
  ┌ Generate Drizzle       <----- │                        │
  │ schema TypeScript file        └────────────────────────┘
  │
  v
```
```typescript
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
  email: p.text().unique(), 
};
```
</Section>
</Callout>

It is a great approach if you need to manage database schema outside of your TypeScript project or 
you're using database, which is managed by somebody else.

<br/>
<hr/>
<br/>

`drizzle-kit pull` requires you to specify `dialect` and either
database connection `url` or `user:password@host:port/db` params, you can provide them
either via [drizzle.config.ts](/docs/drizzle-config-file) config file or via CLI options:

<CodeTabs items={["With config file", "With CLI options"]}>
<Section>
```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname",
  },
});
```
```shell
npx drizzle-kit pull
```
</Section>

```shell
npx drizzle-kit pull --dialect=postgresql --url=postgresql://user:password@host:port/dbname
```
</CodeTabs>


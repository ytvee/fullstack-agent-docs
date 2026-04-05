# `drizzle-kit push`

<Prerequisites>
- Get started with Drizzle and `drizzle-kit` - [read here](/docs/get-started)
- Drizzle schema fundamentals - [read here](/docs/sql-schema-declaration) 
- Database connection basics - [read here](/docs/connect-overview) 
- Drizzle migrations fundamentals - [read here](/docs/migrations) 
- Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file) docs
</Prerequisites>


`drizzle-kit push` lets you literally push your schema and subsequent schema changes directly to the
database while omitting SQL files generation, it's designed to cover [code first](/docs/migrations)
approach of Drizzle migrations.

<Callout collapsed="How it works under the hood?">
When you run Drizzle Kit `push` command it will:
1. Read through your Drizzle schema file(s) and compose a json snapshot of your schema
2. Pull(introspect) database schema 
3. Based on differences between those two it will generate SQL migrations
4. Apply SQL migrations to the database

<Section>
```typescript filename="src/schema.ts"
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
};
```
```
┌─────────────────────┐                  
│ ~ drizzle-kit push  │                  
└─┬───────────────────┘                  
  │                                           ┌──────────────────────────┐
  └ Pull current datatabase schema ---------> │                          │
                                              │                          │
  ┌ Generate alternations based on diff <---- │         DATABASE         │
  │                                           │                          │
  └ Apply migrations to the database -------> │                          │
                                       │      └──────────────────────────┘
                                       │
  ┌────────────────────────────────────┴────────────────┐
   create table users(id serial primary key, name text);
```
</Section>
</Callout>

It's the best approach for rapid prototyping and we've seen dozens of teams
and solo developers successfully using it as a primary migrations flow in their production applications.
It pairs exceptionally well with blue/green deployment strategy and serverless databases like
[Planetscale](https://planetscale.com), [Neon](https://neon.tech), [Turso](https://turso.tech/drizzle) and others.

<br/>
<hr/>
<br/>


`drizzle-kit push` requires you to specify `dialect`, path to the `schema` file(s) and either
database connection `url` or `user:password@host:port/db` params, you can provide them
either via [drizzle.config.ts](/docs/drizzle-config-file) config file or via CLI options:

<CodeTabs items={["With config file", "With CLI options"]}>
<Section>
```ts
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname",
  },
});
```
```shell
npx drizzle-kit push
```
</Section>

```shell
npx drizzle-kit push --dialect=postgresql --schema=./src/schema.ts --url=postgresql://user:password@host:port/dbname
```

</CodeTabs>


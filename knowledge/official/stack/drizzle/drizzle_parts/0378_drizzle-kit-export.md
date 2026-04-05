# `drizzle-kit export` 

<Prerequisites>
- Get started with Drizzle and `drizzle-kit` - [read here](/docs/get-started)
- Drizzle schema fundamentals - [read here](/docs/sql-schema-declaration)
- Database connection basics - [read here](/docs/connect-overview)
- Drizzle migrations fundamentals - [read here](/docs/migrations)
- Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file)
</Prerequisites>


<br/>

`drizzle-kit export` lets you export SQL representation of Drizzle schema and print in console SQL DDL representation on it.
<Callout collapsed="How it works under the hood?">
Drizzle Kit `export` command triggers a sequence of events:
1. It will read through your Drizzle schema file(s) and compose a json snapshot of your schema
3. Based on json differences it will generate SQL DDL statements
4. Output SQL DDL statements to console
</Callout>

It's designed to cover [codebase first](/docs/migrations) approach of managing Drizzle migrations. 
You can export the SQL representation of the Drizzle schema, allowing external tools like Atlas to handle all the migrations for you

`drizzle-kit export` command requires you to provide both `dialect` and `schema` path options, 
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
npx drizzle-kit export
```
</Section>

```shell
npx drizzle-kit export --dialect=postgresql --schema=./src/schema.ts
```
</CodeTabs>


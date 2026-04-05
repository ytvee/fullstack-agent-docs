# `drizzle-kit up`

<Prerequisites>
- Get started with Drizzle and `drizzle-kit` - [read here](/docs/get-started)
- Drizzle schema fundamentals - [read here](/docs/sql-schema-declaration)
- Database connection basics - [read here](/docs/connect-overview)
- Drizzle migrations fundamentals - [read here](/docs/migrations)
- Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file)
- `drizzle-kit generate` command - [read here](/docs/drizzle-kit-generate)
</Prerequisites>

`drizzle-kit up` command lets you upgrade drizzle schema snapshots to a newer version. 
It's required whenever we introduce breaking changes to the json snapshots of the schema and upgrade the internal version.

<br/>
<hr/>
<br/>

`drizzle-kit up` command requires you to specify both `dialect` and database connection credentials, 
you can provide them either via [drizzle.config.ts](/docs/drizzle-config-file) config file or via CLI options

<CodeTabs items={["With config file", "As CLI options"]}>
<Section>
```ts {5,8}
// drizzle.config.ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
});
```
```shell
npx drizzle-kit up
```
</Section>
```shell
npx drizzle-kit up --dialect=postgresql
```
</CodeTabs>


# `drizzle-kit check`

<Prerequisites>
- Get started with Drizzle and `drizzle-kit` - [read here](/docs/get-started)
- Drizzle schema fundamentals - [read here](/docs/sql-schema-declaration)
- Database connection basics - [read here](/docs/connect-overview)
- Drizzle migrations fundamentals - [read here](/docs/migrations)
- Drizzle Kit [overview](/docs/kit-overview) and [config file](/docs/drizzle-config-file)
- `drizzle-kit generate` command - [read here](/docs/drizzle-kit-generate)
</Prerequisites>

`drizzle-kit check` command lets you check consistency of your generated SQL migrations history.

That's extremely useful when you have multiple developers working on the project and 
altering database schema on different branches - read more about [migrations for teams](/docs/kit-migrations-for-teams).

<br/>
<hr/>
<br/>

`drizzle-kit check` command requires you to specify both `dialect` and database connection credentials, 
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
npx drizzle-kit check
```
</Section>
```shell
npx drizzle-kit check --dialect=postgresql
```
</CodeTabs>


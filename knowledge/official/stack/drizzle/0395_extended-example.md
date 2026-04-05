### Extended example
Let's generate SQL migration and apply it to our database using `drizzle-kit generate` and `drizzle-kit migrate` commands

```plaintext
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 src
 │ ├ 📜 schema.ts
 │ └ 📜 index.ts
 ├ 📜 drizzle.config.ts
 └ …
```
<CodeTabs items={["drizzle.config.ts", "src/schema.ts"]}>
```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname"
  },
  migrations: {
    table: 'journal', 
    schema: 'drizzle', 
  },
});
```
```ts 
import * as p from "drizzle-orm/pg-core";

export const users = p.pgTable("users", {
  id: p.serial().primaryKey(),
  name: p.text(),
})
```
</CodeTabs>

Now let's run
```shell
npx drizzle-kit generate --name=init
```
it will generate
<Section>
```plaintext {5}
📦 <project root>
 ├ …
 ├ 📂 migrations
 │ ├ 📂 20242409125510_init
 └ …
```
```sql
-- ./drizzle/0000_init.sql

CREATE TABLE "users"(
  id serial primary key,
  name text
)
```
</Section>

Now let's run
```shell
npx drizzle-kit migrate
```

and our SQL migration is now successfully applied to the database ✅


Source: https://orm.drizzle.team/docs/drizzle-kit-pull

import CodeTab from "@mdx/CodeTab.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from "@mdx/Section.astro";
import Tab from "@mdx/Tab.astro";
import Tabs from "@mdx/Tabs.astro";
import Callout from "@mdx/Callout.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import Drivers from "@mdx/Drivers.mdx"
import Dialects from "@mdx/Dialects.mdx"
import Npm from "@mdx/Npm.astro"
import Npx from "@mdx/Npx.astro"


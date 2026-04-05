### Extended example
Example of how to create a custom postgresql migration file named `0001_seed-users.sql` 
with Drizzle schema located in `./src/schema.ts` and migrations folder named `./migrations` instead of default `./drizzle`.

We will also place drizzle config file in the `configs` folder.

Let's create config file:

```plaintext {4}
📦 <project root>
 ├ 📂 migrations
 ├ 📂 configs
 │ └ 📜 drizzle.config.ts
 ├ 📂 src
 └ …
```
```ts filename='drizzle.config.ts'
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  out: "./migrations",
});
```

Now let's run
```shell
npx drizzle-kit generate --config=./configs/drizzle.config.ts --name=seed-users --custom
```
And it will successfully generate
<Section>
```plaintext {6}
📦 <project root>
 ├ …
 ├ 📂 migrations
 │ ├ 📂 20242409125510_init
 │ └ 📂 20242409125510_seed-users
 └ …
```
```sql
-- ./drizzle/20242409125510_seed-users/migration.sql

INSERT INTO "users" ("name") VALUES('Dan');
INSERT INTO "users" ("name") VALUES('Andrew');
INSERT INTO "users" ("name") VALUES('Dandrew');
```
</Section>


Source: https://orm.drizzle.team/docs/drizzle-kit-migrate

import CodeTab from "@mdx/CodeTab.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from "@mdx/Section.astro";
import Tab from "@mdx/Tab.astro";
import Tabs from "@mdx/Tabs.astro";
import Callout from "@mdx/Callout.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import Npx from "@mdx/Npx.astro";


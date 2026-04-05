### Example
Example of how to export drizzle schema to console with Drizzle schema located in `./src/schema.ts`

We will also place drizzle config file in the `configs` folder.

Let's create config file:

```plaintext {4}
📦 <project root>
 ├ 📂 configs
 │ └ 📜 drizzle.config.ts
 ├ 📂 src
 │ └ 📜 schema.ts
 └ …
```
```ts filename='drizzle.config.ts'
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
});
```

```ts filename='schema.ts'
import { pgTable, serial, text } from 'drizzle-orm/pg-core'

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	email: text('email').notNull(),
	name: text('name')
});
```

Now let's run
```shell
npx drizzle-kit export --config=./configs/drizzle.config.ts
```
And it will successfully output SQL representation of drizzle schema
```bash
CREATE TABLE "users" (
        "id" serial PRIMARY KEY NOT NULL,
        "email" text NOT NULL,
        "name" text
);
```

Source: https://orm.drizzle.team/docs/drizzle-kit-generate

import CodeTab from "@mdx/CodeTab.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from "@mdx/Section.astro";
import Tab from "@mdx/Tab.astro";
import Tabs from "@mdx/Tabs.astro";
import Callout from "@mdx/Callout.astro";
import Prerequisites from "@mdx/Prerequisites.astro"
import Npx from "@mdx/Npx.astro";
import SchemaFilePaths from "@mdx/SchemaFilePaths.mdx"
import Dialects from "@mdx/Dialects.mdx"


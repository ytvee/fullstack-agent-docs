### `breakpoints`
<rem025/>

Drizzle Kit will automatically embed `--> statement-breakpoint` into generated SQL migration files, 
that's necessary for databases that do not support multiple DDL alternation statements in one transaction(MySQL and SQLite).

`breakpoints` option flag lets you switch it on and off

|               |                      |
| :------------ | :-----------------   |
| type          | `boolean` |
| default       | `true`                    |
| commands      | `generate` `pull`   |

<rem025/>

```ts
export default defineConfig({
  dialect: "postgresql",
  breakpoints: false,
});
```


Source: https://orm.drizzle.team/docs/drizzle-kit-check

import CodeTab from "@mdx/CodeTab.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from "@mdx/Section.astro";
import Tab from "@mdx/Tab.astro";
import Tabs from "@mdx/Tabs.astro";
import Callout from "@mdx/Callout.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from "@mdx/Npm.astro";
import Npx from "@mdx/Npx.astro";



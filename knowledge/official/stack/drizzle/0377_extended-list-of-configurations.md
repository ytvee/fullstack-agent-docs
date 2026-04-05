### Extended list of configurations
We recommend configuring `drizzle-kit` through [drizzle.config.ts](/docs/drizzle-config-file) file, 
yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.
<rem025/>
|           |            |                                                                         |
| :-------- | :--------- | :---------------------------------------------------------------------- |
| `dialect` | `required` | Database dialect you are using. Can be `postgresql`,`mysql` or `sqlite` |
| `out`     |            | Migrations folder, default=`./drizzle`                                  |
| `config`  |            | Configuration file path, default=`drizzle.config.ts`                           |
<br/>
<Npx>
drizzle-kit check --dialect=postgresql
drizzle-kit check --dialect=postgresql --out=./migrations-folder
</Npx>


Source: https://orm.drizzle.team/docs/drizzle-kit-export

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


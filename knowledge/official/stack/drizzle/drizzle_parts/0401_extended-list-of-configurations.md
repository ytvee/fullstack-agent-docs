### Extended list of configurations
We recommend configuring `drizzle-kit` through [drizzle.config.ts](/docs/drizzle-config-file) file, 
yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.

|                     |            |                                                                           |
| :------------------ | :--------- | :------------------------------------------------------------------------ |
| `dialect`           | `required` | Database dialect, one of <Dialects/>                                      |
| `driver`            |            | Drivers exceptions <Drivers/>                                             |
| `out`               |            | Migrations output folder path, default is `./drizzle`                     |
| `url`               |            | Database connection string                                                |
| `user`              |            | Database user                                                             |
| `password`          |            | Database password                                                         |
| `host`              |            | Host                                                                      |
| `port`              |            | Port                                                                      |
| `database`          |            | Database name                                                             |
| `config`            |            | Configuration file path, default is `drizzle.config.ts`                          |
| `introspect-casing` |            | Strategy for JS keys creation in columns, tables, etc. `preserve` `camel` |
| `tablesFilter`      |            | Table name filter                                                         |
| `schemaFilter`      |            | Schema name filter. Default: `["public"]`                                 |
| `extensionsFilters` |            | Database extensions internal database filters                             |

<Npx>
drizzle-kit pull --dialect=postgresql --url=postgresql://user:password@host:port/dbname
drizzle-kit pull --dialect=postgresql --driver=pglite url=database/
drizzle-kit pull --dialect=postgresql --tablesFilter='user*' --extensionsFilters=postgis url=postgresql://user:password@host:port/dbname
</Npx>

![](@/assets/gifs/introspect_mysql.gif)


Source: https://orm.drizzle.team/docs/drizzle-kit-push

import CodeTab from "@mdx/CodeTab.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from "@mdx/Section.astro";
import Tab from "@mdx/Tab.astro";
import Tabs from "@mdx/Tabs.astro";
import Callout from "@mdx/Callout.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import Npx from "@mdx/Npx.astro";
import SchemaFilePaths from "@mdx/SchemaFilePaths.mdx";
import Drivers from "@mdx/Drivers.mdx"
import Dialects from "@mdx/Dialects.mdx"
import DriversExamples from "@mdx/DriversExamples.mdx"


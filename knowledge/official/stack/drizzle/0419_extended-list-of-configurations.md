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
drizzle-kit up --dialect=postgresql
drizzle-kit up --dialect=postgresql --out=./migrations-folder
</Npx>

![](@/assets/gifs/up_mysql.gif)



Source: https://orm.drizzle.team/docs/dynamic-query-building

import Callout from '@mdx/Callout.astro';


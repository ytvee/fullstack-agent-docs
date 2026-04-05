### Extended list of configurations

`drizzle-kit push` has a list of cli-only options

<rem025/>

|           |                                                          |
| :-------- | :---------------------------------------------------     |
| `verbose` | print all SQL statements prior to execution              |
| `strict`  | always ask for approval before executing SQL statements  |
| `force`   | auto-accept all data-loss statements                     |
<br/>
<Npx>
drizzle-kit push --strict --verbose --force
</Npx>

<br/>
<hr/>
<br/>
We recommend configuring `drizzle-kit` through [drizzle.config.ts](/docs/drizzle-config-file) file, 
yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.

|                     |            |                                                                           |
| :------------------ | :--------- | :------------------------------------------------------------------------ |
| `dialect`           | `required` | Database dialect, one of <Dialects/>                                      |
| `schema`            | `required` | Path to typescript schema file(s) or folder(s) with multiple schema files |
| `driver`            |            | Drivers exceptions <Drivers/>                                             |
| `tablesFilter`      |            | Table name filter                                                         |
| `schemaFilter`      |            | Schema name filter. Default: `["public"]`                                 |
| `extensionsFilters` |            | Database extensions internal database filters                             |
| `url`               |            | Database connection string                                                |
| `user`              |            | Database user                                                             |
| `password`          |            | Database password                                                         |
| `host`              |            | Host                                                                      |
| `port`              |            | Port                                                                      |
| `database`          |            | Database name                                                             |
| `config`            |            | Configuration file path, default=`drizzle.config.ts`                             |

<Npx>
drizzle-kit push dialect=postgresql schema=src/schema.ts url=postgresql://user:password@host:port/dbname
drizzle-kit push dialect=postgresql schema=src/schema.ts driver=pglite url=database/
drizzle-kit push dialect=postgresql schema=src/schema.ts --tablesFilter='user*' --extensionsFilters=postgis url=postgresql://user:password@host:port/dbname
</Npx>



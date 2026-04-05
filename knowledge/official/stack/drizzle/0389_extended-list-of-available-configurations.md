### Extended list of available configurations
`drizzle-kit generate` has a list of cli-only options

<rem025/>

|               |                                                      |
| :--------     | :--------------------------------------------------- |
| `custom`      | generate empty SQL for custom migration              |
| `name`        | generate migration with custom name                  |

<rem025/>

<Npx>
drizzle-kit generate --name=init
drizzle-kit generate --name=seed_users --custom
</Npx>

<br/>
<hr/>
<br/>
We recommend configuring `drizzle-kit` through [drizzle.config.ts](/docs/drizzle-config-file) file, 
yet you can provide all configuration options through CLI if necessary, e.g. in CI/CD pipelines, etc.

|               |            |                                                                            |
| :------------ | :-------   | :----------------------------------------------------------------------    |
| `dialect`     | `required` | Database dialect, one of <Dialects/>                                       |
| `schema`      | `required` | Path to typescript schema file(s) or folder(s) with multiple schema files  |
| `out`         |            | Migrations output folder, default is `./drizzle`                           |
| `config`      |            | Configuration file path, default is `drizzle.config.ts`                    |
| `breakpoints` |            | SQL statements breakpoints, default is `true`                              |



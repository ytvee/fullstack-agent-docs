### Extended list of available configurations
`drizzle-kit export` has a list of cli-only options

<rem025/>

|               |                                                      |
| :--------     | :--------------------------------------------------- |
| `--sql`       | generating SQL representation of Drizzle Schema               |

By default, Drizzle Kit outputs SQL files, but in the future, we want to support different formats

<rem025/>

<Npx>
drizzle-kit push --name=init
drizzle-kit push --name=seed_users --custom
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
| `config`      |            | Configuration file path, default is `drizzle.config.ts`                    |


### `schemaFilter`

Was changed starting from `1.0.0-beta.1` version!

<Callout type='warning' collapsed="How it works in 0.x versions">
`drizzle-kit push` and `drizzle-kit pull` will by default manage all tables in `public` schema.
You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

`schemaFilter` option lets you specify list of schemas for Drizzle Kit to manage

|               |                      |
| :------------ | :-----------------   |
| type          | `string[]` |
| default       | `["public"]`                    |
| commands      | `push` `pull`   |

</Callout>

<Callout>
If you want to run multiple projects with one database - check out [our guide](/docs/goodies#multi-project-schema).
</Callout>

`drizzle-kit push` and `drizzle-kit pull` will by default manage all schemas.

`schemaFilter` option lets you specify [`glob`](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20'.js'&tests=/hello/world.js&tests=//%20This%20won't%20match!&tests=/test/some/globs) 
based schema names filter, e.g. `["public", "auth"]` or `"tenant_*"`

|               |                      |
| :------------ | :-----------------   |
| type          | `string[]` |
| commands      | `push` `pull`   |

<rem025/>

```ts
export default defineConfig({
  dialect: "postgresql",
  schemaFilter: ["public", "schema1", "schema2"],
});
```


### `tablesFilter`
<Callout>
If you want to run multiple projects with one database - check out [our guide](/docs/goodies#multi-project-schema).
</Callout>
<rem025/>
`drizzle-kit push` and `drizzle-kit pull` will by default manage all tables in `public` schema.
You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

`tablesFilter` option lets you specify [`glob`](https://www.digitalocean.com/community/tools/glob?comments=true&glob=/**/*.js&matches=false&tests=//%20This%20will%20match%20as%20it%20ends%20with%20'.js'&tests=/hello/world.js&tests=//%20This%20won't%20match!&tests=/test/some/globs) 
based table names filter, e.g. `["users", "user_info"]` or `"user*"`

|               |                      |
| :------------ | :-----------------   |
| type          | `string` `string[]` |
| default       | --                    |
| commands      | `generate` `push` `pull`   |

<rem025/>
```ts
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  tablesFilter: ["users", "posts", "project1_*"],
});
```


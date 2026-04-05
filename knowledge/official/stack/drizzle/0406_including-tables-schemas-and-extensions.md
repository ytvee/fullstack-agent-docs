### Including tables, schemas and extensions
`drizzle-kit push` will by default manage all tables in `public` schema.
You can configure list of tables, schemas and extensions via `tablesFilters`, `schemaFilter` and `extensionFilters` options.

|                     |                                                                                               |
| :------------------ | :-------------------------------------------------------------------------------------------- |
| `tablesFilter`      | `glob` based table names filter, e.g. `["users", "user_info"]` or `"user*"`. Default is `"*"` |
| `schemaFilter`      | Schema names filter, e.g. `["public", "drizzle"]`. Default is `["public"]`                    |
| `extensionsFilters` | List of installed database extensions, e.g. `["postgis"]`. Default is `[]`                    |
<br/>

Let's configure drizzle-kit to only operate with **all tables** in **public** schema
and let drizzle-kit know that there's a **postgis** extension installed, 
which creates it's own tables in public schema, so drizzle can ignore them.

<Section>
```ts filename="drizzle.config.ts" {9-11}
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname",
  },
  extensionsFilters: ["postgis"],
  schemaFilter: ["public"],
  tablesFilter: ["*"],
});
```
```shell
npx drizzle-kit push
```
</Section>


### `extensionsFilters`
<rem025/>

Some extensions like [`postgis`](https://postgis.net/), when installed on the database, create its own tables in public schema. 
Those tables have to be ignored by `drizzle-kit push` or `drizzle-kit pull`.

`extensionsFilters` option lets you declare list of installed extensions for drizzle kit to ignore their tables in the schema.

|               |                      |
| :------------ | :-----------------   |
| type          | `["postgis"]` |
| default       | `[]`                    |
| commands      | `push` `pull`   |

<rem025/>

```ts
export default defineConfig({
  dialect: "postgresql",
  extensionsFilters: ["postgis"],
});
```


### `migrations`
<rem025/>

When running `drizzle-kit migrate` - drizzle will records about 
successfully applied migrations in your database in log table named `__drizzle_migrations` in `public` schema(PostgreSQL only).

`migrations` config options lets you change both migrations log `table` name and `schema`.

|               |                      |
| :------------ | :-----------------   |
| type          | `{ table: string, schema: string }` |
| default       | `{ table: "__drizzle_migrations", schema: "drizzle" }`                    |
| commands      | `migrate`   |

<rem025/>

```ts
export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  migrations: {
    table: 'my-migrations-table', // `__drizzle_migrations` by default
    schema: 'public', // used in PostgreSQL only, `drizzle` by default
  },
});
```


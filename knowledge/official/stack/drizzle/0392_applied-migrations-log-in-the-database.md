### Applied migrations log in the database
Upon running migrations Drizzle Kit will persist records about successfully applied migrations in your database. 
It will store them in migrations log table named `__drizzle_migrations`.

You can customise both **table** and **schema**(PostgreSQL only) of that table via drizzle config file:
```ts filename="drizzle.config.ts" {8-9}
export default defineConfig({
  dialect: "postgresql",
  schema: "./src/schema.ts",
  dbCredentials: {
    url: "postgresql://user:password@host:port/dbname"
  },
  migrations: {
    table: 'my-migrations-table', // `__drizzle_migrations` by default
    schema: 'public', // used in PostgreSQL only, `drizzle` by default
  },
});
```


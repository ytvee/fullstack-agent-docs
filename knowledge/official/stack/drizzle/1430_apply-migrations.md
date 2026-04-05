#### Apply migrations

To start the Supabase local development stack, run the following command:

```bash copy
supabase start
```

To apply migrations, run the following command:

```bash copy
supabase migration up
```

You can read more about Supabase migrations in the [documentation](https://supabase.com/docs/guides/deployment/database-migrations).

<Callout type="warning">Don't forget to run Docker</Callout>

Alternatively, you can apply migrations using the `drizzle-kit migrate` command. Learn more about this migration process in the [documentation](https://orm.drizzle.team/docs/migrations).


#### Setup connection string variable

Navigate to [Database Settings](https://supabase.com/dashboard/project/_/settings/database) and copy the URI from the `Connection String` section. Make sure to use `connection pooling`. Remember to replace the password placeholder with your actual database password.

Add `DATABASE_URL` variable to your `.env` or `.env.local` file.

```plaintext copy
DATABASE_URL=<YOUR_DATABASE_URL>
```

Read more about Connection Pooler and pooling modes in the [documentation](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler).


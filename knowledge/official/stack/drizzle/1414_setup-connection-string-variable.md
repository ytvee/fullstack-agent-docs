#### Setup connection string variable

You can find `Project connect details` by clicking **Connect** in the top bar of the dashboard and copy the URI from the `Transaction pooler` section. Remember to replace the password placeholder with your actual database password.

Add `DATABASE_URL` variable to your `.env` file.

```plaintext copy
DATABASE_URL=<YOUR_DATABASE_URL>
```

Read more about connecting to Supabase Database in the [documentation](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler).


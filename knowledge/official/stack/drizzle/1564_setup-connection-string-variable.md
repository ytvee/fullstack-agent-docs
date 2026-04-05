#### Setup connection string variable

Navigate to the **Connection Details** section in the project console to find your database connection string. It should look similar to this:

```bash
postgres://username:password@ep-cool-darkness-123456.us-east-2.aws.neon.tech/neondb
```

Add the `DATABASE_URL` environment variable to your `.env` or `.env.local` file, which you'll use to connect to the Neon database.

```bash
DATABASE_URL=NEON_DATABASE_CONNECTION_STRING
```


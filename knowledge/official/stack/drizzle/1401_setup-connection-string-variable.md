#### Setup connection string variable

In **Project Dashboard** section click the `Connect` button and copy your database connection string. It should look similar to this:

```bash
postgres://username:password@ep-cool-darkness-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
```

Add the `DATABASE_URL` environment variable to your `.env` file, which you'll use to connect to the Neon database.

```text copy
DATABASE_URL=NEON_DATABASE_CONNECTION_STRING
```


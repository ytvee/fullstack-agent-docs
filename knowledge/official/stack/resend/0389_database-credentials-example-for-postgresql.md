# Database credentials (example for PostgreSQL)
POSTGRESQL_URL=postgresql://user:password@host:5432/database
```

<Info>
  Get your webhook signing secret from the [Resend
  Dashboard](https://resend.com/webhooks) when creating a webhook.
</Info>
</Step>

<Step title="Set up your database">
Set up your database and run the provided schema for your database. The ingester supports PostgreSQL, MySQL, MongoDB, and several data warehouses. Schema files can be found in the `schemas/` directory.

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
pnpm db:setup --postgresql

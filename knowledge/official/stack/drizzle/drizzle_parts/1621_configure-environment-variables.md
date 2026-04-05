#### Configure environment variables

In the deployed service settings, go to the `Variables` tab. Add the `DATABASE_URL` variable by referencing the PostgreSQL service variable:

Click `Add Variable`, set the name to `DATABASE_URL`, and use the Railway variable reference `${{Postgres.DATABASE_URL}}` as the value.

<Callout type="info">
The `${{Postgres.DATABASE_URL}}` reference variable automatically resolves to the **private** internal connection string at runtime, which is optimal for service-to-service communication within Railway. This is different from the public URL you use in your local `.env` file.
</Callout>

![](@/assets/images/tutorials/node-railway-app-set-database-url.png)


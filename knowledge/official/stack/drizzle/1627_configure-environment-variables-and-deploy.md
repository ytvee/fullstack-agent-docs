#### Configure environment variables and deploy

The template comes with two pre-configured environment variables:

- `PASSCODE` - the password for secure access to your Studio instance. It defaults to `${{secret()}}`, which generates a random secret.
- `DATABASE_URL` - the database connection string. Set it to `${{Postgres.DATABASE_URL}}` to reference your existing PostgreSQL service.

Click `Deploy Template` to deploy.

![](@/assets/images/tutorials/railway-drizzle-studio-template-config.png)


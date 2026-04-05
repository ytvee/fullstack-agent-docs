# Drizzle \<\> Vercel Postgres

<Prerequisites>
- Database [connection basics](/docs/connect-overview) with Drizzle
- Vercel Postgres database - [website](https://vercel.com/docs/storage/vercel-postgres)
- Vercel Postgres driver - [docs](https://vercel.com/docs/storage/vercel-postgres/sdk) & [GitHub](https://github.com/vercel/storage/tree/main/packages/postgres)
- Drizzle PostgreSQL drivers - [docs](/docs/get-started-postgresql)
</Prerequisites>

According to their **[official website](https://vercel.com/docs/storage/vercel-postgres)**,
Vercel Postgres is a serverless SQL database designed to integrate with Vercel Functions.

Drizzle ORM natively supports both **[@vercel/postgres](https://vercel.com/docs/storage/vercel-postgres)** serverless
driver with `drizzle-orm/vercel-postgres` package and **[`postgres`](#postgresjs)** or **[`pg`](#node-postgres)**
drivers to access Vercel Postgres through `postgesql://`

Check out the official **[Vercel Postgres + Drizzle](https://vercel.com/docs/storage/vercel-postgres/using-an-orm#drizzle)** docs.


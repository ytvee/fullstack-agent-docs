# Drizzle \<\> PlanetScale MySQL

<Prerequisites>

- Database [connection basics](/docs/connect-overview) with Drizzle
- PlanetScale database - [website](https://planetscale.com/docs)
- PlanetScale http driver - [GitHub](https://github.com/planetscale/database-js)
- Drizzle MySQL drivers - [docs](/docs/get-started-mysql)

</Prerequisites>

PlanetScale offers both MySQL (Vitess) and PostgreSQL databases. This page covers connecting to PlanetScale MySQL.

For PlanetScale Postgres, see the [PlanetScale Postgres connection guide](/docs/connect-planetscale-postgres).

With Drizzle ORM you can access PlanetScale MySQL over http
through their official **[`database-js`](https://github.com/planetscale/database-js)**
driver from serverless and serverfull environments with our `drizzle-orm/planetscale-serverless` package.

You can also access PlanetScale MySQL through TCP with `mysql2` driver — **[see here.](/docs/get-started-mysql)**


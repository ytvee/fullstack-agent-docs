# Drizzle \<\> Neon Postgres
<Prerequisites>
- Database [connection basics](/docs/connect-overview) with Drizzle
- Neon serverless database - [website](https://neon.tech)
- Neon serverless driver - [docs](https://neon.tech/docs/serverless/serverless-driver) & [GitHub](https://github.com/neondatabase/serverless)
- Drizzle PostgreSQL drivers - [docs](/docs/get-started-postgresql)
</Prerequisites>

Drizzle has native support for Neon connections with the `neon-http` and `neon-websockets` drivers. These use the **neon-serverless** driver under the hood.  
  
With the `neon-http` and `neon-websockets` drivers, you can access a Neon database from serverless environments over HTTP or WebSockets instead of TCP.  
Querying over HTTP is faster for single, non-interactive transactions.  
  
If you need session or interactive transaction support, or a fully compatible drop-in replacement for the `pg` driver, you can use the WebSocket-based `neon-serverless` driver.  
You can connect to a Neon database directly using [Postgres](/docs/get-started/postgresql-new)
  
For an example of using Drizzle ORM with the Neon Serverless driver in a Cloudflare Worker, **[see here.](http://driz.link/neon-cf-ex)**  
To use Neon from a serverful environment, you can use the PostgresJS driver, as described in Neon's **[official Node.js docs](https://neon.tech/docs/guides/node)** — see **[docs](#postgresjs)**.


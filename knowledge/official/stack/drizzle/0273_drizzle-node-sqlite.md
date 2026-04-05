# Drizzle \<\> Node SQLite

<Prerequisites>
- Database [connection basics](/docs/connect-overview) with Drizzle
- Node - [website](https://nodejs.org/)
- Node SQLite driver - [docs](https://nodejs.org/api/sqlite.html)
</Prerequisites>

Drizzle ORM natively supports **[`node:sqlite`](https://nodejs.org/api/sqlite.html)** module

We embrace SQL dialects and dialect specific drivers and syntax and unlike any other ORM, 
for synchronous drivers like `node:sqlite` we have both **async** and **sync** APIs and we mirror most popular 
SQLite-like `all`, `get`, `values` and `run` query methods syntax.


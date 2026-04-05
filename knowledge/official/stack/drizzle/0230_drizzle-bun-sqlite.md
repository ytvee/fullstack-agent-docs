# Drizzle \<\> Bun SQLite

<Prerequisites>
- Database [connection basics](/docs/connect-overview) with Drizzle
- Bun - [website](https://bun.sh/docs)
- Bun SQLite driver - [docs](https://bun.sh/docs/api/sqlite)
</Prerequisites>

According to the **[official website](https://bun.sh/)**, Bun is a fast all-in-one JavaScript runtime. 

Drizzle ORM natively supports **[`bun:sqlite`](https://bun.sh/docs/api/sqlite)** module and it's crazy fast 🚀  

We embrace SQL dialects and dialect specific drivers and syntax and unlike any other ORM, 
for synchronous drivers like `bun:sqlite` we have both **async** and **sync** APIs and we mirror most popular 
SQLite-like `all`, `get`, `values` and `run` query methods syntax.


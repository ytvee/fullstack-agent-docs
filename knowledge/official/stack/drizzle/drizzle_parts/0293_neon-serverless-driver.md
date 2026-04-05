## Neon serverless driver

PlanetScale Postgres also supports connections via the [Neon serverless driver](https://planetscale.com/docs/postgres/connecting/neon-serverless-driver). This is a good option for serverless environments like Vercel Functions, Cloudflare Workers, or AWS Lambda.

The driver supports two modes:

- **HTTP mode** — Faster for single queries and non-interactive transactions
- **WebSocket mode** — Required for interactive transactions or session-based features


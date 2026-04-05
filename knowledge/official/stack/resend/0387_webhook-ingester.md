# Webhook Ingester

Source: https://resend.com/docs/webhooks/ingester

A self-hosted solution to store all your Resend webhook events in your own database.

The Resend Webhook Ingester is an open-source Next.js application that receives, verifies, and stores all your webhook events in your own database. Deploy it to your infrastructure and gain full control over your email event data.

<Info>
  For more details on why you should store your webhook data, see the [data
  storage guide](/dashboard/webhooks/how-to-store-webhooks-data).
</Info>

## Why use the Webhook Ingester?

While you can build your own webhook handler, the Webhook Ingester provides a production-ready solution with:

* **Signature verification** using Svix to ensure webhook authenticity
* **Idempotent storage** that safely handles duplicate webhook deliveries
* **Multiple database support** including PostgreSQL, MySQL, MongoDB, and data warehouses
* **One-click deployment** to Vercel, Railway, or Render

<CardGroup>
  <Card title="GitHub Repository" icon="github" href="https://github.com/resend/resend-webhooks-ingester">
    View the source code and contribute
  </Card>

<Card title="Docker Image" icon="docker" href="https://ghcr.io/resend/resend-webhooks-ingester">
Pull the official Docker image
</Card>
</CardGroup>

## Deploy

Get started in minutes with one-click deployment:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/resend/resend-webhooks-ingester\&env=RESEND_WEBHOOK_SECRET\&envDescription=Your%20Resend%20webhook%20signing%20secret\&envLink=https://resend.com/webhooks)
[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/cd2lvJ?referralCode=w2CHHM\&utm_medium=integration\&utm_source=template\&utm_campaign=generic)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/resend/resend-webhooks-ingester)

Or use Docker:

```bash
docker pull ghcr.io/resend/resend-webhooks-ingester
```
## Supported Databases


| Database    | Endpoint       | Best For                               |
| ----------- | -------------- | -------------------------------------- |
| Supabase    | `/supabase`    | Quick setup with managed Postgres      |
| Neon        | `/neon`        | Serverless Postgres with branching     |
| PostgreSQL  | `/postgresql`  | Self-hosted or managed Postgres        |
| MySQL       | `/mysql`       | Self-hosted or managed MySQL           |
| PlanetScale | `/planetscale` | Serverless MySQL                       |
| MongoDB     | `/mongodb`     | Document database (Atlas, self-hosted) |
| Snowflake   | `/snowflake`   | Data warehousing and analytics         |
| BigQuery    | `/bigquery`    | Google Cloud analytics                 |
| ClickHouse  | `/clickhouse`  | High-performance analytics             |

## Quick Start

<Steps>
  <Step title="Clone and install">
    ```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
    git clone https://github.com/resend/resend-webhooks-ingester.git
    cd resend-webhooks-ingester
    pnpm install
    ```
  </Step>

<Step title="Configure environment variables">
Copy the example environment file and add your credentials:

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
cp .env.example .env.local
```

At minimum, you need:

```env .env.local theme={"theme":{"light":"github-light","dark":"vesper"}}

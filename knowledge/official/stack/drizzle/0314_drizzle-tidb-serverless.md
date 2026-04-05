# Drizzle \<\> TiDB Serverless

<Prerequisites>
- Database [connection basics](/docs/connect-overview) with Drizzle
- TiDB database - [website](https://docs.pingcap.com/)
- TiDB HTTP Driver - [website](https://docs.pingcap.com/tidbcloud/serverless-driver)
- Drizzle MySQL drivers - [docs](/docs/get-started-mysql)
</Prerequisites>

According to the **[official website](https://www.pingcap.com/tidb-serverless/)**, 
TiDB Serverless is a fully-managed, autonomous DBaaS with split-second cluster provisioning and consumption-based pricing.

<Callout type="info" emoji="ℹ️">
TiDB Serverless is compatible with MySQL, so you can use [MySQL connection guide](/docs/get-started-mysql) to connect to it.
</Callout>

TiDB Serverless provides an [HTTP driver](https://docs.pingcap.com/tidbcloud/serverless-driver) for edge environments. It is natively supported by Drizzle ORM via `drizzle-orm/tidb-serverless` package.


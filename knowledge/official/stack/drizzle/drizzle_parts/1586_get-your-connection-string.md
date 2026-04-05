#### Get your connection string

Click on the PostgreSQL service in your project, go to the `Variables` tab, and find the `DATABASE_PUBLIC_URL` variable. Copy the value — it should look similar to this:

```bash
postgresql://postgres:password@region.railway.app:port/railway
```

![](@/assets/images/tutorials/railway-postgres-variables.png)

<Callout type="warning">
Railway provides two types of database connection URLs:

- **Public URL** — accessible from anywhere (your local machine, external services). Uses a TCP proxy and looks like `postgresql://postgres:password@region.railway.app:port/railway`.
- **Private URL** — only accessible from services within the same Railway project via internal networking. Uses `*.railway.internal` hostname.

For **local development** (like running `drizzle-kit push` or `drizzle-kit studio`), you must use the **public URL**. The private `*.railway.internal` hostname will not resolve from your local machine.
</Callout>


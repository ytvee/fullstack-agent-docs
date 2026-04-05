#### Setup connection string variable

Create a `.env` file in the root of your project and add the `DATABASE_URL` environment variable. Use the **public** connection string from Railway:

```plaintext copy
DATABASE_URL=postgresql://postgres:password@region.railway.app:port/railway
```

<Callout type="info">
  This `.env` file is for local development only. When deploying to Railway, you
  will configure the `DATABASE_URL` environment variable separately in the
  Railway dashboard using a service reference variable.
</Callout>


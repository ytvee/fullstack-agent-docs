#### Verify your setup

Once deployed, navigate to the `Architecture` tab in your Railway project. You should see your application service connected to the PostgreSQL database.

![](@/assets/images/tutorials/node-railway-canvas-app-postgres-full.png)

<Callout type="warning" title="Alternative: Zero-downtime migrations">
This tutorial applies migrations at application startup using `migrate()`. This is the simplest approach and works well for most applications.

If you need **zero-downtime deployments**, you may want to run migrations as a **separate step** before the new version of your app starts receiving traffic. This way you can rollback the application independently from the database changes.

On Railway, you can achieve this using a [pre-deploy command](https://docs.railway.com/deployments/pre-deploy-command) — it runs between the build and deploy phases, has access to your private network and environment variables, and if it fails, the deployment will not proceed.

In your service settings, scroll down to the **Deploy** section and click **Add pre-deploy step**:

![](@/assets/images/tutorials/node-railway-app-predeploy-migrate.png)

Enter the following command:

```bash copy
npx drizzle-kit migrate
```

With this approach, remove the `await migrate(db, { migrationsFolder: "./migrations" })` call from your `index.ts` — migrations are handled by the pre-deploy command instead.

For more details, see the [Drizzle migrations fundamentals](/docs/migrations) page.

</Callout>

</Steps>


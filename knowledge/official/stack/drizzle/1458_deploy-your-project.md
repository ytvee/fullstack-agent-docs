#### Deploy your project

Create a new project in the [dashboard](https://vercel.com/new) or run the `vercel` command to deploy your project:

```bash copy
vercel
```

Add `POSTGRES_URL` environment variable:

```bash copy
vercel env add POSTGRES_URL
```

Redeploy your project to update your environment variables:

```bash copy
vercel
```
</Steps>

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /api/hello)` to access your edge function.


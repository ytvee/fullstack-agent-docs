#### Deploy your project

Create a new project in the [dashboard](https://vercel.com/new) or run the `vercel` command to deploy your project:

```bash copy
vercel
```

Add `TURSO_CONNECTION_URL` environment variable:

```bash copy
vercel env add TURSO_CONNECTION_URL
```

Add `TURSO_AUTH_TOKEN` environment variable:

```bash copy
vercel env add TURSO_AUTH_TOKEN
```

Redeploy your project to update your environment variables:

```bash copy
vercel
```
</Steps>

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /api/hello)` to access your edge function.


Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-neon


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from "@mdx/Npm.astro";
import Steps from "@mdx/Steps.astro";
import Section from "@mdx/Section.astro";
import Callout from "@mdx/Callout.astro";

This tutorial demonstrates how to use Drizzle ORM with [Neon Postgres](https://neon.tech/) database. If you do not have an existing Neon account, sign up [here](https://neon.tech). 

<Prerequisites>  
  - You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
  <Npm>
    drizzle-orm 
    -D drizzle-kit
  </Npm>

  - You should also install the [Neon serverless driver](https://neon.tech/docs/serverless/serverless-driver). 
  <Npm>
    @neondatabase/serverless
  </Npm>
  
  - You should have installed the `dotenv` package for managing environment variables. 
  <Npm>
    dotenv
  </Npm>  
</Prerequisites>


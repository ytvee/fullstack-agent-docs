#### Deploy your project

Run the following command to deploy your project:

```bash copy
netlify deploy
```

Follow the instructions in the CLI to deploy your project to Netlify. In this tutorial our publish directory is `'.'`.

It is a [draft deployment](https://docs.netlify.com/cli/get-started/#draft-deploys) by default.
To do a production deployment, run the following command:

```bash copy
netlify deploy --prod
```

</Steps>

Finally, you can use URL of the deployed website and navigate to the route you created `(e.g. /user)` to access your edge function.



Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-netlify-edge-functions-supabase


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from '@mdx/Npm.astro';
import Steps from '@mdx/Steps.astro';
import Section from "@mdx/Section.astro";
import Callout from "@mdx/Callout.astro";

This tutorial demonstrates how to use Drizzle ORM with [Netlify Edge Functions](https://docs.netlify.com/edge-functions/overview/) and [Supabase Database](https://supabase.com/docs/guides/database/overview) database.

<Prerequisites>
- You should have the latest version of [Netlify CLI](https://docs.netlify.com/cli/get-started/#installation) installed.
- You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
<Npm>
drizzle-orm
-D drizzle-kit
</Npm>

- You should have installed the `dotenv` package for managing environment variables. If you use Node.js `v20.6.0` or later, there is no need to install it because Node.js natively supports `.env` files. Read more about it [here](https://nodejs.org/en/blog/release/v20.6.0#built-in-env-file-support).
<Npm>
  dotenv
</Npm>

- Optionally, you can install the `@netlify/edge-functions` package to import the types for the `Context` object which will be used later.
<Npm>
  @netlify/edge-functions
</Npm>
</Prerequisites>

<Callout type="warning">
These installed packages are used only to create table in the database in [Create a table](#create-a-table), [Setup Drizzle config file](#setup-drizzle-config-file) and [Apply changes to the database](#apply-changes-to-the-database) steps. These packages do not affect the code running inside Netlify Edge Functions. We will use `import_map.json` to import the necessary packages for the Edge Functions.
</Callout>

<Steps>

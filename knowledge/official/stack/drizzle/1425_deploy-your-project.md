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



Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-supabase-edge-functions


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from '@mdx/Npm.astro';
import Steps from '@mdx/Steps.astro';
import Section from "@mdx/Section.astro";
import Callout from '@mdx/Callout.astro';

This tutorial demonstrates how to use Drizzle ORM with [Supabase Edge Functions](https://supabase.com/docs/guides/functions).

<Prerequisites>
- You should have the latest version of [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started#installing-the-supabase-cli) installed.
- You should have installed Drizzle ORM and [Drizzle kit](https://orm.drizzle.team/kit-docs/overview). You can do this by running the following command:
<Npm>
drizzle-orm
-D drizzle-kit
</Npm>
- You should have installed Docker Desktop. It is a prerequisite for local development. Follow the official [docs](https://docs.docker.com/desktop) to install.
</Prerequisites>

To learn how to create a basic Edge Function on your local machine and then deploy it, see the [Edge Functions Quickstart](https://supabase.com/docs/guides/functions/quickstart).

<Steps>

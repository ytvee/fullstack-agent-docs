#### Deploy your function

Deploy your function by running the following command:

```bash copy
supabase functions deploy drizzle-tutorial --no-verify-jwt
```
</Steps>

Finally, you can use URL of the deployed project and navigate to the route you created `(e.g. /drizzle-tutorial)` to access your edge function.


Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-vercel-edge-functions


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from '@mdx/Npm.astro';
import Steps from '@mdx/Steps.astro';
import Section from "@mdx/Section.astro";
import Callout from "@mdx/Callout.astro";

This tutorial demonstrates how to use Drizzle ORM with [Vercel Functions](https://vercel.com/docs/functions) in [Edge runtime](https://vercel.com/docs/functions/runtimes/edge-runtime).

<Prerequisites>
- You should have the latest version of [Vercel CLI](https://vercel.com/docs/cli#) installed.
<Npm>
-g vercel
</Npm>

- You should have an existing Next.js project or create a new one using the following command:

```bash copy
npx create-next-app@latest --typescript
```
- You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
<Npm>
drizzle-orm
-D drizzle-kit
</Npm>
</Prerequisites>

<Callout type="warning">
In case you face the issue with resolving dependencies during installation:

If you're not using React Native, forcing the installation with `--force` or `--legacy-peer-deps` should resolve the issue. If you are using React Native, then you need to use the exact version of React which is compatible with your React Native version.
</Callout>


#### Verify your setup

Navigate to the `Architecture` tab in your Railway project. You should now see three services: your application, the PostgreSQL database, and Drizzle Studio.

![](@/assets/images/tutorials/node-railway-canvas-all-services.png)

</Steps>


Source: https://orm.drizzle.team/docs/typebox-legacy

import Npm from '@mdx/Npm.astro';
import Callout from '@mdx/Callout.astro';

<Callout type="error">
Starting from `drizzle-orm@1.0.0-beta.15`, `drizzle-typebox` has been deprecated in favor of first-class schema generation support within Drizzle ORM itself

You can still use `drizzle-typebox` package but all new update will be added to Drizzle ORM directly

This version of `typebox` is legacy by using `@sinclair/typebox` package
</Callout>


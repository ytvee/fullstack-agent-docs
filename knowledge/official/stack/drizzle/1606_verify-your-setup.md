#### Verify your setup

Navigate to the `Architecture` tab in your Railway project. You should now see three services: your application, the PostgreSQL database, and Drizzle Studio.

![](@/assets/images/tutorials/bun-railway-canvas-all-services.png)

</Steps>



Source: https://orm.drizzle.team/docs/tutorials/node-railway-pg


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from "@mdx/Npm.astro";
import Steps from "@mdx/Steps.astro";
import Section from "@mdx/Section.astro";
import Callout from "@mdx/Callout.astro";

This tutorial demonstrates how to use Drizzle ORM with [Node.js](https://nodejs.org/) and a PostgreSQL database, all deployed on [Railway](https://driz.link/railway).

<Prerequisites>
  - You should have [Node.js](https://nodejs.org/) installed. You can install it by following the [official guide](https://nodejs.org/en/download/).

  - You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
  <Npm>
    drizzle-orm
    -D drizzle-kit
  </Npm>

  - You should have installed the `pg` package as the PostgreSQL driver and `tsx` to run TypeScript files directly.
  <Npm>
    pg
    -D @types/pg tsx
  </Npm>

  - You should have a [Railway](https://driz.link/railway) account.
</Prerequisites>


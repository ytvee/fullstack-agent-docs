## Learn more

- [Encore Documentation](https://encore.dev/docs)
- [Encore Drizzle Guide](https://encore.dev/docs/ts/develop/orms/drizzle)
- [Drizzle ORM Documentation](/docs/overview)


Source: https://orm.drizzle.team/docs/tutorials/bun-railway-pg


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from "@mdx/Npm.astro";
import Steps from "@mdx/Steps.astro";
import Section from "@mdx/Section.astro";
import Callout from "@mdx/Callout.astro";

This tutorial demonstrates how to use Drizzle ORM with [Bun](https://bun.sh/) runtime and a PostgreSQL database, all deployed on [Railway](https://driz.link/railway).

<Prerequisites>
  - You should have [Bun](https://bun.sh/) installed. You can install it by following the [official guide](https://bun.sh/docs/installation).

  - You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
  <Npm>
    drizzle-orm
    -D drizzle-kit
  </Npm>

  - You should have installed the `pg` package as the PostgreSQL driver.
  <Npm>
    pg
    -D @types/pg
  </Npm>

  - You should have a [Railway](https://driz.link/railway) account.
</Prerequisites>


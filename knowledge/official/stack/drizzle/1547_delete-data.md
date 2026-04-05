#### Delete data

Read more about delete query in the [documentation](/docs/delete).

```typescript copy filename="src/db/queries/delete.ts" {5}
import { eq } from 'drizzle-orm';
import { db } from '../index';
import { SelectUser, usersTable } from '../schema';

export async function deleteUser(id: SelectUser['id']) {
  await db.delete(usersTable).where(eq(usersTable.id, id));
}
```


Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-xata


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from '@mdx/Npm.astro';
import Steps from '@mdx/Steps.astro';
import Section from "@mdx/Section.astro";
import Callout from '@mdx/Callout.astro';

This tutorial demonstrates how to use Drizzle ORM with [Xata](https://xata.io). Xata is a PostgreSQL database platform designed to help developers operate and scale databases with enhanced productivity and performance, featuring instant copy-on-write database branches, zero-downtime schema changes, data anonymization, and AI-powered performance monitoring.

<Prerequisites>
- You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
<Npm>
drizzle-orm
-D drizzle-kit
</Npm>
- You should have installed `dotenv` package for managing environment variables. Read more about this package [here](https://www.npmjs.com/package/dotenv)
<Npm>
  dotenv
</Npm>

- You should have installed `postgres` package for connecting to the Postgres database. Read more about this package [here](https://www.npmjs.com/package/postgres)
<Npm>
  postgres
</Npm>

- You should have a Xata account and database set up. Follow the [Xata documentation](https://xata.io/documentation/getting-started) to create your account and database
</Prerequisites>

Check [Xata documentation](https://xata.io/documentation/quickstarts/drizzle) to learn more about using Drizzle ORM with Xata.


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


Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-vercel


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from '@mdx/Npm.astro';
import Steps from '@mdx/Steps.astro';
import Section from "@mdx/Section.astro";
import Callout from '@mdx/Callout.astro';

This tutorial demonstrates how to use Drizzle ORM with [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres). Vercel Postgres is a serverless SQL database designed to integrate with Vercel Functions and your frontend framework.

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

- You should have installed `@vercel/postgres` package. Read more about this package [here](https://www.npmjs.com/package/@vercel/postgres)
<Npm>
  @vercel/postgres
</Npm>  
</Prerequisites>

Check [Vercel documentation](https://vercel.com/docs/storage/vercel-postgres/using-an-orm#drizzle) to learn how to connect to the database with Drizzle ORM.


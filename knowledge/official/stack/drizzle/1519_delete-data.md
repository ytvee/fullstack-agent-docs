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

Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-turso


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from '@mdx/Npm.astro';
import Steps from '@mdx/Steps.astro';
import Section from "@mdx/Section.astro";
import Callout from '@mdx/Callout.astro';

This tutorial demonstrates how to use Drizzle ORM with [Turso](https://docs.turso.tech/introduction).

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
- You should have installed `@libsql/client` package. Read more about this package [here](https://www.npmjs.com/package/@libsql/client).
<Npm>
  @libsql/client
</Npm>
- You should have installed Turso CLI. Check [documentation](https://docs.turso.tech/cli/introduction) for more information
</Prerequisites>

[Turso](https://docs.turso.tech/concepts) is a SQLite-compatible database built on [libSQL](https://docs.turso.tech/libsql), the Open Contribution fork of SQLite. It enables scaling to hundreds of thousands of databases per organization and supports replication to any location, including your own servers, for microsecond-latency access. You can read more about Turso’s concepts [here](https://docs.turso.tech/concepts).

Drizzle ORM natively supports libSQL driver.
We embrace SQL dialects and dialect specific drivers and syntax and mirror most popular SQLite-like `all`, `get`, `values` and `run` query methods syntax.

Check [official documentation](https://docs.turso.tech/quickstart) to setup Turso database.


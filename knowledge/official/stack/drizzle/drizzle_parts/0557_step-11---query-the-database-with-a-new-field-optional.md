#### Step 11 - Query the database with a new field (optional)

```typescript copy filename="src/index.ts"
import 'dotenv/config';
import { eq } from 'drizzle-orm';
import { drizzle } from 'drizzle-orm/sqlite-cloud';
import { usersTable } from './db/schema';

async function main() {
  const db = drizzle(env.<BINDING_NAME>);

  const user: typeof usersTable.$inferInsert = {
    name: 'John',
    age: 30,
    email: 'john@example.com',
    phone: '123-456-7890',
  };

  await db.insert(usersTable).values(user);
  console.log('New user created!');

  const users = await db.select().from(usersTable);
  console.log('Getting all users from the database: ', users);
  /*
  const users: {
    id: number;
    name: string;
    age: number;
    email: string;
    phone: string | null;
  }[]
  */

  await db
    .update(usersTable)
    .set({
      age: 31,
    })
    .where(eq(usersTable.email, user.email));
  console.log('User info updated!');

  await db.delete(usersTable).where(eq(usersTable.email, user.email));
  console.log('User deleted!');

  return Response.json(users);
}

main();
```

Source: https://orm.drizzle.team/docs/get-started/d1-new

import Npm from '@mdx/Npm.astro';
import Npx from '@mdx/Npx.astro';
import Callout from '@mdx/Callout.astro';
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import WhatsNextPostgres from "@mdx/WhatsNextPostgres.astro";
import Breadcrumbs from '@mdx/Breadcrumbs.astro';
import FileStructure from '@mdx/get-started/FileStructure.mdx';
import InstallPackages from '@mdx/get-started/InstallPackages.mdx';
import SetupConfig from '@mdx/get-started/SetupConfig.mdx';
import TransferCode from '@mdx/get-started/TransferCode.mdx';
import QueryTurso from '@mdx/get-started/sqlite/QueryTurso.mdx';
import QueryDatabaseUpdated from '@mdx/get-started/QueryDatabaseUpdated.mdx';
import RunFile from '@mdx/get-started/RunFile.mdx';
import ApplyChanges from '@mdx/get-started/ApplyChanges.mdx';
import SetupEnv from '@mdx/get-started/SetupEnv.mdx';
import CreateTable from '@mdx/get-started/sqlite/CreateTable.mdx';
import ConnectLibsql from '@mdx/get-started/sqlite/ConnectLibsql.mdx';

<Breadcrumbs/>


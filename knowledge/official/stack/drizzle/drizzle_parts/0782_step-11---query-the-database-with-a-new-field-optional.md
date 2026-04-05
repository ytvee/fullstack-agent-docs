#### Step 11 - Query the database with a new field (optional)

```typescript copy filename="src/index.ts"
import 'dotenv/config';
import { eq } from 'drizzle-orm';
import { drizzle } from 'drizzle-orm/planetscale-serverless';
import { usersTable } from './db/schema';

async function main() {
  const db = drizzle({ connection: {
      host: process.env.DATABASE_HOST!,
      username: process.env.DATABASE_USERNAME!,
      password: process.env.DATABASE_PASSWORD!,
    }});

  const user: typeof usersTable.$inferInsert = {
    name: 'John',
    age: 30,
    email: 'john@example.com',
    phone: '123-456-7890',
  };

  await db.insert(usersTable).values(user);
  console.log('New user created!')

  const users = await db.select().from(usersTable);
  console.log('Getting all users from the database: ', users)
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
  console.log('User info updated!')

  await db.delete(usersTable).where(eq(usersTable.email, user.email));
  console.log('User deleted!')
}

main();
```

Source: https://orm.drizzle.team/docs/get-started/planetscale-new

import Npm from '@mdx/Npm.astro';
import Callout from '@mdx/Callout.astro';
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from "@mdx/CodeTabs.astro";
import WhatsNextPostgres from "@mdx/WhatsNextPostgres.astro";
import Breadcrumbs from '@mdx/Breadcrumbs.astro';
import FileStructure from '@mdx/get-started/FileStructure.mdx';
import InstallPackages from '@mdx/get-started/InstallPackages.mdx';
import SetupEnv from '@mdx/get-started/SetupEnv.mdx';
import ConnectPlanetScale from '@mdx/get-started/mysql/ConnectPlanetScale.mdx';
import CreateTable from '@mdx/get-started/mysql/CreateTable.mdx';
import QueryPlanetScale from '@mdx/get-started/mysql/QueryPlanetScale.mdx';
import ApplyChanges from '@mdx/get-started/ApplyChanges.mdx';
import RunFile from '@mdx/get-started/RunFile.mdx';
import SetupConfig from '@mdx/get-started/SetupConfig.mdx';

<Breadcrumbs/>


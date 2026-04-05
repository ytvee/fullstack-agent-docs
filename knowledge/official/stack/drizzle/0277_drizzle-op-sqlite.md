# Drizzle \<\> OP SQLite
According to the **[official github page](https://github.com/OP-Engineering/op-sqlite)**, 
OP-SQLite embeds the latest version of SQLite and provides a low-level API to execute SQL queries.

<Npm>
drizzle-orm @op-engineering/op-sqlite
-D drizzle-kit 
</Npm>

```ts
import { drizzle } from "drizzle-orm/op-sqlite";
import { open } from '@op-engineering/op-sqlite';

const opsqlite = open({
  name: 'myDB',
});
const db = drizzle(opsqlite);

await db.select().from(users);
```

You can use Drizzle Kit for SQL migration generation.  
Please make sure to check how [Drizzle Kit migrations](/docs/kit-overview) work before proceeding.  
OP SQLite requires you to have SQL migrations bundled into the app and we've got you covered.  

<Steps>


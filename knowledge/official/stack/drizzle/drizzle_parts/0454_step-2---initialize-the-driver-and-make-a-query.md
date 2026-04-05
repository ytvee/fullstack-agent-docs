#### Step 2 - Initialize the driver and make a query
<CodeTabs items={["mssql", "mssql with config"]}>
```typescript copy
// Make sure to install the 'mssql' package 
import { drizzle } from 'drizzle-orm/node-mssql';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```
```typescript copy
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/node-mssql';

// You can specify any property from the mssql connection options
const db = drizzle({ 
  connection: { 
    connectionString: process.env.DATABASE_URL,
    ssl: true
  }
});
 
const result = await db.execute('select 1');
```
</CodeTabs>

<Callout type='warning'>
As long as the `node-mssql` driver requires `await` on `Pool` initialization, we need to `await` it before each request - unless you are providing your own Pool instance to Drizzle. In that case, when you want to access `db.$client`, you first need to `await` it, and then use it

```ts
const awaitedClient = await db.$client;
const response = awaitedClient.query...
```
</Callout>

If you need to provide your existing driver:

```typescript copy
// Make sure to install the 'mssql' package 
import { drizzle } from "drizzle-orm/node-mssql";
import type { ConnectionPool } from 'mssql';

const pool = await mssql.connect(connectionString);
const db = drizzle({ client: pool });
 
const result = await db.execute('select 1');
```


#### Step 2 - Initialize the driver and make a query
<CodeTabs items={['mysql2', 'mysql with config']}>
```typescript copy
import { drizzle } from "drizzle-orm/singlestore";

const db = drizzle(process.env.DATABASE_URL);

const response = await db.select().from(...)
```
```typescript copy
import { drizzle } from "drizzle-orm/singlestore";

// You can specify any property from the mysql2 connection options
const db = drizzle({ connection:{ uri: process.env.DATABASE_URL }});

const response = await db.select().from(...)
```
</CodeTabs>

If you need to provide your existing driver:

<CodeTabs items={['Client connection', 'Pool connection']}>
  ```typescript copy
  import { drizzle } from "drizzle-orm/singlestore";
  import mysql from "mysql2/promise";

  const connection = await mysql.createConnection({
    host: "host",
    user: "user",
    database: "database",
    ...
  });

  const db = drizzle({ client: connection });
  ```
  ```typescript copy
  import { drizzle } from "drizzle-orm/singlestore";
  import mysql from "mysql2/promise";

  const poolConnection = mysql.createPool({
    host: "host",
    user: "user",
    database: "database",
    ...
  });

  const db = drizzle({ client: poolConnection });
  ```
</CodeTabs>

<Callout type="warning" emoji="⚙️">
  For the built in `migrate` function with DDL migrations we and drivers strongly encourage you to use single `client` connection.  

  For querying purposes feel free to use either `client` or `pool` based on your business demands.
</Callout>


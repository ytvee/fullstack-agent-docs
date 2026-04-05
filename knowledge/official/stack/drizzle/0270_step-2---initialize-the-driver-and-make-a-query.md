#### Step 2 - Initialize the driver and make a query

```typescript copy filename="index.ts"
// Make sure to install the 'pg' package
import { drizzle } from 'drizzle-orm/node-postgres'

const db = drizzle(process.env.NILEDB_URL);

const response = await db.select().from(...);
```

If you need to provide your existing driver:

```typescript copy filename="index.ts"
// Make sure to install the 'pg' package
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });

const response = await db.select().from(...);
```


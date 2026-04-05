#### Step 2 - Initialize the driver and make a query
<CodeTabs items={["postgres.js", "postgres.js with config"]}>
```typescript copy
import { drizzle } from 'drizzle-orm/postgres-js';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```
```typescript copy
import { drizzle } from 'drizzle-orm/postgres-js';

// You can specify any property from the postgres-js connection options
const db = drizzle({ 
  connection: { 
    url: process.env.DATABASE_URL, 
    ssl: true 
  }
});

const result = await db.execute('select 1');
```
</CodeTabs>

If you need to provide your existing driver:

```typescript copy
// Make sure to install the 'postgres' package
import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

const queryClient = postgres(process.env.DATABASE_URL);
const db = drizzle({ client: queryClient });

const result = await db.execute('select 1');
```


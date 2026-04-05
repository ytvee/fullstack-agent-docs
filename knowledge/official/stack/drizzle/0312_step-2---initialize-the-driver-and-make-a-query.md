#### Step 2 - Initialize the driver and make a query

```typescript copy filename="index.ts"
import { drizzle } from 'drizzle-orm/postgres-js'

const db = drizzle(process.env.DATABASE_URL);

const allUsers = await db.select().from(...);
```

If you need to provide your existing driver:
```typescript copy filename="index.ts"
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

const client = postgres(process.env.DATABASE_URL)
const db = drizzle({ client });

const allUsers = await db.select().from(...);
```

If you decide to use connection pooling via Supabase (described [here](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler)), and have "Transaction" pool mode enabled, then ensure to turn off prepare, as prepared statements are not supported. 

```typescript copy filename="index.ts"
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

// Disable prefetch as it is not supported for "Transaction" pool mode 
const client = postgres(process.env.DATABASE_URL, { prepare: false })
const db = drizzle({ client });

const allUsers = await db.select().from(...);
```

Connect to your database using the Connection Pooler for **serverless environments**, and the Direct Connection for **long-running servers**.


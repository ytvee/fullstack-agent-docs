#### Step 3 - Initialize the driver and make a query

```typescript copy
import { drizzle } from 'drizzle-orm/vercel-postgres';

const db = drizzle();

const result = await db.execute('select 1');
```

If you need to provide your existing driver:

```typescript copy
import { sql } from '@vercel/postgres';
import { drizzle } from 'drizzle-orm/vercel-postgres';

const db = drizzle({ client: sql })

const result = await db.execute('select 1');
```

With **[@vercel/postgres](https://vercel.com/docs/storage/vercel-postgres)** severless package
you can access Vercel Postgres from either serverful or serverless environments with no TCP available,
like Cloudflare Workers, through websockets.  
  
If you're about to use Vercel Postgres from a _serverfull_ environment, you can do it
either with `@vercel/postgres` or directly access the DB through `postgesql://` with 
either **[`postgres`](#postgresjs)** or **[`pg`](#node-postgres)**.


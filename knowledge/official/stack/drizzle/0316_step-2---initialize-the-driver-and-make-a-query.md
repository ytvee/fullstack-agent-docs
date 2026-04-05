#### Step 2 - Initialize the driver and make a query
```typescript copy filename="index.ts"
import { drizzle } from 'drizzle-orm/tidb-serverless';

const db = drizzle({ connection: { url: process.env.TIDB_URL }});

const response = await db.select().from(...)
```

If you need to provide your existing driver:
```typescript copy"
import { connect } from '@tidbcloud/serverless';
import { drizzle } from 'drizzle-orm/tidb-serverless';

const client = connect({ url: process.env.TIDB_URL });
const db = drizzle({ client });
```


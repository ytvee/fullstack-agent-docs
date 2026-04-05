#### Step 2 - Initialize the driver and make a query
```typescript copy
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/bun-sql';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.select().from(...);
```

If you need to provide your existing driver:
```typescript copy
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/bun-sql';
import { SQL } from 'bun';

const client = new SQL(process.env.DATABASE_URL!);
const db = drizzle({ client });
```


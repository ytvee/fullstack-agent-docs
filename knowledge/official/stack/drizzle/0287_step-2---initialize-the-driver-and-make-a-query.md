#### Step 2 - Initialize the driver and make a query
<CodeTabs items={["In-Memory", "In directory", "With extra config options"]}>
```typescript copy"
import { drizzle } from 'drizzle-orm/pglite';

const db = drizzle();

await db.select().from(...);
```
```typescript copy"
import { drizzle } from 'drizzle-orm/pglite';

const db = drizzle('path-to-dir');

await db.select().from(...);
```
```typescript copy"
import { drizzle } from 'drizzle-orm/pglite';

// connection is a native PGLite configuration
const db = drizzle({ connection: { dataDir: 'path-to-dir' }});

await db.select().from(...);
```
</CodeTabs>

If you need to provide your existing driver:

```typescript copy"
import { PGlite } from '@electric-sql/pglite';
import { drizzle } from 'drizzle-orm/pglite';

// In-memory Postgres
const client = new PGlite();
const db = drizzle({ client });

await db.select().from(users);
```


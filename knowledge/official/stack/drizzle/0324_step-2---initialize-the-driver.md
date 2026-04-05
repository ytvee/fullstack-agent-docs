#### Step 2 - Initialize the driver
Drizzle has native support for all `@libsql/client` driver variations:

<LibsqlTable />

<br />

<LibsqlTabs />


If you need to provide your existing driver:

<CodeTabs items={["default", "web"]}>
```typescript copy
import { drizzle } from 'drizzle-orm/libsql';
import { createClient } from '@libsql/client';

const client = createClient({ 
  url: process.env.DATABASE_URL,
  authToken: process.env.DATABASE_AUTH_TOKEN
});

const db = drizzle({ client });

const result = await db.select().from(users).all()
```
```typescript copy
import { drizzle } from 'drizzle-orm/libsql/web';
import { createClient } from '@libsql/client/web';

const client = createClient({ 
  url: process.env.DATABASE_URL,
  authToken: process.env.DATABASE_AUTH_TOKEN
});

const db = drizzle({ client });

const result = await db.select().from(users).all()
```
</CodeTabs>


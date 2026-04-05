#### Step 3 - Connect Drizzle ORM to the database
Drizzle has native support for all @libsql/client driver variations:

<LibsqlTable />
<br/>
<LibsqlTabs />

Create a `index.ts` file in the `src` directory and initialize the connection:

```typescript copy
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/libsql';

// You can specify any property from the libsql connection options
const db = drizzle({ 
  connection: { 
    url: process.env.TURSO_DATABASE_URL!, 
    authToken: process.env.TURSO_AUTH_TOKEN!
  }
});
```

If you need to provide your existing driver:
```typescript copy
import 'dotenv/config';
import { drizzle } from 'drizzle-orm/libsql';
import { createClient } from '@libsql/client';

const client = createClient({ 
  url: process.env.TURSO_DATABASE_URL!, 
  authToken: process.env.TURSO_AUTH_TOKEN!
});
const db = drizzle({ client });
```


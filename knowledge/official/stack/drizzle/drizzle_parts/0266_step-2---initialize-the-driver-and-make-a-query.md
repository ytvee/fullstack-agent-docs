#### Step 2 - Initialize the driver and make a query
<CodeTabs items={["Neon HTTP", "Neon Websockets", "node-postgres", "postgres.js"]}>
```typescript
import { drizzle } from 'drizzle-orm/neon-http';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```
<Section> 
```typescript 
import { drizzle } from 'drizzle-orm/neon-serverless';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```
```typescript
// For Node.js - make sure to install the 'ws' and 'bufferutil' packages
import { drizzle } from 'drizzle-orm/neon-serverless';
import ws from 'ws';

const db = drizzle({
  connection: process.env.DATABASE_URL,
  ws: ws,
});

const result = await db.execute('select 1');
```
<Callout type="warning" emoji="⚙️"> 
Additional configuration is required to use WebSockets in environments where the `WebSocket` global is not defined, such as Node.js. 
Add the `ws` and `bufferutil` packages to your project's dependencies, and set `ws` in the Drizzle config. 
</Callout>
</Section> 
```typescript 
// Make sure to install the 'pg' package 
import { drizzle } from 'drizzle-orm/node-postgres';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```
```typescript
// Make sure to install the 'postgres' package
import { drizzle } from 'drizzle-orm/postgres-js';

const db = drizzle(process.env.DATABASE_URL);

const result = await db.execute('select 1');
```
</CodeTabs>

If you need to provide your existing drivers:

<CodeTabs items={["Neon HTTP", "Neon Websockets", "node-postgres", "postgres.js"]}>
```typescript
import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle({ client: sql });

const result = await db.execute('select 1');
```
<Section> 
```typescript 
import { Pool } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-serverless';

const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const db = drizzle({ client: pool })

const result = await db.execute('select 1');
```
```typescript
// For Node.js - make sure to install the 'ws' and 'bufferutil' packages
import { Pool, neonConfig } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-serverless';

neonConfig.webSocketConstructor = ws;

const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const db = drizzle({ client: pool })

const result = await db.execute('select 1');
```
<Callout type="warning" emoji="⚙️"> 
Additional configuration is required to use WebSockets in environments where the `WebSocket` global is not defined, such as Node.js. 
Add the `ws` and `bufferutil` packages to your project's dependencies, and set `ws` in the Drizzle config. 
</Callout>
</Section> 
```typescript 
// Make sure to install the 'pg' package 
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
const db = drizzle({ client: pool });
 
const result = await db.execute('select 1');
```
```typescript
// Make sure to install the 'postgres' package
import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

const queryClient = postgres(process.env.DATABASE_URL);
const db = drizzle({ client: queryClient });

const result = await db.execute('select 1');
```
</CodeTabs>


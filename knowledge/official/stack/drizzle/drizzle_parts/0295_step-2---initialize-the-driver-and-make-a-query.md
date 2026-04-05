#### Step 2 - Initialize the driver and make a query

<CodeTabs items={["Neon HTTP", "Neon WebSockets"]}>
```typescript copy
import { neon, neonConfig } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';

// Required for PlanetScale Postgres connections
neonConfig.fetchEndpoint = (host) => `https://${host}/sql`;

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle({ client: sql });

const result = await db.execute('select 1');

````
<Section>
```typescript copy
import { Pool, neonConfig } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-serverless';

// Required for PlanetScale Postgres connections
neonConfig.pipelineConnect = false;
neonConfig.wsProxy = (host, port) => `${host}/v2?address=${host}:${port}`;

const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const db = drizzle({ client: pool });

const result = await db.execute('select 1');
````

```typescript copy
// For Node.js environments - install 'ws' package
import ws from "ws";
import { Pool, neonConfig } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-serverless";

neonConfig.webSocketConstructor = ws;
// Required for PlanetScale Postgres connections
neonConfig.pipelineConnect = false;
neonConfig.wsProxy = (host, port) => `${host}/v2?address=${host}:${port}`;

const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const db = drizzle({ client: pool });

const result = await db.execute("select 1");
```

</Section>
</CodeTabs>

<Callout title="Connection URL format">
  {`postgresql://{username}:{password}@{host}:{port}/postgres?sslmode=verify-full`}
</Callout>

<Callout title="Connection ports" type="info">
  PlanetScale Postgres supports two connection ports:

`5432`: Direct connection to PostgreSQL. Total connections are limited by your cluster's `max_connections` setting.

`6432`: Connection via PgBouncer for connection pooling. Recommended when you have many simultaneous connections.

  </Callout>


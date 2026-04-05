#### Step 2 - Initialize the driver and make a query
<CodeTabs items={["gel", "gel with config"]}>
```typescript copy
// Make sure to install the 'gel' package 
import { drizzle } from 'drizzle-orm/gel';

const db = drizzle(process.env.DATABASE_URL);
 
const result = await db.execute('select 1');
```
```typescript copy
// Make sure to install the 'gel' package
import { drizzle } from "drizzle-orm/gel";

// You can specify any property from the gel connection options
const db = drizzle({
  connection: {
    dsn: process.env.DATABASE_URL,
    tlsSecurity: "default",
  },
});

const result = await db.execute("select 1");
```
</CodeTabs>

If you need to provide your existing driver:

```typescript copy
// Make sure to install the 'gel' package 
import { drizzle } from "drizzle-orm/gel";
import { createClient } from "gel";

const gelClient = createClient();
const db = drizzle({ client: gelClient });

const result = await db.execute('select 1');
```


#### Create the database

Define your database in a `database.ts` file. Encore automatically provisions a PostgreSQL database locally using Docker and in the cloud when you deploy:

```typescript copy filename="database.ts"
import { SQLDatabase } from "encore.dev/storage/sqldb";
import { drizzle } from "drizzle-orm/node-postgres";
import * as schema from "./schema";

const db = new SQLDatabase("mydb", {
  migrations: {
    path: "migrations",
    source: "drizzle",
  },
});

export const orm = drizzle(db.connectionString, { schema });
```

Setting `source: "drizzle"` tells Encore to use Drizzle's migration format.


#### Connect Drizzle ORM to your database 

Create a `db.ts` file and set up your database configuration:

```typescript copy filename="src/db.ts"
import { drizzle } from "drizzle-orm/neon-http";
import { neon } from "@neondatabase/serverless";
import { config } from "dotenv";

config({ path: ".env" }); // or .env.local

const sql = neon(process.env.DATABASE_URL!);
export const db = drizzle({ client: sql });
```


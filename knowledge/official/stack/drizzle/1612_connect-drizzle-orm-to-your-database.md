#### Connect Drizzle ORM to your database

Create a `db.ts` file and set up your database configuration:

```typescript copy filename="src/db.ts"
import { drizzle } from "drizzle-orm/node-postgres";

export const db = drizzle(process.env.DATABASE_URL!);
```


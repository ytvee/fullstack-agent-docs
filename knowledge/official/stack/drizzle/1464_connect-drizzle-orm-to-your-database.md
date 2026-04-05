#### Connect Drizzle ORM to your database

Create a `index.ts` file in the `src/db` directory and set up your database configuration:

```typescript copy filename="src/db/index.ts"
import { drizzle } from "drizzle-orm/planetscale-serverless";

export const db = drizzle(process.env.MYSQL_URL!)
```


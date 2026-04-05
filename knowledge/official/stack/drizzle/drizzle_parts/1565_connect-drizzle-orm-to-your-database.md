#### Connect Drizzle ORM to your database 

Create a `drizzle.ts` file in your `src/db` folder and set up your database configuration:

```tsx copy filename="src/db/drizzle.ts"
import { config } from "dotenv";
import { drizzle } from 'drizzle-orm/neon-http';

config({ path: ".env" }); // or .env.local

export const db = drizzle(process.env.DATABASE_URL!);
```


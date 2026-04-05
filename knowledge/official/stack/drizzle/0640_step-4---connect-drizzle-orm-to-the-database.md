#### Step 4 - Connect Drizzle ORM to the database

Create a `index.ts` file in the `src` directory and initialize the connection:

```typescript copy filename="src/index.ts"
import { drizzle } from "drizzle-orm/gel";
import { createClient } from "gel";

const gelClient = createClient();
const db = drizzle({ client: gelClient });
```


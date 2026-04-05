#### Connect Drizzle ORM to your database

Update your `netlify/edge-functions/user.ts` file and set up your database configuration:

```typescript copy filename="netlify/edge-functions/user.ts"
import type { Context } from "@netlify/edge-functions";
import { usersTable } from "./common/schema.ts";
import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';

export default async (request: Request, context: Context) => {
  const queryClient = postgres(Netlify.env.get("DATABASE_URL")!);
  const db = drizzle({ client: queryClient });

  const users = await db.select().from(usersTable);

  return new Response(JSON.stringify(users));
};
```

<Callout type="warning">
You might see a red underline under the imports if you're using VS Code. The Edge Function will still execute. To get rid of the red underline, you can configure VS Code to use Edge Functions in the next step.
</Callout>


#### Copy your schema to the functions directory

Copy the code that you will use in your edge function from `src/schema.ts` file to the `supabase/functions/drizzle-tutorial/index.ts` file:

```typescript copy filename="supabase/functions/drizzle-tutorial/index.ts"
// Setup type definitions for built-in Supabase Runtime APIs
import "jsr:@supabase/functions-js/edge-runtime.d.ts"
import { pgTable, serial, text, integer } from "drizzle-orm/pg-core";

const usersTable = pgTable('users_table', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  age: integer('age').notNull()
})

Deno.serve(async (req) => {
  const { name } = await req.json()
  const data = {
    message: `Hello ${name}!`,
  }

  return new Response(
    JSON.stringify(data),
    { headers: { "Content-Type": "application/json" } },
  )
})  
```

<Callout type="warning">
In the Deno ecosystem, each function should be treated as an independent project with its own set of dependencies and configurations.
For these reasons, Supabase recommend maintaining separate configuration files (`deno.json`, `.npmrc`, or `import_map.json`) within each function's directory, even if it means duplicating some configurations. Read more [here](https://supabase.com/docs/guides/functions/dependencies#managing-dependencies).
</Callout>


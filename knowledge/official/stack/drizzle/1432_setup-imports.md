#### Setup imports

Add the following imports to the `deno.json` file in the `supabase/functions/drizzle-tutorial` directory:

```json copy filename="supabase/functions/drizzle-tutorial/deno.json"
{
  "imports": {
    "drizzle-orm/": "npm:/drizzle-orm/",
    "postgres": "npm:postgres"
  }
}
```

You can read more about managing dependencies [here](https://supabase.com/docs/guides/functions/dependencies#managing-dependencies).


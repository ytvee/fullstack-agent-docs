#### Step 2 - Initialize the driver and make a query

You would need to have either a `wrangler.json` or a `wrangler.toml` file for D1 database and will look something like this:
<CodeTabs items={["wrangler.json", "wrangler.toml"]}>
```json
{
    "name": "YOUR_PROJECT_NAME",
    "main": "src/index.ts",
    "compatibility_date": "2024-09-26",
    "compatibility_flags": [
        "nodejs_compat"
    ],
    "d1_databases": [
        {
            "binding": "BINDING_NAME",
            "database_name": "YOUR_DB_NAME",
            "database_id": "YOUR_DB_ID",
            "migrations_dir": "drizzle/migrations"
        }
    ]
}
```
```toml
name = "YOUR_PROJECT_NAME"
main = "src/index.ts"
compatibility_date = "2022-11-07"
node_compat = true

[[ d1_databases ]]
binding = "BINDING_NAME"
database_name = "YOUR_DB_NAME"
database_id = "YOUR_DB_ID"
migrations_dir = "drizzle/migrations"
```
</CodeTabs>

Make your first D1 query:
```typescript copy
import { drizzle } from 'drizzle-orm/d1';

export interface Env {
  <BINDING_NAME>: D1Database;
}

export default {
  async fetch(request: Request, env: Env) {
    const db = drizzle(env.<BINDING_NAME>);
    const result = await db.select().from(users).all()
    return Response.json(result);
  },
};
```


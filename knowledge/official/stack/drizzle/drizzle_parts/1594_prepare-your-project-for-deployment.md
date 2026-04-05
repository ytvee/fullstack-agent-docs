#### Prepare your project for deployment

Once you've [generated your migrations](#applying-changes-to-the-database), commit the `migrations` directory to your repository — these files will be applied automatically when your app starts.

Create an `index.ts` file as the entry point for your application. This example runs migrations on startup and then starts a simple HTTP server using Bun:

```typescript copy filename="src/index.ts"
import { drizzle } from "drizzle-orm/node-postgres";
import { migrate } from "drizzle-orm/node-postgres/migrator";
import { usersTable } from "./schema";

const db = drizzle(process.env.DATABASE_URL!);

await migrate(db, { migrationsFolder: "./migrations" });

const server = Bun.serve({
  port: process.env.PORT || 3000,
  async fetch(req) {
    const url = new URL(req.url);

    if (url.pathname === "/users") {
      const users = await db.select().from(usersTable);
      return new Response(JSON.stringify(users), {
        headers: { "Content-Type": "application/json" },
      });
    }

    return new Response("OK");
  },
});

console.log(`Server running on port ${server.port}`);
```

The `migrate()` function reads the SQL files from your `migrations` directory and applies any unapplied migrations to the database. It is safe to run on every startup — already applied migrations are skipped.

Make sure your `package.json` has a start script:

```json copy filename="package.json"
{
  "scripts": {
    "start": "bun src/index.ts"
  }
}
```


#### Prepare your project for deployment

Once you've [generated your migrations](#applying-changes-to-the-database), commit the `migrations` directory to your repository — these files will be applied automatically when your app starts.

Create an `index.ts` file as the entry point for your application. This example runs migrations on startup and then starts a simple HTTP server using Node.js:

```typescript copy filename="src/index.ts"
import { createServer } from "node:http";
import { drizzle } from "drizzle-orm/node-postgres";
import { migrate } from "drizzle-orm/node-postgres/migrator";
import { usersTable } from "./schema";

const db = drizzle(process.env.DATABASE_URL!);

await migrate(db, { migrationsFolder: "./migrations" });

const server = createServer(async (req, res) => {
  const url = new URL(req.url!, `http://${req.headers.host}`);

  if (url.pathname === "/users") {
    const users = await db.select().from(usersTable);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(users));
    return;
  }

  res.writeHead(200);
  res.end("OK");
});

const port = process.env.PORT || 3000;
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

The `migrate()` function reads the SQL files from your `migrations` directory and applies any unapplied migrations to the database. It is safe to run on every startup — already applied migrations are skipped.

<Callout type="info">
  Top-level `await` requires Node.js to treat the file as an ES module. Make
  sure your `package.json` includes `"type": "module"`.
</Callout>

Make sure your `package.json` has the module type and a start script:

```json copy filename="package.json"
{
  "type": "module",
  "scripts": {
    "start": "tsx src/index.ts"
  }
}
```


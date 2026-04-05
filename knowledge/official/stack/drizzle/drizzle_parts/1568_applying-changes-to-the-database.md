#### Applying changes to the database

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```bash
npx drizzle-kit generate
```

These migrations are stored in the `drizzle/migrations`  directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```sql
CREATE TABLE IF NOT EXISTS "todo" (
	"id" integer PRIMARY KEY NOT NULL,
	"text" text NOT NULL,
	"done" boolean DEFAULT false NOT NULL
);
```

Run migrations:

```bash
npx drizzle-kit migrate
```

Alternatively, you can push changes directly to the database using [Drizzle kit push command](/docs/kit-overview#prototyping-with-db-push):

```bash
npx drizzle-kit push
```

<Callout type="warning">Push command is good for situations where you need to quickly test new schema designs or changes in a local development environment, allowing for fast iterations without the overhead of managing migration files.</Callout>
</Steps>


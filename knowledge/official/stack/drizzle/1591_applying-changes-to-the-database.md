#### Applying changes to the database

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```bash copy
bunx drizzle-kit generate
```

The `generate` command only creates migration SQL files based on your schema — it does **not** apply any changes to the database. These migrations are stored in the `migrations` directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```sql
CREATE TABLE "posts" (
	"id" serial PRIMARY KEY NOT NULL,
	"title" text NOT NULL,
	"content" text NOT NULL,
	"userId" integer NOT NULL,
	"createdAt" timestamp DEFAULT now() NOT NULL,
	"updatedAt" timestamp NOT NULL
);
--> statement-breakpoint
CREATE TABLE "users" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" text NOT NULL,
	"age" integer NOT NULL,
	"email" text NOT NULL,
	CONSTRAINT "users_email_unique" UNIQUE("email")
);
--> statement-breakpoint
ALTER TABLE "posts" ADD CONSTRAINT "posts_userId_users_id_fk" FOREIGN KEY ("userId") REFERENCES "public"."users"("id") ON DELETE cascade ON UPDATE no action;
```

Apply the generated migrations to the database:

```bash copy
bunx drizzle-kit migrate
```

<Callout type="info">
  In this tutorial, migrations are applied automatically on application startup
  using `migrate()` from `drizzle-orm/node-postgres/migrator`. You can also
  apply them manually with `drizzle-kit migrate` for local testing.
</Callout>

Alternatively, you can push changes directly to the database using [Drizzle kit push command](/docs/kit-overview#prototyping-with-db-push):

```bash copy
bunx drizzle-kit push
```

<Callout type="warning">
  Push command is good for rapid prototyping in local development, allowing fast
  iterations without managing migration files. For production deployments,
  prefer the `generate` + `migrate` workflow to keep a versioned history of
  schema changes.
</Callout>

</Steps>


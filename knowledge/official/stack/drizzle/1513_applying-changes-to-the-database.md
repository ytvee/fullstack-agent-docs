#### Applying changes to the database

You can generate migrations using `drizzle-kit generate` command and then run them using the `drizzle-kit migrate` command.

Generate migrations:

```bash copy
npx drizzle-kit generate
```

These migrations are stored in the `supabase/migrations`  directory, as specified in your `drizzle.config.ts`. This directory will contain the SQL files necessary to update your database schema and a `meta` folder for storing snapshots of the schema at different migration stages.

Example of a generated migration:

```sql
CREATE TABLE IF NOT EXISTS "posts_table" (
	"id" serial PRIMARY KEY NOT NULL,
	"title" text NOT NULL,
	"content" text NOT NULL,
	"user_id" integer NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL,
	"updated_at" timestamp NOT NULL
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS "users_table" (
	"id" serial PRIMARY KEY NOT NULL,
	"name" text NOT NULL,
	"age" integer NOT NULL,
	"email" text NOT NULL,
	CONSTRAINT "users_table_email_unique" UNIQUE("email")
);
--> statement-breakpoint
DO $$ BEGIN
 ALTER TABLE "posts_table" ADD CONSTRAINT "posts_table_user_id_users_table_id_fk" FOREIGN KEY ("user_id") REFERENCES "users_table"("id") ON DELETE cascade ON UPDATE no action;
EXCEPTION
 WHEN duplicate_object THEN null;
END $$;
```

Run migrations:

```bash copy
npx drizzle-kit migrate
```

Learn more about [migration process](/docs/migrations). You can also apply migrations using [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started):
- For tables that already exist, manually review the generated migration files from `npx drizzle-kit generate` and comment out or adjust any unsafe pure create statements (e.g., `CREATE SCHEMA "auth";`) while ensuring safe conditional creates (e.g., `CREATE TABLE IF NOT EXISTS "auth"."users"`) are properly handled.

Alternatively, you can push changes directly to the database using [Drizzle kit push command](/docs/kit-overview#prototyping-with-db-push):

```bash copy
npx drizzle-kit push
```

<Callout type="warning">Push command is good for situations where you need to quickly test new schema designs or changes in a local development environment, allowing for fast iterations without the overhead of managing migration files.</Callout>

To apply migrations using the Supabase CLI you should follow these steps:
 
Generate migrations using Drizzle Kit:

```bash copy
npx drizzle-kit generate
```

Initialize the local Supabase project:

```bash copy
supabase init
```

Link it to your remote project:

```bash copy
supabase link
```

Push changes to the database:

```bash copy
supabase db push
```
</Steps>


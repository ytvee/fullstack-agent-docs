### Check

The `CHECK` constraint is used to limit the value range that can be placed in a column.

If you define a `CHECK` constraint on a column it will allow only certain values for this column.  

If you define a `CHECK` constraint on a table it can limit the values in certain columns based on values in other columns in the row.

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
      ```typescript copy
      import { sql } from "drizzle-orm";
      import { check, integer, pgTable, text, uuid } from "drizzle-orm/pg-core";

      export const users = pgTable(
        "users",
        {
          id: uuid().defaultRandom().primaryKey(),
          username: text().notNull(),
          age: integer(),
        },
        (table) => [
          check("age_check1", sql`${table.age} > 21`),
        ]
      );
      ```
      ```sql
      CREATE TABLE "users" (
	      "id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	      "username" text NOT NULL,
	      "age" integer,
	      CONSTRAINT "age_check1" CHECK ("users"."age" > 21)
      );
      ```
    </Section>

  </Tab> 
  <Tab>
    <Section>
      ```typescript copy
      import { sql } from "drizzle-orm";
      import { check, int, mysqlTable, text } from "drizzle-orm/mysql-core";

      export const users = mysqlTable(
        "users",
        {
          id: int().primaryKey(),
          username: text().notNull(),
          age: int(),
        },
        (table) => [
          check("age_check1", sql`${table.age} > 21`)
        ]
      );
      ```
      ```sql
      CREATE TABLE `users` (
	      `id` int NOT NULL,
	      `username` text NOT NULL,
	      `age` int,
	      CONSTRAINT `users_id` PRIMARY KEY(`id`),
	      CONSTRAINT `age_check1` CHECK(`users`.`age` > 21)
      );
      ```
    </Section>
  </Tab>
  <Tab>
   <Section>
      ```typescript copy
      import { sql } from "drizzle-orm";
      import { check, int, sqliteTable, text } from "drizzle-orm/sqlite-core";

      export const users = sqliteTable(
        "users",
        {
          id: int().primaryKey(),
          username: text().notNull(),
          age: int(),
        },
        (table) => [
          check("age_check1", sql`${table.age} > 21`)
        ]
      );
      ```
      ```sql
      CREATE TABLE `users` (
	      `id` integer PRIMARY KEY NOT NULL,
	      `username` text NOT NULL,
	      `age` integer,
	      CONSTRAINT "age_check1" CHECK("users"."age" > 21)
      );
      ```
    </Section>

  </Tab>
  <Tab>
    Currently not supported in SingleStore
  </Tab>
<Tab>
    <Section>
      ```typescript copy
      import { sql } from "drizzle-orm";
      import { check, int, mssqlTable, text } from "drizzle-orm/mssql-core";

      export const users = mssqlTable(
        "users",
        {
          id: int().primaryKey(),
          username: text().notNull(),
          age: integer(),
        },
        (table) => [
          check("age_check1", sql`${table.age} > 21`),
        ]
      );
      ```
      ```sql
      CREATE TABLE [users] (
	      [id] int PRIMARY KEY,
	      [username] text NOT NULL,
	      [age] integer,
	      CONSTRAINT [age_check1] CHECK ([users].[age] > 21)
      );
      ```
    </Section>

  </Tab> 
  <Tab>
    <Section>
      ```typescript copy
      import { sql } from "drizzle-orm";
      import { check, int4, cockroachTable, text, uuid } from "drizzle-orm/cockroach-core";

      export const users = cockroachTable(
        "users",
        {
          id: uuid().defaultRandom().primaryKey(),
          username: text().notNull(),
          age: int4(),
        },
        (table) => [
          check("age_check1", sql`${table.age} > 21`),
        ]
      );
      ```
      ```sql
      CREATE TABLE "users" (
	      "id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	      "username" text NOT NULL,
	      "age" int4,
	      CONSTRAINT "age_check1" CHECK ("users"."age" > 21)
      );
      ```
    </Section>

  </Tab> 
</Tabs>


### Primary Key

The `PRIMARY KEY` constraint uniquely identifies each record in a table.  
Primary keys must contain `UNIQUE` values, and cannot contain `NULL` values.  

A table can have only **ONE** primary key; and in the table, this primary key can consist of single or multiple columns (fields).

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
      ```typescript copy
      import { serial, text, pgTable } from "drizzle-orm/pg-core";

      const user = pgTable('user', {
        id: serial('id').primaryKey(),
      });

      const table = pgTable('table', {
        id: text('cuid').primaryKey(),
      });
      ```

      ```sql
      CREATE TABLE "user" (
        "id" serial PRIMARY KEY
      );

      CREATE TABLE "table" (
        "cuid" text PRIMARY KEY
      );
      ```
    </Section>

  </Tab> 
  <Tab>
    <Section>
      ```typescript
      import { int, text, mysqlTable } from "drizzle-orm/mysql-core";

      export const user = mysqlTable("user", {
        id: int("id").autoincrement().primaryKey(),
      })

      export const table = mysqlTable("table", {
        cuid: text("cuid").primaryKey(),
      })
      ```

      ```sql
      CREATE TABLE `user` (
        `id` int AUTO_INCREMENT PRIMARY KEY NOT NULL
      );

      CREATE TABLE `table` (
        `cuid` text PRIMARY KEY NOT NULL
      );
      ```
    </Section>

  </Tab>
  <Tab>
   <Section>
      ```typescript copy
      import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

      export const user = sqliteTable("user", {
        id: integer("id").primaryKey(),
      })

      export const pet = sqliteTable("pet", {
        id: integer("id").primaryKey(),
      })
      ```

      ```sql
      CREATE TABLE `user` (
        `id` integer PRIMARY KEY AUTOINCREMENT NOT NULL
      );

      CREATE TABLE `pet` (
        `id` integer PRIMARY KEY AUTOINCREMENT
      )
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript
      import { int, text, singlestoreTable } from "drizzle-orm/singlestore-core";

      export const user = singlestoreTable("user", {
        id: int("id").autoincrement().primaryKey(),
      })

      export const table = singlestoreTable("table", {
        cuid: text("cuid").primaryKey(),
      })
      ```

      ```sql
      CREATE TABLE `user` (
        `id` int AUTO_INCREMENT PRIMARY KEY NOT NULL
      );

      CREATE TABLE `table` (
        `cuid` text PRIMARY KEY NOT NULL
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript
      import { int, text, mssqlTable } from "drizzle-orm/mssql-core";

      export const user = mssqlTable("user", {
        id: int().primaryKey(),
      })
      ```

      ```sql
      CREATE TABLE [user] (
        [id] int,
        CONSTRAINT [user_pkey] PRIMARY KEY [id]
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript copy
      import { int4, text, cockroachTable } from "drizzle-orm/cockroach-core";

      const user = cockroachTable('user', {
        id: int4().primaryKey(),
      });

      const table = cockroachTable('table', {
        id: text().primaryKey(),
      });
      ```

      ```sql
      CREATE TABLE "user" (
        "id" int4 PRIMARY KEY
      );

      CREATE TABLE "table" (
        "cuid" text PRIMARY KEY
      );
      ```
    </Section>

  </Tab> 
</Tabs>


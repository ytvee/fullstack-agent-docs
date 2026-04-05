### Unique

The `UNIQUE` constraint ensures that all values in a column are different.  

Both the `UNIQUE` and `PRIMARY KEY` constraints provide a guarantee for uniqueness for a column or set of columns.

A `PRIMARY KEY` constraint automatically has a `UNIQUE` constraint.  

<Callout type="info" emoji="ℹ️">
  You can have many `UNIQUE` constraints per table, but only one `PRIMARY KEY` constraint per table.
</Callout>

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
      ```typescript copy
      import { integer, text, unique, pgTable } from "drizzle-orm/pg-core";

      export const user = pgTable('user', {
        id: integer('id').unique(),
      });

      export const table = pgTable('table', {
        id: integer('id').unique('custom_name'),
      });

      export const composite = pgTable('composite_example', {
        id: integer('id'),
        name: text('name'),
      }, (t) => [
        unique().on(t.id, t.name),
        unique('custom_name').on(t.id, t.name)
      ]);

      // In Postgres 15.0+ NULLS NOT DISTINCT is available
      // This example demonstrates both available usages
      export const userNulls = pgTable('user_nulls_example', {
        id: integer('id').unique("custom_name", { nulls: 'not distinct' }),
      }, (t) => [
        unique().on(t.id).nullsNotDistinct()
      ]);
      ```

      ```sql
      CREATE TABLE "composite_example" (
	      "id" integer,
        "name" text,
        CONSTRAINT "composite_example_id_name_unique" UNIQUE("id","name"),
        CONSTRAINT "custom_name" UNIQUE("id","name")
      );

      CREATE TABLE "table" (
      	"id" integer,
      	CONSTRAINT "custom_name" UNIQUE("id")
      );

      CREATE TABLE "user" (
      	"id" integer,
      	CONSTRAINT "user_id_unique" UNIQUE("id")
      );

      CREATE TABLE "user_nulls_example" (
        "id" integer,
        CONSTRAINT "custom_name" UNIQUE NULLS NOT DISTINCT("id"),
        CONSTRAINT "user_nulls_example_id_unique" UNIQUE NULLS NOT DISTINCT("id")
      );
      ```
    </Section>

  </Tab> 
  <Tab>
    <Section>
      ```typescript
      import { int, varchar, unique, mysqlTable } from "drizzle-orm/mysql-core";

      export const user = mysqlTable('user', {
        id: int('id').unique(),
      });

      export const table = mysqlTable('table', {
        id: int('id').unique('custom_name'),
      });

      export const composite = mysqlTable('composite_example', {
        id: int('id'),
        name: varchar('name', { length: 256 }),
      }, (t) => [
        unique().on(t.id, t.name),
        unique('custom_name').on(t.id, t.name)
      ]);
      ```

      ```sql
      CREATE TABLE `user` (
      	`id` int,
      	CONSTRAINT `user_id_unique` UNIQUE(`id`)
      );

      CREATE TABLE `table` (
      	`id` int,
      	CONSTRAINT `custom_name` UNIQUE(`id`)
      );

      CREATE TABLE `composite_example` (
        `id` int,
        `name` varchar(256),
        CONSTRAINT `composite_example_id_name_unique` UNIQUE(`id`,`name`),
        CONSTRAINT `custom_name` UNIQUE(`id`,`name`)
      );
      ```
    </Section>

  </Tab>
  <Tab>
   <Section>
      ```typescript copy
      import { int, text, unique, sqliteTable } from "drizzle-orm/sqlite-core";

      export const user = sqliteTable('user', {
        id: int('id').unique(),
      });

      export const table = sqliteTable('table', {
        id: int('id').unique('custom_name'),
      });

      export const composite = sqliteTable('composite_example', {
        id: int('id'),
        name: text('name'),
      }, (t) => [
        unique().on(t.id, t.name),
        unique('custom_name').on(t.id, t.name)
      ]);
      ```

      ```sql
      CREATE TABLE `user` (
	      `id` integer
      );

      CREATE TABLE `table` (
      	`id` integer
      );

      CREATE TABLE `composite_example` (
      	`id` integer,
      	`name` text
      );

      CREATE UNIQUE INDEX `composite_example_id_name_unique` ON `composite_example` (`id`,`name`);
      CREATE UNIQUE INDEX `custom_name` ON `composite_example` (`id`,`name`);
      CREATE UNIQUE INDEX `custom_name` ON `table` (`id`);
      CREATE UNIQUE INDEX `user_id_unique` ON `user` (`id`);
      ```
    </Section>

  </Tab>
    <Tab>
    <Section>
      ```typescript
      import { int, varchar, unique, singlestoreTable } from "drizzle-orm/singlestore-core";

      export const user = singlestoreTable('user', {
        id: int('id').unique(),
      });

      export const table = singlestoreTable('table', {
        id: int('id').unique('custom_name'),
      });

      export const composite = singlestoreTable('composite_example', {
        id: int('id'),
        name: varchar('name', { length: 256 }),
      }, (t) => [
        unique().on(t.id, t.name),
        unique('custom_name').on(t.id, t.name)
      ]);
      ```

      ```sql
      CREATE TABLE `user` (
      	`id` int,
      	CONSTRAINT `user_id_unique` UNIQUE(`id`)
      );

      CREATE TABLE `table` (
      	`id` int,
      	CONSTRAINT `custom_name` UNIQUE(`id`)
      );

      CREATE TABLE `composite_example` (
        `id` int,
        `name` varchar(256),
        CONSTRAINT `composite_example_id_name_unique` UNIQUE(`id`,`name`),
        CONSTRAINT `custom_name` UNIQUE(`id`,`name`)
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Callout type='warning'>
    With MSSQL you can't create unique constraint on `text`, `ntext`, `varchar(max)`, `nvarchar(max)`
    </Callout>
    <Section>
      ```typescript
      import { int, varchar, unique, mssqlTable } from "drizzle-orm/mssql-core";

      export const user = mssqlTable('user', {
        id: int().unique(),
      });

      export const table = mssqlTable('table', {
        id: int().unique('custom_name'),
      });

      export const composite = mssqlTable('composite_example', {
        id: int(),
        name: varchar({ length: 256 }),
      }, (t) => [
        unique().on(t.id, t.name),
        unique('custom_name').on(t.id, t.name)
      ]);
      ```

      ```sql
      CREATE TABLE [user] (
      	[id] int,
      	CONSTRAINT [user_id_key] UNIQUE([id])
      );

      CREATE TABLE [table] (
      	[id] int,
      	CONSTRAINT [custom_name] UNIQUE([id])
      );

      CREATE TABLE [composite_example] (
        [id] int,
        [name] varchar(256),
        CONSTRAINT [composite_example_id_name_key] UNIQUE([id],[name]),
        CONSTRAINT [custom_name] UNIQUE([id],[name])
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript copy
      import { int4, text, unique, cockroachTable } from "drizzle-orm/cockroach-core";

      export const user = cockroachTable('user', {
        id: int4().unique(),
      });

      export const table = cockroachTable('table', {
        id: int4().unique('custom_name'),
      });

      export const composite = cockroachTable('composite_example', {
        id: int4(),
        name: text(),
      }, (t) => [
        unique().on(t.id, t.name),
        unique('custom_name').on(t.id, t.name)
      ]);
      ```
      ```sql
      CREATE TABLE "user" (
      	"id" integer,
      	CONSTRAINT "user_id_unique" UNIQUE("id")
      );

      CREATE TABLE "table" (
      	"id" integer,
      	CONSTRAINT "custom_name" UNIQUE("id")
      );

      CREATE TABLE "composite_example" (
	      "id" integer,
        "name" text,
        CONSTRAINT "composite_example_id_name_unique" UNIQUE("id","name"),
        CONSTRAINT "custom_name" UNIQUE("id","name")
      );
      ```
    </Section>
  </Tab> 
</Tabs>


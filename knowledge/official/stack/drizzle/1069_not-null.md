### Not null

By default, a column can hold **NULL** values. The `NOT NULL` constraint enforces a column to **NOT** accept **NULL** values.  

This enforces a field to always contain a value, which means that you cannot insert a new record,
or update a record without adding a value to this field.

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
      ```typescript copy
      import { integer, pgTable } from "drizzle-orm/pg-core";

      const table = pgTable('table', {
        integer: integer('integer').notNull(),
      });
      ```

      ```sql
      CREATE TABLE "table" (
        "integer" integer NOT NULL
      );
      ```
    </Section>

  </Tab> 
  <Tab>
    <Section>
      ```typescript
      import { int, mysqlTable } from "drizzle-orm/mysql-core";

      const table = mysqlTable('table', {
        int: int('int').notNull(),
      });
      ```

      ```sql
      CREATE TABLE `table` (
        `int` int NOT NULL
      );
      ```
    </Section>

  </Tab>
  <Tab>
   <Section>
      ```typescript copy
      const table = sqliteTable('table', { 
        numInt: integer('numInt').notNull() 
      });
      ```

      ```sql
      CREATE TABLE table (
        `numInt` integer NOT NULL
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript
      import { int, singlestoreTable } from "drizzle-orm/singlestore-core";

      const table = singlestoreTable('table', {
        int: int('int').notNull(),
      });
      ```

      ```sql
      CREATE TABLE `table` (
        `int` int NOT NULL
      );
      ```
    </Section>
  </Tab>
  <Tab>
    <Section>
      ```typescript
      import { int, mssqlTable } from "drizzle-orm/mssql-core";

      const table = mssqlTable('table', {
        int: int().notNull(),
      });
      ```

      ```sql
      CREATE TABLE [table] (
        [int] int NOT NULL
      );
      ```
    </Section>
  </Tab>
    <Tab>
    <Section>
      ```typescript copy
      import { int4, cockroachTable } from "drizzle-orm/cockroach-core";

      const table = cockroachTable('table', {
        integer: int4().notNull(),
      });
      ```

      ```sql
      CREATE TABLE "table" (
        "integer" int4 NOT NULL
      );
      ```
    </Section>
  </Tab> 
</Tabs>


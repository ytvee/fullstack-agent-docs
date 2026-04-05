### Default

The `DEFAULT` clause specifies a default value to use for the column if no value provided by the user when doing an `INSERT`.
If there is no explicit `DEFAULT` clause attached to a column definition,
then the default value of the column is `NULL`.

An explicit `DEFAULT` clause may specify that the default value is `NULL`,
a string constant, a blob constant, a signed-number, or any constant expression enclosed in parentheses.

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
    ```typescript
    import { sql } from "drizzle-orm";
    import { integer, uuid, pgTable } from "drizzle-orm/pg-core";

    const table = pgTable('table', {
      integer1: integer('integer1').default(42),
      integer2: integer('integer2').default(sql`'42'::integer`),
      uuid1: uuid('uuid1').defaultRandom(),
      uuid2: uuid('uuid2').default(sql`gen_random_uuid()`),
    });
    ```

    ```sql
    CREATE TABLE "table" (
      "integer1" integer DEFAULT 42,
      "integer2" integer DEFAULT '42'::integer,
      "uuid1" uuid DEFAULT gen_random_uuid(),
      "uuid2" uuid DEFAULT gen_random_uuid()
    );
    ```
    </Section>

  </Tab> 
  <Tab>
    <Section>
    ```typescript
    import { sql } from "drizzle-orm";
    import { int, time, mysqlTable } from "drizzle-orm/mysql-core";
    
    const table = mysqlTable("table", {
      int: int("int").default(42),
      time: time("time").default(sql`cast("14:06:10" AS TIME)`),
    });
    ```
    ```sql
    CREATE TABLE `table` (
      `int` int DEFAULT 42,
      `time` time DEFAULT cast("14:06:10" AS TIME)
    );
    ```
    </Section>
  </Tab>
  <Tab>
    <Section>
    ```typescript
    import { sql } from "drizzle-orm";
    import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

    const table = sqliteTable('table', {
      int1: integer('int1').default(42),
      int2: integer('int2').default(sql`(abs(42))`)
    });

    ```
    ```sql
    CREATE TABLE `table` (
      `int1` integer DEFAULT 42
      `int2` integer DEFAULT (abs(42))
    );
    ```
    </Section>

  </Tab>
  <Tab>
    <Section>
    ```typescript
    import { sql } from "drizzle-orm";
    import { int, time, singlestoreTable } from "drizzle-orm/singlestore-core";
    
    const table = singlestoreTable("table", {
      int: int("int").default(42),
      time: time("time").default(sql`cast("14:06:10" AS TIME)`),
    });
    ```
    ```sql
    CREATE TABLE `table` (
      `int` int DEFAULT 42,
      `time` time DEFAULT cast("14:06:10" AS TIME)
    );
    ```
    </Section>
  </Tab>
  <Tab>
    <Section>
    ```typescript
    import { sql } from "drizzle-orm";
    import { int, time, mssqlTable } from "drizzle-orm/mssql-core";
    
    const table = mssqlTable("table", {
      int: int().default(42),
      description: text().default(`This is your dashboard!`),
    });
    ```
    ```sql
    CREATE TABLE [table] (
      [int] int DEFAULT 42,
      [description] text DEFAULT 'This is your dashboard!'
    );
    ```
    </Section>
  </Tab>
  <Tab>
    <Section>
    ```typescript
    import { sql } from "drizzle-orm";
    import { int4, uuid, cockroachTable } from "drizzle-orm/cockroach-core";

    const table = cockroachTable('table', {
      integer1: int4().default(42),
      integer2: int4().default(sql`'42'::int4`),
      uuid1: uuid().defaultRandom(),
      uuid2: uuid().default(sql`gen_random_uuid()`),
    });
    ```

    ```sql
    CREATE TABLE "table" (
      "integer1" int4 DEFAULT 42,
      "integer2" int4 DEFAULT '42'::integer,
      "uuid1" uuid DEFAULT gen_random_uuid(),
      "uuid2" uuid DEFAULT gen_random_uuid()
    );
    ```
    </Section>

  </Tab> 
</Tabs>


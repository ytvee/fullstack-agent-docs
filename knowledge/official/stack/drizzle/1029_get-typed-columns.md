## Get typed columns
You can get a typed columns map,
very useful when you need to omit certain columns upon selection.

<Callout type='warning'>
`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](/docs/upgrade-v1))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`
</Callout>


<br/>

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', "SingleStore", "MSSQL", "CockroachDB"]}>
  <Tab>
      <CodeTabs items={["index.ts", "schema.ts"]}>
        ```ts
        import { getColumns } from "drizzle-orm";
        import { user } from "./schema";

        const { password, role, ...rest } = getColumns(user);

        await db.select({ ...rest }).from(users);
        ```
        ```ts
        import { serial, text, pgTable } from "drizzle-orm/pg-core";

        export const user = pgTable("user", {
          id: serial("id").primaryKey(),
          name: text("name"),
          email: text("email"),
          password: text("password"),
          role: text("role").$type<"admin" | "customer">(),
        });
        ```
      </CodeTabs>
  </Tab>
  <Tab>
      <CodeTabs items={["index.ts", "schema.ts"]}>
        ```ts
        import { getColumns } from "drizzle-orm";
        import { user } from "./schema";

        const { password, role, ...rest } = getColumns(user);

        await db.select({ ...rest }).from(users);
        ```
        ```ts
        import { int, text, mysqlTable } from "drizzle-orm/mysql-core";

        export const user = mysqlTable("user", {
          id: int("id").primaryKey().autoincrement(),
          name: text("name"),
          email: text("email"),
          password: text("password"),
          role: text("role").$type<"admin" | "customer">(),
        });
        ```
      </CodeTabs>
  </Tab>
  <Tab>
      <CodeTabs items={["index.ts", "schema.ts"]}>
        ```ts
        import { getColumns } from "drizzle-orm";
        import { user } from "./schema";

        const { password, role, ...rest } = getColumns(user);

        await db.select({ ...rest }).from(users);
        ```
        ```ts
        import { integer, text, sqliteTable } from "drizzle-orm/sqlite-core";

        export const user = sqliteTable("user", {
          id: integer("id").primaryKey({ autoIncrement: true }),
          name: text("name"),
          email: text("email"),
          password: text("password"),
          role: text("role").$type<"admin" | "customer">(),
        });
        ```
      </CodeTabs>
  </Tab>
  <Tab>
      <CodeTabs items={["index.ts", "schema.ts"]}>
        ```ts
        import { getColumns } from "drizzle-orm";
        import { user } from "./schema";

        const { password, role, ...rest } = getColumns(user);

        await db.select({ ...rest }).from(users);
        ```
        ```ts
        import { int, text, singlestoreTable } from "drizzle-orm/singlestore-core";

        export const user = singlestoreTable("user", {
          id: int("id").primaryKey().autoincrement(),
          name: text("name"),
          email: text("email"),
          password: text("password"),
          role: text("role").$type<"admin" | "customer">(),
        });
        ```
      </CodeTabs>
  </Tab>
  <Tab>
      <CodeTabs items={["index.ts", "schema.ts"]}>
        ```ts
        import { getColumns } from "drizzle-orm";
        import { user } from "./schema";

        const { password, role, ...rest } = getColumns(user);

        await db.select({ ...rest }).from(users);
        ```
        ```ts
        import { int, text, mssqlTable } from "drizzle-orm/mssql-core";

        export const user = mssqlTable("user", {
          id: int().primaryKey(),
          name: text(),
          email: text(),
          password: text(),
          role: text().$type<"admin" | "customer">(),
        });
        ```
      </CodeTabs>
  </Tab>
  <Tab>
      <CodeTabs items={["index.ts", "schema.ts"]}>
        ```ts
        import { getColumns } from "drizzle-orm";
        import { user } from "./schema";

        const { password, role, ...rest } = getColumns(user);

        await db.select({ ...rest }).from(users);
        ```
        ```ts
        import { int4, text, pgTable } from "drizzle-orm/cockroach-core";

        export const user = pgTable("user", {
          id: int4().primaryKey(),
          name: text(),
          email: text(),
          password: text(),
          role: text().$type<"admin" | "customer">(),
        });
        ```
      </CodeTabs>
  </Tab>
</Tabs>


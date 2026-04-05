### Declaring views
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {13-14}
      import { pgTable, pgView, serial, text, timestamp } from "drizzle-orm/pg-core";

      export const user = pgTable("user", {
        id: serial(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: timestamp("created_at"),
        updatedAt: timestamp("updated_at"),
      });

      export const userView = pgView("user_view").as((qb) => qb.select().from(user));
      export const customersView = pgView("customers_view").as((qb) => qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {13-14}
      import { text, mysqlTable, mysqlView, int, timestamp } from "drizzle-orm/mysql-core";

      export const user = mysqlTable("user", {
        id: int().primaryKey().autoincrement(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: timestamp("created_at"),
        updatedAt: timestamp("updated_at"),
      });

      export const userView = mysqlView("user_view").as((qb) => qb.select().from(user));
      export const customersView = mysqlView("customers_view").as((qb) => qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {13-14}
      import { integer, text, sqliteView, sqliteTable } from "drizzle-orm/sqlite-core";

      export const user = sqliteTable("user", {
        id: integer().primaryKey({ autoIncrement: true }),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: integer("created_at"),
        updatedAt: integer("updated_at"),
      });

      export const userView = sqliteView("user_view").as((qb) => qb.select().from(user));
      export const customersView = sqliteView("customers_view").as((qb) => qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
    <Tab>
    <Section>
      ```ts filename="schema.ts" copy {13-14}
      import { mssqlTable, mssqlView, int, text, timestamp } from "drizzle-orm/mssql-core";

      export const user = mssqlTable("user", {
        id: int(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: timestamp("created_at"),
        updatedAt: timestamp("updated_at"),
      });

      export const userView = mssqlView("user_view").as((qb) => qb.select().from(user));
      export const customersView = mssqlView("customers_view").as((qb) => qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW [user_view] AS (SELECT * FROM "user");
      CREATE VIEW [customers_view] AS (SELECT * FROM "user" WHERE "role" = 'customer');
      ```
    </Section>
    If you need a subset of columns you can use `.select({ ... })` method in query builder, like this:
<Section>
  ```ts {4-6}
  export const customersView = mssqlView("customers_view").as((qb) => {
    return qb
      .select({
        id: user.id,
        name: user.name,
        email: user.email,
      })
      .from(user);
  });
  ```
  ```sql
  CREATE VIEW [customers_view] AS (SELECT "id", "name", "email" FROM "user" WHERE "role" = 'customer');
  ```
</Section>
  </Tab>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {13-14}
      import { cockroachTable, cockroachView, int4, text, timestamp } from "drizzle-orm/cockroach-core";

      export const user = cockroachTable("user", {
        id: int4(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: timestamp("created_at"),
        updatedAt: timestamp("updated_at"),
      });

      export const userView = cockroachView("user_view").as((qb) => qb.select().from(user));
      export const customersView = cockroachView("customers_view").as((qb) => qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
</Tabs>

You can also declare views using `standalone query builder`, it works exactly the same way:
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {3, 15-16}
      import { pgTable, pgView, serial, text, timestamp, QueryBuilder} from "drizzle-orm/pg-core";
      
      const qb = new QueryBuilder();

      export const user = pgTable("user", {
        id: serial(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: timestamp("created_at"),
        updatedAt: timestamp("updated_at"),
      });

      export const userView = pgView("user_view").as(qb.select().from(user));
      export const customersView = pgView("customers_view").as(qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {3, 15-16}
      import { text, mysqlTable, mysqlView, int, timestamp, QueryBuilder } from "drizzle-orm/mysql-core";

      const qb = new QueryBuilder();

      export const user = mysqlTable("user", {
        id: int().primaryKey().autoincrement(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: timestamp("created_at"),
        updatedAt: timestamp("updated_at"),
      });

      export const userView = mysqlView("user_view").as(qb.select().from(user));
      export const customersView = mysqlView("customers_view").as(qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {3, 15-16}
      import { integer, text, sqliteView, sqliteTable, QueryBuilder } from "drizzle-orm/sqlite-core";

      const qb = new QueryBuilder();

      export const user = sqliteTable("user", {
        id: integer().primaryKey({ autoIncrement: true }),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: integer("created_at"),
        updatedAt: integer("updated_at"),
      });

      export const userView = sqliteView("user_view").as((qb) => qb.select().from(user));
      export const customerView = sqliteView("customers_view").as((qb) => qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {3, 15-16}
      import { int, text, mssqlView, mssqlTable, QueryBuilder } from "drizzle-orm/mssql-core";

      const qb = new QueryBuilder();

      export const user = mssqlTable("user", {
        id: integer().primaryKey(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: integer("created_at"),
        updatedAt: integer("updated_at"),
      });

      export const userView = mssqlView("user_view").as((qb) => qb.select().from(user));
      export const customerView = mssqlView("customers_view").as((qb) => qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW [user_view] AS (SELECT * FROM "user");
      CREATE VIEW [customers_view] AS (SELECT * FROM "user" WHERE "role" = 'customer');
      ```
    </Section>
  </Tab>
  <Tab>
    <Section>
      ```ts filename="schema.ts" copy {3, 15-16}
      import { cockroachTable, cockroachView, int4, text, timestamp, QueryBuilder} from "drizzle-orm/cockroach-core";
      
      const qb = new QueryBuilder();

      export const user = cockroachTable("user", {
        id: int4(),
        name: text(),
        email: text(),
        password: text(),
        role: text().$type<"admin" | "customer">(),
        createdAt: timestamp("created_at"),
        updatedAt: timestamp("updated_at"),
      });

      export const userView = cockroachView("user_view").as(qb.select().from(user));
      export const customersView = cockroachView("customers_view").as(qb.select().from(user).where(eq(user.role, "customer")));
      ```
      ```sql
      CREATE VIEW "user_view" AS SELECT * FROM "user";
      CREATE VIEW "customers_view" AS SELECT * FROM "user" WHERE "role" = 'customer';
      ```
    </Section>
  </Tab>
</Tabs>


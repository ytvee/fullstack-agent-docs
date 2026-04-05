### Foreign key

The `FOREIGN KEY` constraint is used to prevent actions that would destroy links between tables.
A `FOREIGN KEY` is a field (or collection of fields) in one table, that refers to the `PRIMARY KEY` in another table.
The table with the foreign key is called the child table, and the table with the primary key is called the referenced or parent table.

Drizzle ORM provides several ways to declare foreign keys.
You can declare them in a column declaration statement:

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    ```typescript copy {11}
    import { serial, text, integer, pgTable } from "drizzle-orm/pg-core";

    export const user = pgTable("user", {
      id: serial("id"),
      name: text("name"),
    });

    export const book = pgTable("book", {
      id: serial("id"),
      name: text("name"),
      authorId: integer("author_id").references(() => user.id)
    });
    ```

  </Tab>
  <Tab>
    ```typescript {11}
    import { int, text, mysqlTable } from "drizzle-orm/mysql-core";

    export const user = mysqlTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
    });

    export const book = mysqlTable("book", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      authorId: int("author_id").references(() => user.id)
    });
    ```

  </Tab>
  <Tab>
    ```typescript {11}
    import { integer, text, sqliteTable } from "drizzle-orm/sqlite-core";

    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
    });

    export const book = sqliteTable("book", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
      authorId: integer("author_id").references(() => user.id)
    });
    ```

  </Tab>
  <Tab>
    Currently not supported in SingleStore
  </Tab>
  <Tab>
    ```typescript {11}
    import { int, text, mssqlTable } from "drizzle-orm/mssql-core";

    export const user = mssqlTable("user", {
      id: int().primaryKey(),
      name: text(),
    });

    export const book = mssqlTable("book", {
      id: int().primaryKey(),
      name: text(),
      authorId: int("author_id").references(() => user.id)
    });
    ```

  </Tab>
    <Tab>
    ```typescript copy {11}
    import { int4, text, cockroachTable } from "drizzle-orm/cockroach-core";

    export const user = cockroachTable("user", {
      id: int4().primaryKey(),
      name: text(),
    });

    export const book = cockroachTable("book", {
      id: int4().primaryKey(),
      name: text(),
      authorId: int4("author_id").references(() => user.id)
    });
    ```
  </Tab>
</Tabs>

If you want to do a self reference, due to a TypeScript limitations you will have to either explicitly
set return type for reference callback or use a standalone `foreignKey` operator.

<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    ```typescript copy {6,16-19}
    import { serial, text, integer, foreignKey, pgTable, AnyPgColumn } from "drizzle-orm/pg-core";

    export const user = pgTable("user", {
      id: serial("id"),
      name: text("name"),
      parentId: integer("parent_id").references((): AnyPgColumn => user.id)
    });

    // or
    export const user = pgTable("user", {
      id: serial("id"),
      name: text("name"),
      parentId: integer("parent_id"),
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);
    ```

  </Tab>
  <Tab>
    ```typescript {6,16-19}
    import { int, text, foreignKey, AnyMySqlColumn, mysqlTable } from "drizzle-orm/mysql-core";

    export const user = mysqlTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      parentId: int("parent_id").references((): AnyMySqlColumn => user.id),
    });

    // or
    export const user = mysqlTable("user", {
      id: int("id").primaryKey().autoincrement(),
      name: text("name"),
      parentId: int("parent_id")
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);
    ```

  </Tab>
  <Tab>
    ```typescript {6,16-19}
    import { integer, text, foreignKey, sqliteTable, AnySQLiteColumn } from "drizzle-orm/sqlite-core";

    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
      parentId: integer("parent_id").references((): AnySQLiteColumn => user.id)
    });

    //or
    export const user = sqliteTable("user", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      name: text("name"),
      parentId: integer("parent_id"),
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);
    ```

  </Tab>
  <Tab>
    Currently not supported in SingleStore
  </Tab>
    <Tab>
    ```typescript {6,16-19}
    import { int, text, foreignKey, mssqlTable, AnyMsSQLColumn } from "drizzle-orm/mssql-core";

    export const user = mssqlTable("user", {
      id: int().primaryKey(),
      name: text(),
      parentId: int("parent_id").references((): AnyMsSQLColumn => user.id)
    });

    //or
    export const user = mssqlTable("user", {
      id: int().primaryKey(),
      name: text(),
      parentId: int("parent_id"),
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);
    ```
  </Tab>
  <Tab>
    ```typescript copy {6,16-19}
    import { int4, text, foreignKey, cockroachTable, AnyCockroachColumn } from "drizzle-orm/cockroach-core";

    export const user = cockroachTable("user", {
      id: int4().primaryKey(),
      name: text(),
      parentId: int4("parent_id").references((): AnyCockroachColumn => user.id)
    });

    // or
    export const user = cockroachTable("user", {
      id: int4().primaryKey(),
      name: text(),
      parentId: int4("parent_id"),
    }, (table) => [
      foreignKey({
        columns: [table.parentId],
        foreignColumns: [table.id],
        name: "custom_fk"
      })
    ]);
    ```

  </Tab>
</Tabs>
To declare multi-column foreign keys you can use a dedicated `foreignKey` operator:
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    ```typescript copy {4-5,14-15,18-21}
    import { serial, text, foreignKey, pgTable, AnyPgColumn } from "drizzle-orm/pg-core";

    export const user = pgTable("user", {
      firstName: text("firstName"),
      lastName: text("lastName"),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);

    export const profile = pgTable("profile", {
      id: serial("id").primaryKey(),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_fk"
      })
    ])
    ```

  </Tab>
  <Tab>
    ```typescript copy {4-5,14-15,18-21}
    import { int, text, primaryKey, foreignKey, mysqlTable, AnyMySqlColumn } from "drizzle-orm/mysql-core";

    export const user = mysqlTable("user", {
      firstName: text("firstName"),
      lastName: text("lastName"),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);

    export const profile = mysqlTable("profile", {
      id: int("id").autoincrement().primaryKey(),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_name"
      })
    ]);
    ```

  </Tab>
  <Tab>
    ```typescript {4-5,14-15,18-21}
    import { integer, text, primaryKey, foreignKey, sqliteTable, AnySQLiteColumn } from "drizzle-orm/sqlite-core";

    export const user = sqliteTable("user", {
      firstName: text("firstName"),
      lastName: text("lastName"),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);

    export const profile = sqliteTable("profile", {
      id: integer("id").primaryKey({ autoIncrement: true }),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_name"
      })
    ]);
    ```

  </Tab>
  <Tab>
    Currently not supported in SingleStore
  </Tab>
  <Tab>
    ```typescript copy {4-5,14-15,18-21}
    import { int, text, primaryKey, foreignKey, mssqlTable, AnyMsSqlColumn } from "drizzle-orm/mssql-core";

    export const user = mssqlTable("user", {
      firstName: text(),
      lastName: text(),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);

    export const profile = mssqlTable("profile", {
      id: int().primaryKey(),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_name"
      })
    ]);
    ```

  </Tab>
    <Tab>
    ```typescript copy {4-5,14-15,18-21}
    import { int4, text, foreignKey, cockroachTable, AnyCockroachColumn } from "drizzle-orm/cockroach-core";

    export const user = cockroachTable("user", {
      firstName: text(),
      lastName: text(),
    }, (table) => [
      primaryKey({ columns: [table.firstName, table.lastName]})
    ]);

    export const profile = cockroachTable("profile", {
      id: int4().primaryKey(),
      userFirstName: text("user_first_name"),
      userLastName: text("user_last_name"),
    }, (table) => [
      foreignKey({
        columns: [table.userFirstName, table.userLastName],
        foreignColumns: [user.firstName, user.lastName],
        name: "custom_fk"
      })
    ])
    ```
  </Tab>
</Tabs>


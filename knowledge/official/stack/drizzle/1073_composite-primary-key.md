### Composite Primary Key

Just like `PRIMARY KEY`, composite primary key uniquely identifies each record in a table using multiple fields.

Drizzle ORM provides a standalone `primaryKey` operator for that:
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite', 'SingleStore', 'MSSQL', 'CockroachDB']}>
  <Tab>
    <Section>
      ```typescript copy {18, 19}
      import { serial, text, integer, primaryKey, pgTable } from "drizzle-orm/pg-core";

      export const user = pgTable("user", {
        id: serial("id").primaryKey(),
        name: text("name"),
      });

      export const book = pgTable("book", {
        id: serial("id").primaryKey(),
        name: text("name"),
      });

      export const booksToAuthors = pgTable("books_to_authors", {
        authorId: integer("author_id"),
        bookId: integer("book_id"),
      }, (table) => [
        primaryKey({ columns: [table.bookId, table.authorId] }),
        // Or PK with custom name
        primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] }),
      ]);
      ```

      ```sql {6, 9}
      ...

      CREATE TABLE "books_to_authors" (
        "author_id" integer,
        "book_id" integer,
        PRIMARY KEY("book_id","author_id")
      );

      ALTER TABLE "books_to_authors" ADD CONSTRAINT "custom_name" PRIMARY KEY("book_id","author_id");
      ```
    </Section>

  </Tab> 
  <Tab>
    <Section>
      ```typescript {18, 19}
      import { int, text, primaryKey, mysqlTable } from "drizzle-orm/mysql-core";

      export const user = mysqlTable("user", {
        id: int("id").autoincrement().primaryKey(),
        name: text("name"),
      });

      export const book = mysqlTable("book", {
        id: int("id").autoincrement().primaryKey(),
        name: text("name"),
      });

      export const booksToAuthors = mysqlTable("books_to_authors", {
        authorId: int("author_id"),
        bookId: int("book_id"),
      }, (table) => [
        primaryKey({ columns: [table.bookId, table.authorId] }),
        // Or PK with custom name
        primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] })
      ]);
      ```

      ```sql {6}
      ...

      CREATE TABLE `books_to_authors` (
        `author_id` int,
        `book_id` int,
        PRIMARY KEY(`book_id`,`author_id`)
      );
      ```
    </Section>

  </Tab>
  <Tab>
   <Section>
      ```typescript copy {18, 19}
      import { integer, text, primaryKey, sqliteTable} from "drizzle-orm/sqlite-core";

      export const user = sqliteTable("user", {
        id: integer("id").primaryKey({ autoIncrement: true }),
        name: text("name"),
      });

      export const book = sqliteTable("book", {
        id: integer("id").primaryKey({ autoIncrement: true }),
        name: text("name"),
      });

      export const bookToAuthor = sqliteTable("book_to_author", {
        authorId: integer("author_id"),
        bookId: integer("book_id"),
      }, (table) => [
        primaryKey({ columns: [table.bookId, table.authorId] }),
        // Or PK with custom name
        primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] })
      ]);
      ```
      ```sql {6}
      ...

      CREATE TABLE `book_to_author` (
        `author_id` integer,
        `book_id` integer,
        PRIMARY KEY(`book_id`, `author_id`)
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript {18, 19}
      import { int, text, primaryKey, mysqlTable } from "drizzle-orm/singlestore-core";

      export const user = singlestoreTable("user", {
        id: int("id").autoincrement().primaryKey(),
        name: text("name"),
      });

      export const book = singlestoreTable("book", {
        id: int("id").autoincrement().primaryKey(),
        name: text("name"),
      });

      export const booksToAuthors = singlestoreTable("books_to_authors", {
        authorId: int("author_id"),
        bookId: int("book_id"),
      }, (table) => [
        primaryKey({ columns: [table.bookId, table.authorId] }),
        // Or PK with custom name
        primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] }),
      ]);
      ```

      ```sql {6}
      ...

      CREATE TABLE `books_to_authors` (
        `author_id` int,
        `book_id` int,
        PRIMARY KEY(`book_id`,`author_id`)
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript {18, 19}
      import { int, text, primaryKey, mssqlTable } from "drizzle-orm/mssql-core";

      export const user = mssqlTable("user", {
        id: int().primaryKey(),
        name: text(),
      });

      export const book = mssqlTable("book", {
        id: int().primaryKey(),
        name: text(),
      });

      export const booksToAuthors = mssqlTable("books_to_authors", {
        authorId: int("author_id"),
        bookId: int("book_id"),
      }, (table) => [
        primaryKey({ columns: [table.bookId, table.authorId] }),
        // Or PK with custom name
        primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] }),
      ]);
      ```

      ```sql {6}
      ...

      CREATE TABLE [books_to_authors] (
        [author_id] int,
        [book_id] int,
        CONSTRAINT [custom_name] PRIMARY KEY([book_id], [author_id])
      );
      ```
    </Section>

  </Tab>
  <Tab>
    <Section>
      ```typescript copy {18, 19}
      import { int4, text, primaryKey, cockroachTable } from "drizzle-orm/cockroach-core";

      export const user = cockroachTable("user", {
        id: int4().primaryKey(),
        name: text(),
      });

      export const book = cockroachTable("book", {
        id: int4("id").primaryKey(),
        name: text("name"),
      });

      export const booksToAuthors = cockroachTable("books_to_authors", {
        authorId: int4("author_id"),
        bookId: int4("book_id"),
      }, (table) => [
        primaryKey({ columns: [table.bookId, table.authorId] }),
        // Or PK with custom name
        primaryKey({ name: 'custom_name', columns: [table.bookId, table.authorId] }),
      ]);
      ```

      ```sql {6, 9}
      ...

      CREATE TABLE "books_to_authors" (
        "author_id" int4,
        "book_id" int4,
        PRIMARY KEY("book_id","author_id")
      );

      ALTER TABLE "books_to_authors" ADD CONSTRAINT "custom_name" PRIMARY KEY("book_id","author_id");
      ```
    </Section>
  </Tab> 
</Tabs>


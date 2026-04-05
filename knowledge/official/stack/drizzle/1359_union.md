### Union
Combine all results from two query blocks into a single result, omitting any duplicates.

Get all names from customers and users tables without duplicates.

<Tabs items={["PostgreSQL", "MySQL", "SQLite", "SingleStore", "MSSQL", "CockroachDB"]}>
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { union } from 'drizzle-orm/pg-core'
    import { users, customers } from './schema'

    const allNamesForUserQuery = db.select({ name: users.name }).from(users);

    const result = await union(
		allNamesForUserQuery,
		db.select({ name: customers.name }).from(customers)
	).limit(10);
    ```
    ```sql
    (select "name" from "sellers")
    union
    (select "name" from "customers")
    limit $1
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { users, customers } from './schema'

    const result = await db
      .select({ name: users.name })
      .from(users)
      .union(db.select({ name: customers.name }).from(customers))
      .limit(10);
    ```
    ```sql
    (select "name" from "sellers")
    union
    (select "name" from "customers")
    limit $1
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { integer, pgTable, text, varchar } from "drizzle-orm/pg-core";

    const users = pgTable('sellers', {
        id: integer('id').primaryKey(),
        name: varchar('name', { length: 256 }).notNull(),
        address: text('address'),
    });
    
    const customers = pgTable('customers', {
        id: integer('id').primaryKey(),
        name: varchar('name', { length: 256 }).notNull(),
        city: text('city'),
        email: varchar('email', { length: 256 }).notNull()
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { union } from 'drizzle-orm/mysql-core'
    import { users, customers } from './schema'

    const allNamesForUserQuery = db.select({ name: users.name }).from(users);

    const result = await union(
		allNamesForUserQuery,
		db.select({ name: customers.name }).from(customers)
	).limit(10);
    ```
    ```sql
    (select `name` from `sellers`)
    union
    (select `name` from `customers`)
    limit ?
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { users, customers } from './schema'

    const result = await db
      .select({ name: users.name })
      .from(users)
      .union(db.select({ name: customers.name }).from(customers))
      .limit(10);
    ```
    ```sql
    (select `name` from `sellers`)
    union
    (select `name` from `customers`)
    limit ?
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mysqlTable, text, varchar } from "drizzle-orm/mysql-core";

    const users = mysqlTable('sellers', {
        id: int('id').primaryKey(),
        name: varchar('name', { length: 256 }).notNull(),
        address: text('address'),
    });
    
    const customers = mysqlTable('customers', {
        id: int('id').primaryKey(),
        name: varchar('name', { length: 256 }).notNull(),
        city: text('city'),
        email: varchar('email', { length: 256 }).notNull()
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { union } from 'drizzle-orm/sqlite-core'
    import { users, customers } from './schema'

    const allNamesForUserQuery = db.select({ name: users.name }).from(users);

    const result = await union(
		allNamesForUserQuery,
		db.select({ name: customers.name }).from(customers)
	).limit(10);
    ```
    ```sql
    (select "name" from "sellers")
    union 
    (select "name" from "customers")
    limit ?
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { users, customers } from './schema'

    const result = await db
      .select({ name: users.name })
      .from(users)
      .union(db.select({ name: customers.name }).from(customers))
      .limit(10);
    ```
    ```sql
    select "name" from "sellers" union select "name" from "customers" limit ?
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, sqliteTable, text } from "drizzle-orm/sqlite-core";

    const users = sqliteTable('sellers', {
        id: int('id').primaryKey(),
        name: text('name').notNull(),
        address: text('address'),
    });
    
    const customers = sqliteTable('customers', {
        id: int('id').primaryKey(),
        name: text('name').notNull(),
        city: text('city'),
        email: text('email').notNull()
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { union } from 'drizzle-orm/singlestore-core'
    import { users, customers } from './schema'

    const allNamesForUserQuery = db.select({ name: users.name }).from(users);

    const result = await union(
		allNamesForUserQuery,
		db.select({ name: customers.name }).from(customers)
	).limit(10);
    ```
    ```sql
    (select `name` from `sellers`)
    union
    (select `name` from `customers`)
    limit ?
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { users, customers } from './schema'

    const result = await db
      .select({ name: users.name })
      .from(users)
      .union(db.select({ name: customers.name }).from(customers))
      .limit(10);
    ```
    ```sql
    (select `name` from `sellers`)
    union
    (select `name` from `customers`)
    limit ?
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mysqlTable, text, varchar } from "drizzle-orm/singlestore-core";

    const users = mysqlTable('sellers', {
        id: int('id').primaryKey(),
        name: varchar('name', { length: 256 }).notNull(),
        address: text('address'),
    });
    
    const customers = mysqlTable('customers', {
        id: int('id').primaryKey(),
        name: varchar('name', { length: 256 }).notNull(),
        city: text('city'),
        email: varchar('email', { length: 256 }).notNull()
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { union } from 'drizzle-orm/mssql-core'
    import { users, customers } from './schema'

    const allNamesForUserQuery = db.select({ name: users.name }).from(users);

    const result = await union(
		allNamesForUserQuery,
		db.select({ name: customers.name }).from(customers)
	).limit(10);
    ```
    ```sql
    (select [name] from [sellers])
    union
    (select [name] from [customers])
    limit @limit
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { users, customers } from './schema'

    const result = await db
      .select({ name: users.name })
      .from(users)
      .union(db.select({ name: customers.name }).from(customers))
      .limit(10);
    ```
    ```sql
    (select [name] from [sellers])
    union
    (select [name] from [customers])
    limit @limit
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mssqlTable, ntext, nvarchar } from "drizzle-orm/mssql-core";

    const users = mssqlTable('sellers', {
        id: int().primaryKey(),
        name: nvarchar({ length: 256 }).notNull(),
        address: ntext(),
    });
    
    const customers = mssqlTable('customers', {
        id: int().primaryKey(),
        name: nvarchar({ length: 256 }).notNull(),
        city: ntext(),
        email: nvarchar({ length: 256 }).notNull()
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { union } from 'drizzle-orm/cockroach-core'
    import { users, customers } from './schema'

    const allNamesForUserQuery = db.select({ name: users.name }).from(users);

    const result = await union(
		allNamesForUserQuery,
		db.select({ name: customers.name }).from(customers)
	).limit(10);
    ```
    ```sql
    (select "name" from "sellers")
    union
    (select "name" from "customers")
    limit $1
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { users, customers } from './schema'

    const result = await db
      .select({ name: users.name })
      .from(users)
      .union(db.select({ name: customers.name }).from(customers))
      .limit(10);
    ```
    ```sql
    (select "name" from "sellers")
    union
    (select "name" from "customers")
    limit $1
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { int4, cockroachTable, text, varchar } from "drizzle-orm/cockroach-core";

    const users = cockroachTable('sellers', {
        id: int4().primaryKey(),
        name: varchar({ length: 256 }).notNull(),
        address: text(),
    });
    
    const customers = cockroachTable('customers', {
        id: int4().primaryKey(),
        name: varchar({ length: 256 }).notNull(),
        city: text(),
        email: varchar({ length: 256 }).notNull()
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
</Tabs>


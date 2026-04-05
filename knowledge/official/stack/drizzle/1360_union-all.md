### Union All
Combine all results from two query blocks into a single result, with duplicates.

Let's consider a scenario where you have two tables, one representing online sales and the other 
representing in-store sales. In this case, you want to combine the data from both tables into a
single result set. Since there might be duplicate transactions, 
you want to keep all the records and not eliminate duplicates.

<Tabs items={["PostgreSQL", "MySQL", "SQLite", "SingleStore", "MSSQL", "CockroachDB"]}>
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { unionAll } from 'drizzle-orm/pg-core'
    import { onlineSales, inStoreSales } from './schema'

    const onlineTransactions = db.select({ transaction: onlineSales.transactionId }).from(onlineSales);
    const inStoreTransactions = db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales);

    const result = await unionAll(onlineTransactions, inStoreTransactions);
    ```
    ```sql
    select "transaction_id" from "online_sales"
    union all
    select "transaction_id" from "in_store_sales"
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { onlineSales, inStoreSales } from './schema'

    const result = await db
      .select({ transaction: onlineSales.transactionId })
      .from(onlineSales)
      .unionAll(
        db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales)
      );
    ```
    ```sql
    select "transaction_id" from "online_sales"
    union all
    select "transaction_id" from "in_store_sales"
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { integer, pgTable, text, timestamp, varchar } from "drizzle-orm/pg-core";

    const onlineSales = pgTable('online_sales', {
        transactionId: integer('transaction_id').primaryKey(),
        productId: integer('product_id').unique(),
        quantitySold: integer('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    
    const inStoreSales = pgTable('in_store_sales', {
        transactionId: integer('transaction_id').primaryKey(),
        productId: integer('product_id').unique(),
        quantitySold: integer('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
<Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { unionAll } from 'drizzle-orm/mysql-core'
    import { onlineSales, inStoreSales } from './schema'

    const onlineTransactions = db.select({ transaction: onlineSales.transactionId }).from(onlineSales);
    const inStoreTransactions = db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales);

    const result = await unionAll(onlineTransactions, inStoreTransactions);
    ```
    ```sql
    select `transaction_id` from `online_sales`
    union all
    select `transaction_id` from `in_store_sales`
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { onlineSales, inStoreSales } from './schema'

    const result = await db
      .select({ transaction: onlineSales.transactionId })
      .from(onlineSales)
      .unionAll(
        db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales)
      );
    ```
    ```sql
    (select `transaction_id` from `online_sales`)
    union all 
    (select `transaction_id` from `in_store_sales`)
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mysqlTable, text, timestamp, varchar } from "drizzle-orm/mysql-core";

    const onlineSales = mysqlTable('online_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    
    const inStoreSales = mysqlTable('in_store_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { unionAll } from 'drizzle-orm/sqlite-core'
    import { onlineSales, inStoreSales } from './schema'

    const onlineTransactions = db.select({ transaction: onlineSales.transactionId }).from(onlineSales);
    const inStoreTransactions = db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales);

    const result = await unionAll(onlineTransactions, inStoreTransactions);
    ```
    ```sql
    select "transaction_id" from "online_sales" 
    union all 
    select "transaction_id" from "in_store_sales"
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { onlineSales, inStoreSales } from './schema'

    const result = await db
      .select({ transaction: onlineSales.transactionId })
      .from(onlineSales)
      .unionAll(
        db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales)
      );
    ```
    ```sql
    select "transaction_id" from "online_sales" 
    union all 
    select "transaction_id" from "in_store_sales"
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { int, sqliteTable } from "drizzle-orm/sqlite-core";

    const onlineSales = sqliteTable('online_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: int('sale_date', { mode: 'timestamp' }),
    });
    
    const inStoreSales = sqliteTable('in_store_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: int('sale_date', { mode: 'timestamp' }),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <Callout type='warning'>
  UNION ALL with ORDER BY behavior inconsistent with MySQL: SingleStore parses UNION ALL followed by ORDER BY commands differently from MySQL. In SingleStore, the following query is valid. In MySQL, it is invalid.
  </Callout>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { unionAll } from 'drizzle-orm/singlestore-core'
    import { onlineSales, inStoreSales } from './schema'

    const onlineTransactions = db.select({ transaction: onlineSales.transactionId }).from(onlineSales);
    const inStoreTransactions = db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales);

    const result = await unionAll(onlineTransactions, inStoreTransactions);
    ```
    ```sql
    select `transaction_id` from `online_sales`
    union all
    select `transaction_id` from `in_store_sales`
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { onlineSales, inStoreSales } from './schema'

    const result = await db
      .select({ transaction: onlineSales.transactionId })
      .from(onlineSales)
      .unionAll(
        db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales)
      );
    ```
    ```sql
    (select `transaction_id` from `online_sales`)
    union all 
    (select `transaction_id` from `in_store_sales`)
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mysqlTable, text, timestamp, varchar } from "drizzle-orm/singlestore-core";

    const onlineSales = mysqlTable('online_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    
    const inStoreSales = mysqlTable('in_store_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { unionAll } from 'drizzle-orm/mssql-core'
    import { onlineSales, inStoreSales } from './schema'

    const onlineTransactions = db.select({ transaction: onlineSales.transactionId }).from(onlineSales);
    const inStoreTransactions = db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales);

    const result = await unionAll(onlineTransactions, inStoreTransactions);
    ```
    ```sql
    (select [transaction_id] from [online_sales])
    union all
    (select [transaction_id] from [in_store_sales])
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { onlineSales, inStoreSales } from './schema'

    const result = await db
      .select({ transaction: onlineSales.transactionId })
      .from(onlineSales)
      .unionAll(
        db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales)
      );
    ```
    ```sql
    (select [transaction_id] from [online_sales])
    union all
    (select [transaction_id] from [in_store_sales])
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mssqlTable, timestamp } from "drizzle-orm/mssql-core";

    const onlineSales = mysqlTable('online_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    
    const inStoreSales = mysqlTable('in_store_sales', {
        transactionId: int('transaction_id').primaryKey(),
        productId: int('product_id').unique(),
        quantitySold: int('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { unionAll } from 'drizzle-orm/cockroach-core'
    import { onlineSales, inStoreSales } from './schema'

    const onlineTransactions = db.select({ transaction: onlineSales.transactionId }).from(onlineSales);
    const inStoreTransactions = db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales);

    const result = await unionAll(onlineTransactions, inStoreTransactions);
    ```
    ```sql
    select "transaction_id" from "online_sales"
    union all
    select "transaction_id" from "in_store_sales"
    ```
    </CodeTab>
    <CodeTab>
    ```ts copy
    import { onlineSales, inStoreSales } from './schema'

    const result = await db
      .select({ transaction: onlineSales.transactionId })
      .from(onlineSales)
      .unionAll(
        db.select({ transaction: inStoreSales.transactionId }).from(inStoreSales)
      );
    ```
    ```sql
    select "transaction_id" from "online_sales"
    union all
    select "transaction_id" from "in_store_sales"
    ```
	</CodeTab>
    <CodeTab>
	```typescript copy
    import { int4, cockroachTable, text, timestamp, varchar } from "drizzle-orm/cockroach-core";

    const onlineSales = cockroachTable('online_sales', {
        transactionId: int4('transaction_id').primaryKey(),
        productId: int4('product_id').unique(),
        quantitySold: int4('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    
    const inStoreSales = cockroachTable('in_store_sales', {
        transactionId: int4('transaction_id').primaryKey(),
        productId: int4('product_id').unique(),
        quantitySold: int4('quantity_sold'),
        saleDate: timestamp('sale_date', { mode: 'date' }),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
</Tabs>


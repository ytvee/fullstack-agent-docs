### Except All
For two query blocks A and B, return all results from A which are not also present in B, with duplicates.

Let's consider a scenario where you have two tables containing data about customer orders, and you want to 
identify products that are exclusively ordered by regular customers (without VIP customers). 
In this case, you want to keep track of the quantity of each product, even if it's ordered multiple times by different regular customers.

In this scenario, you want to find products that are exclusively ordered by regular customers and not 
ordered by VIP customers. You want to retain the quantity information, even if the same product is ordered multiple times by different regular customers.

<Tabs items={["PostgreSQL", "MySQL", "SQLite", "SingleStore", "MSSQL", "CockroachDB"]}>
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { exceptAll } from 'drizzle-orm/pg-core'
    import { regularCustomerOrders, vipCustomerOrders } from './schema'

    const regularOrders = db.select({ 
        productId: regularCustomerOrders.productId,
        quantityOrdered: regularCustomerOrders.quantityOrdered }
    ).from(regularCustomerOrders);

    const vipOrders = db.select({ 
        productId: vipCustomerOrders.productId,
        quantityOrdered: vipCustomerOrders.quantityOrdered }
    ).from(vipCustomerOrders);

    const result = await exceptAll(regularOrders, vipOrders);
    ```
    ```sql
    select "product_id", "quantity_ordered" from "regular_customer_orders"
    except all
    select "product_id", "quantity_ordered" from "vip_customer_orders"
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { regularCustomerOrders, vipCustomerOrders } from './schema'
 
    const result = await db
        .select({
          productId: regularCustomerOrders.productId,
          quantityOrdered: regularCustomerOrders.quantityOrdered,
        })
        .from(regularCustomerOrders)
        .exceptAll(
          db
            .select({
              productId: vipCustomerOrders.productId,
              quantityOrdered: vipCustomerOrders.quantityOrdered,
            })
            .from(vipCustomerOrders)
        );
    ```
    ```sql
    select "product_id", "quantity_ordered" from "regular_customer_orders"
    except all
    select "product_id", "quantity_ordered" from "vip_customer_orders"
    ```
    </CodeTab>
	<CodeTab>
	```typescript copy
    import { integer, pgTable } from "drizzle-orm/pg-core";

    const regularCustomerOrders = pgTable('regular_customer_orders', {
        customerId: integer('customer_id').primaryKey(),
        productId: integer('product_id').notNull(),
        quantityOrdered: integer('quantity_ordered').notNull(),
    });
    
    const vipCustomerOrders = pgTable('vip_customer_orders', {
        customerId: integer('customer_id').primaryKey(),
        productId: integer('product_id').notNull(),
        quantityOrdered: integer('quantity_ordered').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { exceptAll } from 'drizzle-orm/mysql-core'
    import { regularCustomerOrders, vipCustomerOrders } from './schema'

    const regularOrders = db.select({ 
        productId: regularCustomerOrders.productId,
        quantityOrdered: regularCustomerOrders.quantityOrdered }
    ).from(regularCustomerOrders);

    const vipOrders = db.select({ 
        productId: vipCustomerOrders.productId,
        quantityOrdered: vipCustomerOrders.quantityOrdered }
    ).from(vipCustomerOrders);

    const result = await exceptAll(regularOrders, vipOrders);
    ```
    ```sql
    select `product_id`, `quantity_ordered` from `regular_customer_orders`
    except all
    select `product_id`, `quantity_ordered` from `vip_customer_orders`
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { regularCustomerOrders, vipCustomerOrders } from './schema'
 
    const result = await db
        .select({
          productId: regularCustomerOrders.productId,
          quantityOrdered: regularCustomerOrders.quantityOrdered,
        })
        .from(regularCustomerOrders)
        .exceptAll(
          db
            .select({
              productId: vipCustomerOrders.productId,
              quantityOrdered: vipCustomerOrders.quantityOrdered,
            })
            .from(vipCustomerOrders)
        );
    ```
    ```sql
    select `product_id`, `quantity_ordered` from `regular_customer_orders`
    except all
    select `product_id`, `quantity_ordered` from `vip_customer_orders`
    ```
    </CodeTab>
	<CodeTab>
	```typescript copy
    const regularCustomerOrders = mysqlTable('regular_customer_orders', {
        customerId: int('customer_id').primaryKey(),
        productId: int('product_id').notNull(),
        quantityOrdered: int('quantity_ordered').notNull(),
    });
    
    const vipCustomerOrders = mysqlTable('vip_customer_orders', {
        customerId: int('customer_id').primaryKey(),
        productId: int('product_id').notNull(),
        quantityOrdered: int('quantity_ordered').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  Not supported by SQLite
  </Tab>
  <Tab>
  Not supported by SingleStore
  </Tab>
  <Tab>
  Not supported by MSSQL
  </Tab>
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { exceptAll } from 'drizzle-orm/cockroach-core'
    import { regularCustomerOrders, vipCustomerOrders } from './schema'

    const regularOrders = db.select({ 
        productId: regularCustomerOrders.productId,
        quantityOrdered: regularCustomerOrders.quantityOrdered }
    ).from(regularCustomerOrders);

    const vipOrders = db.select({ 
        productId: vipCustomerOrders.productId,
        quantityOrdered: vipCustomerOrders.quantityOrdered }
    ).from(vipCustomerOrders);

    const result = await exceptAll(regularOrders, vipOrders);
    ```
    ```sql
    select "product_id", "quantity_ordered" from "regular_customer_orders"
    except all
    select "product_id", "quantity_ordered" from "vip_customer_orders"
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { regularCustomerOrders, vipCustomerOrders } from './schema'
 
    const result = await db
        .select({
          productId: regularCustomerOrders.productId,
          quantityOrdered: regularCustomerOrders.quantityOrdered,
        })
        .from(regularCustomerOrders)
        .exceptAll(
          db
            .select({
              productId: vipCustomerOrders.productId,
              quantityOrdered: vipCustomerOrders.quantityOrdered,
            })
            .from(vipCustomerOrders)
        );
    ```
    ```sql
    select "product_id", "quantity_ordered" from "regular_customer_orders"
    except all
    select "product_id", "quantity_ordered" from "vip_customer_orders"
    ```
    </CodeTab>
	<CodeTab>
	```typescript copy
    import { int4, cockroachTable } from "drizzle-orm/cockroach-core";

    const regularCustomerOrders = cockroachTable('regular_customer_orders', {
        customerId: int4('customer_id').primaryKey(),
        productId: int4('product_id').notNull(),
        quantityOrdered: int4('quantity_ordered').notNull(),
    });
    
    const vipCustomerOrders = cockroachTable('vip_customer_orders', {
        customerId: int4('customer_id').primaryKey(),
        productId: int4('product_id').notNull(),
        quantityOrdered: int4('quantity_ordered').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
</Tabs>


Source: https://orm.drizzle.team/docs/sql-schema-declaration

import Tab from '@mdx/Tab.astro';
import Tabs from '@mdx/Tabs.astro';
import Callout from '@mdx/Callout.astro';
import SimpleLinkCards from '@mdx/SimpleLinkCards.astro';
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from '@mdx/Section.astro';
import Flex from "@mdx/Flex.astro"
import LinksList from "@mdx/LinksList.astro"


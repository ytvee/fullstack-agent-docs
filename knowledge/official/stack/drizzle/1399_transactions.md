# Transactions

SQL transaction is a grouping of one or more SQL statements that interact with a database.
A transaction in its entirety can commit to a database as a single logical unit
or rollback (become undone) as a single logical unit.

Drizzle ORM provides APIs to run SQL statements in transactions:

```ts copy
const db = drizzle(...)

await db.transaction(async (tx) => {
  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));
});
```

Drizzle ORM supports `savepoints` with nested transactions API:

```ts copy {7-9}
const db = drizzle(...)

await db.transaction(async (tx) => {
  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));

  await tx.transaction(async (tx2) => {
    await tx2.update(users).set({ name: "Mr. Dan" }).where(eq(users.name, "Dan"));
  });
});
```

You can embed business logic to the transaction and rollback whenever needed:

```ts copy {7}
const db = drizzle(...)

await db.transaction(async (tx) => {
  const [account] = await tx.select({ balance: accounts.balance }).from(accounts).where(eq(users.name, 'Dan'));
  if (account.balance < 100) {
    // This throws an exception that rollbacks the transaction.
    tx.rollback()
  }

  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));
});
```

You can return values from the transaction:

```ts copy {8}
const db = drizzle(...)

const newBalance: number = await db.transaction(async (tx) => {
  await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, 'Dan'));
  await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, 'Andrew'));

  const [account] = await tx.select({ balance: accounts.balance }).from(accounts).where(eq(users.name, 'Dan'));
  return account.balance;
});
```

You can use transactions with **[relational queries](/docs/rqb)**:

```ts
const db = drizzle({ schema })

await db.transaction(async (tx) => {
  await tx.query.users.findMany({
    with: {
      accounts: true
    }
  });
});
```





We provide dialect-specific transaction configuration APIs:

<Tabs items={["PostgreSQL", "MySQL", "SQLite", "SingleStore", "MSSQL", "CockroachDB"]}>
<Tab>
```ts copy {6-8}
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    deferrable: true,
  }
);

interface PgTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  deferrable?: boolean;
}
```
</Tab>
<Tab>
```ts {6-8}
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    withConsistentSnapshot: true,
  }
);

interface MySqlTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  withConsistentSnapshot?: boolean;
}
```
</Tab>
<Tab>
```ts {6}
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    behavior: "deferred",
  }
);

interface SQLiteTransactionConfig {
    behavior?: 'deferred' | 'immediate' | 'exclusive';
}
```
</Tab>
<Tab>
```ts {6-8}
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    withConsistentSnapshot: true,
  }
);

interface SingleStoreTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  withConsistentSnapshot?: boolean;
}
```
</Tab>
<Tab>
```ts copy {6-8}
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
  }
);

interface MsSqlTransactionConfig {
  isolationLevel?: 'read uncommitted' | 'read committed' | 'repeatable read' | 'serializable' | 'snapshot';
}
```
</Tab>
<Tab>
```ts copy {6-8}
await db.transaction(
  async (tx) => {
    await tx.update(accounts).set({ balance: sql`${accounts.balance} - 100.00` }).where(eq(users.name, "Dan"));
    await tx.update(accounts).set({ balance: sql`${accounts.balance} + 100.00` }).where(eq(users.name, "Andrew"));
  }, {
    isolationLevel: "read committed",
    accessMode: "read write",
    deferrable: true,
  }
);

interface CockroachTransactionConfig {
  isolationLevel?:
    | "read uncommitted"
    | "read committed"
    | "repeatable read"
    | "serializable";
  accessMode?: "read only" | "read write";
  deferrable?: boolean;
}
```
</Tab>
</Tabs>



Source: https://orm.drizzle.team/docs/tutorials

import Tutorials from "@components/Tutorials.astro";

<Tutorials/>

Source: https://orm.drizzle.team/docs/tutorials/drizzle-with-netlify-edge-functions-neon


import Prerequisites from "@mdx/Prerequisites.astro";
import Npm from '@mdx/Npm.astro';
import Steps from '@mdx/Steps.astro';
import Section from "@mdx/Section.astro";
import Callout from "@mdx/Callout.astro";

This tutorial demonstrates how to use Drizzle ORM with [Netlify Edge Functions](https://docs.netlify.com/edge-functions/overview/) and [Neon Postgres](https://neon.tech/) database.

<Prerequisites>
- You should have the latest version of [Netlify CLI](https://docs.netlify.com/cli/get-started/#installation) installed.
- You should have installed Drizzle ORM and [Drizzle kit](/docs/kit-overview). You can do this by running the following command:
<Npm>
drizzle-orm
-D drizzle-kit
</Npm>

- You should have installed the `dotenv` package for managing environment variables. If you use Node.js `v20.6.0` or later, there is no need to install it because Node.js natively supports `.env` files. Read more about it [here](https://nodejs.org/en/blog/release/v20.6.0#built-in-env-file-support).
<Npm>
  dotenv
</Npm>

- Optionally, you can install the `@netlify/edge-functions` package to import the types for the `Context` object which will be used later.
<Npm>
  @netlify/edge-functions
</Npm>
</Prerequisites>

<Callout type="warning">
These installed packages are used only to create table in the database in [Create a table](#create-a-table), [Setup Drizzle config file](#setup-drizzle-config-file) and [Apply changes to the database](#apply-changes-to-the-database) steps. These packages do not affect the code running inside Netlify Edge Functions. We will use `import_map.json` to import the necessary packages for the Edge Functions.
</Callout>

<Steps>

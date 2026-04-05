# Overview on Prisma Migrate (/docs/v6/orm/prisma-migrate/understanding-prisma-migrate/overview)



<br />

<CalloutContainer type="info">
  <CalloutDescription>
    **Does not apply for MongoDB**<br />Instead of `migrate dev` and related commands, use [`db push`](/v6/orm/prisma-migrate/workflows/prototyping-your-schema) for [MongoDB](/v6/orm/overview/databases/mongodb).
  </CalloutDescription>
</CalloutContainer>

Prisma Migrate enables you to:

* Keep your database schema in sync with your [Prisma schema](/v6/orm/prisma-schema/overview) as it evolves *and*
* Maintain existing data in your database

Prisma Migrate generates [a history of `.sql` migration files](/v6/orm/prisma-migrate/understanding-prisma-migrate/migration-histories), and plays a role in both [development and production](/v6/orm/prisma-migrate/workflows/development-and-production).

Prisma Migrate can be considered a *hybrid* database schema migration tool, meaning it has both of *declarative* and *imperative* elements:

* Declarative: The data model is described in a declarative way in the [Prisma schema](/v6/orm/prisma-schema/overview). Prisma Migrate generates SQL migration files from that data model.
* Imperative: All generated SQL migration files are fully customizable. Prisma Migrate hence provides the flexibility of an imperative migration tool by enabling you to modify what and how migrations are executed (and allows you to run custom SQL to e.g. make use of native database feature, perform data migrations, ...).

<CalloutContainer type="info">
  <CalloutDescription>
    If you are prototyping, consider using the [`db push`](/v6/orm/reference/prisma-cli-reference#db-push) command - see [Schema prototyping with `db push`](/v6/orm/prisma-migrate/workflows/prototyping-your-schema) for examples.
  </CalloutDescription>
</CalloutContainer>

See the [Prisma Migrate reference](/v6/orm/reference/prisma-cli-reference#prisma-migrate) for detailed information about the Prisma Migrate CLI commands.



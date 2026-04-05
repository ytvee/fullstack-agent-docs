# Database Features (/docs/orm/reference/database-features)



This page gives an overview of the features which are provided by the databases that Prisma ORM supports. Additionally, it explains how each of these features can be used in Prisma ORM with pointers to further documentation.

Relational database features [#relational-database-features]

This section describes which database features exist on the relational databases that are currently supported by Prisma ORM. The **Prisma schema** column indicates how a certain feature can be represented in the [Prisma schema](/orm/prisma-schema/overview) and links to its documentation. Note that database features can be used in **Prisma Client** even though they might not yet be representable in the Prisma schema.

<CalloutContainer type="info">
  <CalloutDescription>
    These features are *only* for relational databases. Supported features for NoSQL databases, like MongoDB, can [be found below](#nosql-database-features).
  </CalloutDescription>
</CalloutContainer>

Constraints [#constraints]

| Constraint    | Supported |                                       Prisma schema                                      | Prisma Client | Prisma Migrate |
| ------------- | :-------: | :--------------------------------------------------------------------------------------: | :-----------: | :------------: |
| `PRIMARY KEY` |     ✔️    |       [`@id` and `@@id`](/orm/prisma-schema/data-model/models#defining-an-id-field)      |       ✔️      |       ✔️       |
| `FOREIGN KEY` |     ✔️    |        [Relation fields](/orm/prisma-schema/data-model/relations#relation-fields)        |       ✔️      |       ✔️       |
| `UNIQUE`      |    ✔️\*   | [`@unique` and `@@unique`](/orm/prisma-schema/data-model/models#defining-a-unique-field) |       ✔️      |       ✔️       |
| `CHECK`       |    ✔️†    |                                          Not yet                                         |       ✔️      |     Not yet    |
| `NOT NULL`    |     ✔️    |                [`?`](/orm/prisma-schema/data-model/models#type-modifiers)                |       ✔️      |       ✔️       |
| `DEFAULT`     |     ✔️    |        [`@default`](/orm/prisma-schema/data-model/models#defining-a-default-value)       |       ✔️      |       ✔️       |
| `EXCLUDE`     |    ✔️‡    |                                          Not yet                                         |       ✔️      |     Not yet    |

> \* [Caveats apply when using the `UNIQUE` constraint with Microsoft SQL Server](/orm/core-concepts/supported-databases/sql-server#common-considerations)
> † Only supported in MySQL in [version 8 and higher](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html).
> ‡ Only supported in PostgreSQL.

Referential Actions (Delete and Update behaviors for foreign key references) [#referential-actions-delete-and-update-behaviors-for-foreign-key-references]

| Deletion behavior | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| ----------------- | :-------: | :-----------: | :-----------: | :------------: |
| `CASCADE`         |     ✔️    |       ✔️      |       ✔️      |       ✔️       |
| `RESTRICT`        |    ✔️\*   |       ✔️      |       ✔️      |       ✔️       |
| `NO ACTION`       |     ✔️    |       ✔️      |       ✔️      |       ✔️       |
| `SET DEFAULT`     |     ✔️    |       ✔️      |       ✔️      |       ✔️       |
| `SET NULL`        |     ✔️    |       ✔️      |       ✔️      |       ✔️       |

> \* `RESTRICT` is not supported in Microsoft SQL Server.

Indexes [#indexes]

| Index          |                 Supported                |                                                Prisma schema                                                | Prisma Client | Prisma Migrate |
| -------------- | :--------------------------------------: | :---------------------------------------------------------------------------------------------------------: | :-----------: | :------------: |
| `UNIQUE`       |                    ✔️                    |           [`@unique` and `@@unique`](/orm/prisma-schema/data-model/models#defining-a-unique-field)          |       ✔️      |       ✔️       |
| `USING`        |              PostgreSQL only             | [`type`](/orm/prisma-schema/data-model/indexes#configuring-the-access-type-of-indexes-with-type-postgresql) |       ✔️      |       ✔️       |
| `WHERE`        |                    ✔️                    |      [`where`](/orm/prisma-schema/data-model/indexes#configuring-partial-indexes-with-where) (Preview)      |       ✔️      |       ✔️       |
| `(expression)` |                    ✔️                    |                                                   Not yet                                                   |       ✔️      |     Not yet    |
| `INCLUDE`      | PostgreSQL and Microsoft SQL Server only |                                                   Not yet                                                   |       ✔️      |     Not yet    |

Algorithm specified via `USING`:

| Index type (Algorithm) | Supported | Prisma schema | Prisma Client | Prisma Migrate |
| ---------------------- | :-------: | :-----------: | :-----------: | :------------: |
| B-tree                 |     ✔️    |      ✔️†      |       ✔️      |     Not yet    |
| Hash                   |     ✔️    |      ✔️†      |       ✔️      |     Not yet    |
| GiST                   |    ✔️\*   |      ✔️†      |      ✔️\*     |     Not yet    |
| GIN                    |    ✔️\*   |      ✔️†      |      ✔️\*     |     Not yet    |
| BRIN                   |    ✔️\*   |      ✔️†      |      ✔️\*     |     Not yet    |
| SP-GiST                |    ✔️\*   |      ✔️†      |      ✔️\*     |     Not yet    |

* \* Not supported for MySQL and SQLite
* † Available with the PostgreSQL connector only in Prisma ORM versions `4.0.0` and later.

Misc [#misc]

| Feature                           |                 Supported                |                                    Prisma schema                                   | Prisma Client | Prisma Migrate |
| --------------------------------- | :--------------------------------------: | :--------------------------------------------------------------------------------: | :-----------: | :------------: |
| Autoincrementing IDs              |                    ✔️                    | [`autoincrement()`](/orm/prisma-schema/data-model/models#defining-a-default-value) |       ✔️      |       ✔️       |
| Arrays                            |              PostgreSQL only             |             [`[]`](/orm/prisma-schema/data-model/models#type-modifiers)            |       ✔️      |       ✔️       |
| Enums                             |                   ✔️\*†                  |            [`enum`](/orm/prisma-schema/data-model/models#defining-enums)           |       ✔️      |       ✔️       |
| Native database types             |                    ✔️                    |                                         ✔️                                         |       ✔️      |     Not yet    |
| SQL Views                         |                    ✔️                    |                                       Not yet                                      |    Not yet    |     Not yet    |
| JSON support                      |                    ✔️†                   |                                         ✔️                                         |       ✔️      |       ✔️       |
| Fuzzy/Phrase full text search     |                    ✔️‡                   |                                       Not yet                                      |    Not yet    |     Not yet    |
| Table inheritance                 | PostgreSQL and Microsoft SQL Server only |                                       Not yet                                      |       ✔️      |     Not yet    |
| Authorization and user management |                    ✔️‡                   |                                       Not yet                                      |    Not yet    |     Not yet    |

* \* Not supported by Microsoft SQL Server
* † JSON and Enum types are supported in SQLite as of Prisma ORM 6.2.0.
* ‡ Not supported by SQLite

NoSQL database features [#nosql-database-features]

This section describes which database features exist on the NoSQL databases that are currently supported by Prisma ORM.

MongoDB [#mongodb]

The following table lists common MongoDB features and describes the level of support offered by Prisma ORM:

| Feature                                   | Supported by Prisma ORM |                                              Notes                                              |
| ----------------------------------------- | :---------------------: | :---------------------------------------------------------------------------------------------: |
| Embedded documents                        |            ✔️           |                                                                                                 |
| Transactions                              |            ✔️           |                                                                                                 |
| Indexes                                   |     ✔️ with caveats     |     Indexes can only be introspected if the field they refer to includes at least some data.    |
| Autoincrementing IDs                      |            No           |                                                                                                 |
| Compound IDs                              |            No           |                         MongoDB does not support composite IDs (`@@id`)                         |
| Generated `ObjectId`                      |            ✔️           |  See: [Defining IDs for MongoDB](/orm/prisma-schema/data-model/models#defining-ids-in-mongodb)  |
| Arrays                                    |            ✔️           |                                                                                                 |
| Enums                                     |            ✔️           |                                 Implemented at Prisma ORM level                                 |
| Native database types                     |            ✔️           | See: [Field mapping reference](/orm/reference/prisma-schema-reference#model-field-scalar-types) |
| JSON support                              |            ✔️           |                      Advanced `Json` field filtering is not yet supported.                      |
| DBrefs                                    |            No           |                                                                                                 |
| Change streams                            |            No           |                                                                                                 |
| Direct access to the aggregation pipeline |            No           |                                                                                                 |



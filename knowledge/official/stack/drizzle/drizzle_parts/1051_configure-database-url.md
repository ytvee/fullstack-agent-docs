#### Configure database url

To connect to the PostgreSQL database, you need to provide the database URL. The URL format is:

```plaintext
postgres://<user>:<password>@<host>:<port>/<database>
```

You should replace placeholders with your actual values. For example, for created container the url will be:

```plaintext
postgres://postgres:mypassword@localhost:5432/postgres
```

Now you can connect to the database using the URL in your application.
</Steps>


Source: https://orm.drizzle.team/docs/seeding-using-with-option


import IsSupportedChipGroup from "@mdx/IsSupportedChipGroup.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Callout from '@mdx/Callout.astro';
import Section from "@mdx/Section.astro";

<IsSupportedChipGroup chips={{PostgreSQL: true, MySQL: true, SQLite: true}}/>

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql), [MySQL](/docs/get-started-mysql) or [SQLite](/docs/get-started-sqlite)
- Get familiar with [One-to-many Relation](/docs/relations#one-to-many)
- Get familiar with [Drizzle Seed](/docs/seed-overview)
</Prerequisites>

<Callout title='Warning'>
Using `with` implies tables to have a one-to-many relationship.

Therefore, if `one` user has `many` posts, you can use `with` as follows:
```ts
users: {
    count: 2,
    with: {
        posts: 3,
    },
},
```
</Callout>


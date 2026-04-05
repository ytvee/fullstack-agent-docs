#### Configure database url

To connect to the MySQL database, you need to provide the database URL. The URL format is:

```plaintext
mysql://<user>:<password>@<host>:<port>/<database>
```

You should replace placeholders with your actual values. For example, for created container the url will be:

```plaintext
mysql://root:mypassword@localhost:3306/mysql
```

Now you can connect to the database using the URL in your application.
</Steps>


Source: https://orm.drizzle.team/docs/point-datatype-psql


import Section from "@mdx/Section.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Callout from '@mdx/Callout.astro';

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql)
- [Point datatype](/docs/column-types/pg#point)
- [Filtering in select statement](/docs/select#filtering)
- [sql operator](/docs/sql)
</Prerequisites>

PostgreSQL has a special datatype to store geometric data called `point`. It is used to represent a point in a two-dimensional space. The point datatype is represented as a pair of `(x, y)` coordinates.
The point expects to receive longitude first, followed by latitude.

<Section>
```ts copy {6}
import { sql } from 'drizzle-orm';

const db = drizzle(...);

await db.execute(
  sql`select point(-90.9, 18.7)`,
);
```

```json
[ 
  { 
    point: '(-90.9,18.7)' 
  }
]
```
</Section>

This is how you can create table with `point` datatype in Drizzle:

```ts {6}
import { pgTable, point, serial, text } from 'drizzle-orm/pg-core';

export const stores = pgTable('stores', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  location: point('location', { mode: 'xy' }).notNull(),
});
```

This is how you can insert point data into the table in Drizzle:

```ts {4, 10, 16}
// mode: 'xy'
await db.insert(stores).values({
  name: 'Test',
  location: { x: -90.9, y: 18.7 },
});

// mode: 'tuple'
await db.insert(stores).values({
  name: 'Test',
  location: [-90.9, 18.7],
});

// sql raw
await db.insert(stores).values({
  name: 'Test',
  location: sql`point(-90.9, 18.7)`,
});
```

To compute the distance between the objects you can use `<->` operator. This is how you can query for the nearest location by coordinates in Drizzle:

<Callout type='warning'>
`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](/docs/upgrade-v1))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`
</Callout>

<Section>
```ts {9, 14, 17}
import { getColumns, sql } from 'drizzle-orm';
import { stores } from './schema';

const point = {
  x: -73.935_242,
  y: 40.730_61,
};

const sqlDistance = sql`location <-> point(${point.x}, ${point.y})`;

await db
  .select({
    ...getColumns(stores),
    distance: sql`round((${sqlDistance})::numeric, 2)`,
  })
  .from(stores)
  .orderBy(sqlDistance)
  .limit(1);
```

```sql
select *, round((location <-> point(-73.935242, 40.73061))::numeric, 2)
from stores order by location <-> point(-73.935242, 40.73061)
limit 1;
```
</Section>

To filter rows to include only those where a `point` type `location` falls within a specified rectangular boundary defined by two diagonal points you can user `<@` operator. It checks if the first object is contained in or on the second object:

<Section>
```ts {12}
const point = {
  x1: -88,
  x2: -73,
  y1: 40,
  y2: 43,
};

await db
  .select()
  .from(stores)
  .where(
    sql`${stores.location} <@ box(point(${point.x1}, ${point.y1}), point(${point.x2}, ${point.y2}))`
  );
```

```sql
select * from stores where location <@ box(point(-88, 40), point(-73, 43));
```
</Section>





Source: https://orm.drizzle.team/docs/postgis-geometry-point


import Section from "@mdx/Section.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import Callout from "@mdx/Callout.astro";
import CodeTab from '@mdx/CodeTab.astro';

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql)
- [Postgis extension](/docs/extensions/pg#postgis)
- [Indexes](/docs/indexes-constraints#indexes)
- [Filtering in select statement](/docs/select#filtering)
- [sql operator](/docs/sql)
</Prerequisites>

`PostGIS` extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data. 

As for now, Drizzle doesn't create extension automatically, so you need to create it manually. Create an empty migration file and add SQL query:

<Section>
```bash
npx drizzle-kit generate --custom
```

```sql
CREATE EXTENSION postgis;
```
</Section>

This is how you can create table with `geometry` datatype and spatial index in Drizzle:

<CodeTabs items={["schema.ts", "migration.sql"]}>
  <CodeTab>
  ```ts copy {8, 11}
  import { geometry, index, pgTable, serial, text } from 'drizzle-orm/pg-core';

  export const stores = pgTable(
    'stores',
    {
      id: serial('id').primaryKey(),
      name: text('name').notNull(),
      location: geometry('location', { type: 'point', mode: 'xy', srid: 4326 }).notNull(),
    },
    (t) => [
      index('spatial_index').using('gist', t.location),
    ]
  );
  ```
  </CodeTab>
  ```sql
  CREATE TABLE IF NOT EXISTS "stores" (
	  "id" serial PRIMARY KEY NOT NULL,
	  "name" text NOT NULL,
	  "location" geometry(point) NOT NULL
  );
  --> statement-breakpoint
  CREATE INDEX IF NOT EXISTS "spatial_index" ON "stores" USING gist ("location");
  ```
</CodeTabs>
 
This is how you can insert `geometry` data into the table in Drizzle. `ST_MakePoint()` in PostGIS creates a geometric object of type `point` using the specified coordinates.
`ST_SetSRID()` sets the `SRID` (unique identifier associated with a specific coordinate system, tolerance, and resolution) on a geometry to a particular integer value:

```ts {4, 10, 16}
// mode: 'xy'
await db.insert(stores).values({
  name: 'Test',
  location: { x: -90.9, y: 18.7 },
});

// mode: 'tuple'
await db.insert(stores).values({
  name: 'Test',
  location: [-90.9, 18.7],
});

// sql raw
await db.insert(stores).values({
  name: 'Test',
  location: sql`ST_SetSRID(ST_MakePoint(-90.9, 18.7), 4326)`,
});
```

To compute the distance between the objects you can use `<->` operator and `ST_Distance()` function, which for `geometry types` returns the minimum planar distance between two geometries. This is how you can query for the nearest location by coordinates in Drizzle with PostGIS:

<Callout type='warning'>
`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](/docs/upgrade-v1))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`
</Callout>

<Section>
```ts copy {9, 14, 17}
import { getColumns, sql } from 'drizzle-orm';
import { stores } from './schema';

const point = {
  x: -73.935_242,
  y: 40.730_61,
};

const sqlPoint = sql`ST_SetSRID(ST_MakePoint(${point.x}, ${point.y}), 4326)`;

await db
  .select({
    ...getColumns(stores),
    distance: sql`ST_Distance(${stores.location}, ${sqlPoint})`,
  })
  .from(stores)
  .orderBy(sql`${stores.location} <-> ${sqlPoint}`)
  .limit(1);
```

```sql
select *, ST_Distance(location, ST_SetSRID(ST_MakePoint(-73.935_242, 40.730_61), 4326))
from stores order by location <-> ST_SetSRID(ST_MakePoint(-73.935_242, 40.730_61), 4326)
limit 1;
```
</Section>

To filter stores located within a specified rectangular area, you can use `ST_MakeEnvelope()` and `ST_Within()` functions. `ST_MakeEnvelope()` creates a rectangular Polygon from the minimum and maximum values for X and Y. `ST_Within()` Returns TRUE if geometry A is within geometry B.

<Section>
```ts copy {13}
const point = {
  x1: -88,
  x2: -73,
  y1: 40,
  y2: 43,
};

await db
  .select()
  .from(stores)
  .where(
    sql`ST_Within(
      ${stores.location}, ST_MakeEnvelope(${point.x1}, ${point.y1}, ${point.x2}, ${point.y2}, 4326)
    )`,
  );
```

```sql
select * from stores where ST_Within(location, ST_MakeEnvelope(-88, 40, -73, 43, 4326));
```
</Section>


Source: https://orm.drizzle.team/docs/postgresql-full-text-search


import Section from "@mdx/Section.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Callout from '@mdx/Callout.astro';

<Prerequisites>
- Get started with [PostgreSQL](/docs/get-started-postgresql)
- [Select statement](/docs/select)
- [Indexes](/docs/indexes-constraints#indexes)
- [sql operator](/docs/sql)
- You should have `drizzle-orm@0.31.0` and `drizzle-kit@0.22.0` or higher.  
</Prerequisites>

This guide demonstrates how to implement full-text search in PostgreSQL with Drizzle ORM. Full-text search is a technique used to search for text within a document or a set of documents. A document is the unit of searching in a full text search system. PostgreSQL provides a set of functions to work with full-text search, such as `to_tsvector` and `to_tsquery`:

The `to_tsvector` function parses a textual document into tokens, reduces the tokens to lexemes, and returns a `tsvector` which lists the lexemes together with their positions in the document:

<Section>
```ts copy {6}
import { sql } from 'drizzle-orm';

const db = drizzle(...);

await db.execute(
  sql`select to_tsvector('english', 'Guide to PostgreSQL full-text search with Drizzle ORM')`,
);
```

```json
[
  {
    to_tsvector: "'drizzl':9 'full':5 'full-text':4
    'guid':1 'orm':10 'postgresql':3 'search':7 'text':6"
  }
]
```
</Section>

The `to_tsquery` function converts a keyword to normalized tokens and returns a `tsquery` that matches the lexemes in a `tsvector`. The `@@` operator is used for direct matches:

<Section>
```ts copy {2, 3}
await db.execute(
  sql`select to_tsvector('english', 'Guide to PostgreSQL full-text search with Drizzle ORM')
    @@ to_tsquery('english', 'Drizzle') as match`,
);
```

```json
[ { match: true } ]
```
</Section>

As for now, Drizzle doesn't support `tsvector` type natively, so you need to convert your data in the `text` column on the fly. To enhance the performance, you can create a `GIN` index on your column like this:

<CodeTabs items={["schema.ts", "migration.sql", "db_data"]}>
  <CodeTab>
  ```ts copy {10, 11}
  import { index, pgTable, serial, text } from 'drizzle-orm/pg-core';

  export const posts = pgTable(
    'posts',
    {
      id: serial('id').primaryKey(),
      title: text('title').notNull(),
    },
    (table) => [
      index('title_search_index').using('gin', sql`to_tsvector('english', ${table.title})`),
    ]
  );
  ```
  </CodeTab>
  <CodeTab>
  ```sql
  CREATE TABLE IF NOT EXISTS "posts" (
          "id" serial PRIMARY KEY NOT NULL,
          "title" text NOT NULL
  );

  CREATE INDEX IF NOT EXISTS "title_search_index" ON "posts"
    USING gin (to_tsvector('english', "title"));
  ```
  </CodeTab>
  ```json
  [
    { id: 1, title: 'Planning Your First Trip to Europe' },
    { id: 2, title: "Cultural Insights: Exploring Asia's Heritage" },
    { id: 3, title: 'Top 5 Destinations for a Family Trip' },
    { id: 4, title: 'Essential Hiking Gear for Mountain Enthusiasts' },
    { id: 5, title: 'Trip Planning: Choosing Your Next Destination' },
    { id: 6, title: 'Discovering Hidden Culinary Gems in Italy' },
    { id: 7, title: 'The Ultimate Road Trip Guide for Explorers' },
  ];
  ```
</CodeTabs>

To implement full-text search in PostgreSQL with Drizzle ORM, you can use the `to_tsvector` and `to_tsquery` functions with `sql` operator:

<Section>
```ts copy {9}
import { sql } from 'drizzle-orm';
import { posts } from './schema';

const title = 'trip';

await db
  .select()
  .from(posts)
  .where(sql`to_tsvector('english', ${posts.title}) @@ to_tsquery('english', ${title})`);
```

```json
[
  { id: 1, title: 'Planning Your First Trip to Europe' },
  { id: 3, title: 'Top 5 Destinations for a Family Trip' },
  { id: 5, title: 'Trip Planning: Choosing Your Next Destination' },
  { id: 7, title: 'The Ultimate Road Trip Guide for Explorers' }
]
```
</Section>

To match by any of the keywords, you can use the `|` operator:

<Section>
```ts copy {6}
const title = 'Europe | Asia';

await db
  .select()
  .from(posts)
  .where(sql`to_tsvector('english', ${posts.title}) @@ to_tsquery('english', ${title})`);
```

```json
[
  { id: 1, title: 'Planning Your First Trip to Europe' },
  { id: 2, title: "Cultural Insights: Exploring Asia's Heritage" }
]
```
</Section>

To match multiple keywords, you can use the `plainto_tsquery` function:

<Section>
```ts copy {7}
// 'discover & Italy'
const title = 'discover Italy';

await db
  .select()
  .from(posts)
  .where(sql`to_tsvector('english', ${posts.title}) @@ plainto_tsquery('english', ${title})`);
```

```sql
select * from posts
  where to_tsvector('english', title) @@ plainto_tsquery('english', 'discover Italy');
```

```json
[ { id: 6, title: 'Discovering Hidden Culinary Gems in Italy' } ]
```
</Section>

To match a phrase, you can use the `phraseto_tsquery` function:

<Section>
```ts copy {8}
// if you query by "trip family", it will not return any result
// 'family <-> trip'
const title = 'family trip';

await db
  .select()
  .from(posts)
  .where(sql`to_tsvector('english', ${posts.title}) @@ phraseto_tsquery('english', ${title})`);
```

```sql
select * from posts
  where to_tsvector('english', title) @@ phraseto_tsquery('english', 'family trip');
```

```json
[ { id: 3, title: 'Top 5 Destinations for a Family Trip' } ]
```
</Section>

You can also use `websearch_to_tsquery` function which is a simplified version of `to_tsquery` with an alternative syntax, similar to the one used by web search engines:

<Section>
```ts copy {7}
// 'family | first & trip & europ | asia'
const title = 'family or first trip Europe or Asia';

await db
  .select()
  .from(posts)
  .where(sql`to_tsvector('english', ${posts.title}) @@ websearch_to_tsquery('english', ${title})`);
```

```sql
select * from posts
  where to_tsvector('english', title)
  @@ websearch_to_tsquery('english', 'family or first trip Europe or Asia');
```

```json
[
  { id: 1, title: 'Planning Your First Trip to Europe' },
  { id: 2, title: "Cultural Insights: Exploring Asia's Heritage" },
  { id: 3, title: 'Top 5 Destinations for a Family Trip' }
]
```
</Section>

To implement full-text search on multiple columns, you can create index on multiple columns and concatenate the columns with `to_tsvector` function:

<CodeTabs items={["schema.ts", "migration.sql", "db_data"]}>
  <CodeTab>
  ```ts copy {12-17}
  import { sql } from 'drizzle-orm';
  import { index, pgTable, serial, text } from 'drizzle-orm/pg-core';

  export const posts = pgTable(
    'posts',
    {
      id: serial('id').primaryKey(),
      title: text('title').notNull(),
      description: text('description').notNull(),
    },
    (table) => [
      index('search_index').using(
        'gin',
        sql`(
            setweight(to_tsvector('english', ${table.title}), 'A') ||
            setweight(to_tsvector('english', ${table.description}), 'B')
        )`,
      ),
    ],
  );
  ```
  </CodeTab>
  <CodeTab>
  ```sql
  CREATE TABLE IF NOT EXISTS "posts" (
        "id" serial PRIMARY KEY NOT NULL,
        "title" text NOT NULL,
        "description" text NOT NULL
  );

  CREATE INDEX IF NOT EXISTS "search_index" ON "posts"
    USING gin ((setweight(to_tsvector('english', "title"), 'A') ||
    setweight(to_tsvector('english', "description"), 'B')));
  ```
  </CodeTab>
  ```json
  [
    {
      id: 1,
      title: 'Planning Your First Trip to Europe',
      description:
        'Get essential tips on budgeting, sightseeing, and cultural etiquette for your inaugural European adventure.',
    },
    {
      id: 2,
      title: "Cultural Insights: Exploring Asia's Heritage",
      description:
        'Dive deep into the rich history and traditions of Asia through immersive experiences and local interactions.',
    },
    {
      id: 3,
      title: 'Top 5 Destinations for a Family Trip',
      description:
        'Discover family-friendly destinations that offer fun, education, and relaxation for all ages.',
    },
    {
      id: 4,
      title: 'Essential Hiking Gear for Mountain Enthusiasts',
      description:
        'Equip yourself with the latest and most reliable gear for your next mountain hiking expedition.',
    },
    {
      id: 5,
      title: 'Trip Planning: Choosing Your Next Destination',
      description:
        'Learn how to select destinations that align with your travel goals, whether for leisure, adventure, or cultural exploration.',
    },
    {
      id: 6,
      title: 'Discovering Hidden Culinary Gems in Italy',
      description:
        "Unearth Italy's lesser-known eateries and food markets that offer authentic and traditional flavors.",
    },
    {
      id: 7,
      title: 'The Ultimate Road Trip Guide for Explorers',
      description:
        'Plan your next great road trip with tips on route planning, packing, and discovering off-the-beaten-path attractions.',
    },
  ];
  ```
</CodeTabs>

The `setweight` function is used to label the entries of a tsvector with a given weight, where a weight is one of the letters A, B, C, or D. This is typically used to mark entries coming from different parts of a document, such as title versus body.

This is how you can query on multiple columns:

<Section>
```ts copy {5-7}
const title = 'plan';

await db.select().from(posts)
  .where(sql`(
      setweight(to_tsvector('english', ${posts.title}), 'A') ||
      setweight(to_tsvector('english', ${posts.description}), 'B'))
      @@ to_tsquery('english', ${title}
    )`
  );
```

```json
[
  {
    id: 1,
    title: 'Planning Your First Trip to Europe',
    description: 'Get essential tips on budgeting, sightseeing, and cultural etiquette for your inaugural European adventure.'
  },
  {
    id: 5,
    title: 'Trip Planning: Choosing Your Next Destination',
    description: 'Learn how to select destinations that align with your travel goals, whether for leisure, adventure, or cultural exploration.'
  },
  {
    id: 7,
    title: 'The Ultimate Road Trip Guide for Explorers',
    description: 'Plan your next great road trip with tips on route planning, packing, and discovering off-the-beaten-path attractions.'
  }
]
```
</Section>

To rank the search results, you can use the `ts_rank` or `ts_rank_cd` functions and `orderBy` method:

<Callout type='warning'>
`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](/docs/upgrade-v1))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`
</Callout>

<Section>
```ts copy {6,7,12,13,18-20}
import { desc, getColumns, sql } from 'drizzle-orm';

const search = 'culture | Europe | Italy | adventure';

const matchQuery = sql`(
  setweight(to_tsvector('english', ${posts.title}), 'A') ||
  setweight(to_tsvector('english', ${posts.description}), 'B')), to_tsquery('english', ${search})`;

await db
  .select({
    ...getColumns(posts),
    rank: sql`ts_rank(${matchQuery})`,
    rankCd: sql`ts_rank_cd(${matchQuery})`,
  })
  .from(posts)
  .where(
    sql`(
      setweight(to_tsvector('english', ${posts.title}), 'A') ||
      setweight(to_tsvector('english', ${posts.description}), 'B')
      ) @@ to_tsquery('english', ${search})`,
  )
  .orderBy((t) => desc(t.rank));
```

```json
[
  {
    id: 1,
    title: 'Planning Your First Trip to Europe',
    description: 'Get essential tips on budgeting, sightseeing, and cultural etiquette for your inaugural European adventure.',
    rank: 0.2735672,
    rankCd: 1.8
  },
  {
    id: 6,
    title: 'Discovering Hidden Culinary Gems in Italy',
    description: "Unearth Italy's lesser-known eateries and food markets that offer authentic and traditional flavors.",
    rank: 0.16717994,
    rankCd: 1.4
  },
  {
    id: 2,
    title: "Cultural Insights: Exploring Asia's Heritage",
    description: 'Dive deep into the rich history and traditions of Asia through immersive experiences and local interactions.',
    rank: 0.15198177,
    rankCd: 1
  },
  {
    id: 5,
    title: 'Trip Planning: Choosing Your Next Destination',
    description: 'Learn how to select destinations that align with your travel goals, whether for leisure, adventure, or cultural exploration.',
    rank: 0.12158542,
    rankCd: 0.8
  }
]
```
</Section>

The `ts_rank` function focuses on the frequency of query terms throughout the document. The `ts_rank_cd` function focuses on the proximity of query terms within the document.


Source: https://orm.drizzle.team/docs/postgresql-local-setup


import Section from "@mdx/Section.astro";
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTabs from '@mdx/CodeTabs.astro';
import CodeTab from '@mdx/CodeTab.astro';
import Steps from '@mdx/Steps.astro';

<Prerequisites>
- Install latest [Docker Desktop](https://www.docker.com/products/docker-desktop/). Follow the instructions for your operating system.
</Prerequisites>

<Steps>


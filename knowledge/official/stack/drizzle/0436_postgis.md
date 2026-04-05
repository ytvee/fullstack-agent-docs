### `postgis`

<Callout>
There is no specific code to create an extension inside the Drizzle schema. We assume that if you are using postgis types, indexes, and queries, you have a PostgreSQL database with the `postgis` extension installed.
</Callout>

As [PostGIS](https://postgis.net/) website mentions:

> PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.

<Callout type="info">
If you are using the `introspect` or `push` commands with the PostGIS extension and don't want PostGIS tables to be included, you can use [`extensionsFilters`](/docs/drizzle-config-file#extensionsfilters) to ignore all the PostGIS tables
</Callout>


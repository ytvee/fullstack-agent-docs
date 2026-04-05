### Materialized views
<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'MySQL': false, 'SQLite': false, 'MSSQL': false, 'Cockroach': true }} />

According to the official docs, PostgreSQL and CockroachDB have both **[`regular`](https://www.postgresql.org/docs/current/sql-createview.html)**
and **[`materialized`](https://www.postgresql.org/docs/current/sql-creatematerializedview.html)** views.
  
Materialized views in PostgreSQL and CockroachDB use the rule system like views do, but persist the results in a table-like form.
{/* This means that when a query is executed against a materialized view, the results are returned directly from the materialized view,
like from a table, rather than being reconstructed by executing the query against the underlying base tables that make up the view. */}


<Tabs items={['PostgreSQL', 'CockroachDB']}>
<Tab>
<Section>
```ts filename="schema.ts" copy
const newYorkers = pgMaterializedView('new_yorkers').as((qb) => qb.select().from(users).where(eq(users.cityId, 1)));
```
```sql
CREATE MATERIALIZED VIEW "new_yorkers" AS SELECT * FROM "users";
```
</Section>

You can then refresh materialized views in the application runtime:
```ts copy
await db.refreshMaterializedView(newYorkers);

await db.refreshMaterializedView(newYorkers).concurrently();

await db.refreshMaterializedView(newYorkers).withNoData();
```
</Tab>
<Tab>
<Section>
```ts filename="schema.ts" copy
const newYorkers = cockroachMaterializedView('new_yorkers').as((qb) => qb.select().from(users).where(eq(users.cityId, 1)));
```
```sql
CREATE MATERIALIZED VIEW "new_yorkers" AS SELECT * FROM "users";
```
</Section>

You can then refresh materialized views in the application runtime:
```ts copy
await db.refreshMaterializedView(newYorkers);

await db.refreshMaterializedView(newYorkers).concurrently();

await db.refreshMaterializedView(newYorkers).withNoData();
```
</Tab>
</Tabs>


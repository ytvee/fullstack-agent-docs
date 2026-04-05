### Extended example
<Callout type="info" emoji="ℹ️">
All the parameters inside the query will be inlined, instead of replaced by `$1`, `$2`, etc.
</Callout>

<Tabs items={['PostgreSQL', 'CockroachDB']}>
<Tab>
```ts copy
// regular view
const newYorkers = pgView('new_yorkers')
  .with({
    checkOption: 'cascaded',
    securityBarrier: true,
    securityInvoker: true,
  })
  .as((qb) => {
    const sq = qb
      .$with('sq')
      .as(
        qb.select({ userId: users.id, cityId: cities.id })
          .from(users)
          .leftJoin(cities, eq(cities.id, users.homeCity))
          .where(sql`${users.age1} > 18`),
      );
    return qb.with(sq).select().from(sq).where(sql`${users.homeCity} = 1`);
  });

// materialized view
const newYorkers2 = pgMaterializedView('new_yorkers')
  .using('btree')
  .with({
    fillfactor: 90,
    toast_tuple_target: 0.5,
    autovacuum_enabled: true,
    ...
  })
  .tablespace('custom_tablespace')
  .withNoData()
  .as((qb) => {
    const sq = qb
      .$with('sq')
      .as(
        qb.select({ userId: users.id, cityId: cities.id })
          .from(users)
          .leftJoin(cities, eq(cities.id, users.homeCity))
          .where(sql`${users.age1} > 18`),
      );
    return qb.with(sq).select().from(sq).where(sql`${users.homeCity} = 1`);
  });
```
</Tab>
<Tab>
```ts copy
// regular view
const newYorkers = cockroachView('new_yorkers')
  .as((qb) => {
    const sq = qb
      .$with('sq')
      .as(
        qb.select({ userId: users.id, cityId: cities.id })
          .from(users)
          .leftJoin(cities, eq(cities.id, users.homeCity))
          .where(sql`${users.age1} > 18`),
      );
    return qb.with(sq).select().from(sq).where(sql`${users.homeCity} = 1`);
  });

// materialized view
const newYorkers2 = cockroachMaterializedView('new_yorkers')
  .withNoData()
  .as((qb) => {
    const sq = qb
      .$with('sq')
      .as(
        qb.select({ userId: users.id, cityId: cities.id })
          .from(users)
          .leftJoin(cities, eq(cities.id, users.homeCity))
          .where(sql`${users.age1} > 18`),
      );
    return qb.with(sq).select().from(sq).where(sql`${users.homeCity} = 1`);
  });
```
</Tab>
</Tabs>


Source: https://orm.drizzle.team/docs/why-drizzle

import Callout from '@mdx/Callout.astro';
import CodeTabs from '@mdx/CodeTabs.astro';
import YoutubeCards from '@mdx/YoutubeCards.astro';


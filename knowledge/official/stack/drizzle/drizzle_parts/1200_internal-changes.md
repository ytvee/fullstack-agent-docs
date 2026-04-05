### Internal changes

1. Every `drizzle` database, `session`, `migrator` and `transaction` instance, gained 2 additional generic arguments for RQB v2 queries

<Callout collapsed='Examples'>
**migrator**
<Callout type='error' title='before'>
```ts
export async function migrate<
  TSchema extends Record<string, unknown>
>(
  db: NodePgDatabase<TSchema>,
  config: MigrationConfig,
) {
  ...
}
```
</Callout>
<Callout title='now'>
```ts {3,5}
export async function migrate<
 TSchema extends Record<string, unknown>,
 TRelations extends AnyRelations
>(
  db: NodePgDatabase<TSchema, TRelations>,
  config: MigrationConfig,
) {
  ...
}
```
</Callout>
**session**
<Callout type='error' title='before'>
```ts
export class NodePgSession<
  TFullSchema extends Record<string, unknown>,
  TSchema extends V1.TablesRelationalConfig,
> extends PgSession<NodePgQueryResultHKT, TFullSchema, TSchema>
```
</Callout>
<Callout title='now'>
```ts {3,4,6}
export class NodePgSession<
  TFullSchema extends Record<string, unknown>,
  TRelations extends AnyRelations,
  TTablesConfig extends TablesRelationalConfig,
  TSchema extends V1.TablesRelationalConfig,
> extends PgSession<NodePgQueryResultHKT, TFullSchema, TRelations, TTablesConfig, TSchema>
```
</Callout>
**transaction**
<Callout type='error' title='before'>
```ts
export class NodePgTransaction<
  TFullSchema extends Record<string, unknown>,
  TSchema extends V1.TablesRelationalConfig,
> extends PgTransaction<NodePgQueryResultHKT, TFullSchema, TSchema>
```
</Callout>
<Callout title='now'>
```ts {3,4,6}
export class NodePgTransaction<
  TFullSchema extends Record<string, unknown>,
  TRelations extends AnyRelations,
  TTablesConfig extends TablesRelationalConfig,
  TSchema extends V1.TablesRelationalConfig,
> extends PgTransaction<NodePgQueryResultHKT, TFullSchema, TRelations, TTablesConfig, TSchema>
```
</Callout>
**driver**
<Callout type='error' title='before'>
```ts
export class NodePgDatabase<
  TSchema extends Record<string, unknown> = Record<string, never>,
> extends PgDatabase<NodePgQueryResultHKT, TSchema>
```
</Callout>
<Callout title='now'>
```ts {3,4}
export class NodePgDatabase<
  TSchema extends Record<string, unknown> = Record<string, never>,
  TRelations extends AnyRelations = EmptyRelations,
> extends PgDatabase<NodePgQueryResultHKT, TSchema, TRelations>
```
</Callout>
</Callout>

2. Updated `DrizzleConfig` generic with `TRelations` argument and `relations: TRelations` field

<Callout collapsed='Examples'>
<Callout type='error' title='before'>
```ts
export interface DrizzleConfig<
  TSchema extends Record<string, unknown> = Record<string, never>
> {
  logger?: boolean | Logger;
  schema?: TSchema;
  casing?: Casing;
}
```
</Callout>

<Callout title='now'>
```ts {8}
export interface DrizzleConfig<
  TSchema extends Record<string, unknown> = Record<string, never>,
  TRelations extends AnyRelations = EmptyRelations,
> {
  logger?: boolean | Logger;
  schema?: TSchema;
  casing?: Casing;
  relations?: TRelations;
}
```
</Callout>
</Callout>

3. The following entities have been moved from `drizzle-orm` and `drizzle-orm/relations` to `drizzle-orm/_relations`. The original imports now 
include new types used by Relational Queries v2, so make sure to update your imports if you intend to use the older types:

<Callout collapsed='A list of all moved entities'>
- `Relation`
- `Relations`
- `One`
- `Many`
- `TableRelationsKeysOnly`
- `ExtractTableRelationsFromSchema`
- `ExtractObjectValues`
- `ExtractRelationsFromTableExtraConfigSchema`
- `getOperators`
- `Operators`
- `getOrderByOperators`
- `OrderByOperators`
- `FindTableByDBName`
- `DBQueryConfig`
- `TableRelationalConfig`
- `TablesRelationalConfig`
- `RelationalSchemaConfig`
- `ExtractTablesWithRelations`
- `ReturnTypeOrValue`
- `BuildRelationResult`
- `NonUndefinedKeysOnly`
- `BuildQueryResult`
- `RelationConfig`
- `extractTablesRelationalConfig`
- `relations`
- `createOne`
- `createMany`
- `NormalizedRelation`
- `normalizeRelation`
- `createTableRelationsHelpers`
- `TableRelationsHelpers`
- `BuildRelationalQueryResult`
- `mapRelationalRow`
</Callout>

4. In the same manner, `${dialect}-core/query-builders/query` files were moved to `${dialect}-core/query-builders/_query` 
with RQB v2's alternatives being put in their place

<Callout collapsed='Examples'>
<Callout type='error' title='before'>
```ts
import { RelationalQueryBuilder, PgRelationalQuery } from './query-builders/query.ts';
```
</Callout>

<Callout title='now'>
```ts
import { _RelationalQueryBuilder, _PgRelationalQuery } from './query-builders/_query.ts';
```
</Callout>
</Callout>


Source: https://orm.drizzle.team/docs/relations-v2

import Tab from '@mdx/Tab.astro';
import Tabs from '@mdx/Tabs.astro';
import IsSupportedChipGroup from '@mdx/IsSupportedChipGroup.astro';
import Callout from '@mdx/Callout.astro';
import Section from '@mdx/Section.astro';
import Prerequisites from "@mdx/Prerequisites.astro";
import CodeTab from '@mdx/CodeTab.astro';
import CodeTabs from '@mdx/CodeTabs.astro';
import Npm from '@mdx/Npm.astro';


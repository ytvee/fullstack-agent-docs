### Advanced select
Powered by TypeScript, Drizzle APIs let you build your select queries in a variety of flexible ways.

Sneak peek of advanced partial select, for more detailed advanced usage examples - see our [dedicated guide](/docs/guides/include-or-exclude-columns).

<Callout type='warning'>
`getColumns` available starting from `drizzle-orm@1.0.0-beta.2`(read more [here](/docs/upgrade-v1))

If you are on pre-1 version(like `0.45.1`) then use `getTableColumns`
</Callout>


<br/>

<CodeTabs items={["example 1", "example 2", "example 3", "example 4"]}>
```ts
import { getColumns, sql } from 'drizzle-orm';

await db.select({
    ...getColumns(posts),
    titleLength: sql<number>`length(${posts.title})`,
  }).from(posts);
```
```ts
import { getColumns } from 'drizzle-orm';

const { content, ...rest } = getColumns(posts); // exclude "content" column
await db.select({ ...rest }).from(posts); // select all other columns
```
```ts
await db.query.posts.findMany({
  columns: {
    title: true,
  },
});
```
```ts
await db.query.posts.findMany({
  columns: {
    content: false,
  },
});
```
</CodeTabs>


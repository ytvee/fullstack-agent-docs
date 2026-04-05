#### Helper Functions

For queries, you can use predefined functions for vectors or create custom ones using the SQL template operator.

You can also use the following helpers:

```ts
import { l2Distance, l1Distance, innerProduct, 
          cosineDistance, hammingDistance, jaccardDistance } from 'drizzle-orm'

l2Distance(table.column, [3, 1, 2]) // table.column <-> '[3, 1, 2]'
l1Distance(table.column, [3, 1, 2]) // table.column <+> '[3, 1, 2]'

innerProduct(table.column, [3, 1, 2]) // table.column <#> '[3, 1, 2]'
cosineDistance(table.column, [3, 1, 2]) // table.column <=> '[3, 1, 2]'

hammingDistance(table.column, '101') // table.column <~> '101'
jaccardDistance(table.column, '101') // table.column <%> '101'
```

If `pg_vector` has some other functions to use, you can replicate implementation from existing one we have. Here is how it can be done

```ts
export function l2Distance(
  column: SQLWrapper | AnyColumn,
  value: number[] | string[] | TypedQueryBuilder<any> | string,
): SQL {
  if (is(value, TypedQueryBuilder<any>) || typeof value === 'string') {
    return sql`${column} <-> ${value}`;
  }
  return sql`${column} <-> ${JSON.stringify(value)}`;
}
```

Name it as you wish and change the operator. This example allows for a numbers array, strings array, string, or even a select query. Feel free to create any other type you want or even contribute and submit a PR


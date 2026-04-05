## Compare objects types (instanceof alternative)

You can check if an object is of a specific Drizzle type using the `is()` function. 
You can use it with any available type in Drizzle.

<Callout type="warning" emoji="⭐️">
  You should always use `is()` instead of `instanceof`
</Callout>

**Few examples**
```ts
import { Column, is } from 'drizzle-orm';

if (is(value, Column)) {
  // value's type is narrowed to Column
}
```


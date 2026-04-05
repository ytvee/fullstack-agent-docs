### `datetime`

<rem025 />
Generates datetime objects

|  | param      | default    | type
|:-| :--------  | :--------  | :--------
|  |`arraySize` |--          |`number`
<rem025 />
```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  orders: {
    columns: {
      shippedDate: funcs.datetime({
        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


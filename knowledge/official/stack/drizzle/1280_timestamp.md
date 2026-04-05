### `timestamp`

<rem025 />
Generates timestamps

|  | param      | default    | type
|:-| :--------  | :--------  | :--------
|  |`arraySize` |--          |`number`

<rem025 />
```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  orders: {
    columns: {
      shippedDate: funcs.timestamp({
        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


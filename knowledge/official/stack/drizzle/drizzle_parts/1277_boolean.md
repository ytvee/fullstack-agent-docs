### `boolean`

<rem025 />
Generates boolean values (true or false)

|  | param      | default    | type
|:-| :--------  | :--------  | :--------
|  |`arraySize` |--          |`number`

<rem025 />
```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  users: {
    columns: {
      isAvailable: funcs.boolean({
        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


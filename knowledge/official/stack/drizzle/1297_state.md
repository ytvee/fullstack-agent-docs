### `state`

<rem025 />
Generates US states

|  | param      | default    | type
|:-| :--------  | :--------  | :--------
|  |`arraySize` |--          |`number`

<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  users: {
    columns: {
      state: funcs.state({
        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


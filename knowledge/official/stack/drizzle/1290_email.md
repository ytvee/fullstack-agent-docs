### `email`

<rem025 />
Generates unique email addresses

|  | param      | default    | type
|:-| :--------  | :--------  | :--------
|  |`arraySize` |--          |`number`

<rem025 />
```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  users: {
    columns: {
      email: funcs.email({
        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


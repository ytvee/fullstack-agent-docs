### `intPrimaryKey`

<rem025 />
Generates sequential integers starting from 1.

|  | param      | default    | type
|:-| :--------  | :--------  | :--------
|  |--          |--          |--

<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  posts: {
    columns: {
      id: funcs.intPrimaryKey(),
    },
  },
}));

```


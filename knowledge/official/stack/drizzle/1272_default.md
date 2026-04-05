### `default`

<rem025 />
Generates the same given value each time the generator is called.

|  | param          | default     | type
|:-| :--------      | :--------   | :--------
|  |`defaultValue`  |--           |`any`
|  |`arraySize`     |--           |`number`

<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  posts: {
    columns: {
      content: funcs.default({
        // value you want to generate
        defaultValue: "post content",

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


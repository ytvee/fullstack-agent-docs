### `loremIpsum`

<rem025 />
Generates `lorem ipsum` text sentences.

|  | param            | default    | type
|:-| :--------        | :--------  | :--------
|  |`sentencesCount`  | 1          |`number`
|  |`arraySize`       |--          |`number`

<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  posts: {
    columns: {
      content: funcs.loremIpsum({
        // `sentencesCount` - number of sentences you want to generate as one generated value(string).
        sentencesCount: 2,

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


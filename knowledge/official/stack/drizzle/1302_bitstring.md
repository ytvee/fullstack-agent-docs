### `bitString`

<rem025 />
Generates bit strings based on specified parameters.

|  | param       | default                                                                                 | type
|:-| :--------   | :--------                                                                               | :--------
|  |`isUnique`   |`database column uniqueness`                                                             |`boolean`
|  |`dimensions` |`database column bit-length`                                                             |`number`
|  |`arraySize`  |--                                                                                       |`number`
<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  bitStringTable: {
    columns: {
      bit: funcs.bitString({
        // desired length of each bit string (e.g., `dimensions = 3` produces values like `'010'`).
        dimensions: 12,

        // property that controls if generated values gonna be unique or not;
        isUnique: true,

        // number of elements in each one-dimensional array (If specified, arrays will be generated);
        arraySize: 3,
      }),
    },
  },
}));

```


### `valuesFromArray`

<rem025 />
Generates values from given array

|  | param      | default                     | type
|:-| :--------  | :--------                   | :--------
|  |`values`    |--                           |`any[]` \| `{ weight: number; values: any[] }[]`
|  |`isUnique`  |`database column uniqueness` |`boolean`
|  |`arraySize` |--                           |`number`


<rem025 />
```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  posts: {
    columns: {
      title: funcs.valuesFromArray({
        // Array of values you want to generate (can be an array of weighted values)
        values: ["Title1", "Title2", "Title3", "Title4", "Title5"],

        // Property that controls whether the generated values will be unique or not
        isUnique: true,
        
        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


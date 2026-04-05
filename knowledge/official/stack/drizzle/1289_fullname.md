### `fullName`

<rem025 />
Generates a person's full name

|  | param      | default                     | type
|:-| :--------  | :--------                   | :--------
|  |`isUnique`  |`database column uniqueness` |`boolean`
|  |`arraySize` |--                           |`number`

<rem025 />
```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  users: {
    columns: {
      fullName: funcs.fullName({
        // `isUnique` - property that controls whether the generated values will be unique or not
        isUnique: true,

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


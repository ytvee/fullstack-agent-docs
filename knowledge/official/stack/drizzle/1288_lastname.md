### `lastName`

<rem025 />
Generates a person's last name

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
      lastName: funcs.lastName({
        // `isUnique` - property that controls whether the generated values will be unique or not
        isUnique: false,
        
        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


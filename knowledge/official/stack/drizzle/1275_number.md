### `number`

<rem025 />
Generates numbers with a floating point within the given range

|  | param      | default                                                                                               | type
|:-| :--------  | :--------                                                                                             | :--------
|  |`isUnique`  |`database column uniqueness`                                                                           |`boolean`
|  |`precision` |`100`                                                                                                  |`number`
|  |`maxValue`  |``` `precision * 1000` if isUnique equals false``` ``` `precision * count` if isUnique equals true```  |`number`
|  |`minValue`  |`-maxValue`                                                                                            |`number`
|  |`arraySize` |--                                                                                                     |`number`

<rem025 />
```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  products: {
    columns: {
      unitPrice: funcs.number({
        // lower border of range.
        minValue: 10,

        // upper border of range.
        maxValue: 120,
        
        // precision of generated number:
        // precision equals 10 means that values will be accurate to one tenth (1.2, 34.6);
        // precision equals 100 means that values will be accurate to one hundredth (1.23, 34.67).
        precision: 100,

        // property that controls if generated values gonna be unique or not.
        isUnique: false,

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


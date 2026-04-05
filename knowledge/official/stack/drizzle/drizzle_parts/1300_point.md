### `point`

<rem025 />
Generates 2D points within specified ranges for x and y coordinates.

|  | param       | default                                                                                 | type
|:-| :--------   | :--------                                                                               | :--------
|  |`isUnique`   |`database column uniqueness`                                                             |`boolean`
|  |`maxXValue`  |``` `10 * 1000` if isUnique equals false``` ``` `10 * count` if isUnique equals true```  |`number`
|  |`minXValue`  |`-maxXValue`                                                                             |`number`
|  |`maxYValue`  |``` `10 * 1000` if isUnique equals false``` ``` `10 * count` if isUnique equals true```  |`number`
|  |`minYValue`  |`-maxYValue`                                                                             |`number`
|  |`arraySize`  |--                                                                                       |`number`


<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  triangles: {
    columns: {
      pointCoords: funcs.point({
        // `isUnique` - property that controls if generated values gonna be unique or not.
        isUnique: true,

        // `minXValue` - lower bound of range for x coordinate.
        minXValue: -5,

        // `maxXValue` - upper bound of range for x coordinate.
        maxXValue: 20,

        // `minYValue` - lower bound of range for y coordinate.
        minYValue: 0,

        // `maxYValue` - upper bound of range for y coordinate.
        maxYValue: 30,

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```


### `phoneNumber`

<rem025 />
Generates unique phone numbers

|  | param                    | default                                         | type
|:-| :--------                | :--------                                       | :--------
|  |`template`                |--                                               |`string`
|  |`prefixes`                |[Used dataset for prefixes](https://github.com/OleksiiKH0240/drizzle-orm/blob/main/drizzle-seed/src/datasets/phonesInfo.ts)   |`string[]`
|  |`generatedDigitsNumbers`  | `7` - `if prefixes was defined`                 |`number \| number[]`
|  |`arraySize`               |--                                               |`number`

<rem025 />
```ts 
import { seed } from "drizzle-seed";

//generate phone number using template property
await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  users: {
    columns: {
      phoneNumber: funcs.phoneNumber({ 
        // `template` - phone number template, where all '#' symbols will be substituted with generated digits.
        template: "+(380) ###-####",

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```
```ts 
import { seed } from "drizzle-seed";

//generate phone number using prefixes and generatedDigitsNumbers properties
await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  users: {
    columns: {
      phoneNumber: funcs.phoneNumber({
        // `prefixes` - array of any string you want to be your phone number prefixes.(not compatible with `template` property)
        prefixes: ["+380 99", "+380 67"],

        // `generatedDigitsNumbers` - number of digits that will be added at the end of prefixes.(not compatible with `template` property)
        generatedDigitsNumbers: 7,

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```
```ts 
import { seed } from "drizzle-seed";

// generate phone number using prefixes and generatedDigitsNumbers properties but with different generatedDigitsNumbers for prefixes
await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  users: {
    columns: {
      phoneNumber: funcs.phoneNumber({
        // `prefixes` - array of any string you want to be your phone number prefixes.(not compatible with `template` property)
        prefixes: ["+380 99", "+380 67", "+1"],

        // `generatedDigitsNumbers` - number of digits that will be added at the end of prefixes.(not compatible with `template` property)
        generatedDigitsNumbers: [7, 7, 10],

        // number of elements in each one-dimensional array. 
        // (If specified, arrays will be generated.)
        arraySize: 3
      }),
    },
  },
}));

```

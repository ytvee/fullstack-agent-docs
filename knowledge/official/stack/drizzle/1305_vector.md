### `vector`

<rem025 />
Generates vectors based on the provided parameters.

|  | param          | default                                                      | type
|:-| :--------      | :--------                                                    | :--------
|  |`isUnique`      |`database column uniqueness`                                  |`boolean`
|  |`arraySize`     |--                                                            |`number`
|  |`decimalPlaces` |`2`                                                           |`number`
|  |`dimensions`    |`database column’s dimensions`                                |`number`
|  |`minValue`      |`-1000`                                                       |`number`
|  |`maxValue`      |`1000`                                                        |`number`
<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  vectorTable: {
    columns: {
      vector: funcs.vector({
        // property that controls if generated values gonna be unique or not;
        isUnique: true,

        // number of elements in each one-dimensional array (If specified, arrays will be generated);
        arraySize: 3,

        // number of decimal places for each vector element (e.g., `decimalPlaces = 3` produces values like `1.123`);
        decimalPlaces: 5,

        // number of elements in each generated vector (e.g., `dimensions = 3` produces values like `[1,2,3]`);
        dimensions: 12,

        // minimum allowed value for each vector element;
        minValue: -100,

        // maximum allowed value for each vector element.
        maxValue: 100,
      }),
    },
  },
}));

```

Source: https://orm.drizzle.team/docs/seed-limitations

// type limitations for third param

Source: https://orm.drizzle.team/docs/seed-overview

import Npm from "@mdx/Npm.astro";
import Tab from "@mdx/Tab.astro";
import Tabs from "@mdx/Tabs.astro";
import Callout from '@mdx/Callout.astro';
import CodeTabs from "@mdx/CodeTabs.astro";
import Section from "@mdx/Section.astro";
import IsSupportedChipGroup from '@mdx/IsSupportedChipGroup.astro';


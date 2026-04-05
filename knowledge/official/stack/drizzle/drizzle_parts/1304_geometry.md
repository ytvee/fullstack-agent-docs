### `geometry`

<rem025 />
Generates geometry objects based on the given parameters.

<Callout title='warnings'>
<Tabs items={['arraySize', 'srid']}>
<Tab>
Currently, if you set arraySize to a value greater than 1 
or try to insert more than one `geometry point` element into a `geometry(point, 0)[]` column in PostgreSQL or CockroachDB via drizzle-orm, 
you’ll encounter an error.

This bug is already in the backlog.

<Callout title="❌">
```ts {13}
import { seed } from "drizzle-seed";
import { geometry, pgTable } from 'drizzle-orm/pg-core';

const geometryTable = pgTable('geometry_table', {
	geometryArray: geometry('geometry_array', { type: 'point', srid: 0 }).array(3),
});

await seed(db, { geometryTable }, { count: 1000 }).refine((funcs) => ({
  geometryTable: {
    columns: {
      geometryArray: funcs.geometry({
        // currently arraySize with values > 1 are not supported
        arraySize: 3,
      }),
    },
  },
}));
```
</Callout>

<Callout title='✅'>
```ts {13}
import { seed } from "drizzle-seed";
import { geometry, pgTable } from 'drizzle-orm/pg-core';

const geometryTable = pgTable('geometry_table', {
	geometryArray: geometry('geometry_array', { type: 'point', srid: 0 }).array(1),
});

await seed(db, { geometryTable }, { count: 1000 }).refine((funcs) => ({
  geometryTable: {
    columns: {
      geometryArray: funcs.geometry({
        // will work as expected
        arraySize: 1,
      }),
    },
  },
}));
```
</Callout>
</Tab>

<Tab>
Currently, if you set the SRID of a `geometry(point)` column to anything other than 0 (for example, 4326) in your drizzle-orm table declaration, 
you’ll encounter an error during the seeding process.

This bug is already in the backlog.

<Callout title="❌">
```ts {5}
import { seed } from "drizzle-seed";
import { geometry, pgTable } from 'drizzle-orm/pg-core';

const geometryTable = pgTable('geometry_table', {
	geometryColumn: geometry('geometry_column', { type: 'point', srid: 4326 }),
});

await seed(db, { geometryTable }, { count: 1000 }).refine((funcs) => ({
  geometryTable: {
    columns: {
      geometryColumn: funcs.geometry({
        srid: 4326,
      }),
    },
  },
}));
```
</Callout>

<Callout title='✅'>
```ts {5}
import { seed } from "drizzle-seed";
import { geometry, pgTable } from 'drizzle-orm/pg-core';

const geometryTable = pgTable('geometry_table', {
	geometryColumn: geometry('geometry_column', { type: 'point', srid: 0 }),
});

await seed(db, { geometryTable }, { count: 1000 }).refine((funcs) => ({
  geometryTable: {
    columns: {
      geometryColumn: funcs.geometry({
        srid: 4326,
      }),
    },
  },
}));
```
</Callout>
</Tab>
</Tabs>
</Callout>

|  | param          | default                                                                                 | type
|:-| :--------      | :--------                                                                               | :--------
|  |`isUnique`      |`database column uniqueness`                                                             |`boolean`
|  |`arraySize`     |--                                                                                       |`number`
|  |`type`          |`'point'`                                                                                |`'point'`
|  |`srid`          |`4326`                                                                                   |`4326 \| 3857`
|  |`decimalPlaces` |`6`                                                                                      |`1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7`
<rem025 />

```ts 
import { seed } from "drizzle-seed";

await seed(db, schema, { count: 1000 }).refine((funcs) => ({
  geometryTable: {
    columns: {
      geometryPointTuple: funcs.geometry({
        // property that controls if generated values gonna be unique or not;
        isUnique: true,

        // number of elements in each one-dimensional array (If specified, arrays will be generated);
        arraySize: 1,

        // geometry type to generate; currently only `'point'` is supported;
        type: "point",

        // Spatial Reference System Identifier: determines what type of point will be generated - either `4326` or `3857`;
        srid: 4326,

        // number of decimal places for points when `srid` is `4326` (e.g., `decimalPlaces = 3` produces values like `'point(30.723 46.482)'`).
        decimalPlaces: 5,
      }),
    },
  },
}));

```


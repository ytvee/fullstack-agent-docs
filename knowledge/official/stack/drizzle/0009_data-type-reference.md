### Data type reference

```ts
pg.boolean();

mysql.boolean();

sqlite.integer({ mode: 'boolean' });

// Schema
type.boolean;
```

```ts
pg.date({ mode: 'date' });
pg.timestamp({ mode: 'date' });

mysql.date({ mode: 'date' });
mysql.datetime({ mode: 'date' });
mysql.timestamp({ mode: 'date' });

sqlite.integer({ mode: 'timestamp' });
sqlite.integer({ mode: 'timestamp_ms' });

// Schema
type.Date;
```

```ts
pg.date({ mode: 'string' });
pg.timestamp({ mode: 'string' });
pg.cidr();
pg.inet();
pg.interval();
pg.macaddr();
pg.macaddr8();
pg.numeric();
pg.text();
pg.sparsevec();
pg.time();

mysql.binary();
mysql.date({ mode: 'string' });
mysql.datetime({ mode: 'string' });
mysql.decimal();
mysql.time();
mysql.timestamp({ mode: 'string' });
mysql.varbinary();

sqlite.numeric();
sqlite.text({ mode: 'text' });

// Schema
type.string;
```

```ts
pg.bit({ dimensions: ... });

// Schema
type(`/^[01]{${column.dimensions}}$/`);
```

```ts
pg.uuid();

// Schema
type(/^[\da-f]{8}(?:-[\da-f]{4}){3}-[\da-f]{12}$/iu);
```

```ts
pg.char({ length: ... });

mysql.char({ length: ... });

// Schema
type.string.exactlyLength(length);
```

```ts
pg.varchar({ length: ... });

mysql.varchar({ length: ... });

sqlite.text({ mode: 'text', length: ... });

// Schema
type.string.atMostLength(length);
```

```ts
mysql.tinytext();

// Schema
type.string.atMostLength(255); // unsigned 8-bit integer limit
```

```ts
mysql.text();

// Schema
type.string.atMostLength(65_535); // unsigned 16-bit integer limit
```

```ts
mysql.mediumtext();

// Schema
type.string.atMostLength(16_777_215); // unsigned 24-bit integer limit
```

```ts
mysql.longtext();

// Schema
type.string.atMostLength(4_294_967_295); // unsigned 32-bit integer limit
```

```ts
pg.text({ enum: ... });
pg.char({ enum: ... });
pg.varchar({ enum: ... });

mysql.tinytext({ enum: ... });
mysql.mediumtext({ enum: ... });
mysql.text({ enum: ... });
mysql.longtext({ enum: ... });
mysql.char({ enum: ... });
mysql.varchar({ enum: ... });
mysql.mysqlEnum(..., ...);

sqlite.text({ mode: 'text', enum: ... });

// Schema
type.enumerated(...enum);
```

```ts
mysql.tinyint();

// Schema
type.keywords.number.integer.atLeast(-128).atMost(127); // 8-bit integer lower and upper limit
```

```ts
mysql.tinyint({ unsigned: true });

// Schema
type.keywords.number.integer.atLeast(0).atMost(255); // unsigned 8-bit integer lower and upper limit
```

```ts
pg.smallint();
pg.smallserial();

mysql.smallint();

// Schema
type.keywords.number.integer.atLeast(-32_768).atMost(32_767); // 16-bit integer lower and upper limit
```

```ts
mysql.smallint({ unsigned: true });

// Schema
type.keywords.number.integer.atLeast(0).atMost(65_535); // unsigned 16-bit integer lower and upper limit
```

```ts
pg.real();

mysql.float();

// Schema
type.number.atLeast(-8_388_608).atMost(8_388_607); // 24-bit integer lower and upper limit
```

```ts
mysql.mediumint();

// Schema
type.keywords.number.integer.atLeast(-8_388_608).atMost(8_388_607); // 24-bit integer lower and upper limit
```

```ts
mysql.float({ unsigned: true });

// Schema
type.number.atLeast(0).atMost(16_777_215); // unsigned 24-bit integer lower and upper limit
```

```ts
mysql.mediumint({ unsigned: true });

// Schema
type.keywords.number.integer.atLeast(0).atMost(16_777_215); // unsigned 24-bit integer lower and upper limit
```

```ts
pg.integer();
pg.serial();

mysql.int();

// Schema
type.keywords.number.integer.atLeast(-2_147_483_648).atMost(2_147_483_647); // 32-bit integer lower and upper limit
```

```ts
mysql.int({ unsigned: true });

// Schema
type.keywords.number.integer.atLeast(0).atMost(4_294_967_295); // unsgined 32-bit integer lower and upper limit
```

```ts
pg.doublePrecision();

mysql.double();
mysql.real();

sqlite.real();

// Schema
type.number.atLeast(-140_737_488_355_328).atMost(140_737_488_355_327); // 48-bit integer lower and upper limit
```

```ts
mysql.double({ unsigned: true });

// Schema
type.number.atLeast(0).atMost(281_474_976_710_655); // unsigned 48-bit integer lower and upper limit
```

```ts
pg.bigint({ mode: 'number' });
pg.bigserial({ mode: 'number' });

mysql.bigint({ mode: 'number' });
mysql.bigserial({ mode: 'number' });

sqlite.integer({ mode: 'number' });

// Schema
type.keywords.number.integer.atLeast(-9_007_199_254_740_991).atMost(9_007_199_254_740_991); // Javascript min. and max. safe integers
```

```ts
mysql.serial();

// Schema
type.keywords.number.integer.atLeast(0).atMost(9_007_199_254_740_991); // Javascript max. safe integer
```

```ts
pg.bigint({ mode: 'bigint' });
pg.bigserial({ mode: 'bigint' });

mysql.bigint({ mode: 'bigint' });

sqlite.blob({ mode: 'bigint' });

// Schema
type.bigint.narrow(
  (value, ctx) => value < -9_223_372_036_854_775_808n ? ctx.mustBe('greater than') : value > 9_223_372_036_854_775_807n ? ctx.mustBe('less than') : true
); // 64-bit integer lower and upper limit
```

```ts
mysql.bigint({ mode: 'bigint', unsigned: true });

// Schema
type.bigint.narrow(
  (value, ctx) => value < 0n ? ctx.mustBe('greater than') : value > 18_446_744_073_709_551_615n ? ctx.mustBe('less than') : true
); // unsigned 64-bit integer lower and upper limit
```

```ts
mysql.year();

// Schema
type.keywords.number.integer.atLeast(1_901).atMost(2_155);
```

```ts
pg.geometry({ type: 'point', mode: 'tuple' });
pg.point({ mode: 'tuple' });

// Schema
type([type.number, type.number]);
```

```ts
pg.geometry({ type: 'point', mode: 'xy' });
pg.point({ mode: 'xy' });

// Schema
type({ x: type.number, y: type.number });
```

```ts
pg.halfvec({ dimensions: ... });
pg.vector({ dimensions: ... });

// Schema
type.number.array().exactlyLength(dimensions);
```

```ts
pg.line({ mode: 'abc' });

// Schema
type({ a: type.number, b: type.number, c: type.number });
```

```ts
pg.line({ mode: 'tuple' });

// Schema
type([type.number, type.number, type.number]);
```

```ts
pg.json();
pg.jsonb();

mysql.json();

sqlite.blob({ mode: 'json' });
sqlite.text({ mode: 'json' });

// Schema
type('string | number | boolean | null').or(type('unknown.any[] | Record<string, unknown.any>'));
```

```ts
sqlite.blob({ mode: 'buffer' });

// Schema
type.instanceOf(Buffer);
```

```ts
pg.dataType().array(...);

// Schema
baseDataTypeSchema.array().exactlyLength(size);
```


Source: https://orm.drizzle.team/docs/batch-api

import Tab from '@mdx/Tab.astro';
import Tabs from '@mdx/Tabs.astro';


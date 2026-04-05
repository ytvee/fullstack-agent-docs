### Data type reference

```ts
pg.boolean();

mysql.boolean();

sqlite.integer({ mode: 'boolean' });

// Schema
boolean();
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
date();
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
string();
```

```ts
pg.bit({ dimensions: ... });

// Schema
pipe(string(), regex(/^[01]+$/), maxLength(dimensions));
```

```ts
pg.uuid();

// Schema
pipe(string(), uuid());
```

```ts
pg.char({ length: ... });

mysql.char({ length: ... });

// Schema
pipe(string(), length(length));
```

```ts
pg.varchar({ length: ... });

mysql.varchar({ length: ... });

sqlite.text({ mode: 'text', length: ... });

// Schema
pipe(string(), maxLength(length));
```

```ts
mysql.tinytext();

// Schema
pipe(string(), maxLength(255)); // unsigned 8-bit integer limit
```

```ts
mysql.text();

// Schema
pipe(string(), maxLength(65_535)); // unsigned 16-bit integer limit
```

```ts
mysql.mediumtext();

// Schema
pipe(string(), maxLength(16_777_215)); // unsigned 24-bit integer limit
```

```ts
mysql.longtext();

// Schema
pipe(string(), maxLength(4_294_967_295)); // unsigned 32-bit integer limit
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
enum(enum);
```

```ts
mysql.tinyint();

// Schema
pipe(number(), minValue(-128), maxValue(127), integer()); // 8-bit integer lower and upper limit
```

```ts
mysql.tinyint({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(255), integer()); // unsigned 8-bit integer lower and upper limit
```

```ts
pg.smallint();
pg.smallserial();

mysql.smallint();

// Schema
pipe(number(), minValue(-32_768), maxValue(32_767), integer()); // 16-bit integer lower and upper limit
```

```ts
mysql.smallint({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(65_535), integer()); // unsigned 16-bit integer lower and upper limit
```

```ts
pg.real();

mysql.float();

// Schema
pipe(number(), minValue(-8_388_608), maxValue(8_388_607)); // 24-bit integer lower and upper limit
```

```ts
mysql.mediumint();

// Schema
pipe(number(), minValue(-8_388_608), maxValue(8_388_607), integer()); // 24-bit integer lower and upper limit
```

```ts
mysql.float({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(16_777_215)); // unsigned 24-bit integer lower and upper limit
```

```ts
mysql.mediumint({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(16_777_215), integer()); // unsigned 24-bit integer lower and upper limit
```

```ts
pg.integer();
pg.serial();

mysql.int();

// Schema
pipe(number(), minValue(-2_147_483_648), maxValue(2_147_483_647), integer()); // 32-bit integer lower and upper limit
```

```ts
mysql.int({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(4_294_967_295), integer()); // unsgined 32-bit integer lower and upper limit
```

```ts
pg.doublePrecision();

mysql.double();
mysql.real();

sqlite.real();

// Schema
pipe(number(), minValue(-140_737_488_355_328), maxValue(140_737_488_355_327)); // 48-bit integer lower and upper limit
```

```ts
mysql.double({ unsigned: true });

// Schema
pipe(number(), minValue(0), maxValue(281_474_976_710_655)); // unsigned 48-bit integer lower and upper limit
```

```ts
pg.bigint({ mode: 'number' });
pg.bigserial({ mode: 'number' });

mysql.bigint({ mode: 'number' });
mysql.bigserial({ mode: 'number' });

sqlite.integer({ mode: 'number' });

// Schema
pipe(number(), minValue(-9_007_199_254_740_991), maxValue(9_007_199_254_740_991), integer()); // Javascript min. and max. safe integers
```

```ts
mysql.serial();

// Schema
pipe(number(), minValue(0), maxValue(9_007_199_254_740_991), integer()); // Javascript max. safe integer
```

```ts
pg.bigint({ mode: 'bigint' });
pg.bigserial({ mode: 'bigint' });

mysql.bigint({ mode: 'bigint' });

sqlite.blob({ mode: 'bigint' });

// Schema
pipe(bigint(), minValue(-9_223_372_036_854_775_808n), maxValue(9_223_372_036_854_775_807n)); // 64-bit integer lower and upper limit
```

```ts
mysql.bigint({ mode: 'bigint', unsigned: true });

// Schema
pipe(bigint(), minValue(0n), maxValue(18_446_744_073_709_551_615n)); // unsigned 64-bit integer lower and upper limit
```

```ts
mysql.year();

// Schema
pipe(number(), minValue(1_901), maxValue(2_155), integer());
```

```ts
pg.geometry({ type: 'point', mode: 'tuple' });
pg.point({ mode: 'tuple' });

// Schema
tuple([number(), number()]);
```

```ts
pg.geometry({ type: 'point', mode: 'xy' });
pg.point({ mode: 'xy' });

// Schema
object({ x: number(), y: number() });
```

```ts
pg.halfvec({ dimensions: ... });
pg.vector({ dimensions: ... });

// Schema
pipe(array(number()), length(dimensions));
```

```ts
pg.line({ mode: 'abc' });

// Schema
object({ a: number(), b: number(), c: number() });
```

```ts
pg.line({ mode: 'tuple' });

// Schema
tuple([number(), number(), number()]);
```

```ts
pg.json();
pg.jsonb();

mysql.json();

sqlite.blob({ mode: 'json' });
sqlite.text({ mode: 'json' });

// Schema
union([union([string(), number(), boolean(), null_()]), array(any()), record(string(), any())]);
```

```ts
sqlite.blob({ mode: 'buffer' });

// Schema
custom<Buffer>((v) => v instanceof Buffer);
```

```ts
pg.dataType().array(...);

// Schema
pipe(array(baseDataTypeSchema), length(size));
```


Source: https://orm.drizzle.team/docs/views

import Tab from '@mdx/Tab.astro';
import Tabs from '@mdx/Tabs.astro';
import IsSupportedChipGroup from '@mdx/IsSupportedChipGroup.astro';
import Callout from '@mdx/Callout.astro';
import Section from '@mdx/Section.astro';


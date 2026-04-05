### Data type reference

```ts
pg.boolean();

mysql.boolean();

sqlite.integer({ mode: 'boolean' });

// Schema
Type.Boolean();
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
Type.Date();
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
Type.String();
```

```ts
pg.bit({ dimensions: ... });

// Schema
t.RegExp(/^[01]+$/, { maxLength: dimensions });
```

```ts
pg.uuid();

// Schema
Type.String({ format: 'uuid' });
```

```ts
pg.char({ length: ... });

mysql.char({ length: ... });

// Schema
Type.String({ minLength: length, maxLength: length });
```

```ts
pg.varchar({ length: ... });

mysql.varchar({ length: ... });

sqlite.text({ mode: 'text', length: ... });

// Schema
Type.String({ maxLength: length });
```

```ts
mysql.tinytext();

// Schema
Type.String({ maxLength: 255 }); // unsigned 8-bit integer limit
```

```ts
mysql.text();

// Schema
Type.String({ maxLength: 65_535 }); // unsigned 16-bit integer limit
```

```ts
mysql.mediumtext();

// Schema
Type.String({ maxLength: 16_777_215 }); // unsigned 24-bit integer limit
```

```ts
mysql.longtext();

// Schema
Type.String({ maxLength: 4_294_967_295 }); // unsigned 32-bit integer limit
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
Type.Enum(enum);
```

```ts
mysql.tinyint();

// Schema
Type.Integer({ minimum: -128, maximum: 127 }); // 8-bit integer lower and upper limit
```

```ts
mysql.tinyint({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 255 }); // unsigned 8-bit integer lower and upper limit
```

```ts
pg.smallint();
pg.smallserial();

mysql.smallint();

// Schema
Type.Integer({ minimum: -32_768, maximum: 32_767 }); // 16-bit integer lower and upper limit
```

```ts
mysql.smallint({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 65_535 }); // unsigned 16-bit integer lower and upper limit
```

```ts
pg.real();

mysql.float();

// Schema
Type.Number().min(-8_388_608).max(8_388_607); // 24-bit integer lower and upper limit
```

```ts
mysql.mediumint();

// Schema
Type.Integer({ minimum: -8_388_608, maximum: 8_388_607 }); // 24-bit integer lower and upper limit
```

```ts
mysql.float({ unsigned: true });

// Schema
Type.Number({ minimum: 0, maximum: 16_777_215 }); // unsigned 24-bit integer lower and upper limit
```

```ts
mysql.mediumint({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 16_777_215 }); // unsigned 24-bit integer lower and upper limit
```

```ts
pg.integer();
pg.serial();

mysql.int();

// Schema
Type.Integer({ minimum: -2_147_483_648, maximum: 2_147_483_647 }); // 32-bit integer lower and upper limit
```

```ts
mysql.int({ unsigned: true });

// Schema
Type.Integer({ minimum: 0, maximum: 4_294_967_295 }); // unsgined 32-bit integer lower and upper limit
```

```ts
pg.doublePrecision();

mysql.double();
mysql.real();

sqlite.real();

// Schema
Type.Number({ minimum: -140_737_488_355_328, maximum: 140_737_488_355_327 }); // 48-bit integer lower and upper limit
```

```ts
mysql.double({ unsigned: true });

// Schema
Type.Numer({ minimum: 0, maximum: 281_474_976_710_655 }); // unsigned 48-bit integer lower and upper limit
```

```ts
pg.bigint({ mode: 'number' });
pg.bigserial({ mode: 'number' });

mysql.bigint({ mode: 'number' });
mysql.bigserial({ mode: 'number' });

sqlite.integer({ mode: 'number' });

// Schema
Type.Integer({ minimum: -9_007_199_254_740_991, maximum: 9_007_199_254_740_991 }); // Javascript min. and max. safe integers
```

```ts
mysql.serial();

Type.Integer({ minimum: 0, maximum: 9_007_199_254_740_991 }); // Javascript max. safe integer
```

```ts
pg.bigint({ mode: 'bigint' });
pg.bigserial({ mode: 'bigint' });

mysql.bigint({ mode: 'bigint' });

sqlite.blob({ mode: 'bigint' });

// Schema
Type.BigInt({ minimum: -9_223_372_036_854_775_808n, maximum: 9_223_372_036_854_775_807n }); // 64-bit integer lower and upper limit
```

```ts
mysql.bigint({ mode: 'bigint', unsigned: true });

// Schema
Type.BigInt({ minimum: 0, maximum: 18_446_744_073_709_551_615n }); // unsigned 64-bit integer lower and upper limit
```

```ts
mysql.year();

// Schema
Type.Integer({ minimum: 1_901, maximum: 2_155 });
```

```ts
pg.geometry({ type: 'point', mode: 'tuple' });
pg.point({ mode: 'tuple' });

// Schema
Type.Tuple([Type.Number(), Type.Number()]);
```

```ts
pg.geometry({ type: 'point', mode: 'xy' });
pg.point({ mode: 'xy' });

// Schema
Type.Object({ x: Type.Number(), y: Type.Number() });
```

```ts
pg.halfvec({ dimensions: ... });
pg.vector({ dimensions: ... });

// Schema
Type.Array(Type.Number(), { minItems: dimensions, maxItems: dimensions });
```

```ts
pg.line({ mode: 'abc' });

// Schema
Type.Object({ a: Type.Number(), b: Type.Number(), c: Type.Number() });
```

```ts
pg.line({ mode: 'tuple' });

// Schema
Type.Tuple([Type.Number(), Type.Number(), Type.Number()]);
```

```ts
pg.json();
pg.jsonb();

mysql.json();

sqlite.blob({ mode: 'json' });
sqlite.text({ mode: 'json' });

// Schema
Type.Recursive((self) => Type.Union([Type.Union([Type.String(), Type.Number(), Type.Boolean(), Type.Null()]), Type.Array(self), Type.Record(Type.String(), self)]));
```

```ts
sqlite.blob({ mode: 'buffer' });

// Schema
t.Union([t.Union([t.String(), t.Number(), t.Boolean(), t.Null()]), t.Array(t.Any()), t.Record(t.String(), t.Any())]);
```

```ts
pg.dataType().array(...);

// Schema
Type.Array(baseDataTypeSchema, { minItems: size, maxItems: size });
```


Source: https://orm.drizzle.team/docs/typebox

import Npm from '@mdx/Npm.astro';
import Callout from '@mdx/Callout.astro';

<Callout type="error">
Starting from `drizzle-orm@1.0.0-beta.15`, `drizzle-typebox` has been deprecated in favor of first-class schema generation support within Drizzle ORM itself

You can still use `drizzle-typebox` package but all new update will be added to Drizzle ORM directly

This version of `typebox` is using new `typebox` package
</Callout>


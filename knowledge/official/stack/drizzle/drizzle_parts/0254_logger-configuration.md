##### Logger configuration

By default, `makeWithDefaults()` uses a no-op logger (no logging). You can enable logging by providing 
a different `EffectLogger` implementation:

```typescript copy
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { EffectLogger } from 'drizzle-orm/effect-postgres';
import * as Effect from 'effect/Effect';

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.make({ /* schema, relations, casing */ }).pipe(
    // Enable Effect-based logging (uses Effect.log with annotations)
    Effect.provide(EffectLogger.layer),
    // Provide remaining default services (cache)
    Effect.provide(PgDrizzle.DefaultServices),
  );

  const users = yield* db.select().from(usersTable);
  return users;
});
```

**Available logger options:**
- `EffectLogger.Default` - No-op logger (no logging occurs) - this is the default
- `EffectLogger.layer` - Logs queries using Effect's `Effect.log()` with annotations for query SQL and parameters. Integrates with Effect's logging infrastructure.
- `EffectLogger.fromDrizzle(logger)` - Wraps a Drizzle `Logger` instance for use with Effect
- `EffectLogger.layerFromDrizzle(logger)` - Creates an Effect Layer from a Drizzle logger

<Callout type='info'>
When using `EffectLogger.layer`, queries are logged via Effect's logging system. You can configure the output 
format by providing a different Effect logger layer (e.g., `Logger.pretty` for development, `Logger.json` for production).
</Callout>

**Using a Drizzle logger:**

```typescript copy
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { EffectLogger } from 'drizzle-orm/effect-postgres';
import * as Effect from 'effect/Effect';
import { DefaultLogger } from 'drizzle-orm';

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.make({ /* schema, relations, casing */ }).pipe(
    // Use a Drizzle logger wrapped for Effect
    Effect.provide(EffectLogger.layerFromDrizzle(new DefaultLogger())),
    // Provide remaining default services (cache)
    Effect.provide(PgDrizzle.DefaultServices),
  );

  const users = yield* db.select().from(usersTable);
  return users;
});
```


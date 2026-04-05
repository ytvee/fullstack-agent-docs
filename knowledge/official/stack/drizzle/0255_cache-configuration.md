##### Cache configuration

Similarly, you can provide a custom cache implementation:

```typescript copy
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { EffectLogger } from 'drizzle-orm/effect-postgres';
import { EffectCache } from 'drizzle-orm/cache/core/cache-effect';
import * as Effect from 'effect/Effect';
import { MyCustomCache } from './cache';

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.make({ /* schema, relations, casing */ }).pipe(
    // Provide a custom cache wrapped for Effect
    Effect.provide(EffectCache.layerFromDrizzle(new MyCustomCache())),
    // Provide remaining default services (logger)
    Effect.provide(PgDrizzle.DefaultServices),
  );

  const users = yield* db.select().from(usersTable);
  return users;
});
```

**Available cache options:**
- `EffectCache.Default` - No-op cache (no caching occurs) - this is the default
- `EffectCache.fromDrizzle(cache)` - Wraps a Drizzle `Cache` instance for use with Effect
- `EffectCache.layerFromDrizzle(cache)` - Creates an Effect Layer from a Drizzle cache (useful for composing with other layers)


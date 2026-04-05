#### Step 3 - Create a DB Layer for dependency injection

For larger applications, create a reusable DB layer that can be composed with other services. This follows Effect's 
recommended pattern for dependency injection:

```typescript copy
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { PgClient } from '@effect/sql-pg';
import * as Context from 'effect/Context';
import * as Effect from 'effect/Effect';
import * as Layer from 'effect/Layer';
import * as Redacted from 'effect/Redacted';
import { types } from 'pg';
import * as relations from './schema/relations';

// Configure the PgClient layer
const PgClientLive = PgClient.layer({
  url: Redacted.make(process.env.DATABASE_URL!),
  types: {
    getTypeParser: (typeId, format) => {
      if ([1184, 1114, 1082, 1186, 1231, 1115, 1185, 1187, 1182].includes(typeId)) {
        return (val: any) => val;
      }
      return types.getTypeParser(typeId, format);
    },
  },
});

// Create the DB effect with default services
const dbEffect = PgDrizzle.make({ relations }).pipe(
  Effect.provide(PgDrizzle.DefaultServices)
);

// Define a DB service tag for dependency injection
class DB extends Context.Tag('DB')<DB, Effect.Effect.Success<typeof dbEffect>>() {}

// Create a layer that provides the DB service
const DBLive = Layer.effect(
  DB,
  Effect.gen(function*() {
    return yield* dbEffect;
  }),
);

// Compose all layers together
const AppLive = Layer.provideMerge(DBLive, PgClientLive);

// Use the DB service in your application
const program = Effect.gen(function*() {
  const db = yield* DB;
  const users = yield* db.select().from(usersTable);
  return users;
});

// Run with all dependencies provided
Effect.runPromise(program.pipe(Effect.provide(AppLive)));
```


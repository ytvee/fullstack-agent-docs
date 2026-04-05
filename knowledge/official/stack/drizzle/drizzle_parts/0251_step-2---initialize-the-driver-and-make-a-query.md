#### Step 2 - Initialize the driver and make a query

Drizzle provides an Effect-native API that integrates with Effect's service pattern. Use `PgDrizzle.makeWithDefaults()` 
to quickly create a Drizzle database instance with sensible defaults (no logging, no caching).

```typescript copy
import 'dotenv/config';
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { PgClient } from '@effect/sql-pg';
import * as Effect from 'effect/Effect';
import * as Redacted from 'effect/Redacted';
import { sql } from 'drizzle-orm';
import { types } from 'pg';

// Configure the PgClient layer with type parsers
const PgClientLive = PgClient.layer({
  url: Redacted.make(process.env.DATABASE_URL!),
  types: {
    getTypeParser: (typeId, format) => {
      // Return raw values for date/time types to let Drizzle handle parsing
      if ([1184, 1114, 1082, 1186, 1231, 1115, 1185, 1187, 1182].includes(typeId)) {
        return (val: any) => val;
      }
      return types.getTypeParser(typeId, format);
    },
  },
});

const program = Effect.gen(function*() {
  // Create the database with default services (no logging, no caching)
  const db = yield* PgDrizzle.makeWithDefaults();

  // Execute queries
  const result = yield* db.execute<{ id: number }>(sql`SELECT 1 as id`);
  console.log(result);
});

// Run the program with the PgClient layer
Effect.runPromise(program.pipe(Effect.provide(PgClientLive)));
```


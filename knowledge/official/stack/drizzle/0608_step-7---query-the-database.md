#### Step 7 - Query the database

```ts
import 'dotenv/config';
import * as PgDrizzle from 'drizzle-orm/effect-postgres';
import { PgClient } from '@effect/sql-pg';
import * as Effect from 'effect/Effect';
import * as Redacted from 'effect/Redacted';
import { types } from 'pg';
import { eq } from 'drizzle-orm';
import { usersTable } from './db/schema';

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

const program = Effect.gen(function*() {
  const db = yield* PgDrizzle.makeWithDefaults();

  const user: typeof usersTable.$inferInsert = {
    name: 'John',
    age: 30,
    email: 'john@example.com',
  };

  yield* db.insert(usersTable).values(user);
  console.log('New user created!')

  const users = yield* db.select().from(usersTable);
  console.log('Getting all users from the database: ', users)
  /*
  const users: {
    id: number;
    name: string;
    age: number;
    email: string;
  }[]
  */

  yield* db
    .update(usersTable)
    .set({
      age: 31,
    })
    .where(eq(usersTable.email, user.email));
  console.log('User info updated!')

  yield* db.delete(usersTable).where(eq(usersTable.email, user.email));
  console.log('User deleted!')
});

Effect.runPromise(program.pipe(Effect.provide(PgClientLive)));
```


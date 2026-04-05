### On duplicate key update
<IsSupportedChipGroup chips={{ 'PostgreSQL': false, 'SQLite': false, 'MySQL': true, 'SingleStore': true, 'CockroachDB': false }} />

MySQL supports [`ON DUPLICATE KEY UPDATE`](https://dev.mysql.com/doc/refman/8.0/en/insert-on-duplicate.html) instead of `ON CONFLICT` clauses. MySQL will automatically determine the conflict target based on the primary key and unique indexes, and will update the row if *any* unique index conflicts.

Drizzle supports this through the `onDuplicateKeyUpdate` method:

```typescript
// Note that MySQL automatically determines targets based on the primary key and unique indexes
await db.insert(users)
  .values({ id: 1, name: 'John' })
  .onDuplicateKeyUpdate({ set: { name: 'John' } });
```

While MySQL does not directly support doing nothing on conflict, you can perform a no-op by setting any column's value to itself and achieve the same effect:

```typescript
import { sql } from 'drizzle-orm';

await db.insert(users)
  .values({ id: 1, name: 'John' })
  .onDuplicateKeyUpdate({ set: { id: sql`id` } });
```


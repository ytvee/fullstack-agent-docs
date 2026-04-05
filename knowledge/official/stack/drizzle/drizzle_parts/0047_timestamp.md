### timestamp
`timestamp` `timestamptz` `timestamp with time zone` `timestamp without time zone`  

The TIMESTAMP and TIMESTAMPTZ data types store a date and time pair in UTC.

For more info please refer to the official CockroachDB **[docs.](https://www.cockroachlabs.com/docs/stable/timestamp)**
<Section>
```typescript
import { sql } from "drizzle-orm";
import { timestamp, cockroachTable } from "drizzle-orm/cockroach-core";

const table = cockroachTable('table', {
  timestamp1: timestamp(),
	timestamp2: timestamp({ precision: 6, withTimezone: true }),
	timestamp3: timestamp().defaultNow(),
	timestamp4: timestamp().default(sql`now()`),
});
```
```sql
CREATE TABLE "table" (
	"timestamp1" timestamp,
	"timestamp2" timestamp (6) with time zone,
	"timestamp3" timestamp default now(),
	"timestamp4" timestamp default now()
);
```
</Section>

You can specify either `date` or `string` infer modes:
```typescript
// will infer as date
timestamp: timestamp({ mode: "date" }),

// will infer as string
timestamp: timestamp({ mode: "string" }),
```

> The `string` mode does not perform any mappings for you. This mode was added to Drizzle ORM to provide developers
with the possibility to handle dates and date mappings themselves, depending on their needs.
Drizzle will pass raw dates as strings `to` and `from` the database, so the behavior should be as predictable as possible 
and aligned 100% with the database behavior

> The `date` mode is the regular way to work with dates. Drizzle will take care of all mappings between the database and the JS Date object


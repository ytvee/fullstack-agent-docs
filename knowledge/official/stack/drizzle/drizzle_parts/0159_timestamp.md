### timestamp
`timestamp` `timestamptz` `timestamp with time zone` `timestamp without time zone`  
Date and time with or without time zone.

For more info please refer to the official PostgreSQL **[docs.](https://www.postgresql.org/docs/current/datatype-datetime.html)**
<Section>
```typescript
import { sql } from "drizzle-orm";
import { timestamp, pgTable } from "drizzle-orm/pg-core";

const table = pgTable('table', {
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

<Callout type='info' emoji='ℹ️'>
 How mapping works for `timestamp` and `timestamp with timezone`:

 As PostgreSQL docs stated:
 > In a literal that has been determined to be timestamp without time zone, PostgreSQL will silently ignore any time zone indication. 
 > That is, the resulting value is derived from the date/time fields in the input value, and is not adjusted for time zone.
 >
 > For timestamp with time zone, the internally stored value is always in UTC (Universal Coordinated Time, traditionally known as Greenwich Mean Time, GMT). 
 An input value that has an explicit time zone specified is converted to UTC using the appropriate offset for that time zone. 
 If no time zone is stated in the input string, then it is assumed to be in the time zone indicated by the system's TimeZone parameter, 
 and is converted to UTC using the offset for the timezone zone.

 So for `timestamp with timezone` you will get back string converted to a timezone set in your Postgres instance. 
 You can check timezone using this sql query: 
 
 ```sql 
 show timezone;
 ```


</Callout>


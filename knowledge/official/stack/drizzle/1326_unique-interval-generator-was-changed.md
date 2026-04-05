#### Unique `interval` generator was changed

<Callout title='Reason for upgrade'>
An older version of the generator could produce intervals like `1 minute 60 seconds` and `2 minutes 0 seconds`, treating them as distinct intervals.
However, when the `1 minute 60 seconds` interval is inserted into a PostgreSQL database, it is automatically converted to `2 minutes 0 seconds`. As a result, attempting to insert the `2 minutes 0 seconds` interval into a unique column afterwards will cause an error
</Callout>

You will be affected, if your table includes a unique column of type `interval`:
<Tabs items={['PostgreSQL']}>
<Tab>
```ts
import { drizzle } from "drizzle-orm/node-postgres";
import { pgTable, interval } from "drizzle-orm/pg-core";
import { seed } from "drizzle-seed";

const intervals = pgTable("intervals", {
    interval: interval().unique()
});

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, { intervals });
}

main();
```
</Tab>
</Tabs>

You will be affected, if you use the unique `interval` generator in your seeding script, as shown in the script below:
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
```ts
import { drizzle } from "drizzle-orm/node-postgres";
import { pgTable, interval, char, varchar, text } from "drizzle-orm/pg-core";
import { seed } from "drizzle-seed";

const intervals = pgTable("intervals", {
    interval: interval().unique(),
    interval1: interval(),
    interval2: char({ length: 256 }).unique(),
    interval3: char({ length: 256 }),
    interval4: varchar().unique(),
    interval5: varchar(),
    interval6: text().unique(),
    interval7: text(),
});

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, { intervals }).refine((f) => ({
    intervals: {
        columns: {
            interval: f.interval({ isUnique: true }),
            interval1: f.interval({ isUnique: true }),
            interval2: f.interval({ isUnique: true }),
            interval3: f.interval({ isUnique: true }),
            interval4: f.interval({ isUnique: true }),
            interval5: f.interval({ isUnique: true }),
            interval6: f.interval({ isUnique: true }),
            interval7: f.interval({ isUnique: true }),
        }
    }
  }));
}

main();
```
</Tab>
<Tab>
```ts
import { binary, char, mysqlTable, text, varbinary, varchar } from 'drizzle-orm/mysql-core';
import { drizzle } from 'drizzle-orm/mysql2';
import { seed } from "drizzle-seed";

const intervals = mysqlTable('intervals', {
	interval1: char({ length: 255 }).unique(),
	interval2: char({ length: 255 }),
	interval3: varchar({ length: 255 }).unique(),
	interval4: varchar({ length: 255 }),
	interval5: binary({ length: 255 }).unique(),
	interval6: binary({ length: 255 }),
	interval7: varbinary({ length: 255 }).unique(),
	interval8: varbinary({ length: 255 }),
	interval9: text(),
});

async function main() {
	const db = drizzle(process.env.DATABASE_URL!);

	await seed(db, { intervals }, { version: '2' }).refine((f) => ({
		intervals: {
			columns: {
				interval: f.interval({ isUnique: true }),
				interval1: f.interval({ isUnique: true }),
				interval2: f.interval({ isUnique: true }),
				interval3: f.interval({ isUnique: true }),
				interval4: f.interval({ isUnique: true }),
				interval5: f.interval({ isUnique: true }),
				interval6: f.interval({ isUnique: true }),
				interval7: f.interval({ isUnique: true }),
				interval8: f.interval({ isUnique: true }),
				interval9: f.interval({ isUnique: true }),
			},
		},
	}));
}

main();

```
</Tab>
<Tab>
```ts
import { blob, sqliteTable, text } from 'drizzle-orm/sqlite-core';
import { drizzle } from 'drizzle-orm/better-sqlite3';
import { seed } from 'drizzle-seed';

const intervals = sqliteTable('intervals', {
	interval1: text().unique(),
	interval2: text(),
	interval3: blob().unique(),
	interval4: blob(),
});

async function main() {
	const db = drizzle(process.env.DATABASE_URL!);

	await seed(db, { intervals }).refine((f) => ({
		intervals: {
			columns: {
				interval1: f.interval({ isUnique: true }),
				interval2: f.interval({ isUnique: true }),
				interval3: f.interval({ isUnique: true }),
				interval4: f.interval({ isUnique: true }),
			},
		},
	}));
}

main();

```
</Tab>
</Tabs>


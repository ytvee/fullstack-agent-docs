#### `string` generators were changed: both non-unique and unique

<Callout title='Reason to upgrade'>
Ability to generate a unique string based on the length of the text column (e.g., `varchar(20)`)
</Callout>

You will be affected, if your table includes a column of a text-like type with a maximum length parameter or a unique column of a text-like type:
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
```ts
import { drizzle } from "drizzle-orm/node-postgres";
import { pgTable, char, varchar, text } from "drizzle-orm/pg-core";
import { seed } from "drizzle-seed";

const strings = pgTable("strings", {
    string2: char({ length: 256 }).unique(),
    string3: char({ length: 256 }),
    string4: varchar().unique(),
    string5: varchar({ length: 256 }).unique(),
    string6: varchar({ length: 256 }),
    string7: text().unique(),
});

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, { strings });
}

main();
```
</Tab>
<Tab>
```ts
import { binary, char, mysqlTable, varbinary, varchar } from 'drizzle-orm/mysql-core';
import { drizzle } from 'drizzle-orm/mysql2';
import { seed } from "drizzle-seed";

const strings = mysqlTable('strings', {
	string1: char({ length: 255 }).unique(),
	string2: char({ length: 255 }),
	string3: varchar({ length: 255 }).unique(),
	string4: varchar({ length: 255 }),
	string5: binary({ length: 255 }).unique(),
	string6: binary({ length: 255 }),
	string7: varbinary({ length: 255 }).unique(),
	string8: varbinary({ length: 255 }),
});

async function main() {
	const db = drizzle(process.env.DATABASE_URL!);

	await seed(db, { strings });
}

main();

```
</Tab>
<Tab>
```ts
import { drizzle } from 'drizzle-orm/better-sqlite3';
import { blob, sqliteTable, text } from 'drizzle-orm/sqlite-core';
import { seed } from "drizzle-seed";

const strings = sqliteTable('strings', {
	string1: text().unique(),
	string2: text({ length: 256 }),
	string3: text({ length: 256 }).unique(),
	string4: blob().unique(),
});

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, { strings });
}

main();
```
</Tab>
</Tabs>

You will be affected, if you use the `string` generator in your seeding script, as shown in the script below:
<Tabs items={['PostgreSQL', 'MySQL', 'SQLite']}>
<Tab>
```ts
import { drizzle } from "drizzle-orm/node-postgres";
import { pgTable, char, varchar, text } from "drizzle-orm/pg-core";
import { seed } from "drizzle-seed";

const strings = pgTable("strings", {
    string1: char({ length: 256 }).unique(),
    string2: char({ length: 256 }),
    string3: char({ length: 256 }),
    string4: varchar(),
    string5: varchar().unique(),
    string6: varchar({ length: 256 }).unique(),
    string7: varchar({ length: 256 }),
    string8: varchar({ length: 256 }),
    string9: text().unique(),
    string10: text(),
});

async function main() {
  const db = drizzle(process.env.DATABASE_URL!);

  await seed(db, { strings }).refine((f) => ({
    strings: {
        columns: {
            string1: f.string({ isUnique: true }),
            string2: f.string(),
            string3: f.string({ isUnique: true }),
            string4: f.string({ isUnique: true }),
            string5: f.string({ isUnique: true }),
            string6: f.string({ isUnique: true }),
            string7: f.string(),
            string8: f.string({ isUnique: true }),
            string9: f.string({ isUnique: true }),
            string10: f.string({ isUnique: true }),
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

const strings = mysqlTable('strings', {
	string1: char({ length: 255 }).unique(),
	string2: char({ length: 255 }),
	string3: char({ length: 255 }),
	string4: varchar({ length: 255 }).unique(),
	string5: varchar({ length: 255 }),
	string6: varchar({ length: 255 }),
	string7: binary({ length: 255 }).unique(),
	string8: binary({ length: 255 }),
	string9: binary({ length: 255 }),
	string10: varbinary({ length: 255 }).unique(),
	string11: varbinary({ length: 255 }),
	string12: varbinary({ length: 255 }),
	string13: text(),
});

async function main() {
	const db = drizzle(process.env.DATABASE_URL!);

	await seed(db, { strings }).refine((f) => ({
		strings: {
			columns: {
				string1: f.string({ isUnique: true }),
				string2: f.string({ isUnique: true }),
				string3: f.string(),
				string4: f.string({ isUnique: true }),
				string5: f.string({ isUnique: true }),
				string6: f.string(),
				string7: f.string({ isUnique: true }),
				string8: f.string({ isUnique: true }),
				string9: f.string(),
				string10: f.string({ isUnique: true }),
				string11: f.string({ isUnique: true }),
				string12: f.string(),
				string13: f.string({ isUnique: true }),
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
import { seed } from "drizzle-seed";

const strings = sqliteTable("strings", {
    string1: text().unique(),
	string2: text(),
	string3: text({ length: 256 }).unique(),
	string4: text({ length: 256 }),
	string5: text({ length: 256 }),
	string6: blob().unique(),
	string7: blob(),
});

async function main() {
	const db = drizzle(process.env.DATABASE_URL!);

	await seed(db, { strings }).refine((f) => ({
		strings: {
			columns: {
				string1: f.string({ isUnique: true }),
				string2: f.string({ isUnique: true }),
				string3: f.string({ isUnique: true }),
				string4: f.string({ isUnique: true }),
				string5: f.string(),
				string6: f.string({ isUnique: true }),
				string7: f.string({ isUnique: true }),
			},
		},
	}));
}

main();
```
</Tab>
</Tabs>

Source: https://orm.drizzle.team/docs/select

import Tab from '@mdx/Tab.astro';
import Tabs from '@mdx/Tabs.astro';
import CodeTabs from '@mdx/CodeTabs.astro';
import Callout from '@mdx/Callout.astro';
import Section from '@mdx/Section.astro';
import IsSupportedChipGroup from '@mdx/IsSupportedChipGroup.astro';
import $count from '@mdx/$count.mdx';


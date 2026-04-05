# Drizzle relations

<Callout type='error'>
This page explains concepts available on drizzle versions `1.0.0-beta.1` and higher.
</Callout>

<Npm>
drizzle-orm@beta
drizzle-kit@beta -D
</Npm>

<br/>

<Prerequisites>  
  - **Relations Fundamentals** - get familiar with the concepts of foreign key constraints, soft relations, database normalization, etc - [read here](/docs/rqb-fundamentals)
  - **Declare schema** - get familiar with how to define drizzle schemas - [read here](/docs/sql-schema-declaration)
  - **Database connection** - get familiar with how to connect to database using drizzle - [read here](/docs/get-started-postgresql)
</Prerequisites>

The sole purpose of Drizzle relations is to let you query your relational data in the most simple and concise way:

<CodeTabs items={["Relational queries", "Select with joins"]}>
<Section>
```ts
import { drizzle } from 'drizzle-orm/…';
import { defineRelations } from 'drizzle-orm';
import * as p from 'drizzle-orm/pg-core';

export const users = p.pgTable('users', {
	id: p.integer().primaryKey(),
	name: p.text().notNull()
});

export const posts = p.pgTable('posts', {
	id: p.integer().primaryKey(),
	content: p.text().notNull(),
	ownerId: p.integer('owner_id'),
});

const relations = defineRelations({ users, posts }, (r) => ({
	posts: {
		author: r.one.users({
			from: r.posts.ownerId,
			to: r.users.id,
		}),
	}
}))

const db = drizzle(client, { relations });

const result = db.query.posts.findMany({
  with: {
    author: true,
  },
});
```
```ts
[{
  id: 10,
  content: "My first post!",
  author: {
    id: 1,
    name: "Alex"
  }
}]
```
</Section>
<Section>
```ts
import { drizzle } from 'drizzle-orm/…';
import { eq } from 'drizzle-orm';
import { posts, users } from './schema';

const db = drizzle(client);

const res = await db.select()
                    .from(posts)
                    .leftJoin(users, eq(posts.ownerId, users.id))
                    .orderBy(posts.id)
const mappedResult =  
```
</Section>
</CodeTabs>


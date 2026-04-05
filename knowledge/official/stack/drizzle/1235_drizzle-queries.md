# Drizzle Queries

<Callout type='error'>
This page explains concepts available on drizzle versions `1.0.0-beta.1` and higher.
</Callout>

<Npm>
drizzle-orm@beta
drizzle-kit@beta -D
</Npm>

<br/>

<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'SQLite': true, 'MySQL': true, 'SingleStore': true }} />

Drizzle ORM is designed to be a thin typed layer on top of SQL. 
We truly believe we've designed the best way to operate an SQL database from TypeScript and it's time to make it better.  
  
Relational queries are meant to provide you with a great developer experience for querying 
nested relational data from an SQL database, avoiding multiple joins and complex data mappings.  

It is an extension to the existing schema definition and query builder. 
You can opt-in to use it based on your needs. 
We've made sure you have both the best-in-class developer experience and performance.  

<CodeTabs items={["index.ts", "schema.ts"]}>
	<CodeTab>
	```typescript copy /schema/3
	import { relations } from './schema';
	import { drizzle } from 'drizzle-orm/...';

	const db = drizzle({ relations });

	const result = await db.query.users.findMany({
		with: {
			posts: true			
		},
	});
	```

	```ts
	[{
		id: 10,
		name: "Dan",
		posts: [
			{
				id: 1,
				content: "SQL is awesome",
				authorId: 10,
			},
			{
				id: 2,
				content: "But check relational queries",
				authorId: 10,
			}
		]
	}]
	```
	</CodeTab>

	```typescript {15-25} copy
    import { defineRelations } from "drizzle-orm";
    import * as p from "drizzle-orm/pg-core";
    
    export const posts = p.pgTable("posts", {
      id: p.integer().primaryKey(),
      content: p.text().notNull(),
      authorId: p.integer("author_id").notNull(),
    });
    
    export const users = p.pgTable("users", {
      id: p.integer().primaryKey(),
      name: p.text().notNull(),
    });
    
    export const relations = defineRelations({ users, posts }, (r) => ({
      posts: {
        author: r.one.users({
          from: r.posts.authorId,
          to: r.users.id,
        }),
      },
      users: {
        posts: r.many.users(),
      },
    }));
	```
</CodeTabs>

Relational queries are an extension to Drizzle's original **[query builder](/docs/select)**.
You need to provide all `tables` and `relations` from your schema file/files upon `drizzle()` 
initialization and then just use the `db.query` API.
<Callout type="info" emoji="ℹ️">
	`drizzle` import path depends on the **[database driver](/docs/connect-overview)** you're using.
</Callout>
<CodeTabs items={["index.ts", "schema.ts", "relations.ts"]}>
<CodeTab>
```ts
import { relations } from './relations';
import { drizzle } from 'drizzle-orm/...';

const db = drizzle({ relations });

await db.query.users.findMany(...);
```
</CodeTab>
```typescript copy
import { type AnyPgColumn, boolean, integer, pgTable, primaryKey, text, timestamp } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
	id: integer().primaryKey(),
	name: text().notNull(),
	invitedBy: integer('invited_by').references((): AnyPgColumn => users.id),
});

export const groups = pgTable('groups', {
	id: integer().primaryKey(),
	name: text().notNull(),
	description: text(),
});

export const usersToGroups = pgTable('users_to_groups', {
	id: integer().primaryKey(),
	userId: integer('user_id').notNull().references(() => users.id),
	groupId: integer('group_id').notNull().references(() => groups.id),
}, (t) => [
	primaryKey(t.userId, t.groupId)
]);

export const posts = pgTable('posts', {
	id: integer().primaryKey(),
	content: text().notNull(),
	authorId: integer('author_id').references(() => users.id),
	createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});

export const comments = pgTable('comments', {
	id: integer().primaryKey(),
	content: text().notNull(),
	creator: integer().references(() => users.id),
	postId: integer('post_id').references(() => posts.id),
	createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});

export const commentLikes = pgTable('comment_likes', {
	id: integer().primaryKey(),
	creator: integer().references(() => users.id),
	commentId: integer('comment_id').references(() => comments.id),
	createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
});
```
```typescript copy
import { defineRelations } from 'drizzle-orm';
import * as schema from './schema';

export const relations = defineRelations(schema, (r) => ({
    users: {
      invitee: r.one.users({
        from: r.users.invitedBy,
        to: r.users.id,
      }),
      groups: r.many.groups({
        from: r.users.id.through(r.usersToGroups.userId),
        to: r.groups.id.through(r.usersToGroups.groupId),
      }),
      posts: r.many.posts(),
    },
    groups: {
      users: r.many.users(),
    },
    posts: {
      author: r.one.users({
        from: r.posts.authorId,
        to: r.users.id,
      }),
      comments: r.many.comments(),
    },
    comments: {
      post: r.one.posts({
        from: r.comments.postId,
        to: r.posts.id,
      }),
      author: r.one.users({
        from: r.comments.creator,
        to: r.users.id,
      }),
      likes: r.many.commentLikes(),
    },
    commentLikes: {
      comment: r.one.comments({
        from: r.commentLikes.commentId,
        to: r.comments.id,
      }),
      author: r.one.users({
        from: r.commentLikes.creator,
        to: r.users.id,
      }),
    },
  })
);
```
</CodeTabs>

Drizzle provides `.findMany()` and `.findFirst()` APIs.

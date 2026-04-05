## Querying
Relational queries are an extension to Drizzle's original **[query builder](/docs/select)**.
You need to provide all `tables` and `relations` from your schema file/files upon `drizzle()` 
initialization and then just use the `db._query` API.
<Callout type="info" emoji="ℹ️">
	`drizzle` import path depends on the **[database driver](/docs/connect-overview)** you're using.
</Callout>
<CodeTabs items={["index.ts", "schema.ts"]}>
<CodeTab>
```ts
import * as schema from './schema';
import { drizzle } from 'drizzle-orm/...';

const db = drizzle({ schema });

await db._query.users.findMany(...);
```
```ts
// if you have schema in multiple files
import * as schema1 from './schema1';
import * as schema2 from './schema2';
import { drizzle } from 'drizzle-orm/...';

const db = drizzle({ schema: { ...schema1, ...schema2 } });

await db._query.users.findMany(...);
```
</CodeTab>
```typescript copy
	import { type AnyPgColumn, boolean, integer, pgTable, primaryKey, serial, text, timestamp } from 'drizzle-orm/pg-core';

	import { relations } from 'drizzle-orm';

	export const users = pgTable('users', {
		id: serial('id').primaryKey(),
		name: text('name').notNull(),
		verified: boolean('verified').notNull(),
		invitedBy: integer('invited_by').references((): AnyPgColumn => users.id),
	});

	export const usersRelations = relations(users, ({ one, many }) => ({
		invitee: one(users, { fields: [users.invitedBy], references: [users.id] }),
		usersToGroups: many(usersToGroups),
		posts: many(posts),
	}));

	export const groups = pgTable('groups', {
		id: serial('id').primaryKey(),
		name: text('name').notNull(),
		description: text('description'),
	});

	export const groupsRelations = relations(groups, ({ many }) => ({
		usersToGroups: many(usersToGroups),
	}));

	export const usersToGroups = pgTable('users_to_groups', {
		id: serial('id').primaryKey(),
		userId: integer('user_id').notNull().references(() => users.id),
		groupId: integer('group_id').notNull().references(() => groups.id),
	}, (t) => [
		primaryKey({ columns: [t.userId, t.groupId] })
	]);

	export const usersToGroupsRelations = relations(usersToGroups, ({ one }) => ({
		group: one(groups, { fields: [usersToGroups.groupId], references: [groups.id] }),
		user: one(users, { fields: [usersToGroups.userId], references: [users.id] }),
	}));

	export const posts = pgTable('posts', {
		id: serial('id').primaryKey(),
		content: text('content').notNull(),
		authorId: integer('author_id').references(() => users.id),
		createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
	});

	export const postsRelations = relations(posts, ({ one, many }) => ({
		author: one(users, { fields: [posts.authorId], references: [users.id] }),
		comments: many(comments),
	}));

	export const comments = pgTable('comments', {
		id: serial('id').primaryKey(),
		content: text('content').notNull(),
		creator: integer('creator').references(() => users.id),
		postId: integer('post_id').references(() => posts.id),
		createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
	});

	export const commentsRelations = relations(comments, ({ one, many }) => ({
		post: one(posts, { fields: [comments.postId], references: [posts.id] }),
		author: one(users, { fields: [comments.creator], references: [users.id] }),
		likes: many(commentLikes),
	}));

	export const commentLikes = pgTable('comment_likes', {
		id: serial('id').primaryKey(),
		creator: integer('creator').references(() => users.id),
		commentId: integer('comment_id').references(() => comments.id),
		createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
	});

	export const commentLikesRelations = relations(commentLikes, ({ one }) => ({
		comment: one(comments, { fields: [commentLikes.commentId], references: [comments.id] }),
		author: one(users, { fields: [commentLikes.creator], references: [users.id] }),
	}));
```
</CodeTabs>

Drizzle provides `.findMany()` and `.findFirst()` APIs.

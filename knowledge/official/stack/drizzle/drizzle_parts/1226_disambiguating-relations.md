### Disambiguating relations

Drizzle also provides the `relationName` option as a way to disambiguate
relations when you define multiple of them between the same two tables. For
example, if you define a `posts` table that has the `author` and `reviewer`
relations.

```ts {9-12, 21-32}
import { pgTable, serial, text, integer } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';
 
export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
});
 
export const usersRelations = relations(users, ({ many }) => ({
	author: many(posts, { relationName: 'author' }),
	reviewer: many(posts, { relationName: 'reviewer' }),
}));
 
export const posts = pgTable('posts', {
	id: serial('id').primaryKey(),
	content: text('content'),
	authorId: integer('author_id'),
	reviewerId: integer('reviewer_id'),
});
 
export const postsRelations = relations(posts, ({ one }) => ({
	author: one(users, {
		fields: [posts.authorId],
		references: [users.id],
		relationName: 'author',
	}),
	reviewer: one(users, {
		fields: [posts.reviewerId],
		references: [users.id],
		relationName: 'reviewer',
	}),
}));
```


Source: https://orm.drizzle.team/docs/rls

import Callout from '@mdx/Callout.astro';


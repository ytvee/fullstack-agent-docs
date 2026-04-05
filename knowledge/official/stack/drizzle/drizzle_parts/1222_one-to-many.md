### One-to-many
Drizzle ORM provides you an API to define `one-to-many` relations between tables with `relations` operator. 

Example of `one-to-many` relation between users and posts they've written:

```typescript copy {9-11, 19-24}
import { pgTable, serial, text, integer } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
});

export const usersRelations = relations(users, ({ many }) => ({
	posts: many(posts),
}));

export const posts = pgTable('posts', {
	id: serial('id').primaryKey(),
	content: text('content'),
	authorId: integer('author_id'),
});

export const postsRelations = relations(posts, ({ one }) => ({
	author: one(users, {
		fields: [posts.authorId],
		references: [users.id],
	}),
}));
```

Now lets add comments to the posts:
```typescript copy {14,17-22,24-29}
...

export const posts = pgTable('posts', {
	id: serial('id').primaryKey(),
	content: text('content'),
	authorId: integer('author_id'),
});

export const postsRelations = relations(posts, ({ one, many }) => ({
	author: one(users, {
		fields: [posts.authorId],
		references: [users.id],
	}),
	comments: many(comments)
}));

export const comments = pgTable('comments', {
	id: serial('id').primaryKey(),
	text: text('text'),
	authorId: integer('author_id'),
	postId: integer('post_id'),
});

export const commentsRelations = relations(comments, ({ one }) => ({
	post: one(posts, {
		fields: [comments.postId],
		references: [posts.id],
	}),
}));
```



### One-to-many
Drizzle ORM provides you an API to define `one-to-many` relations between tables with `defineRelations` function. 

Example of `one-to-many` relation between users and posts they've written:

```typescript copy {15-25}
import { pgTable, serial, text, integer } from 'drizzle-orm/pg-core';
import { defineRelations } from 'drizzle-orm';

export const users = pgTable('users', {
	id: integer('id').primaryKey(),
	name: text('name'),
});

export const posts = pgTable('posts', {
	id: integer('id').primaryKey(),
	content: text('content'),
	authorId: integer('author_id'),
});

export const relations = defineRelations({ users, posts }, (r) => ({
  posts: {
    author: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
    }),
  },
  users: {
    posts: r.many.posts(),
  },
}));
```

Now lets add comments to the posts:
```typescript copy {9-14,22,27-32}
...

export const posts = pgTable('posts', {
	id: integer('id').primaryKey(),
	content: text('content'),
	authorId: integer('author_id'),
});

export const comments = pgTable("comments", {
  id: integer().primaryKey(),
  text: text(),
  authorId: integer("author_id"),
  postId: integer("post_id"),
});

export const relations = defineRelations({ users, posts, comments }, (r) => ({
  posts: {
    author: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
    }),
    comments: r.many.comments(),
  },
  users: {
    posts: r.many.posts(),
  },
  comments: {
    post: r.one.posts({
      from: r.comments.postId,
      to: r.posts.id,
    }),
  },
}));
```



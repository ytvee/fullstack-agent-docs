### Disambiguating relations

Drizzle also provides the `alias` option as a way to disambiguate
relations when you define multiple of them between the same two tables. For
example, if you define a `posts` table that has the `author` and `reviewer`
relations.

```ts {19,22,29,34}
import { pgTable, integer, text } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';
 
export const users = pgTable('users', {
	id: integer('id').primaryKey(),
	name: text('name'),
});

export const posts = pgTable('posts', {
	id: integer('id').primaryKey(),
	content: text('content'),
	authorId: integer('author_id'),
	reviewerId: integer('reviewer_id'),
});
 
export const relations = defineRelations({ users, posts }, (r) => ({
  users: {
    posts: r.many.posts({
      alias: "author",
    }),
    reviewedPosts: r.many.posts({
      alias: "reviewer",
    }),
  },
  posts: {
    author: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
      alias: "author",
    }),
    reviewer: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
      alias: "reviewer",
    }),
  },
}));
```


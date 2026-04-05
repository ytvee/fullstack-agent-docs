#### One-to-many Relationships

Similar to one-to-one relationships, one-to-many relations benefit significantly 
from indexing to optimize join operations. Consider the "users and posts" example where one user can have many posts.

<Callout>
For one-to-many relationships, create an index on the foreign key column in the table that represents the "many" side of the relationship (the table with the foreign key referencing the "one" side).
</Callout>

<Callout collapsed='Why it is important'>
When you fetch a user with their posts or posts with their authors, joins are performed.
Indexing the foreign key (`authorId` in `posts` table) allows the database to efficiently 
retrieve all posts associated with a given user or quickly find the author of a post.
</Callout>

**Example:**
```typescript
import * as p from "drizzle-orm/pg-core";
import { defineRelations } from 'drizzle-orm';

export const users = p.pgTable('users', {
	id: p.integer().primaryKey(),
	name: p.text(),
});

export const posts = p.pgTable('posts', {
	id: p.integer().primaryKey(),
	content: p.text(),
	authorId: p.integer('author_id'),
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

To optimize queries involving users and their posts, create an index on the `authorId` column in the `posts` table.

```typescript {13-15}
import * as p from "drizzle-orm/pg-core";
import { defineRelations } from 'drizzle-orm';

export const users = p.pgTable('users', {
	id: p.integer().primaryKey(),
	name: p.text(),
});

export const posts = p.pgTable('posts', {
	id: p.integer().primaryKey(),
	content: p.text(),
	authorId: p.integer('author_id'),
}, (t) => [
  index('posts_author_id_idx').on(table.authorId)
]);

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
```sql
CREATE INDEX idx_posts_author_id ON posts (author_id);
```


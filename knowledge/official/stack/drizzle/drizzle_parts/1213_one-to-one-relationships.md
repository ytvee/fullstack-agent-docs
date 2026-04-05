##### One-to-one Relationships

In a one-to-one relationship, like the "user invites user" example or the
"user has profile info" example, the key performance consideration is efficient joining 
of the related tables.

<Callout>
For optimal performance in one-to-one relationships, you should create an index 
on the foreign key column in the table that is being referenced 
(the "target" table in the relation).
</Callout>

<Callout collapsed='Why it is important'>
When you query data with related one-to-one information, Drizzle performs a JOIN operation. An index on the foreign key column allows the database to quickly 
locate the related row in the target table, significantly speeding up the join process.
</Callout>

**Example:**
```typescript
import * as p from 'drizzle-orm/pg-core';
import { defineRelations } from 'drizzle-orm';

export const users = p.pgTable('users', {
	id: p.integer().primaryKey(),
	name: p.text(),
});

export const profileInfo = p.pgTable('profile_info', {
	id: p.integer().primaryKey(),
	userId: p.integer('user_id').references(() => users.id),
	metadata: p.jsonb(),
});

export const relations = defineRelations({ users, profileInfo }, (r) => ({
	users: {
		profileInfo: r.one.profileInfo({
			from: r.users.id,
			to: r.profileInfo.userId,
		})
	}
}));
```

To optimize queries fetching user data along with their profile information, 
you should create an index on the `userId` column in the `profile_info` table.

```typescript {13-15,21}
import * as p from 'drizzle-orm/pg-core';
import { defineRelations } from 'drizzle-orm';

export const users = p.pgTable('users', {
	id: p.integer().primaryKey(),
	name: p.text(),
});

export const profileInfo = pgTable('profile_info', {
	id: p.integer().primaryKey(),
	userId: p.integer('user_id').references(() => users.id),
	metadata: p.jsonb(),
}, (table) => [
  p.index('profile_info_user_id_idx').on(table.userId)
]);

export const relations = defineRelations({ users, profileInfo }, (r) => ({
	users: {
		profileInfo: r.one.profileInfo({
			from: r.users.id,
			to: r.profileInfo.userId,
		})
	}
}));
```
```sql
CREATE INDEX idx_profile_info_user_id ON profile_info (user_id);
```


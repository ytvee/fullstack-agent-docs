### One-to-one
Drizzle ORM provides you an API to define `one-to-one` relations between tables with the `defineRelations` function.

An example of a `one-to-one` relation between users and users, where a user can invite another (this example uses a self reference):

```typescript copy {10-17}
import { pgTable, serial, text, boolean } from 'drizzle-orm/pg-core';
import { defineRelations } from 'drizzle-orm';

export const users = pgTable('users', {
	id: integer().primaryKey(),
	name: text(),
	invitedBy: integer('invited_by'),
});

export const relations = defineRelations({ users }, (r) => ({
	users: {
		invitee: r.one.users({
			from: r.users.invitedBy,
			to: r.users.id,
		})
	}
}));
```

Another example would be a user having a profile information stored in separate table. In this case, because the foreign key is stored in the "profile_info" table, the user relation have neither fields or references. This tells Typescript that `user.profileInfo` is nullable:

```typescript copy {15-22}
import { pgTable, serial, text, integer, jsonb } from 'drizzle-orm/pg-core';
import { defineRelations } from 'drizzle-orm';

export const users = pgTable('users', {
	id: integer().primaryKey(),
	name: text(),
});

export const profileInfo = pgTable('profile_info', {
	id: serial().primaryKey(),
	userId: integer('user_id').references(() => users.id),
	metadata: jsonb(),
});

export const relations = defineRelations({ users, profileInfo }, (r) => ({
	users: {
		profileInfo: r.one.profileInfo({
			from: r.users.id,
			to: r.profileInfo.userId,
		})
	}
}));

const user = await db.query.posts.findFirst({ with: { profileInfo: true } });
//____^? type { id: number, profileInfo: { ... } | null  }
```


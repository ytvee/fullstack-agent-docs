### One-to-one
Drizzle ORM provides you an API to define `one-to-one` relations between tables with the `relations` operator.

An example of a `one-to-one` relation between users and users, where a user can invite another (this example uses a self reference):

```typescript copy {10-15}
import { pgTable, serial, text, integer, boolean } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
	invitedBy: integer('invited_by'),
});

export const usersRelations = relations(users, ({ one }) => ({
	invitee: one(users, {
		fields: [users.invitedBy],
		references: [users.id],
	}),
}));
```

Another example would be a user having a profile information stored in separate table. In this case, because the foreign key is stored in the "profile_info" table, the user relation have neither fields or references. This tells Typescript that `user.profileInfo` is nullable:

```typescript copy {9-17}
import { pgTable, serial, text, integer, jsonb } from 'drizzle-orm/pg-core';
import { relations } from 'drizzle-orm';

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
});

export const usersRelations = relations(users, ({ one }) => ({
	profileInfo: one(profileInfo),
}));

export const profileInfo = pgTable('profile_info', {
	id: serial('id').primaryKey(),
	userId: integer('user_id').references(() => users.id),
	metadata: jsonb('metadata'),
});

export const profileInfoRelations = relations(profileInfo, ({ one }) => ({
	user: one(users, { fields: [profileInfo.userId], references: [users.id] }),
}));

const user = await queryUserWithProfileInfo();
//____^? type { id: number, profileInfo: { ... } | null  }
```


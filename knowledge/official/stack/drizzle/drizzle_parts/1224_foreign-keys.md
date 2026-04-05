### Foreign keys

You might've noticed that `relations` look similar to foreign keys — they even have a `references` property. So what's the difference?

While foreign keys serve a similar purpose, defining relations between tables, they work on a different level compared to `relations`.

Foreign keys are a database level constraint, they are checked on every `insert`/`update`/`delete` operation and throw an error if a constraint is violated.
On the other hand, `relations` are a higher level abstraction, they are used to define relations between tables on the application level only.
They do not affect the database schema in any way and do not create foreign keys implicitly.

What this means is `relations` and foreign keys can be used together, but they are not dependent on each other.
You can define `relations` without using foreign keys (and vice versa), which allows them to be used with databases that do not support foreign keys.

The following two examples will work exactly the same in terms of querying the data using Drizzle relational queries.
<CodeTabs items={["schema1.ts", "schema2.ts"]}>
<CodeTab>
```ts {15}
export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
});

export const usersRelations = relations(users, ({ one, many }) => ({
	profileInfo: one(users, {
		fields: [profileInfo.userId],
		references: [users.id],
	}),
}));

export const profileInfo = pgTable('profile_info', {
	id: serial('id').primaryKey(),
	userId: integer("user_id"),
	metadata: jsonb("metadata"),
});
```
</CodeTab>
<CodeTab>
```ts {15}
export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
});

export const usersRelations = relations(users, ({ one, many }) => ({
	profileInfo: one(users, {
		fields: [profileInfo.userId],
		references: [users.id],
	}),
}));

export const profileInfo = pgTable('profile_info', {
	id: serial('id').primaryKey(),
	userId: integer("user_id").references(() => users.id),
	metadata: jsonb("metadata"),
});
```
</CodeTab>
</CodeTabs>


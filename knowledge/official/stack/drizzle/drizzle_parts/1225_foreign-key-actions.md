### Foreign key actions

For more information check the [PostgreSQL foreign keys docs](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK)

You can specify actions that should occur when the referenced data in the parent table is modified. These actions are known as "foreign key actions." PostgreSQL provides several options for these actions.

On Delete/ Update Actions

- `CASCADE`: When a row in the parent table is deleted, all corresponding rows in the child table will also be deleted. This ensures that no orphaned rows exist in the child table.

- `NO ACTION`: This is the default action. It prevents the deletion of a row in the parent table if there are related rows in the child table. The DELETE operation in the parent table will fail.

- `RESTRICT`: Similar to NO ACTION, it prevents the deletion of a parent row if there are dependent rows in the child table. It is essentially the same as NO ACTION and included for compatibility reasons.

- `SET DEFAULT`: If a row in the parent table is deleted, the foreign key column in the child table will be set to its default value if it has one. If it doesn't have a default value, the DELETE operation will fail.

- `SET NULL`: When a row in the parent table is deleted, the foreign key column in the child table will be set to NULL. This action assumes that the foreign key column in the child table allows NULL values.

> Analogous to ON DELETE there is also ON UPDATE which is invoked when a referenced column is changed (updated). The possible actions are the same, except that column lists cannot be specified for SET NULL and SET DEFAULT. In this case, CASCADE means that the updated values of the referenced column(s) should be copied into the referencing row(s).
in drizzle you can add foreign key action using `references()` second argument.

type of the actions

```typescript
export type UpdateDeleteAction = 'cascade' | 'restrict' | 'no action' | 'set null' | 'set default';

// second argument of references interface
actions?: {
		onUpdate?: UpdateDeleteAction;
		onDelete?: UpdateDeleteAction;
	} | undefined
```

In the following example, adding `onDelete: 'cascade'` to the author field on the `posts` schema means that deleting the `user` will also delete all related Post records.


```typescript {11}
import { pgTable, serial, text, integer } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
});

export const posts = pgTable('posts', {
	id: serial('id').primaryKey(),
	name: text('name'),
	author: integer('author').references(() => users.id, {onDelete: 'cascade'}).notNull(),
});
```

For constraints specified with the `foreignKey` operator, foreign key actions are defined with the syntax:

```typescript {18-19}
import { foreignKey, pgTable, serial, text, integer } from 'drizzle-orm/pg-core';

export const users = pgTable('users', {
	id: serial('id').primaryKey(),
	name: text('name'),
});

export const posts = pgTable('posts', {
	id: serial('id').primaryKey(),
	name: text('name'),
	author: integer('author').notNull(),
}, (table) => [
	foreignKey({
		name: "author_fk",
		columns: [table.author],
		foreignColumns: [users.id],
	})
		.onDelete('cascade')
		.onUpdate('cascade')
]);
```


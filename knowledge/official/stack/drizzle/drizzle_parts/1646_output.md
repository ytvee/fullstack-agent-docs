### Output
<IsSupportedChipGroup chips={{ 'MSSQL': true }} />
You can update a row and get back the row before updated and after:

```typescript copy
type User = typeof users.$inferSelect;

const updatedUserId: User[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output();
```

To return partial users after update: 

```ts
const updatedUserId: { inserted: { updatedId: number }}[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output({ inserted: { updatedId: users.id }});
```

To return rows that were in database before update:

```ts
type User = typeof users.$inferSelect;

const updatedUserId: { deleted: User }[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output({ deleted: true });
```

To return both previous and new version on a row:

```ts
type User = typeof users.$inferSelect;

const updatedUserId: { deleted: User, inserted: User }[] = await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'))
  .output({ deleted: true, inserted: true });
```


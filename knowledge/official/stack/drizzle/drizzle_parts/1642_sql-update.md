# SQL Update

```typescript copy
await db.update(users)
  .set({ name: 'Mr. Dan' })
  .where(eq(users.name, 'Dan'));
```

The object that you pass to `update` should have keys that match column names in your database schema.
Values of `undefined` are ignored in the object: to set a column to `null`, pass `null`.
You can pass SQL as a value to be used in the update object, like this:

```typescript copy
await db.update(users)
  .set({ updatedAt: sql`NOW()` })
  .where(eq(users.name, 'Dan'));
```


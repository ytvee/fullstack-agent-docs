# SQL Delete
You can delete all rows in the table:
```typescript copy
await db.delete(users);
```
And you can delete with filters and conditions:
```typescript copy
await db.delete(users).where(eq(users.name, 'Dan'));
```


### Conditional select

You can have a dynamic selection object based on some condition:

```typescript
async function selectUsers(withName: boolean) {
  return db
    .select({
      id: users.id,
      ...(withName ? { name: users.name } : {}),
    })
    .from(users);
}

const users = await selectUsers(true);
```


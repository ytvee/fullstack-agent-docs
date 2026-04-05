#### `where` clauses

`on conflict do update` can have a `where` clause in two different places -
as part of the conflict target (i.e. for partial indexes) or as part of the `update` clause:

```sql
insert into employees (employee_id, name)
values (123, 'John Doe')
on conflict (employee_id) where name <> 'John Doe'
do update set name = excluded.name

insert into employees (employee_id, name)
values (123, 'John Doe')
on conflict (employee_id) do update set name = excluded.name
where name <> 'John Doe';
```

To specify these conditions in Drizzle, you can use `setWhere` and `targetWhere` clauses:

```typescript
await db.insert(employees)
  .values({ employeeId: 123, name: 'John Doe' })
  .onConflictDoUpdate({
    target: employees.employeeId,
    targetWhere: sql`name <> 'John Doe'`,
    set: { name: sql`excluded.name` }
  });

await db.insert(employees)
  .values({ employeeId: 123, name: 'John Doe' })
  .onConflictDoUpdate({
    target: employees.employeeId,
    set: { name: 'John Doe' },
    setWhere: sql`name <> 'John Doe'`
  });
```

<hr />

Upsert with composite indexes, or composite primary keys for `onConflictDoUpdate`:

```typescript
await db.insert(users)
  .values({ firstName: 'John', lastName: 'Doe' })
  .onConflictDoUpdate({
    target: [users.firstName, users.lastName],
    set: { firstName: 'John1' }
  });
```


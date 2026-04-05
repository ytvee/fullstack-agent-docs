### Advanced pagination
Powered by TypeScript, Drizzle APIs let you implement all possible SQL pagination and sorting approaches.

Sneak peek of advanced pagination, for more detailed advanced
usage examples - see our dedicated [limit offset pagination](/docs/guides/limit-offset-pagination)
and [cursor pagination](/docs/guides/cursor-based-pagination) guides.

<CodeTabs items={["example 1", "example 2", "example 3", "example 4"]}>
```ts
await db
  .select()
  .from(users)
  .orderBy(asc(users.id)) // order by is mandatory
  .limit(4) // the number of rows to return
  .offset(4); // the number of rows to skip
```
```ts
const getUsers = async (page = 1, pageSize = 3) => {
  await db.query.users.findMany({
    orderBy: (users, { asc }) => asc(users.id),
    limit: pageSize,
    offset: (page - 1) * pageSize,
  });
};
await getUsers();
```
```ts
const getUsers = async (page = 1, pageSize = 10) => {
   const sq = db
    .select({ id: users.id })
    .from(users)
    .orderBy(users.id)
    .limit(pageSize)
    .offset((page - 1) * pageSize)
    .as('subquery');
   await db.select().from(users).innerJoin(sq, eq(users.id, sq.id)).orderBy(users.id);
};
```
```ts
const nextUserPage = async (cursor?: number, pageSize = 3) => {
  await db
    .select()
    .from(users)
    .where(cursor ? gt(users.id, cursor) : undefined) // if cursor is provided, get rows after it
    .limit(pageSize) // the number of rows to return
    .orderBy(asc(users.id)); // ordering
};
// pass the cursor of the last row of the previous page (id)
await nextUserPage(3);
```
</CodeTabs>


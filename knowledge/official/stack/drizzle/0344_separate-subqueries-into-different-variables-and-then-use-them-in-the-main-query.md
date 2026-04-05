#### Separate subqueries into different variables, and then use them in the main query
```ts
const subquery = db
	.select()
	.from(internalStaff)
	.leftJoin(customUser, eq(internalStaff.userId, customUser.id))
	.as('internal_staff');

const mainQuery = await db
	.select()
	.from(ticket)
	.leftJoin(subquery, eq(subquery.internal_staff.userId, ticket.staffId));
```


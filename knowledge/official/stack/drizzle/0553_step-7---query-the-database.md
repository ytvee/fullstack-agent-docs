#### Step 7 - Query the database

```typescript copy
import { drizzle } from 'drizzle-orm/d1';

export interface Env {
  <BINDING_NAME>: D1Database;
}
export default {
  async fetch(request: Request, env: Env) {
    const db = drizzle(env.<BINDING_NAME>);

    const user: typeof usersTable.$inferInsert = {
      name: 'John',
      age: 30,
      email: 'john@example.com',
    };

    await db.insert(usersTable).values(user);
    console.log('New user created!');

    const users = await db.select().from(usersTable);
    console.log('Getting all users from the database: ', users);
    /*
    const users: {
      id: number;
      name: string;
      age: number;
      email: string;
    }[]
    */

    await db
      .update(usersTable)
      .set({
        age: 31,
      })
      .where(eq(usersTable.email, user.email));
    console.log('User info updated!');

    await db.delete(usersTable).where(eq(usersTable.email, user.email));
    console.log('User deleted!');

    return Response.json(users);
  },
};
```


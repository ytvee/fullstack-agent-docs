#### Create an API endpoint

Use Drizzle in your Encore endpoints:

```typescript copy filename="users.ts"
import { api } from "encore.dev/api";
import { orm } from "./database";
import { users } from "./schema";
import { eq } from "drizzle-orm";

interface User {
  id: number;
  name: string;
  email: string;
}

export const list = api(
  { expose: true, method: "GET", path: "/users" },
  async (): Promise<{ users: User[] }> => {
    const result = await orm.select().from(users);
    return { users: result };
  }
);

export const create = api(
  { expose: true, method: "POST", path: "/users" },
  async (req: { name: string; email: string }): Promise<User> => {
    const [user] = await orm
      .insert(users)
      .values({ name: req.name, email: req.email })
      .returning();
    return user;
  }
);
```


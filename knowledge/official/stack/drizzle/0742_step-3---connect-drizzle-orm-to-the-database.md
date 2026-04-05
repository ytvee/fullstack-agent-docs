#### Step 3 - Connect Drizzle ORM to the database

Create a `App.tsx` file in the root directory and initialize the connection:

```ts
import { open } from '@op-engineering/op-sqlite';
import { drizzle } from 'drizzle-orm/op-sqlite';

const opsqliteDb = open({
  name: 'db',
});

const db = drizzle(opsqliteDb);
```


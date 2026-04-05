#### Step 4 - Connect Drizzle ORM to the database

Create a `App.tsx` file in the root directory and initialize the connection:

```ts
import * as SQLite from 'expo-sqlite';
import { drizzle } from 'drizzle-orm/expo-sqlite';

const expo = SQLite.openDatabaseSync('db.db');

const db = drizzle(expo);
```


#### Add Drizzle extension to your Prisma client

<CodeTabs items={["PostgreSQL", "MySQL", "SQLite"]}>
<CodeTab>
```ts copy
import { PrismaClient } from '@prisma/client';
import { drizzle } from 'drizzle-orm/prisma/pg';

const prisma = new PrismaClient().$extends(drizzle());
```
</CodeTab>
<CodeTab>
```ts copy
import { PrismaClient } from '@prisma/client';
import { drizzle } from 'drizzle-orm/prisma/mysql';

const prisma = new PrismaClient().$extends(drizzle());
```
</CodeTab>
<CodeTab>
```ts copy
import { PrismaClient } from '@prisma/client';
import { drizzle } from 'drizzle-orm/prisma/sqlite';

const prisma = new PrismaClient().$extends(drizzle());
```
</CodeTab>
</CodeTabs>


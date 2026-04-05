#### Step 7 - Applying changes to the database

Generate migrations:
```bash copy
npx drizzle-kit generate
```

You can apply migrations only from Cloudflare Workers. 
To achieve this, let's define the migrate functionality in MyDurableObject:
```ts copy {4-5,17-19}
import { drizzle, type DrizzleSqliteDODatabase } from 'drizzle-orm/durable-sqlite';
import { DurableObject } from 'cloudflare:workers'
import { migrate } from 'drizzle-orm/durable-sqlite/migrator';
import migrations from '../drizzle/migrations';

export class MyDurableObject extends DurableObject {
	storage: DurableObjectStorage;
	db: DrizzleSqliteDODatabase;

	constructor(ctx: DurableObjectState, env: Env) {
		super(ctx, env);
		this.storage = ctx.storage;
		this.db = drizzle(this.storage, { logger: false });
	}

	async migrate() {
		migrate(this.db, migrations);
	}
}
```


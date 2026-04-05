#### Run Drizzle queries via `prisma.$drizzle` ✨

In order to use Drizzle query builder, you need references to Drizzle tables.
You can import them from the output path that you specified in the generator config.

```ts copy
import { User } from './drizzle';

await prisma.$drizzle.insert().into(User).values({ email: 'sorenbs@drizzle.team', name: 'Søren' });
const users = await prisma.$drizzle.select().from(User);
```

</Steps>


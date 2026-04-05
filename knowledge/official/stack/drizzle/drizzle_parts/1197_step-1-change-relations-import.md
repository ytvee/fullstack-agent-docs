##### Step 1: Change relations import

To define relations using Relational Queries v1, you would need to import it from `drizzle-orm`

<Callout type='error' title='v1'>
```ts
import { relations } from 'drizzle-orm';
```
</Callout>

In Relational Queries v2 we moved it to `drizzle-orm/_relations` to give you some time for a migration

<Callout title='v2'>
```ts
import { relations } from "drizzle-orm/_relations";
```
</Callout>


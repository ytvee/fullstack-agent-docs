#### What is working differently from v1

{/* ##### Drizzle Relations schema definition */}

One of the biggest updates were in **Relations Schema definition**

The first difference is that you no longer need to specify `relations` for each table separately in different objects and 
then pass them all to `drizzle()` along with your schema. In Relational Queries v2, you now have one dedicated place to
specify all the relations for all the tables you need. 

The `r` parameter in the callback provides comprehensive autocomplete 
functionality - including all tables from your schema and functions such as `one`, `many`, and `through` - essentially 
offering everything you need to specify your relations.

```ts
// relations.ts
import * as schema from "./schema"
import { defineRelations } from "drizzle-orm"

export const relations = defineRelations(schema, (r) => ({
    ...
}));
```
```ts
// index.ts
import { relations } from "./relations"
import { drizzle } from "drizzle-orm/..."

const db = drizzle(process.env.DATABASE_URL, { relations })
```


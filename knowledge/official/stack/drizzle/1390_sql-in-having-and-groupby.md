## `sql` in having and groupBy

The `sql` template can indeed be used in the HAVING and GROUP BY clauses when you need specific functionality for ordering that is not
available in Drizzle, but you prefer not to resort to raw SQL.

<Section>
```typescript copy
import { sql } from 'drizzle-orm'
import { usersTable } from 'schema'

await db.select({ 
    projectId: usersTable.projectId,
    count: sql<number>`count(${usersTable.id})`.mapWith(Number)
}).from(usersTable)
    .groupBy(sql`${usersTable.projectId}`)
    .having(sql`count(${usersTable.id}) > 300`)
```
```sql
select "project_id", count("users"."id") from users group by "users"."project_id" having count("users"."id") > 300; 
```
</Section>


Source: https://orm.drizzle.team/docs/sustainability

import { Image } from "astro:assets";
import roman from "@/assets/images/core/roman.jpg";
import smm from "@/assets/images/core/smm.jpg";
import group from "@/assets/images/core/group.jpeg";
import alex_sherman from "@/assets/images/core/alex_sherman.jpg";
import reka from "@/assets/images/team/reka.png";
import andrew from "@/assets/images/core/andrew.jpeg";
import blokh from "@/assets/images/core/blokh.jpeg";
import dan from "@/assets/images/core/dan.jpeg";


### Select filters
Just like in our SQL-like query builder, 
relational queries API lets you define filters and conditions with the list of our **[`operators`](/docs/operators)**.  

You can either import them from `drizzle-orm` or use from the callback syntax:
<Section>
```typescript copy
const users = await db.query.users.findMany({
	where: {
		id: 1
	}
});
```
```sql
select * from users where id = 1
```
</Section>

Find post with `id=1` and comments that were created before particular date:
```typescript copy
await db.query.posts.findMany({
  where: {
    id: 1,
  },
  with: {
    comments: {
      where: {
        createdAt: { lt: new Date() },
      },
    },
  },
});
```

**List of all filter operators**
```ts
where: {
    OR: [],
    AND: [],
    NOT: {},
    RAW: (table) => sql`${table.id} = 1`,

    // filter by relations
    [relation]: {},

	  // filter by columns
    [column]: {
      OR: [],
      AND: [],
      NOT: {},
      eq: 1,
      ne: 1,
      gt: 1,
      gte: 1,
      lt: 1,
      lte: 1,
      in: [1],
      notIn: [1],
      like: "",
      ilike: "",
      notLike: "",
      notIlike: "",
      isNull: true,
      isNotNull: true,
      arrayOverlaps: [1, 2],
      arrayContained: [1, 2],
      arrayContains: [1, 2]
    },
},
```

**Examples**
<CodeTabs items={["simple eq", "using AND", "using OR", "using NOT", "complex example using RAW"]}>
<CodeTab>
```ts
const response = db.query.users.findMany({
  where: {
    age: 15,
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name"
from "users" 
where ("users"."age" = 15)
```
</CodeTab>
<CodeTab>
```ts
const response = db.query.users.findMany({
  where: {
    age: 15,
    name: 'John'
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name"
from "users" 
where ("users"."age" = 15 and "users"."name" = 'John')
```
</CodeTab>
<CodeTab>
```ts
const response = await db.query.users.findMany({
  where: {
    OR: [
      {
        id: {
          gt: 10,
        },
      },
	  {
		name: {
          like: "John%",
        },
	  }
    ],
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name" 
from "users" 
where ("users"."id" > 10 or "users"."name" like 'John%')
```
</CodeTab>
<CodeTab>
```ts
const response = db.query.users.findMany({
  where: {
    NOT: {
      id: {
        gt: 10,
      },
    },
    name: {
      like: "John%",
    },
  },
});
```
```sql {3}
select "users"."id" as "id", "users"."name" as "name" 
from "users" 
where (not "users"."id" > 10 and "users"."name" like 'John%')
```
</CodeTab>
<CodeTab>
```ts
// schema.ts
import { integer, jsonb, pgTable, text, timestamp } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: integer("id").primaryKey(),
  name: text("name"),
  email: text("email").notNull(),
  age: integer("age"),
  createdAt: timestamp("created_at").defaultNow(),
  lastLogin: timestamp("last_login"),
  subscriptionEnd: timestamp("subscription_end"),
  lastActivity: timestamp("last_activity"),
  preferences: jsonb("preferences"),      // JSON column for user settings/preferences
  interests: text("interests").array(),     // Array column for user interests
});
```
```ts
const response = db.query.users.findMany({
  where: {
    AND: [
      {
        OR: [
          { RAW: (table) => sql`LOWER(${table.name}) LIKE 'john%'` },
          { name: { ilike: "jane%" } },
        ],
      },
      {
        OR: [
          { RAW: (table) => sql`${table.preferences}->>'theme' = 'dark'` },
          { RAW: (table) => sql`${table.preferences}->>'theme' IS NULL` },
        ],
      },
      { RAW: (table) => sql`${table.age} BETWEEN 25 AND 35` },
    ],
  },
});
```
```sql
select "d0"."id" as "id", "d0"."name" as "name", 
"d0"."email" as "email", "d0"."age" as "age", 
"d0"."created_at" as "createdAt", "d0"."last_login" as "lastLogin", 
"d0"."subscription_end" as "subscriptionEnd", "d0"."last_activity" as "lastActivity", 
"d0"."preferences" as "preferences", "d0"."interests" as "interests" 
from "users" as "d0" 
where ((LOWER("d0"."name") LIKE 'john%' or "d0"."name" ilike 'jane%') 
and ("d0"."preferences"->>'theme' = 'dark' or "d0"."preferences"->>'theme' IS NULL) 
and "d0"."age" BETWEEN 25 AND 35)
```
</CodeTab>
</CodeTabs>


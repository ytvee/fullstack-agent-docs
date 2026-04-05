##### `where` is now object

<Callout title="❌ v1">
```ts
const response = db._query.users.findMany({
  where: (users, { eq }) => eq(users.id, 1),
});
```
</Callout>

<Callout title="✅ v2">
```ts
const response = db.query.users.findMany({
  where: {
    id: 1,
  },
});
```

For a complete API Reference please check our [Select Filters docs](/docs/rqb-v2#select-filters)
</Callout>

<Callout collapsed='Complex filter example using RAW'>
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
</Callout>


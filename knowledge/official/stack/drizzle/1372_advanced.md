### Advanced

There are a few tricks you can use with Drizzle ORM. As long as Drizzle is entirely in TypeScript files, 
you can essentially do anything you would in a simple TypeScript project with your code.

One common feature is to separate columns into different places and then reuse them. 
For example, consider the `updated_at`, `created_at`, and `deleted_at` columns. Many tables/models may need these 
three fields to track and analyze the creation, deletion, and updates of entities in a system

We can define those columns in a separate file and then import and spread them across all the table objects you have

<Section>
```ts
// columns.helpers.ts
const timestamps = {
  updated_at: timestamp(),
  created_at: timestamp().defaultNow().notNull(),
  deleted_at: timestamp(),
}
```
```ts
// users.sql.ts
export const users = pgTable('users', {
  id: integer(),
  ...timestamps
})
```
```ts
// posts.sql.ts
export const posts = pgTable('posts', {
  id: integer(),
  ...timestamps
})
```
</Section>


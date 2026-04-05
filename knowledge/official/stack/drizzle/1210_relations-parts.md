### Relations Parts

In a case you need to separate relations config into several parts you can use `defineRelationsPart` helpers

```ts
import { defineRelations, defineRelationsPart } from 'drizzle-orm';
import * as schema from "./schema";

export const relations = defineRelations(schema, (r) => ({
  users: {
    invitee: r.one.users({
      from: r.users.invitedBy,
      to: r.users.id,
    }),
    posts: r.many.posts(),
  }
}));

export const part = defineRelationsPart(schema, (r) => ({
  posts: {
    author: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
    }),
  }
}));
```

and then you can provide it to the db instance

```ts
const db = drizzle(process.env.DB_URL, { relations: { ...relations, ...part } })
```

<Callout type='warning'>
There are a few rules you would need to follow to make sure it `defineRelationsParts` works as expected

**Rule 1**: If you specify reltions with parts, when passing it to drizzle db function you would need to specify it in the right order(main relations goes first)
```ts
// ✅
const db = drizzle(process.env.DB_URL, { relations: { ...relations, ...part } })

// ❌
const db = drizzle(process.env.DB_URL, { relations: { ...part, ...relations } })
```

<Callout collapsed="Why it's important?">
Even if there will be no type or runtime error, this is how "..." works with objects. As long as main relation 
recursively infer all tables names, so it can be available in autocomplete. Here is an example:

```ts
export const relations = defineRelations(schema, (r) => ({
  users: {
    invitee: r.one.users({
      from: r.users.invitedBy,
      to: r.users.id,
    }),
    posts: r.many.posts(),
  }
}));

export const part = defineRelationsPart(schema, (r) => ({
  posts: {
    author: r.one.users({
      from: r.posts.authorId,
      to: r.users.id,
    }),
  }
}));
```

Here `relations` and `part` can be represented and this object:
```json
// relations
{
  "users": {"invitee": {...}, "posts": {...}},
  // added here, so all tables from schema will exist in autocomplete
  "posts": {}
}

// part
{
  "posts": {"author": {...}}
}
```

Having `{ ...relations, ...part }` will result in 
```json
{
  "users": {"invitee": {...}, "posts": {...}},
  "posts": {"author": {...}}
}
```

and having `{ ...relations, ...part }` will result in
```json
{
  "users": {"invitee": {...}, "posts": {...}},
  // As you can see in the final object, posts relations information will be lost
  "posts": {}
}
```

</Callout>

**Rule 2**: You should have min relations, so drizzle can infer all of the table for autocomplete. If you want to have only parts, then 
one of your parts should be empty, like this:

```ts
export const mainPart = defineRelationsPart(schema);
```

In this case, all tables will be inferred correctly, and you'll have complete information about your schema
</Callout>


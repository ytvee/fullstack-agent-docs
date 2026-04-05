### Advanced filters
In combination with TypeScript, Drizzle APIs provide you powerful and flexible ways to combine filters in queries.

Sneak peek of conditional filtering, for more detailed advanced usage examples - see our [dedicated guide](/docs/guides/conditional-filters-in-query).
<CodeTabs items={["example 1", "example 2"]}>
```ts
const searchPosts = async (term?: string) => {
  await db
    .select()
    .from(posts)
    .where(term ? ilike(posts.title, term) : undefined);
};
await searchPosts();
await searchPosts('AI');
```
```ts
const searchPosts = async (filters: SQL[]) => {
  await db
    .select()
    .from(posts)
    .where(and(...filters));
};
const filters: SQL[] = [];
filters.push(ilike(posts.title, 'AI'));
filters.push(inArray(posts.category, ['Tech', 'Art', 'Science']));
filters.push(gt(posts.views, 200));
await searchPosts(filters);
```
</CodeTabs>


### Find first
<Callout>
  `.findFirst()` will add `limit 1` to the query.
</Callout>
<Section>
```typescript copy
const user = await db._query.users.findFirst();
```
```ts
// result type
const result: {
	id: number;
	name: string;
	verified: boolean;
	invitedBy: number | null;
};
```
</Section>


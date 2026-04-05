### Find many
<Section>
```typescript copy
const users = await db._query.users.findMany();
```
```ts
// result type
const result: {
	id: number;
	name: string;
	verified: boolean;
	invitedBy: number | null;
}[];
```
</Section>


### Find many
<Section>
```typescript copy
const users = await db.query.users.findMany();
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


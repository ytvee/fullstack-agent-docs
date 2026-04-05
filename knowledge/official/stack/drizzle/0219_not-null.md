### Not null
`NOT NULL` constraint dictates that the associated column may not contain a `NULL` value.
<Section>
```typescript
const table = sqliteTable('table', { 
	numInt: integer().notNull() 
});
```

```sql
CREATE TABLE table (
	`numInt` integer NOT NULL
);
```
</Section>


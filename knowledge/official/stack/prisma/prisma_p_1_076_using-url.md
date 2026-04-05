# Using --url
prisma db execute --file ./script.sql --url "$DATABASE_URL"
```

**After (v7):**

```bash
prisma db execute --file ./script.sql
```

The database URL is now read from `prisma.config.ts`.

### `prisma migrate diff` options changed

Several options have been removed and replaced:

| Removed Option             | Replacement                     |
| -------------------------- | ------------------------------- |
| `--from-url`               | `--from-config-datasource`      |
| `--to-url`                 | `--to-config-datasource`        |
| `--from-schema-datasource` | `--from-config-datasource`      |
| `--to-schema-datasource`   | `--to-config-datasource`        |
| `--shadow-database-url`    | Configure in `prisma.config.ts` |

**Before (v6):**

```bash
prisma migrate diff \
  --from-url "$DATABASE_URL" \
  --to-schema schema.prisma \
  --script
```

**After (v7):**

```bash
prisma migrate diff \
  --from-config-datasource \
  --to-schema schema.prisma \
  --script
```

### Migration Action

- Update any scripts or CI pipelines that use `prisma db execute --schema` or `prisma db execute --url`.
- Update any scripts using `prisma migrate diff` with `--from-url`, `--to-url`, `--from-schema-datasource`, `--to-schema-datasource`, or `--shadow-database-url`.
- Configure your database connection in `prisma.config.ts` instead.

---

## Safety Checks & Edge Cases

- **MongoDB provider** detected → stop and recommend staying on Prisma 6 until v7 MongoDB support returns.
- **Multiple entrypoints** (workers, scripts, tests): apply the same client/adapter/dotenv pattern everywhere.
- **Typed SQL** or custom extensions: keep as-is; ensure they compile after client re-generation.
- Preserve existing output path if the project uses custom locations.

---

## 11) Mapped Enum Breaking Change

In Prisma v7, the generated TypeScript enum values now use `@map` values instead of schema names.

### Example

Given this schema:

```prisma
enum SuggestionStatus {
  PENDING  @map("pending")
  ACCEPTED @map("accepted")
  REJECTED @map("rejected")
}
```

**v6 generated enum:**

```ts
export const SuggestionStatus = {
  PENDING: "PENDING",
  ACCEPTED: "ACCEPTED",
  REJECTED: "REJECTED",
} as const;
```

**v7 generated enum:**

```ts
export const SuggestionStatus = {
  PENDING: "pending",
  ACCEPTED: "accepted",
  REJECTED: "rejected",
} as const;
```

### Known Bug (as of v7.2.0)

⚠️ **There is a known bug** where using mapped enum values with Prisma Client operations causes runtime errors. The TypeScript types expect mapped values, but the engine expects schema names. Track this at [GitHub #28591](https://github.com/prisma/prisma/issues/28591).

### Temporary Workarounds

1. **Use schema names as string literals** (causes TS error but works at runtime):

   ```ts
   await prisma.suggestion.create({
     data: {
       status: "PENDING" as any, // Use schema name, not mapped value
     },
   });
   ```

2. **Remove `@map` from enum values** temporarily if you don't strictly need different database values:

   ```prisma
   // Before: with @map directives
   enum SuggestionStatus {
     PENDING  @map("pending")
     ACCEPTED @map("accepted")
     REJECTED @map("rejected")
   }

   // After: without @map directives
   enum SuggestionStatus {
     PENDING
     ACCEPTED
     REJECTED
   }
   ```

   With this change, both the schema names and the database values will be `PENDING`, `ACCEPTED`, and `REJECTED`.

### Migration Action

- Inform users about this breaking change if their schema uses `@map` on enum values.
- Warn about the current bug and suggest workarounds until it's fixed.

---

## Deliverables

- A short **CHANGELOG** summary in the PR body:
  - Dependency bumps and added adapter
  - Schema generator change
  - New `prisma.config.ts`
  - Runtime refactor to adapter + optional Accelerate messaging
  - ESM/TS config updates
  - Seed script updates
  - No automatic removal of Accelerate
  - CLI flag changes (`--schema` and `--url` removal from `db execute`, `migrate diff` option changes)
  - Mapped enum breaking change warning (if applicable)
````



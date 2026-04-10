# QA Mode — Operating Protocol

You write tests and run quality gates. You never write feature code.

## Quality gate sequence

Run in this order. Stop on first failure and report before continuing.

| Gate | Command | Pass condition |
|---|---|---|
| Type check | `npx tsc --noEmit` | Zero errors |
| Lint | `npx eslint .` | Zero errors, zero warnings |
| Format | `npx prettier --check .` | Zero diff |
| Tests | `npx vitest run` | All pass |
| Build | `npx next build` | Successful build |

Output the results as a table before writing any test files.

## Test file placement

```
src/features/[name]/actions.ts   → src/features/[name]/actions.test.ts
src/features/[name]/queries.ts   → src/features/[name]/queries.test.ts
src/features/[name]/components/X.tsx → src/features/[name]/components/X.test.tsx
```

## Server Action test template

Every Server Action must have these three cases:

```typescript
describe('actionName', () => {
  it('returns Unauthorized when not authenticated', async () => {
    vi.mocked(verifySession).mockRejectedValueOnce(new Error('Unauthorized'))
    const result = await actionName(new FormData())
    expect(result).toEqual({ error: 'Unauthorized' })
  })

  it('returns validation error on invalid input', async () => {
    vi.mocked(verifySession).mockResolvedValueOnce(mockSession)
    const formData = new FormData()
    // omit required fields
    const result = await actionName(formData)
    expect(result.error).toBeDefined()
  })

  it('succeeds and revalidates cache on valid input', async () => {
    vi.mocked(verifySession).mockResolvedValueOnce(mockSession)
    vi.mocked(db.resource.create).mockResolvedValueOnce(mockResource)
    const formData = buildValidFormData()
    const result = await actionName(formData)
    expect(result).toEqual({ data: mockResource })
    expect(revalidatePath).toHaveBeenCalledWith('/expected-path')
  })
})
```

## Mock-only these dependencies

Never mock business logic. Only mock:

- Database client (Prisma) via `vi.mock('@/lib/db')`
- Auth session (`verifySession`) via `vi.mock('@/lib/dal')`
- Next.js cache functions (`revalidatePath`, `revalidateTag`) via `vi.mock('next/cache')`

## After all gates pass

Output a commit suggestion:

```
test: add tests for [feature-name] — N tests, N passing
```

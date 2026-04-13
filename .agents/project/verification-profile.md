# Verification Profile

Run checks in this order when the task changes implementation:

1. `npx tsc --noEmit`
2. `npx eslint .`
3. `npx prettier --check .`
4. `npm run build` for structural Next.js changes

To auto-fix formatting issues:

```
npx prettier --write .
```

## When to run each check

| Change type | Checks to run |
|---|---|
| TypeScript source files | `tsc --noEmit`, `eslint .`, `prettier --check .` |
| CSS or markup only | `prettier --check .` |
| Next.js routes, layouts, config | all four, including `npm run build` |
| Docs, skills, or markdown only | `prettier --check .` only |

## Notes

- There is no dedicated test runner in this repository today
- Run only the checks relevant to the touched surface — see table above
- Stop at the first failing check; fix it before running the next one

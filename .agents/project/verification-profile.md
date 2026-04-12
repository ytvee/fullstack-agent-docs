# Verification Profile

Run checks in this order when the task changes implementation:

1. `npx tsc --noEmit`
2. `npx eslint .`
3. `npx prettier --check .`
4. `npm run build` for structural Next.js changes

## Notes

- There is no dedicated test runner in this repository today
- If a task changes only docs, skills, or markdown references, TypeScript and
  ESLint may be unnecessary; still run Prettier checks for touched text files

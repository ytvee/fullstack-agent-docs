# Debug Mode — Operating Protocol

You isolate the root cause and apply the minimal fix.

## Error analysis structure

When given an error, output this before any fix attempt:

```
## Error analysis
Message:    [exact error text]
Location:   [file:line if available]
Hypothesis: [1-2 sentences on root cause]
Fix plan:   [what to change and why]
```

## First checks — in this order

Before reading application code, verify these common Next.js 15 causes:

1. Is Next.js >= 15.2.3? (CVE-2025-29927 — check `package.json`)
2. Are `params` and `searchParams` awaited in every `page.tsx` and `layout.tsx`?
3. Is a `server-only` module imported across a client boundary?
4. Is `fetch()` missing an explicit cache strategy? (Next.js 15 default = no cache)
5. Is `ssr: false` used directly inside a Server Component?
6. Is a Node.js API (`fs`, Prisma) used in Edge Runtime (middleware)?

## Fix discipline

- Never patch a symptom — find the root cause.
- Do not add `// @ts-ignore` or `// eslint-disable` to suppress errors.
- Do not add `try/catch` around a call just to silence an error.
- If the fix requires changing a pattern: flag it as a systemic issue and reference the rule from `.roo/rules/` that was violated.

## After the fix

```bash
npx tsc --noEmit
npx next build
```

Report both results. Do not declare success until both pass.

## If stuck after 2 attempts

Stop. Output:

```
## Stuck after 2 attempts
What I know: [observations]
What I tried: [attempt 1, attempt 2]
What I need: [specific information or file to proceed]
```

## "Fast and Loose" Incremental Checking

TypeScript 3.8 introduces a new compiler option called [`assumeChangesOnlyAffectDirectDependencies`](/tsconfig#assumeChangesOnlyAffectDirectDependencies).
When this option is enabled, TypeScript will avoid rechecking/rebuilding all truly possibly-affected files, and only recheck/rebuild files that have changed as well as files that directly import them.

For example, consider a file `fileD.ts` that imports `fileC.ts` that imports `fileB.ts` that imports `fileA.ts` as follows:

```
fileA.ts <- fileB.ts <- fileC.ts <- fileD.ts
```

In `--watch` mode, a change in `fileA.ts` would typically mean that TypeScript would need to at least re-check `fileB.ts`, `fileC.ts`, and `fileD.ts`.
Under [`assumeChangesOnlyAffectDirectDependencies`](/tsconfig#assumeChangesOnlyAffectDirectDependencies), a change in `fileA.ts` means that only `fileA.ts` and `fileB.ts` need to be re-checked.

In a codebase like Visual Studio Code, this reduced rebuild times for changes in certain files from about 14 seconds to about 1 second.
While we don't necessarily recommend this option for all codebases, you might be interested if you have an extremely large codebase and are willing to defer full project errors until later (e.g. a dedicated build via a `tsconfig.fullbuild.json` or in CI).

For more details, you can [see the original pull request](https://github.com/microsoft/TypeScript/pull/35711).

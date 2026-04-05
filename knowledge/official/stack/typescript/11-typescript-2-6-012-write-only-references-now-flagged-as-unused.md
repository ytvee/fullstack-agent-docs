## Write-only references now flagged as unused

TypeScript 2.6 adds revised implementation the [`noUnusedLocals`](/tsconfig#noUnusedLocals) and [`noUnusedParameters`](/tsconfig#noUnusedParameters) [compiler options](/docs/handbook/compiler-options.html).
Declarations are only written to but never read from are now flagged as unused.

## `es2020` for `target` and `module`

TypeScript 3.8 supports `es2020` as an option for `module` and [`target`](/tsconfig#target).
This will preserve newer ECMAScript 2020 features like optional chaining, nullish coalescing, `export * as ns`, and dynamic `import(...)` syntax.
It also means `bigint` literals now have a stable [`target`](/tsconfig#target) below `esnext`.

## New `--declarationMap`

Enabling [`declarationMap`](/tsconfig#declarationMap) alongside [`declaration`](/tsconfig#declaration) causes the compiler to emit `.d.ts.map` files alongside the output `.d.ts` files.
Language Services can also now understand these map files, and uses them to map declaration-file based definition locations to their original source, when available.

In other words, hitting go-to-definition on a declaration from a `.d.ts` file generated with [`declarationMap`](/tsconfig#declarationMap) will take you to the source file (`.ts`) location where that declaration was defined, and not to the `.d.ts`.

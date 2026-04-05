## Speed Improvements in `build` mode with `--noEmitOnError`

Previously, compiling a program after a previous compile with errors under [`incremental`](/tsconfig#incremental) would be extremely slow when using the [`noEmitOnError`](/tsconfig#noEmitOnError) flag.
This is because none of the information from the last compilation would be cached in a `.tsbuildinfo` file based on the [`noEmitOnError`](/tsconfig#noEmitOnError) flag.

TypeScript 4.0 changes this which gives a great speed boost in these scenarios, and in turn improves `--build` mode scenarios (which imply both [`incremental`](/tsconfig#incremental) and [`noEmitOnError`](/tsconfig#noEmitOnError)).

For details, [read up more on the pull request](https://github.com/microsoft/TypeScript/pull/38853).

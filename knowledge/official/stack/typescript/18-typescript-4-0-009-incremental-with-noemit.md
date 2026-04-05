## `--incremental` with `--noEmit`

TypeScript 4.0 allows us to use the [`noEmit`](/tsconfig#noEmit) flag while still leveraging [`incremental`](/tsconfig#incremental) compiles.
This was previously not allowed, as [`incremental`](/tsconfig#incremental) needs to emit a `.tsbuildinfo` files; however, the use-case to enable faster incremental builds is important enough to enable for all users.

For more details, you can [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/39122).

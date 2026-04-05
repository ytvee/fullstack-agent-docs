## The `transpileDeclaration` API

TypeScript's API exposes a function called `transpileModule`.
It's intended to make it easy to compile a single file of TypeScript code.
Because it doesn't have access to an entire *program*, the caveat is that it may not produce the right output if the code violates any errors under the `isolatedModules` option.

In TypeScript 5.5, we've added a new similar API called `transpileDeclaration`.
This API is similar to `transpileModule`, but it's specifically designed to generate a single *declaration file* based on some input source text.
Just like `transpileModule`, it doesn't have access to a full program, and a similar caveat applies: it only generates an accurate declaration file if the input code is free of errors under the new `isolatedDeclarations` option.

If desired, this function can be used to parallelize declaration emit across all files under `isolatedDeclarations` mode.

For more information, [see the implementation here](https://github.com/microsoft/TypeScript/pull/58261).

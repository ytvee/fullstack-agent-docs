### Skipped Checking in `transpileModule` and `transpileDeclaration`

TypeScript's `transpileModule` API can be used for compiling a single TypeScript file's contents into JavaScript.
Similarly, the `transpileDeclaration` API (see below) can be used to generate a declaration file for a single TypeScript file.
One of the issues with these APIs is that TypeScript internally would perform a full type-checking pass over the entire contents of the file before emitting the output.
This was necessary to collect certain information which would later be used for the emit phase.

In TypeScript 5.5, we've found a way to avoid performing a full check, only lazily collecting this information as necessary, and `transpileModule` and `transpileDeclaration` both enable this functionality by default.
As a result, tools that integrate with these APIs, like [ts-loader](https://www.npmjs.com/package/ts-loader) with `transpileOnly` and [ts-jest](https://www.npmjs.com/package/ts-jest), should see a noticeable speedup.
In our testing, [we generally witness around a 2x speed-up in build time using `transpileModule`](https://github.com/microsoft/TypeScript/pull/58364#issuecomment-2138580690).

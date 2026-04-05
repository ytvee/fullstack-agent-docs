### Simplified Reference Directive Declaration Emit

When producing a declaration file, TypeScript would synthesize a reference directive when it believed one was required.
For example, all Node.js modules are declared ambiently, so cannot be loaded by module resolution alone.
A file like:

```tsx
import path from "path";
export const myPath = path.parse(__filename);
```

Would emit a declaration file like:

```tsx
/// <reference types="node" />
import path from "path";
export declare const myPath: path.ParsedPath;
```

Even though the reference directive never appeared in the original source.

Similarly, TypeScript also *removed* reference directives that it did not believe needed to be a part of the output.
For example, let's imagine we had a reference directive to `jest`;
however, imagine the reference directive isn't necessary to generate the declaration file.
TypeScript would simply drop it.
So in the following example:

```tsx
/// <reference types="jest" />
import path from "path";
export const myPath = path.parse(__filename);
```

TypeScript would still emit:

```tsx
/// <reference types="node" />
import path from "path";
export declare const myPath: path.ParsedPath;
```

In the course of working on `isolatedDeclarations`, we realized that this logic was untenable for anyone attempting to implement a declaration emitter without type checking or using more than a single file's context.
This behavior is also hard to understand from a user's perspective; whether or not a reference directive appeared in the emitted file seems inconsistent and difficult to predict unless you understand exactly what's going on during typechecking.
To prevent declaration emit from being different when `isolatedDeclarations` was enabled, we knew that our emit needed to change.

Through [experimentation](https://github.com/microsoft/TypeScript/pull/57569), we found that nearly all cases where TypeScript synthesized reference directives were just to pull in `node` or `react`.
These are cases where the expectation is that a downstream user already references those types through tsconfig.json `"types"` or library imports, so no longer synthesizing these reference directives would be unlikely to break anyone.
It's worth noting that this is already how it works for `lib.d.ts`; TypeScript doesn't synthesize a reference to `lib="es2015"` when a module exports a `WeakMap`, instead assuming that a downstream user will have included that as part of their environment.

For reference directives that had been written by library authors (not synthesized), [further experimentation](https://github.com/microsoft/TypeScript/pull/57656) showed that nearly all were removed, never showing up in the output.
Most reference directives that were preserved were broken and likely not intended to be preserved.

Given those results, we decided to greatly simplfy reference directives in declaration emit in TypeScript 5.5.
A more consistent strategy will help library authors and consumers have better control of their declaration files.

Reference directives are no longer synthesized.
User-written reference directives are no longer preserved, unless annotated with a new `preserve="true"` attribute.
Concretely, an input file like:

```tsx
/// <reference types="some-lib" preserve="true" />
/// <reference types="jest" />
import path from "path";
export const myPath = path.parse(__filename);
```

will emit:

```tsx
/// <reference types="some-lib" preserve="true" />
import path from "path";
export declare const myPath: path.ParsedPath;
```

Adding `preserve="true"` is backwards compatible with older versions of TypeScript as unknown attributes are ignored.

This change also improved performance; in our benchmarks, the emit stage saw a 1-4% improvement in projects with declaration emit enabled.

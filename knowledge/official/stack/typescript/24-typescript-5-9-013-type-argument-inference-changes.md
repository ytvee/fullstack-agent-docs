## Type Argument Inference Changes

In an effort to fix "leaks" of type variables during inference, TypeScript 5.9 may introduce changes in types and possibly new errors in some codebases.
These are hard to predict, but can often be fixed by adding type arguments to generic functions calls.
[See more details here](https://github.com/microsoft/TypeScript/pull/61668).

### Implicit returns

Functions with code paths that do not return a value in JS implicitly return `undefined`.
These can now be flagged by the compiler as implicit returns.
The check is turned _off_ by default; use [`noImplicitReturns`](/tsconfig#noImplicitReturns) to turn it on.

## User-defined type guard functions

TypeScript 1.6 adds a new way to narrow a variable type inside an `if` block, in addition to `typeof` and `instanceof`.
A user-defined type guard functions is one with a return type annotation of the form `x is T`, where `x` is a declared parameter in the signature, and `T` is any type.
When a user-defined type guard function is invoked on a variable in an `if` block, the type of the variable will be narrowed to `T`.

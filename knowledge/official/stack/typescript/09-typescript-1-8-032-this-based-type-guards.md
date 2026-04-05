## `this`-based type guards

TypeScript 1.8 extends [user-defined type guard functions](./typescript-1.6.html#user-defined-type-guard-functions) to class and interface methods.

`this is T` is now valid return type annotation for methods in classes and interfaces.
When used in a type narrowing position (e.g. `if` statement), the type of the call expression target object would be narrowed to `T`.

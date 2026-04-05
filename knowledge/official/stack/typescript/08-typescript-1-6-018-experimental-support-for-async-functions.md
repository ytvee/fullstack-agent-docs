## Experimental support for `async` functions

TypeScript 1.6 introduces experimental support of `async` functions when targeting ES6.
Async functions are expected to invoke an asynchronous operation and await its result without blocking normal execution of the program.
This accomplished through the use of an ES6-compatible `Promise` implementation, and transposition of the function body into a compatible form to resume execution when the awaited asynchronous operation completes.

An _async function_ is a function or method that has been prefixed with the `async` modifier. This modifier informs the compiler that function body transposition is required, and that the keyword `await` should be treated as a unary expression instead of an identifier.
An _Async Function_ must provide a return type annotation that points to a compatible `Promise` type. Return type inference can only be used if there is a globally defined, compatible `Promise` type.

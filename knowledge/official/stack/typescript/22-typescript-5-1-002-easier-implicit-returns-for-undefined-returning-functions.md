## Easier Implicit Returns for `undefined`-Returning Functions

In JavaScript, if a function finishes running without hitting a `return`, it returns the value `undefined`.

```ts
function foo() {
    // no return
}
// x = undefined
let x = foo();
```

However, in previous versions of TypeScript, the *only* functions that could have absolutely no return statements were `void`- and `any`-returning functions.
That meant that even if you explicitly said "this function returns `undefined`" you were forced to have at least one return statement.

```ts
// ✅ fine - we inferred that 'f1' returns 'void'
function f1() {
    // no returns
}
// ✅ fine - 'void' doesn't need a return statement
function f2(): void {
    // no returns
}
// ✅ fine - 'any' doesn't need a return statement
function f3(): any {
    // no returns
}
// ❌ error!
// A function whose declared type is neither 'void' nor 'any' must return a value.
function f4(): undefined {
    // no returns
}
```

This could be a pain if some API expected a function returning `undefined` - you would need to have either at least one explicit return of `undefined` or a `return` statement *and* an explicit annotation.

```ts
declare function takesFunction(f: () => undefined): undefined;
// ❌ error!
// Argument of type '() => void' is not assignable to parameter of type '() => undefined'.
takesFunction(() => {
    // no returns
});
// ❌ error!
// A function whose declared type is neither 'void' nor 'any' must return a value.
takesFunction((): undefined => {
    // no returns
});
// ❌ error!
// Argument of type '() => void' is not assignable to parameter of type '() => undefined'.
takesFunction(() => {
    return;
});
// ✅ works
takesFunction(() => {
    return undefined;
});
// ✅ works
takesFunction((): undefined => {
    return;
});
```

This behavior was frustrating and confusing, especially when calling functions outside of one's control.
Understanding the interplay between inferring `void` over `undefined`, whether an `undefined`-returning function needs a `return` statement, etc. seems like a distraction.

First, TypeScript 5.1 now allows `undefined`-returning functions to have no return statement.

```ts
// ✅ Works in TypeScript 5.1!
function f4(): undefined {
    // no returns
}
// ✅ Works in TypeScript 5.1!
takesFunction((): undefined => {
    // no returns
});
```

Second, if a function has no return expressions and is being passed to something expecting a function that returns `undefined`, TypeScript infers `undefined` for that function's return type.

```ts
// ✅ Works in TypeScript 5.1!
takesFunction(function f() {
    //                 ^ return type is undefined
    // no returns
});
// ✅ Works in TypeScript 5.1!
takesFunction(function f() {
    //                 ^ return type is undefined
    return;
});
```

To address another similar pain-point, under TypeScript's `--noImplicitReturns` option, functions returning *only* `undefined` now have a similar exception to `void`, in that not every single code path must end in an explicit `return`.

```ts
// ✅ Works in TypeScript 5.1 under '--noImplicitReturns'!
function f(): undefined {
    if (Math.random()) {
        // do some stuff...
        return;
    }
}
```

For more information, you can read up on [the original issue](https://github.com/microsoft/TypeScript/issues/36288) and [the implementing pull request](https://github.com/microsoft/TypeScript/pull/53607).

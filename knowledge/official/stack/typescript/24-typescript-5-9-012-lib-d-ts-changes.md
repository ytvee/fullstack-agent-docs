### `lib.d.ts` Changes

Types generated for the DOM may have an impact on type-checking your codebase.

Additionally, one notable change is that `ArrayBuffer` has been changed in such a way that it is no longer a supertype of several different `TypedArray` types.
This also includes subtypes of `UInt8Array`, such as `Buffer` from Node.js.
As a result, you'll see new error messages such as:

```
error TS2345: Argument of type 'ArrayBufferLike' is not assignable to parameter of type 'BufferSource'.
error TS2322: Type 'ArrayBufferLike' is not assignable to type 'ArrayBuffer'.
error TS2322: Type 'Buffer' is not assignable to type 'Uint8Array<ArrayBufferLike>'.
error TS2322: Type 'Buffer' is not assignable to type 'ArrayBuffer'.
error TS2345: Argument of type 'Buffer' is not assignable to parameter of type 'string | Uint8Array<ArrayBufferLike>'.
```

If you encounter issues with `Buffer`, you may first want to check that you are using the latest version of the `@types/node` package.
This might include running

```
npm update @types/node --save-dev
```

Much of the time, the solution is to specify a more specific underlying buffer type instead of using the default `ArrayBufferLike` (i.e. explicitly writing out `Uint8Array<ArrayBuffer>` rather than a plain `Uint8Array`).
In instances where some `TypedArray` (like `Uint8Array`) is passed to a function expecting an `ArrayBuffer` or `SharedArrayBuffer`, you can also try accessing the `buffer` property of that `TypedArray` like in the following example:

```diff
  let data = new Uint8Array([0, 1, 2, 3, 4]);
- someFunc(data)
+ someFunc(data.buffer)
```

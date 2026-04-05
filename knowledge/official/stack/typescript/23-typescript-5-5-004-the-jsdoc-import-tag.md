## The JSDoc `@import` Tag

Today, if you want to import something only for type-checking in a JavaScript file, it is cumbersome.
JavaScript developers can't simply import a type named `SomeType` if it's not there at runtime.

```js
// ./some-module.d.ts
export interface SomeType {
    // ...
}

// ./index.js
import { SomeType } from "./some-module"; // ❌ runtime error!

/**
 * @param {SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

`SomeType` won't exist at runtime, so the import will fail.
Developers can instead use a namespace import instead.

```js
import * as someModule from "./some-module";

/**
 * @param {someModule.SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

But `./some-module` is still imported at runtime - which might also not be desirable.

To avoid this, developers typically had to use `import(...)` types in JSDoc comments.

```js
/**
 * @param {import("./some-module").SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

If you wanted to reuse the same type in multiple places, you could use a `typedef` to avoid repeating the import.

```js
/**
 * @typedef {import("./some-module").SomeType} SomeType
 */

/**
 * @param {SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

This helps with local uses of `SomeType`, but it gets repetitive for many imports and can be a bit verbose.

That's why TypeScript now supports a new `@import` comment tag that has the same syntax as ECMAScript imports.

```js
/** @import { SomeType } from "some-module" */

/**
 * @param {SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

Here, we used named imports.
We could also have written our import as a namespace import.

```js
/** @import * as someModule from "some-module" */

/**
 * @param {someModule.SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

Because these are just JSDoc comments, they don't affect runtime behavior at all.

We would like to extend a big thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) who contributed [this change](https://github.com/microsoft/TypeScript/pull/57207)!

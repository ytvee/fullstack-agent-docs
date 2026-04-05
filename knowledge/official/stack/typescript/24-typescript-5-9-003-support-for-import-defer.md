## Support for `import defer`

TypeScript 5.9 introduces support for [ECMAScript's deferred module evaluation proposal](https://github.com/tc39/proposal-defer-import-eval/) using the new `import defer` syntax.
This feature allows you to import a module without immediately executing the module and its dependencies, providing better control over when work and side-effects occur.

The syntax only permits namespace imports:

```ts
import defer * as feature from "./some-feature.js";
```

The key benefit of `import defer` is that the module is only evaluated when one of its exports is first accessed.
Consider this example:

```ts
// ./some-feature.ts
initializationWithSideEffects();

function initializationWithSideEffects() {
  // ...
  specialConstant = 42;

  console.log("Side effects have occurred!");
}

export let specialConstant: number;
```

When using `import defer`, the `initializationWithSideEffects()` function will not be called until you actually access a property of the imported namespace:

```ts
import defer * as feature from "./some-feature.js";

// No side effects have occurred yet

// ...

// As soon as `specialConstant` is accessed, the contents of the `feature`
// module are run and side effects have taken place.
console.log(feature.specialConstant); // 42
```

Because evaluation of the module is deferred until you access a member off of the module, you cannot use named imports or default imports with `import defer`:

```ts
// ❌ Not allowed
import defer { doSomething } from "some-module";

// ❌ Not allowed  
import defer defaultExport from "some-module";

// ✅ Only this syntax is supported
import defer * as feature from "some-module";
```

Note that when you write `import defer`, the module and its dependencies are fully loaded and ready for execution.
That means that the module will need to exist, and will be loaded from the file system or a network resource.
The key difference between a regular `import` and `import defer` is that *the execution of statements and declarations* is deferred until you access a property of the imported namespace.

This feature is particularly useful for conditionally loading modules with expensive or platform-specific initialization. It can also improve startup performance by deferring module evaluation for app features until they are actually needed.

Note that `import defer` is not transformed or "downleveled" at all by TypeScript.
It is intended to be used in runtimes that support the feature natively, or by tools such as bundlers that can apply the appropriate transformation.
That means that `import defer` will only work under the `--module` modes `preserve` and `esnext`.

We'd like to extend our thanks to [Nicolò Ribaudo](https://github.com/nicolo-ribaudo) who championed the proposal in TC39 and also provided [the implementation for this feature](https://github.com/microsoft/TypeScript/pull/60757).

## resolution-mode

With Node's ECMAScript resolution, the mode of the containing file and the syntax you use determines how imports are resolved;
however it would be useful to reference the types of a CommonJS module from an ECMAScript module, or vice-versa.

TypeScript now allows `/// <reference types="..." />` directives.

```ts
/// <reference types="pkg" resolution-mode="require" />

// or

/// <reference types="pkg" resolution-mode="import" />
```

Additionally, in nightly versions of TypeScript, `import type` can specify an import assertion to achieve something similar.

```ts
// Resolve `pkg` as if we were importing with a `require()`
import type { TypeFromRequire } from "pkg" assert {
    "resolution-mode": "require"
};

// Resolve `pkg` as if we were importing with an `import`
import type { TypeFromImport } from "pkg" assert {
    "resolution-mode": "import"
};

export interface MergedType extends TypeFromRequire, TypeFromImport {}
```

These import assertions can also be used on `import()` types.

```ts
export type TypeFromRequire =
    import("pkg", { assert: { "resolution-mode": "require" } }).TypeFromRequire;

export type TypeFromImport =
    import("pkg", { assert: { "resolution-mode": "import" } }).TypeFromImport;

export interface MergedType extends TypeFromRequire, TypeFromImport {}
```

The `import type` and `import()` syntaxes only support `resolution-mode` in [nightly builds of TypeScript](https://www.typescriptlang.org/docs/handbook/nightly-builds.html).
You'll likely get an error like

```
Resolution mode assertions are unstable. Use nightly TypeScript to silence this error. Try updating with 'npm install -D typescript@next'.
```

If you do find yourself using this feature in nightly versions of TypeScript, [consider providing feedback on this issue](https://github.com/microsoft/TypeScript/issues/49055).

You can see the respective changes [for reference directives](https://github.com/microsoft/TypeScript/pull/47732) and [for type import assertions](https://github.com/microsoft/TypeScript/pull/47807).

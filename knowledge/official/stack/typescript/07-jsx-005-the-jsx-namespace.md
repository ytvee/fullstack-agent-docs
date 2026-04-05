### The `JSX` namespace

JSX in TypeScript is typed by the `JSX` namespace. The `JSX` namespace may be defined in various places, depending on the `jsx` compiler option.

The `jsx` options `preserve`, `react`, and `react-native` use the type definitions for classic runtime. This means a variable needs to be in scope that’s determined by the `jsxFactory` compiler option. The `JSX` namespace should be specified on the top-most identifier of the JSX factory. For example, React uses the default factory `React.createElement`. This means its `JSX` namespace should be defined as `React.JSX`.

```ts
export function createElement(): any;

export namespace JSX {
  // …
}
```

And the user should always import React as `React`.

```ts
import * as React from 'react';
```

Preact uses the JSX factory `h`. That means its types should be defined as the `h.JSX`.

```ts
export function h(props: any): any;

export namespace h.JSX {
  // …
}
```

The user should use a named import to import `h`.

```ts
import { h } from 'preact';
```

For the `jsx` options `react-jsx` and `react-jsxdev`, the `JSX` namespace should be exported from the matching entry points. For `react-jsx` this is `${jsxImportSource}/jsx-runtime`. For `react-jsxdev`, this is `${jsxImportSource}/jsx-dev-runtime`. Since these don’t use a file extension, you must use the [`exports`](https://nodejs.org/api/packages.html#exports) field in `package.json` map in order to support ESM users.

```json 
{
  "exports": {
    "./jsx-runtime": "./jsx-runtime.js",
    "./jsx-dev-runtime": "./jsx-dev-runtime.js",
  }
}
```

Then in `jsx-runtime.d.ts` and `jsx-dev-runtime.d.ts`:

```ts
export namespace JSX {
  // …
}
```

Note that while exporting the `JSX` namespace is sufficient for type checking, the production runtime needs the `jsx`, `jsxs`, and `Fragment` exports at runtime, and the development runtime needs `jsxDEV` and `Fragment`. Ideally you add types for those too.

If the `JSX` namespace isn’t available in the appropriate location, both the classic and the automatic runtime fall back to the global `JSX` namespace.

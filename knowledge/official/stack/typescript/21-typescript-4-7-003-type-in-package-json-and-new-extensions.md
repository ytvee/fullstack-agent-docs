### `type` in `package.json` and New Extensions

Node.js supports [a new setting in `package.json`](https://nodejs.org/api/packages.html#packages_package_json_and_file_extensions) called `type`.
`"type"` can be set to either `"module"` or `"commonjs"`.

```jsonc
{
    "name": "my-package",
    "type": "module",

    "//": "...",
    "dependencies": {
    }
}
```

This setting controls whether `.js` and `.d.ts` files are interpreted as ES modules or CommonJS modules, and defaults to CommonJS when not set.
When a file is considered an ES module, a few different rules come into play compared to CommonJS:

* `import`/`export` statements can be used.
* Top-level `await` can be used
* Relative import paths need full extensions (we have to write `import "./foo.js"` instead of `import "./foo"`).
* Imports might resolve differently from dependencies in `node_modules`.
* Certain global-like values like `require` and `module` cannot be used directly.
* CommonJS modules get imported under certain special rules.

We'll come back to some of these.

To overlay the way TypeScript works in this system, `.ts` and `.tsx` files now work the same way.
When TypeScript finds a `.ts`, `.tsx`, `.js`, or `.jsx` file, it will walk up looking for a `package.json` to see whether that file is an ES module, and use that to determine:

* how to find other modules which that file imports
* and how to transform that file if producing outputs

When a `.ts` file is compiled as an ES module, ECMAScript `import`/`export` statements are left alone in the `.js` output;
when it's compiled as a CommonJS module, it will produce the same output you get today under `--module commonjs`.

This also means paths resolve differently between `.ts` files that are ES modules and ones that are CJS modules.
For example, let's say you have the following code today:

```ts
// ./foo.ts
export function helper() {
    // ...
}

// ./bar.ts
import { helper } from "./foo"; // only works in CJS

helper();
```

This code works in CommonJS modules, but will fail in ES modules because relative import paths need to use extensions.
As a result, it will have to be rewritten to use the extension of the *output* of `foo.ts` - so `bar.ts` will instead have to import from `./foo.js`.

```ts
// ./bar.ts
import { helper } from "./foo.js"; // works in ESM & CJS

helper();
```

This might feel a bit cumbersome at first, but TypeScript tooling like auto-imports and path completion will typically just do this for you.

One other thing to mention is the fact that this applies to `.d.ts` files too.
When TypeScript finds a `.d.ts` file in a package, it is interpreted based on the containing package.

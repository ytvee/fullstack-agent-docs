### `package.json` Exports, Imports, and Self-Referencing

Node.js supports [a new field for defining entry points in `package.json` called `"exports"`](https://nodejs.org/api/packages.html#packages_exports).
This field is a more powerful alternative to defining `"main"` in `package.json`, and can control what parts of your package are exposed to consumers.

Here's a `package.json` that supports separate entry-points for CommonJS and ESM:

```jsonc
// package.json
{
    "name": "my-package",
    "type": "module",
    "exports": {
        ".": {
            // Entry-point for `import "my-package"` in ESM
            "import": "./esm/index.js",

            // Entry-point for `require("my-package") in CJS
            "require": "./commonjs/index.cjs",
        },
    },

    // CJS fall-back for older versions of Node.js
    "main": "./commonjs/index.cjs",
}
```

There's a lot to this feature, [which you can read more about on the Node.js documentation](https://nodejs.org/api/packages.html).
Here we'll try to focus on how TypeScript supports it.

With TypeScript's original Node support, it would look for a `"main"` field, and then look for declaration files that corresponded to that entry.
For example, if `"main"` pointed to `./lib/index.js`, TypeScript would look for a file called `./lib/index.d.ts`.
A package author could override this by specifying a separate field called `"types"` (e.g. `"types": "./types/index.d.ts"`).

The new support works similarly with [import conditions](https://nodejs.org/api/packages.html).
By default, TypeScript overlays the same rules with import conditions - if you write an `import` from an ES module, it will look up the `import` field, and from a CommonJS module, it will look at the `require` field.
If it finds them, it will look for a corresponding declaration file.
If you need to point to a different location for your type declarations, you can add a `"types"` import condition.

```jsonc
// package.json
{
    "name": "my-package",
    "type": "module",
    "exports": {
        ".": {
            // Entry-point for `import "my-package"` in ESM
            "import": {
                // Where TypeScript will look.
                "types": "./types/esm/index.d.ts",

                // Where Node.js will look.
                "default": "./esm/index.js"
            },
            // Entry-point for `require("my-package") in CJS
            "require": {
                // Where TypeScript will look.
                "types": "./types/commonjs/index.d.cts",

                // Where Node.js will look.
                "default": "./commonjs/index.cjs"
            },
        }
    },

    // Fall-back for older versions of TypeScript
    "types": "./types/index.d.ts",

    // CJS fall-back for older versions of Node.js
    "main": "./commonjs/index.cjs"
}
```

> The `"types"` condition should always come first in `"exports"`.

It's important to note that the CommonJS entrypoint and the ES module entrypoint each needs its own declaration file, even if the contents are the same between them.
Every declaration file is interpreted either as a CommonJS module or as an ES module, based on its file extension and the `"type"` field of the `package.json`, and this detected module kind must match the module kind that Node will detect for the corresponding JavaScript file for type checking to be correct.
Attempting to use a single `.d.ts` file to type both an ES module entrypoint and a CommonJS entrypoint will cause TypeScript to think only one of those entrypoints exists, causing compiler errors for users of the package.

TypeScript also supports [the `"imports"` field of `package.json`](https://nodejs.org/api/packages.html#packages_imports) in a similar manner by looking for declaration files alongside corresponding files, and supports [packages self-referencing themselves](https://nodejs.org/api/packages.html#packages_self_referencing_a_package_using_its_name).
These features are generally not as involved to set up, but are supported.

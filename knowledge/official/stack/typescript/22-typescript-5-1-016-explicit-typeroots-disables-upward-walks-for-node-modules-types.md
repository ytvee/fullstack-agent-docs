### Explicit `typeRoots` Disables Upward Walks for `node_modules/@types`

Previously, when the `typeRoots` option was specified in a `tsconfig.json` but resolution to any `typeRoots` directories had failed, TypeScript would still continue walking up parent directories, trying to resolve packages within each parent's `node_modules/@types` folder.

This behavior could prompt excessive look-ups and has been disabled in TypeScript 5.1.
As a result, you may begin to see errors like the following based on entries in your `tsconfig.json`'s `types` option or `/// <reference >` directives

```
error TS2688: Cannot find type definition file for 'node'.
error TS2688: Cannot find type definition file for 'mocha'.
error TS2688: Cannot find type definition file for 'jasmine'.
error TS2688: Cannot find type definition file for 'chai-http'.
error TS2688: Cannot find type definition file for 'webpack-env"'.
```

The solution is typically to add specific entries for `node_modules/@types` to your `typeRoots`:

```jsonc
{
    "compilerOptions": {
        "types": [
            "node",
            "mocha"
        ],
        "typeRoots": [
            // Keep whatever you had around before.
            "./some-custom-types/",
            // You might need your local 'node_modules/@types'.
            "./node_modules/@types",
            // You might also need to specify a shared 'node_modules/@types'
            // if you're using a "monorepo" layout.
            "../../node_modules/@types",
        ]
    }
}
```

More information is available [on the original change on our issue tracker](https://github.com/microsoft/TypeScript/pull/51715).

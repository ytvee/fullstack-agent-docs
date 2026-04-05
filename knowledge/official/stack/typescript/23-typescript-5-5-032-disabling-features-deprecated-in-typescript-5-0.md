### Disabling Features Deprecated in TypeScript 5.0

TypeScript 5.0 deprecated the following options and behaviors:

* `charset`
* `target: ES3`
* `importsNotUsedAsValues`
* `noImplicitUseStrict`
* `noStrictGenericChecks`
* `keyofStringsOnly`
* `suppressExcessPropertyErrors`
* `suppressImplicitAnyIndexErrors`
* `out`
* `preserveValueImports`
* `prepend` in project references
* implicitly OS-specific `newLine`

To continue using the deprecated options above, developers using TypeScript 5.0 and other more recent versions have had to specify a new option called `ignoreDeprecations` with the value `"5.0"`.

In TypeScript 5.5, these options no longer have any effect.
To help with a smooth upgrade path, you may still specify them in your tsconfig, but these will be an error to specify in TypeScript 6.0.
See also the [Flag Deprecation Plan](https://github.com/microsoft/TypeScript/issues/51000) which outlines our deprecation strategy.

[More information around these deprecation plans is available on GitHub](https://github.com/microsoft/TypeScript/issues/51909), which contains suggestions in how to best adapt your codebase.

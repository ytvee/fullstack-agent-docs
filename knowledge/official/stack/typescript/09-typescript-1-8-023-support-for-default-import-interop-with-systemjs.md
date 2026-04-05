## Support for `default` import interop with SystemJS

Module loaders like SystemJS wrap CommonJS modules and expose them as a `default` ES6 import. This makes it impossible to share the definition files between the SystemJS and CommonJS implementation of the module as the module shape looks different based on the loader.

Setting the new compiler flag [`allowSyntheticDefaultImports`](/tsconfig#allowSyntheticDefaultImports) indicates that the module loader performs some kind of synthetic default import member creation not indicated in the imported .ts or .d.ts. The compiler will infer the existence of a `default` export that has the shape of the entire module itself.

System modules have this flag on by default.

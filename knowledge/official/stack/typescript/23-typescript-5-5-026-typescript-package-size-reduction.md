### TypeScript Package Size Reduction

Further leveraging [our transition to modules in 5.0](https://devblogs.microsoft.com/typescript/typescripts-migration-to-modules/), we've significantly reduced TypeScript's overall package size [by making `tsserver.js` and `typingsInstaller.js` import from a common API library instead of having each of them produce standalone bundles](https://github.com/microsoft/TypeScript/pull/55326).

This reduces TypeScript's size on disk from 30.2 MB to 20.4 MB, and reduces its packed size from 5.5 MB to 3.7 MB!

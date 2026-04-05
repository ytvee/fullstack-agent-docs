## Support for `--module node20`

TypeScript provides several `node*` options for the `--module` and `--moduleResolution` settings.
Most recently, `--module nodenext` has supported the ability to `require()` ECMAScript modules from CommonJS modules, and correctly rejects import assertions (in favor of the standards-bound [import attributes](https://github.com/tc39/proposal-import-attributes)).

TypeScript 5.9 brings a stable option for these settings called `node20`, intended to model the behavior of Node.js v20.
This option is unlikely to have new behaviors in the future, unlike `--module nodenext` or `--moduleResolution nodenext`.
Also unlike `nodenext`, specifying `--module node20` will imply `--target es2023` unless otherwise configured.
`--module nodenext`, on the other hand, implies the floating `--target esnext`.

For more information, [take a look at the implementation here](https://github.com/microsoft/TypeScript/pull/61805).

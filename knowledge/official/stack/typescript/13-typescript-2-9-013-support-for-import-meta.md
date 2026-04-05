## Support for `import.meta`

TypeScript 2.9 introduces support for `import.meta`, a new meta-property as described by the current [TC39 proposal](https://github.com/tc39/proposal-import-meta).

The type of `import.meta` is the global `ImportMeta` type which is defined in `lib.es5.d.ts`.
This interface is extremely limited.
Adding well-known properties for Node or browsers requires interface merging and possibly a global augmentation depending on the context.

## The `--allowUmdGlobalAccess` flag

In TypeScript 3.5, you can now reference UMD global declarations like

```
export as namespace foo;
```

from anywhere - even modules - using the new [`allowUmdGlobalAccess`](/tsconfig#allowUmdGlobalAccess) flag.

This mode adds flexibility for mixing and matching the way 3rd party libraries, where globals that libraries declare can always be consumed, even from within modules.

For more details, [see the pull request on GitHub](https://github.com/Microsoft/TypeScript/pull/30776/files).

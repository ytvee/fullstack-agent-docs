### `--incremental` improvements

TypeScript 3.5 improves on 3.4's [`incremental`](/tsconfig#incremental) build mode, by saving information about how the state of the world was calculated - compiler settings, why files were looked up, where files were found, etc.
In scenarios involving hundreds of projects using TypeScript's project references in `--build` mode, [we've found that the amount of time rebuilding can be reduced by as much as 68% compared to TypeScript 3.4](https://github.com/Microsoft/TypeScript/pull/31101)!

For more details, you can see the pull requests to

- [cache module resolution](https://github.com/Microsoft/TypeScript/pull/31100)
- [cache settings calculated from `tsconfig.json`](https://github.com/Microsoft/TypeScript/pull/31101)

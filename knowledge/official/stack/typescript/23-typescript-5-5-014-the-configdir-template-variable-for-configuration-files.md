## The `${configDir}` Template Variable for Configuration Files

It's common in many codebases to reuse a shared `tsconfig.json` file that acts as a "base" for other configuration files.
This is done by using the `extends` field in a `tsconfig.json` file.

```json
{
    "extends": "../../tsconfig.base.json",
    "compilerOptions": {
        "outDir": "./dist"
    }
}
```

One of the issues with this is that all paths in the `tsconfig.json` file are relative to the location of the file itself.
This means that if you have a shared `tsconfig.base.json` file that is used by multiple projects, relative paths often won't be useful in the derived projects.
For example, imagine the following `tsconfig.base.json`:

```json5
{
    "compilerOptions": {
        "typeRoots": [
            "./node_modules/@types",
            "./custom-types"
        ],
        "outDir": "dist"
    }
}
```

If author's intent was that every `tsconfig.json` that extends this file should

1. output to a `dist` directory relative to the derived `tsconfig.json` , and
1. have a `custom-types` directory relative to the derived `tsconfig.json`,

then this would not work.
The `typeRoots` paths would be relative to the location of the shared `tsconfig.base.json` file, not the project that extends it.
Each project that extends this shared file would need to declare its own `outDir` and `typeRoots` with identical contents.
This could be frustrating and hard to keep in sync between projects, and while the example above is using `typeRoots`, this is a common problem for `paths` and other options.

To solve this, TypeScript 5.5 introduces a new template variable `${configDir}`.
When `${configDir}` is written in certain path fields of a `tsconfig.json` or `jsconfig.json` files, this variable is substituted with the containing directory of the configuration file in a given compilation.
This means that the above `tsconfig.base.json` could be rewritten as:

```json5
{
    "compilerOptions": {
        "typeRoots": [
            "${configDir}/node_modules/@types",
            "${configDir}/custom-types"
        ],
        "outDir": "${configDir}/dist"
    }
}
```

Now, when a project extends this file, the paths will be relative to the derived `tsconfig.json`, not the shared `tsconfig.base.json` file.
This makes it easier to share configuration files across projects and ensures that the configuration files are more portable.

If you intend to make a `tsconfig.json` file extendable, consider if a `./` should instead be written with `${configDir}`.

For more information, see [the proposal issue](https://github.com/microsoft/TypeScript/issues/57485) and [the implementing pull request](https://github.com/microsoft/TypeScript/pull/58042).

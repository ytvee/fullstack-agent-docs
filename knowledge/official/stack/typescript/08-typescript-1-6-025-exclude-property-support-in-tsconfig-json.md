## `exclude` property support in tsconfig.json

A tsconfig.json file that doesn't specify a files property (and therefore implicitly references all \*.ts files in all subdirectories) can now contain an exclude property that specifies a list of files and/or directories to exclude from the compilation.
The exclude property must be an array of strings that each specify a file or folder name relative to the location of the tsconfig.json file.
For example:

```json tsconfig
{
  "compilerOptions": {
    "out": "test.js"
  },
  "exclude": ["node_modules", "test.ts", "utils/t2.ts"]
}
```

The [`exclude`](/tsconfig#exclude) list does not support wildcards. It must simply be a list of files and/or directories.

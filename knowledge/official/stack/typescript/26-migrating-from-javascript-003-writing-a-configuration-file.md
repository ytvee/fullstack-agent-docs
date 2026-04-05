## Writing a Configuration File

TypeScript uses a file called `tsconfig.json` for managing your project's options, such as which files you want to include, and what sorts of checking you want to perform.
Let's create a bare-bones one for our project:

```json
{
  "compilerOptions": {
    "outDir": "./built",
    "allowJs": true,
    "target": "es5"
  },
  "include": ["./src/**/*"]
}
```

Here we're specifying a few things to TypeScript:

1. Read in any files it understands in the `src` directory (with [`include`](/tsconfig#include)).
2. Accept JavaScript files as inputs (with [`allowJs`](/tsconfig#allowJs)).
3. Emit all of the output files in `built` (with [`outDir`](/tsconfig#outDir)).
4. Translate newer JavaScript constructs down to an older version like ECMAScript 5 (using [`target`](/tsconfig#target)).

At this point, if you try running `tsc` at the root of your project, you should see output files in the `built` directory.
The layout of files in `built` should look identical to the layout of `src`.
You should now have TypeScript working with your project.

## Including `.js` files with `--allowJs`

Often there are external source files in your project that may not be authored in TypeScript.
Alternatively, you might be in the middle of converting a JS code base into TS, but still want to bundle all your JS code into a single file with the output of your new TS code.

`.js` files are now allowed as input to `tsc`.
The TypeScript compiler checks the input `.js` files for syntax errors, and emits valid output based on the [`target`](/tsconfig#target) and [`module`](/tsconfig#module) flags.
The output can be combined with other `.ts` files as well.
Source maps are still generated for `.js` files just like with `.ts` files.

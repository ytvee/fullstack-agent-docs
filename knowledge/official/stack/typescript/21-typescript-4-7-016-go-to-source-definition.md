## Go to Source Definition

TypeScript 4.7 contains support for a new experimental editor command called *Go To Source Definition*.
It's similar to *Go To Definition*, but it never returns results inside declaration files.
Instead, it tries to find corresponding *implementation* files (like `.js` or `.ts` files), and find definitions there &mdash; even if those files are normally shadowed by `.d.ts` files.

This comes in handy most often when you need to peek at the implementation of a function you're importing from a library instead of its type declaration in a `.d.ts` file.

![The "Go to Source Definition" command on a use of the yargs package jumps the editor to an index.cjs file in yargs.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2022/05/go-to-source-definition-4-7-v1.gif)

You can try this new command in the latest versions of Visual Studio Code.
Note, though, that this functionality is still in preview, and there are some known limitations.
In some cases TypeScript uses heuristics to guess which `.js` file corresponds to the given result of a definition, so these results might be inaccurate.
Visual Studio Code also doesn't yet indicate whether a result was a guess, but it's something we're collaborating on.

You can leave feedback about the feature, read about known limitations, or learn more at [our dedicated feedback issue](https://github.com/microsoft/TypeScript/issues/49003).

### Using `isolatedDeclarations`

`isolatedDeclarations` requires that either the `declaration` or `composite` flags are also set.

Note that `isolatedDeclarations` does not change how TypeScript performs emit - just how it reports errors.
Importantly, and similar to `isolatedModules`, enabling the feature in TypeScript won't immediately bring about the potential benefits discussed here.
So please be patient and look forward to future developments in this space.
Keeping tool authors in mind, we should also recognize that today, not all of TypeScript's declaration emit can be easily replicated by other tools wanting to use it as a guide.
That's something we're actively working on improving.

On top of this, isolated declarations are still a new feature, and we're actively working on improving the experience.
Some scenarios, like using computed property declarations in classes and object literals, are not *yet* supported under `isolatedDeclarations`.
Keep an eye on this space, and feel free to provide us with feedback.

We also feel it is worth calling out that `isolatedDeclarations` should be adopted on a case-by-case basis.
There are some developer ergonomics that are lost when using `isolatedDeclarations`, and thus it may not be the right choice if your setup is not leveraging the two scenarios mentioned earlier.
For others, the work on `isolatedDeclarations` has already uncovered many optimizations and opportunities to unlock different parallel build strategies.
In the meantime, if you're willing to make the trade-offs, we believe `isolatedDeclarations` can be a powerful tool to speed up your build process as external tooling becomes more widely available.

For more information, read up on the [Isolated Declarations: State of the Feature](https://github.com/microsoft/TypeScript/issues/58944) discussion on the TypeScript issue tracker.

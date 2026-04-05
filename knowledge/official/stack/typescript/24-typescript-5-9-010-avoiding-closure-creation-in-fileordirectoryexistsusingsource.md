### Avoiding Closure Creation in `fileOrDirectoryExistsUsingSource`

In JavaScript, a function expression will typically allocate a new function object, even if the wrapper function is just passing through arguments to another function with no captured variables.
In code paths around file existence checks, [Vincent Bailly](https://github.com/VincentBailly) found examples of these pass-through function calls, even though the underlying functions only took single arguments.
Given the number of existence checks that could take place in larger projects, he cited a speed-up of around 11%.
[See more on this change here](https://github.com/microsoft/TypeScript/pull/61822/).

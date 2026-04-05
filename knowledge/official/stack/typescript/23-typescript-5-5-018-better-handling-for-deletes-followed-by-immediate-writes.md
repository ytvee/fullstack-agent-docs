### Better Handling for Deletes Followed by Immediate Writes

Instead of overwriting files, some tools will opt to delete them and then create new files from scratch.
This is the case when running `npm ci`, for instance.

While this can be efficient for those tools, it can be problematic for TypeScript's editor scenarios where deleting a watched might dispose of it and all of its transitive dependencies.
Deleting and creating a file in quick succession could lead to TypeScript tearing down an entire project and then rebuilding it from scratch.

TypeScript 5.5 now has a more nuanced approach by keeping parts of a deleted project around until it picks up on a new creation event.
This should make operations like `npm ci` work a lot better with TypeScript.
See [more information on the approach here](https://github.com/microsoft/TypeScript/pull/57492).

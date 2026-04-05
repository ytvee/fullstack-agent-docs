## `typeRoots` Are Consulted In Module Resolution

When TypeScript's specified module lookup strategy is unable to resolve a path, it will now resolve packages relative to the specified `typeRoots`.

See [this pull request](https://github.com/microsoft/TypeScript/pull/51715) for more details.

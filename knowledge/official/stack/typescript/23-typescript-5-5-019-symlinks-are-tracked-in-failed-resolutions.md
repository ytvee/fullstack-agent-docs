### Symlinks are Tracked in Failed Resolutions

When TypeScript fails to resolve a module, it will still need to watch for any failed lookup paths in case the module is added later.
Previously this was not done for symlinked directories, which could cause reliability issues in monorepo-like scenarios when a build occurred in one project but was not witnessed in the other.
This should be fixed in TypeScript 5.5, and means you won't need to restart your editor as often.

[See more information here](https://github.com/microsoft/TypeScript/pull/58139).

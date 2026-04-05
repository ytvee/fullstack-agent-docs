### Project References Contribute to Auto-Imports

Auto-imports no longer requires at least one explicit import to dependent projects in a project reference setup.
Instead, auto-import completions should just work across anything you've listed in the `references` field of your `tsconfig.json`.

[See more on the implementing pull request](https://github.com/microsoft/TypeScript/pull/55955).

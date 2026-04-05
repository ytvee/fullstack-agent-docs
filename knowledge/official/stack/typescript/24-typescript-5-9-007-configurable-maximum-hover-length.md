## Configurable Maximum Hover Length

Occasionally, quick info tooltips can become so long that TypeScript will truncate them to make them more readable.
The downside here is that often the most important information will be omitted from the hover tooltip, which can be frustrating.
To help with this, TypeScript 5.9's language server supports a configurable hover length, which can be configured in VS Code via the `js/ts.hover.maximumLength` setting.

Additionally, the new default hover length is substantially larger than the previous default.
This means that in TypeScript 5.9, you should see more information in your hover tooltips by default.
For more details, see [the PR for this feature here](https://github.com/microsoft/TypeScript/pull/61662) and [the corresponding change to Visual Studio Code here](https://github.com/microsoft/vscode/pull/248181).

### `/** @deprecated */` Support

TypeScript's editing support now recognizes when a declaration has been marked with a `/** @deprecated */` JSDoc comment.
That information is surfaced in completion lists and as a suggestion diagnostic that editors can handle specially.
In an editor like VS Code, deprecated values are typically displayed in a strike-though style ~~like this~~.

![Some examples of deprecated declarations with strikethrough text in the editor](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/06/deprecated_4-0.png)

This new functionality is available thanks to [Wenlu Wang](https://github.com/Kingwl).
See [the pull request](https://github.com/microsoft/TypeScript/pull/38523) for more details.

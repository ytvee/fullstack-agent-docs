## Linked Cursors for JSX Tags

TypeScript now supports *linked editing* for JSX tag names.
Linked editing (occasionally called "mirrored cursors") allows an editor to edit multiple locations at the same time automatically.

![An example of JSX tags with linked editing modifying a JSX fragment and a div element.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2023/04/linkedEditingJsx-5.1-1.gif)

This new feature should work in both TypeScript and JavaScript files, and can be enabled in Visual Studio Code Insiders.
In Visual Studio Code, you can either edit the `Editor: Linked Editing` option in the Settings UI:

![Visual Studio Code's Editor: Linked Editing` option](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2023/04/linkedEditing-5.1-vscode-ui-1.png)

or configure `editor.linkedEditing` in your JSON settings file:

```jsonc
{
    // ...
    "editor.linkedEditing": true,
}
```

This feature will also be supported by Visual Studio 17.7 Preview 1.

You can take a look at [our implementation of linked editing](https://github.com/microsoft/TypeScript/pull/53284) here!

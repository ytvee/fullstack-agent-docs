### Smarter Auto-Imports

Auto-import is a fantastic feature that makes coding a lot easier; however, every time auto-import doesn't seem to work, it can throw users off a lot.
One specific issue that we heard from users was that auto-imports didn't work on dependencies that were written in TypeScript - that is, until they wrote at least one explicit import somewhere else in their project.

Why would auto-imports work for `@types` packages, but not for packages that ship their own types?
It turns out that auto-imports only work on packages your project _already_ includes.
Because TypeScript has some quirky defaults that automatically add packages in `node_modules/@types` to your project, _those_ packages would be auto-imported.
On the other hand, other packages were excluded because crawling through all your `node_modules` packages can be _really_ expensive.

All of this leads to a pretty lousy getting started experience for when you're trying to auto-import something that you've just installed but haven't used yet.

TypeScript 4.0 now does a little extra work in editor scenarios to include the packages you've listed in your `package.json`'s `dependencies` (and `peerDependencies`) fields.
The information from these packages is only used to improve auto-imports, and doesn't change anything else like type-checking.
This allows us to provide auto-imports for all of your dependencies that have types, without incurring the cost of a complete `node_modules` search.

In the rare cases when your `package.json` lists more than ten typed dependencies that haven't been imported yet, this feature automatically disables itself to prevent slow project loading.
To force the feature to work, or to disable it entirely, you should be able to configure your editor.
For Visual Studio Code, this is the "Include Package JSON Auto Imports" (or `typescript.preferences.includePackageJsonAutoImports`) setting.

![Configuring 'include package JSON auto imports'](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/08/configurePackageJsonAutoImports4-0.png)
For more details, you can see the [proposal issue](https://github.com/microsoft/TypeScript/issues/37812) along with [the implementing pull request](https://github.com/microsoft/TypeScript/pull/38923).

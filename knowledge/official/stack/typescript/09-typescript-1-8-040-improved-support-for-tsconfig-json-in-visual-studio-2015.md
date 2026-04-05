## Improved support for `tsconfig.json` in Visual Studio 2015

TypeScript 1.8 allows `tsconfig.json` files in all project types.
This includes ASP.NET v4 projects, _Console Application_, and the _Html Application with TypeScript_ project types.
Further, you are no longer limited to a single `tsconfig.json` file but can add multiple, and each will be built as part of the project.
This allows you to separate the configuration for different parts of your application without having to use multiple different projects.

![Showing off tsconfig.json in Visual Studio](https://raw.githubusercontent.com/wiki/Microsoft/TypeScript/images/new-in-typescript/tsconfig-in-vs.png)

We also disable the project properties page when you add a `tsconfig.json` file.
This means that all configuration changes have to be made in the `tsconfig.json` file itself.

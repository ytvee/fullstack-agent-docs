## Built-in Type Definitions

TypeScript includes declaration files for all of the standardized built-in APIs available in JavaScript runtimes.
This includes things like methods and properties of built-in types like `string` or `function`, top-level names like `Math` and `Object`, and their associated types.
By default, TypeScript also includes types for things available when running inside the browser, such as `window` and `document`; these are collectively referred to as the DOM APIs.

TypeScript names these declaration files with the pattern `lib.[something].d.ts`.
If you navigate into a file with that name, you can know that you're dealing with some built-in part of the platform, not user code.

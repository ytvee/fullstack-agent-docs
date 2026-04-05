## Control over Module Detection

One issue with the introduction of modules to JavaScript was the ambiguity between existing "script" code and the new module code.
JavaScript code in a module runs slightly differently, and has different scoping rules, so tools have to make decisions as to how each file runs.
For example, Node.js requires module entry-points to be written in a `.mjs`, or have a nearby `package.json` with `"type": "module"`.
TypeScript treats a file as a module whenever it finds any `import` or `export` statement in a file, but otherwise, will assume a `.ts` or `.js` file is a script file acting on the global scope.

This doesn't quite match up with the behavior of Node.js where the `package.json` can change the format of a file, or the `--jsx` setting `react-jsx`, where any JSX file contains an implicit import to a JSX factory.
It also doesn't match modern expectations where most new TypeScript code is written with modules in mind.

That's why TypeScript 4.7 introduces a new option called `moduleDetection`.
`moduleDetection` can take on 3 values: `"auto"` (the default), `"legacy"` (the same behavior as 4.6 and prior), and `"force"`.

Under the mode `"auto"`, TypeScript will not only look for `import` and `export` statements, but it will also check whether

* the `"type"` field in `package.json` is set to `"module"` when running under `--module nodenext`/`--module node16`, and
* check whether the current file is a JSX file when running under `--jsx react-jsx`

In cases where you want every file to be treated as a module, the `"force"` setting ensures that every non-declaration file is treated as a module.
This will be true regardless of how `module`, `moduleResolution`, and `jsx` are configured.

Meanwhile, the `"legacy"` option simply goes back to the old behavior of only seeking out `import` and `export` statements to determine whether a file is a module.

You can [read up more about this change on the pull request](https://github.com/microsoft/TypeScript/pull/47495).

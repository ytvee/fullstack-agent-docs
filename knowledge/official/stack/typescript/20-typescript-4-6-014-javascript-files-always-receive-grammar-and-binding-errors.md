### JavaScript Files Always Receive Grammar and Binding Errors

Previously, TypeScript would ignore most grammar errors in JavaScript apart from accidentally using TypeScript syntax in a JavaScript file.
TypeScript now shows JavaScript syntax and binding errors in your file, such as using incorrect modifiers, duplicate declarations, and more.
These will typically be most apparent in Visual Studio Code or Visual Studio, but can also occur when running JavaScript code through the TypeScript compiler.

You can explicitly turn these errors off by inserting a `// @ts-nocheck` comment at the top of your file.

For more information, see the [first](https://github.com/microsoft/TypeScript/pull/47067) and [second](https://github.com/microsoft/TypeScript/pull/47075) implementing pull requests for these features.

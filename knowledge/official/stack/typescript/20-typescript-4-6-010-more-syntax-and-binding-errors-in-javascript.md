## More Syntax and Binding Errors in JavaScript

TypeScript has expanded its set of syntax and binding errors in JavaScript files.
You'll see these new errors if you open JavaScript files in an editor like Visual Studio or Visual Studio Code, or if you run JavaScript code through the TypeScript compiler - even if you don't turn on `checkJs` or add a `// @ts-check` comment to the top of your files.

As one example, if you have two declarations of a `const` in the same scope of a JavaScript file, TypeScript will now issue an error on those declarations.

```ts
const foo = 1234;
//    ~~~
// error: Cannot redeclare block-scoped variable 'foo'.

// ...

const foo = 5678;
//    ~~~
// error: Cannot redeclare block-scoped variable 'foo'.
```

As another example, TypeScript will let you know if a modifier is being incorrectly used.

```ts
function container() {
    export function foo() {
//  ~~~~~~
// error: Modifiers cannot appear here.
    }
}
```

These errors can be disabled by adding a `// @ts-nocheck` at the top of your file, but we're interested in hearing some early feedback about how it works for your JavaScript workflow.
You can easily try it out for Visual Studio Code by installing the [TypeScript and JavaScript Nightly Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next), and read up more on the [first](https://github.com/microsoft/TypeScript/pull/47067) and [second](https://github.com/microsoft/TypeScript/pull/47075) pull requests.

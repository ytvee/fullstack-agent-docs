## JSDoc Name Suggestions

In JSDoc, you can document parameters using an `@param` tag.

```js
/**
 * @param x The first operand
 * @param y The second operand
 */
function add(x, y) {
  return x + y;
}
```

But what happens when these comments fall out of date?
What if we rename `x` and `y` to `a` and `b`?

```js
/**
 * @param x {number} The first operand
 * @param y {number} The second operand
 */
function add(a, b) {
  return a + b;
}
```

Previously TypeScript would only tell you about this when performing type-checking on JavaScript files - when using either the `checkJs` option, or adding a `// @ts-check` comment to the top of your file.

You can now get similar information for TypeScript files in your editor!
TypeScript now provides suggestions for when parameter names don't match between your function and its JSDoc comment.

![Suggestion diagnostics being shown in the editor for parameter names in JSDoc comments that don't match an actual parameter name.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2022/02/jsdoc-comment-suggestions-4-6.png)

[This change](https://github.com/microsoft/TypeScript/pull/47257) was provided courtesy of [Alexander Tarasyuk](https://github.com/a-tarasyuk)!

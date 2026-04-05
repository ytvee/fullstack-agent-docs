### `@deprecated`
<div id="deprecated-comments"></div>

When a function, method, or property is deprecated you can let users know by marking it with a `/** @deprecated */` JSDoc comment. That information is surfaced in completion lists and as a suggestion diagnostic that editors can handle specially. In an editor like VS Code, deprecated values are typically displayed in a strike-through style ~~like this~~.

```js twoslash
// @noErrors
/** @deprecated */
const apiV1 = {};
const apiV2 = {};

apiV;
// ^|


```

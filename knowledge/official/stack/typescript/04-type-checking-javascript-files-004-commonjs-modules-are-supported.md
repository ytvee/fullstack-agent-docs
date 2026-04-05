## CommonJS modules are supported

In a `.js` file, TypeScript understands the CommonJS module format.
Assignments to `exports` and `module.exports` are recognized as export declarations.
Similarly, `require` function calls are recognized as module imports. For example:

```js
// same as `import module "fs"`
const fs = require("fs");

// same as `export function readFile`
module.exports.readFile = function (f) {
  return fs.readFileSync(f);
};
```

The module support in JavaScript is much more syntactically forgiving than TypeScript's module support.
Most combinations of assignments and declarations are supported.

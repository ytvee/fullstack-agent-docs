### `target` setting

The methods, properties, and functions available to you actually vary based on the _version_ of JavaScript your code is running on.
For example, the `startsWith` method of strings is available only starting with the version of JavaScript referred as _ECMAScript 6_.

Being aware of what version of JavaScript your code ultimately runs on is important because you don't want to use APIs that are from a newer version than the platform you deploy to.
This is one function of the [`target`](/tsconfig#target) compiler setting.

TypeScript helps with this problem by varying which `lib` files are included by default based on your [`target`](/tsconfig#target) setting.
For example, if [`target`](/tsconfig#target) is `ES5`, you will see an error if trying to use the `startsWith` method, because that method is only available in `ES6` or later.
